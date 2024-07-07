from pydantic import BaseModel
from typing import List

class TrendItem(BaseModel):
    name: str
    url: str
    tweet_volume: int
