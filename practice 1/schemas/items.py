from pydantic import BaseModel

class ItemsRequest(BaseModel):
    name:str
    work_time:str
