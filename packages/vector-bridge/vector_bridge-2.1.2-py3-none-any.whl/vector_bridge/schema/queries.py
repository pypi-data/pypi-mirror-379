import base64
import pickle
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from weaviate.collections.classes.filters import _Filters
from weaviate.collections.classes.grpc import _Sorting


class QueryResponse(BaseModel):
    items: list[Any]
    limit: int | None = None
    offset: int | None = None


class Query(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    near_text: str | None = None
    near_id: UUID | None = None
    limit: int | None = None
    offset: int | None = None
    filters: _Filters | None = None
    sort: _Sorting | None = None
    kwargs: dict[str, Any] = {}

    def serialize_bytes(self) -> dict:
        """
        Convert filters/sort into base64-encoded pickle strings for transport.
        """
        serialized_query = self.model_dump()

        if self.filters is not None:
            serialized_query["filters"] = base64.b64encode(pickle.dumps(self.filters)).decode("utf-8")

        if self.sort is not None:
            serialized_query["sort"] = base64.b64encode(pickle.dumps(self.sort)).decode("utf-8")

        if self.near_id is not None:
            serialized_query["near_id"] = str(self.near_id)

        return serialized_query
