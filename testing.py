from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1:{"name":"biswatosh", "age":30},
    2:{"name":"amarendra", "age":45},
    3:{"name":"bainak", "age":45}
}

class User(BaseModel):
    name:str
    age:int

@app.put("/user_db/data/v1/update/{user_id}")
def user_update(user_id:int, user):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {"message": "User Updated successfully", "user": user_db[user_id]}
    else:
        return {"message":"User not found"}

@app.delete("/user_db/data/v1/delete/{user_id}")    
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}


