from fastapi import FastAPI

app = FastAPI()


@app.get("/0")
async def get_0():
    return {"message": "Hello. I'm App 0"}


@app.get("/1")
async def get_1():
    return {"message": "Hello. I'm App 1"}


@app.get("/2")
async def get_2():
    return {"message": "Hello. I'm App 2"}


@app.get("/")
async def get():
    return {"message": "Hello. Choose /0, /1, or /2"}
