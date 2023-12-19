from fastapi import FastAPI
from routers import products, users

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)


# comando para levantar el servidor: uvicorn main:app --reload

@app.get("/")
async def root():
    return "Hola FastAPI"

@app.get("/url")
async def url():
    return { "url_curso": "https://github.com/Facuu13/app-fullstack-base-2023-i09" }