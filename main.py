from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/doanything/{name}")
async def say_hello(name: str):
    return name