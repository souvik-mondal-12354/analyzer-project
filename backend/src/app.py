from fastapi import FastAPI
from log_config import init_config
from logging import getLogger
from config import config
from routes.analysis_graph_router import analysis_graph_router


init_config()
logger = getLogger(__name__)

app = FastAPI()

@app.get('/')
async def root():
    return {"hello": "world"}


app.include_router(analysis_graph_router, prefix="/graph")