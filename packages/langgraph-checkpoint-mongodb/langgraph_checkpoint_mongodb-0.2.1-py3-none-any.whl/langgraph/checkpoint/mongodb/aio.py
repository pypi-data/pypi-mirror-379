from __future__ import annotations

import asyncio
import builtins
import sys
import warnings
from collections.abc import AsyncIterator, Iterator, Sequence
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Any, Optional, cast

from langchain_core.runnables import RunnableConfig
from pymongo import UpdateOne
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.asynchronous.mongo_client import AsyncMongoClient

from langgraph.checkpoint.base import (
    WRITES_IDX_MAP,
    BaseCheckpointSaver,
    ChannelVersions,
    Checkpoint,
    CheckpointMetadata,
    CheckpointTuple,
    get_checkpoint_id,
)

from .utils import (
    DRIVER_METADATA,
    _append_client_metadata,
    dumps_metadata,
    loads_metadata,
)

if sys.version_info >= (3, 10):
    anext = builtins.anext
    aiter = builtins.aiter
else:

    async def anext(cls: Any) -> Any:
        """Compatibility function until we drop 3.9 support: https://docs.python.org/3/library/functions.html#anext."""
        return await cls.__anext__()

    def aiter(cls: Any) -> Any:
        """Compatibility function until we drop 3.9 support: https://docs.python.org/3/library/functions.html#anext."""
        return cls.__aiter__()


__all__ = ["AsyncMongoDBSaver"]


class AsyncMongoDBSaver(BaseCheckpointSaver):
    """A checkpoint saver that stores checkpoints in a MongoDB database asynchronously.

    The synchronous MongoDBSaver has extended documentation, but
    Asynchronous usage is shown below.

    Examples:
        >>> import asyncio
        >>> from langgraph.checkpoint.mongodb.aio import AsyncMongoDBSaver
        >>> from langgraph.graph import StateGraph

        >>> async def main() -> None:
        >>>     builder = StateGraph(int)
        >>>     builder.add_node("add_one", lambda x: x + 1)
        >>>     builder.set_entry_point("add_one")
        >>>     builder.set_finish_point("add_one")
        >>>     async with AsyncMongoDBSaver.from_conn_string("mongodb://localhost:27017") as memory:
        >>>         graph = builder.compile(checkpointer=memory)
        >>>         config = {"configurable": {"thread_id": "1"}}
        >>>         input = 3
        >>>         output = await graph.ainvoke(input, config)
        >>>         print(f"{input=}, {output=}")

        >>> if __name__ == "__main__":
        >>>     asyncio.run(main())
        input=3, output=4
    """

    client: AsyncMongoClient
    db: AsyncDatabase

    def __init__(
        self,
        client: AsyncMongoClient,
        db_name: str = "checkpointing_db",
        checkpoint_collection_name: str = "checkpoints_aio",
        writes_collection_name: str = "checkpoint_writes_aio",
        ttl: Optional[int] = None,
        **kwargs: Any,
    ) -> None:
        warnings.warn(
            f"{self.__class__.__name__} is deprecated and will be removed in 0.3.0 release. "
            "Please use the async methods of MongoDBSaver instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__()
        self.client = client
        self.db = self.client[db_name]
        self.checkpoint_collection = self.db[checkpoint_collection_name]
        self.writes_collection = self.db[writes_collection_name]
        self._setup_future: asyncio.Future | None = None
        self.loop = asyncio.get_running_loop()
        self.ttl = ttl

        # append_metadata was added in PyMongo 4.14.0, but is a valid database name on earlier versions
        _append_client_metadata(self.client)

    async def _setup(self) -> None:
        """Create indexes if not present."""
        if self._setup_future is not None:
            return await self._setup_future
        self._setup_future = asyncio.Future()
        if isinstance(self.client, AsyncMongoClient):
            num_indexes = len(
                await (await self.checkpoint_collection.list_indexes()).to_list()
            )
        else:
            num_indexes = len(await self.checkpoint_collection.list_indexes().to_list())
        if num_indexes < 2:
            await self.checkpoint_collection.create_index(
                keys=[("thread_id", 1), ("checkpoint_ns", 1), ("checkpoint_id", -1)],
                unique=True,
            )
            if self.ttl:
                await self.checkpoint_collection.create_index(
                    keys=[("created_at", 1)],
                    expireAfterSeconds=self.ttl,
                )
        if isinstance(self.client, AsyncMongoClient):
            num_indexes = len(
                await (await self.writes_collection.list_indexes()).to_list()
            )
        else:
            num_indexes = len(await self.writes_collection.list_indexes().to_list())
        if num_indexes < 2:
            await self.writes_collection.create_index(
                keys=[
                    ("thread_id", 1),
                    ("checkpoint_ns", 1),
                    ("checkpoint_id", -1),
                    ("task_id", 1),
                    ("idx", 1),
                ],
                unique=True,
            )
            if self.ttl:
                await self.writes_collection.create_index(
                    keys=[("created_at", 1)],
                    expireAfterSeconds=self.ttl,
                )
        self._setup_future.set_result(None)

    @classmethod
    @asynccontextmanager
    async def from_conn_string(
        cls,
        conn_string: str,
        db_name: str = "checkpointing_db",
        checkpoint_collection_name: str = "checkpoints_aio",
        writes_collection_name: str = "checkpoint_writes_aio",
        ttl: Optional[int] = None,
        **kwargs: Any,
    ) -> AsyncIterator[AsyncMongoDBSaver]:
        """Create asynchronous checkpointer

        This includes creation of collections and indexes if they don't exist
        """
        client: Optional[AsyncMongoClient] = None
        try:
            client = AsyncMongoClient(
                conn_string,
                driver=DRIVER_METADATA,
            )
            saver = AsyncMongoDBSaver(
                client,
                db_name,
                checkpoint_collection_name,
                writes_collection_name,
                ttl,
                **kwargs,
            )
            await saver._setup()
            yield saver

        finally:
            if client:
                await client.close()

    async def aget_tuple(self, config: RunnableConfig) -> Optional[CheckpointTuple]:
        """Get a checkpoint tuple from the database asynchronously.

        This method retrieves a checkpoint tuple from the MongoDB database based on the
        provided config. If the config contains a "checkpoint_id" key, the checkpoint with
        the matching thread ID and checkpoint ID is retrieved. Otherwise, the latest checkpoint
        for the given thread ID is retrieved.

        Args:
            config (RunnableConfig): The config to use for retrieving the checkpoint.

        Returns:
            Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.
        """
        await self._setup()
        thread_id = config["configurable"]["thread_id"]
        checkpoint_ns = config["configurable"].get("checkpoint_ns", "")
        if checkpoint_id := get_checkpoint_id(config):
            query = {
                "thread_id": thread_id,
                "checkpoint_ns": checkpoint_ns,
                "checkpoint_id": checkpoint_id,
            }
        else:
            query = {"thread_id": thread_id, "checkpoint_ns": checkpoint_ns}

        result = self.checkpoint_collection.find(
            query, sort=[("checkpoint_id", -1)], limit=1
        )
        async for doc in result:
            config_values = {
                "thread_id": thread_id,
                "checkpoint_ns": checkpoint_ns,
                "checkpoint_id": doc["checkpoint_id"],
            }
            checkpoint = self.serde.loads_typed((doc["type"], doc["checkpoint"]))
            serialized_writes = self.writes_collection.find(config_values)
            pending_writes = [
                (
                    wrt["task_id"],
                    wrt["channel"],
                    self.serde.loads_typed((wrt["type"], wrt["value"])),
                )
                async for wrt in serialized_writes
            ]
            return CheckpointTuple(
                {"configurable": config_values},
                checkpoint,
                loads_metadata(doc["metadata"]),
                (
                    {
                        "configurable": {
                            "thread_id": thread_id,
                            "checkpoint_ns": checkpoint_ns,
                            "checkpoint_id": doc["parent_checkpoint_id"],
                        }
                    }
                    if doc.get("parent_checkpoint_id")
                    else None
                ),
                pending_writes,
            )

    async def alist(
        self,
        config: Optional[RunnableConfig],
        *,
        filter: Optional[dict[str, Any]] = None,
        before: Optional[RunnableConfig] = None,
        limit: Optional[int] = None,
    ) -> AsyncIterator[CheckpointTuple]:
        """List checkpoints from the database asynchronously.

        This method retrieves a list of checkpoint tuples from the MongoDB database based
        on the provided config. The checkpoints are ordered by checkpoint ID in descending order (newest first).

        Args:
            config (Optional[RunnableConfig]): Base configuration for filtering checkpoints.
            filter (Optional[dict[str, Any]]): Additional filtering criteria for metadata.
            before (Optional[RunnableConfig]): If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.
            limit (Optional[int]): Maximum number of checkpoints to return.

        Yields:
            AsyncIterator[CheckpointTuple]: An asynchronous iterator of matching checkpoint tuples.
        """
        await self._setup()
        query = {}
        if config is not None:
            if "thread_id" in config["configurable"]:
                query["thread_id"] = config["configurable"]["thread_id"]
            if "checkpoint_ns" in config["configurable"]:
                query["checkpoint_ns"] = config["configurable"]["checkpoint_ns"]

        if filter:
            for key, value in filter.items():
                query[f"metadata.{key}"] = dumps_metadata(value)

        if before is not None:
            query["checkpoint_id"] = {"$lt": before["configurable"]["checkpoint_id"]}

        result = self.checkpoint_collection.find(
            query, limit=0 if limit is None else limit, sort=[("checkpoint_id", -1)]
        )

        async for doc in result:
            config_values = {
                "thread_id": doc["thread_id"],
                "checkpoint_ns": doc["checkpoint_ns"],
                "checkpoint_id": doc["checkpoint_id"],
            }
            serialized_writes = self.writes_collection.find(config_values)
            pending_writes = [
                (
                    wrt["task_id"],
                    wrt["channel"],
                    self.serde.loads_typed((wrt["type"], wrt["value"])),
                )
                async for wrt in serialized_writes
            ]

            yield CheckpointTuple(
                config={
                    "configurable": {
                        "thread_id": doc["thread_id"],
                        "checkpoint_ns": doc["checkpoint_ns"],
                        "checkpoint_id": doc["checkpoint_id"],
                    }
                },
                checkpoint=self.serde.loads_typed((doc["type"], doc["checkpoint"])),
                metadata=loads_metadata(doc["metadata"]),
                parent_config=(
                    {
                        "configurable": {
                            "thread_id": doc["thread_id"],
                            "checkpoint_ns": doc["checkpoint_ns"],
                            "checkpoint_id": doc["parent_checkpoint_id"],
                        }
                    }
                    if doc.get("parent_checkpoint_id")
                    else None
                ),
                pending_writes=pending_writes,
            )

    async def aput(
        self,
        config: RunnableConfig,
        checkpoint: Checkpoint,
        metadata: CheckpointMetadata,
        new_versions: ChannelVersions,
    ) -> RunnableConfig:
        """Save a checkpoint to the database asynchronously.

        This method saves a checkpoint to the MongoDB database. The checkpoint is associated
        with the provided config and its parent config (if any).

        Args:
            config (RunnableConfig): The config to associate with the checkpoint.
            checkpoint (Checkpoint): The checkpoint to save.
            metadata (CheckpointMetadata): Additional metadata to save with the checkpoint.
            new_versions (ChannelVersions): New channel versions as of this write.

        Returns:
            RunnableConfig: Updated configuration after storing the checkpoint.
        """
        await self._setup()
        thread_id = config["configurable"]["thread_id"]
        checkpoint_ns = config["configurable"]["checkpoint_ns"]
        checkpoint_id = checkpoint["id"]
        type_, serialized_checkpoint = self.serde.dumps_typed(checkpoint)
        metadata = metadata.copy()
        metadata.update(config.get("metadata", {}))
        doc: dict[str, Any] = {
            "parent_checkpoint_id": config["configurable"].get("checkpoint_id"),
            "type": type_,
            "checkpoint": serialized_checkpoint,
            "metadata": dumps_metadata(metadata),
        }
        upsert_query = {
            "thread_id": thread_id,
            "checkpoint_ns": checkpoint_ns,
            "checkpoint_id": checkpoint_id,
        }

        if self.ttl:
            doc["created_at"] = datetime.now()
        # Perform your operations here
        await self.checkpoint_collection.update_one(
            upsert_query, {"$set": doc}, upsert=True
        )
        return {
            "configurable": {
                "thread_id": thread_id,
                "checkpoint_ns": checkpoint_ns,
                "checkpoint_id": checkpoint_id,
            }
        }

    async def aput_writes(
        self,
        config: RunnableConfig,
        writes: Sequence[tuple[str, Any]],
        task_id: str,
        task_path: str = "",
    ) -> None:
        """Store intermediate writes linked to a checkpoint asynchronously.

        This method saves intermediate writes associated with a checkpoint to the database.

        Args:
            config (RunnableConfig): Configuration of the related checkpoint.
            writes (Sequence[tuple[str, Any]]): List of writes to store, each as (channel, value) pair.
            task_id (str): Identifier for the task creating the writes.
            task_path (str): Path of the task creating the writes.
        """
        await self._setup()
        thread_id = config["configurable"]["thread_id"]
        checkpoint_ns = config["configurable"]["checkpoint_ns"]
        checkpoint_id = config["configurable"]["checkpoint_id"]
        set_method = (  # Allow replacement on existing writes only if there were errors.
            "$set" if all(w[0] in WRITES_IDX_MAP for w in writes) else "$setOnInsert"
        )
        operations = []
        now = datetime.now()
        for idx, (channel, value) in enumerate(writes):
            upsert_query = {
                "thread_id": thread_id,
                "checkpoint_ns": checkpoint_ns,
                "checkpoint_id": checkpoint_id,
                "task_id": task_id,
                "task_path": task_path,
                "idx": WRITES_IDX_MAP.get(channel, idx),
            }

            type_, serialized_value = self.serde.dumps_typed(value)

            update_doc: dict[str, Any] = {
                "channel": channel,
                "type": type_,
                "value": serialized_value,
            }

            if self.ttl:
                update_doc["created_at"] = now

            operations.append(
                UpdateOne(
                    filter=upsert_query,
                    update={set_method: update_doc},
                    upsert=True,
                )
            )
        await self.writes_collection.bulk_write(operations)

    async def adelete_thread(
        self,
        thread_id: str,
    ) -> None:
        """Delete all checkpoints and writes associated with a specific thread ID asynchronously.

        Args:
            thread_id (str): The thread ID whose checkpoints should be deleted.
        """
        # Delete all checkpoints associated with the thread ID
        await self.checkpoint_collection.delete_many({"thread_id": thread_id})

        # Delete all writes associated with the thread ID
        await self.writes_collection.delete_many({"thread_id": thread_id})

    def delete_thread(
        self,
        thread_id: str,
    ) -> None:
        """Delete all checkpoints and writes associated with a specific thread ID.

        Args:
            thread_id (str): The thread ID whose checkpoints should be deleted.
        """
        return asyncio.run_coroutine_threadsafe(
            self.adelete_thread(thread_id), self.loop
        ).result()

    def list(
        self,
        config: Optional[RunnableConfig],
        *,
        filter: Optional[dict[str, Any]] = None,
        before: Optional[RunnableConfig] = None,
        limit: Optional[int] = None,
    ) -> Iterator[CheckpointTuple]:
        """List checkpoints from the database.

        This method retrieves a list of checkpoint tuples from the MongoDB database
         based on the provided config. The checkpoints are ordered by checkpoint ID in
         descending order (newest first).

        Args:
            config (Optional[RunnableConfig]): Base configuration for filtering checkpoints.
            filter (Optional[dict[str, Any]]): Additional filtering criteria for metadata.
            before (Optional[RunnableConfig]): If provided, only checkpoints before the specified checkpoint ID are returned. Defaults to None.
            limit (Optional[int]): Maximum number of checkpoints to return.

        Yields:
            Iterator[CheckpointTuple]: An iterator of matching checkpoint tuples.
        """
        aiter_ = self.alist(config, filter=filter, before=before, limit=limit)
        while True:
            try:
                yield asyncio.run_coroutine_threadsafe(
                    cast(Any, anext(aiter_)),
                    self.loop,
                ).result()
            except StopAsyncIteration:
                break

    def get_tuple(self, config: RunnableConfig) -> Optional[CheckpointTuple]:
        """Get a checkpoint tuple from the database.

        This method retrieves a checkpoint tuple from the MongoDB database based on
        the provided config. If the config contains a "checkpoint_id" key, the
        checkpoint with the matching thread ID and "checkpoint_id" is retrieved.
        Otherwise, the latest checkpoint for the given thread ID is retrieved.

        Args:
            config (RunnableConfig): The config to use for retrieving the checkpoint.

        Returns:
            Optional[CheckpointTuple]: The retrieved checkpoint tuple, or None if no matching checkpoint was found.
        """
        try:
            # check if we are in the main thread, only bg threads can block
            # we don't check in other methods to avoid the overhead
            if asyncio.get_running_loop() is self.loop:
                raise asyncio.InvalidStateError(
                    "Synchronous calls to AsyncMongoDBSaver are only allowed from a "
                    "different thread. From the main thread, use the async interface."
                    "For example, use `await checkpointer.aget_tuple(...)` or `await "
                    "graph.ainvoke(...)`."
                )
        except RuntimeError:
            pass
        return asyncio.run_coroutine_threadsafe(
            self.aget_tuple(config), self.loop
        ).result()

    def put(
        self,
        config: RunnableConfig,
        checkpoint: Checkpoint,
        metadata: CheckpointMetadata,
        new_versions: ChannelVersions,
    ) -> RunnableConfig:
        """Save a checkpoint to the database.

        This method saves a checkpoint to the MongoDB database. The checkpoint
        is associated with the provided config and its parent config (if any).

        Args:
            config (RunnableConfig): The config to associate with the checkpoint.
            checkpoint (Checkpoint): The checkpoint to save.
            metadata (CheckpointMetadata): Additional metadata to save with the checkpoint.
            new_versions (ChannelVersions): New channel versions as of this write.

        Returns:
            RunnableConfig: Updated configuration after storing the checkpoint.
        """
        return asyncio.run_coroutine_threadsafe(
            self.aput(config, checkpoint, metadata, new_versions), self.loop
        ).result()

    def put_writes(
        self,
        config: RunnableConfig,
        writes: Sequence[tuple[str, Any]],
        task_id: str,
        task_path: str = "",
    ) -> None:
        """Store intermediate writes linked to a checkpoint.

        This method saves intermediate writes associated with a checkpoint to the database.

        Args:
            config (RunnableConfig): Configuration of the related checkpoint.
            writes (Sequence[tuple[str, Any]]): List of writes to store, each as (channel, value) pair.
            task_id (str): Identifier for the task creating the writes.
        """
        return asyncio.run_coroutine_threadsafe(
            self.aput_writes(config, writes, task_id, task_path), self.loop
        ).result()
