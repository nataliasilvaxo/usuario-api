import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))
db = client["curso_python"]
coleccion = db["usuarios"]