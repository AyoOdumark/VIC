import datetime
from redis_om import HashModel

class Message(HashModel):
    role: str
    content: str
    created_at: datetime.datetime = datetime.datetime.now()