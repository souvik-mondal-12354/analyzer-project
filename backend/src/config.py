from os import getenv
from dotenv import load_dotenv

load_dotenv()

config = {
    "mongodb_host": getenv('MONGODB_HOST', 'localhost'),
    "mongodb_port": getenv('MONGODB_PORT', '27017'),
    "mongodb_user": getenv('MONGODB_USER', None),
    "mongodb_pass": getenv('MONGODB_PASS', None),
    "mongodb_database": getenv('MONGODB_DATABASE','analyzer')
}
