from os import environ
import json
from typing import Optional
from loguru import logger

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"response": "helloworld"}
