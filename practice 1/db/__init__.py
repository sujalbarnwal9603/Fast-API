from bson import ObjectId
from pymongo import MongoClient
from datetime import datetime

url='mongodb://localhost:27017'
client=MongoClient(url)
db=client['backend']

def create_item(item:dict):
    item['created_at']=datetime.utcnow()
    return db.items.insert_one(item)

def get_item_by_id(item_id:str):
    try:
        item=db.items.find_one({"_id":ObjectId(item_id)})
        if item:
            return {
                "id":str(item["_id"]),
                "name":item["name"],
                "work_time":item["work_time"],
                "created_at": item["created_at"].isoformat()
            }
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def del_item_by_id(item_id:str):
    try:
        result=db.items.delete_one({"_id":ObjectId(item_id)})
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None