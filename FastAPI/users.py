from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# comando para levantar el servidor: uvicorn users:app --reload

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(name="Facu",surname="villa",url="google.com",age=28),
            User(name="alan",surname="villa",url="google.com",age=25),
            User(name="gina",surname="villa",url="google.com",age=23)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"Brais","surname":"Moure","url":"https://moure.dev","age":35},
            {"name":"Brais","surname":"Dev","url":"https://moure.dev","age":82}]

@app.get("/users")
async def users():
    return users_list