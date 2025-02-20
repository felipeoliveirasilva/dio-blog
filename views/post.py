from pydantic import BaseModel
from datetime import datetime

class PostOut(BaseModel):
    title: str
    #author: str
    #published_at: datetime