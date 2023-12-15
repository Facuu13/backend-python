from fastapi import FastAPI

app = FastAPI()

# comando para levantar el servidor: uvicorn main:app --reload

@app.get("/")
async def root():
    return "Hola FastAPI"

@app.get("/url")
async def url():
    return { "url_curso": "https://github.com/Facuu13/app-fullstack-base-2023-i09" }