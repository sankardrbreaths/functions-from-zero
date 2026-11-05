from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn

from mylib.bot import get_summary
from pydantic import BaseModel

app = FastAPI()


class Wiki(BaseModel):
    name: str
    length: int = 1


@app.post("/predict")
async def predict_story(wiki: Wiki):
    summary = get_summary(wiki.name, wiki.length)
    payload = {"wikipage": summary}
    return JSONResponse(content=jsonable_encoder({"summary": payload}))


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/add/{a}/{b}")
async def add_numbers(a: int, b: int):
    return {"sum": a + b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
