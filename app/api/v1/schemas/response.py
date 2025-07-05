from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    status: int = Field(
        description="HTTP status code", default=200, examples=[200, 201, 404, 500]
    )
    message: str = Field(
        description="Message from server", examples=["success", "failed"]
    )
    data: T = Field(description="Data that server responsed")

