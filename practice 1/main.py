
from fastapi import FastAPI, HTTPException
import uvicorn
from requests import delete

from schemas.items import ItemsRequest
from db import create_item, get_item_by_id, del_item_by_id


app=FastAPI()

items={}

@app.get('/')
def root():
    return{'message':"The api has been started"}

@app.post('/items')
def create_items(item:ItemsRequest):
    item_dict=item.dict()
    res=create_item(item_dict)
    return {"message":"Succesfully Created","id":str(res.inserted_id)}

@app.get('/items')
def get_items(item_id:str):
    item=get_item_by_id(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete('/items')
def del_items(item_id:str):
    result=del_item_by_id(item_id)
    if result.deleted_count==1:
        return {"message": f"Item with ID {item_id} has been deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
