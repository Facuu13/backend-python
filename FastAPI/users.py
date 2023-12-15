from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# comando para levantar el servidor: uvicorn users:app --reload

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id=1,name="Facu",surname="villa",url="google.com",age=28),
            User(id=2,name="alan",surname="villa",url="google.com",age=25),
            User(id=3,name="gina",surname="villa",url="google.com",age=23)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"Brais","surname":"Moure","url":"https://moure.dev","age":35},
            {"name":"Brais","surname":"Dev","url":"https://moure.dev","age":82}]

@app.get("/users")
async def users():
    return users_list

#path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#query
#http://127.0.0.1:8000/userquery/?id=1    
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)


def search_user(id:int):
    users= filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado un usuario"}