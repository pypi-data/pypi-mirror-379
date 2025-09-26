from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from .types import TrackIdType


class VerifyRequest(BaseModel):
    track_id: TrackIdType = Field(..., description="Transaction ID returned by Zibal")

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel,
    )
