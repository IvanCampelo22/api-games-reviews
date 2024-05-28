from pydantic import BaseModel
import datetime
from enum import Enum
from typing import Optional


class RateEnum(str, Enum):
    Péssimo = "Péssimo"
    Ruim = "Ruim"
    Regular = "Regular"
    Bom = "Bom"
    Muito_Bom = "Muito Bom"

class ReviewCreate(BaseModel):
    user_id: int
    game: str
    rate: Optional[RateEnum] = None
    text_review: str
