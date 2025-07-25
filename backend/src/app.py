from fastapi import FastAPI
from log_config import init_config
from logging import getLogger
from config import config

init_config()
logger = getLogger(__name__)

app = FastAPI()

@app.get('/')
async def root():
    return {"hello": "world"}