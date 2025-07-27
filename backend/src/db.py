from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from config import config

mongo_url = None

if config.get('mongodb_user') != None and config.get('mongodb_pass') != None:
    mongo_url = f"mongodb://{config.get('mongodb_user')}:{config.get('mongodb_pass')}@{config.get('mongodb_host')}:{config.get('mongodb_port')}"
else:
    mongo_url= f"mongodb://{config.get('mongodb_host')}:{config.get('mongodb_port')}"

client = AsyncIOMotorClient(
    mongo_url
)
engine = AIOEngine(client,config.get('mongodb_database'))
