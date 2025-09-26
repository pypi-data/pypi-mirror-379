"""The module with image representation of posts data"""

from typing import Literal

from pydantic import BaseModel


class BoostyPostDataImageDTO(BaseModel):
    """Image content piece in posts"""

    type: Literal['image']
    url: str
    width: int | None = None
    height: int | None = None
