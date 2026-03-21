import os
from pymongo import MongoClient

def get_coleccion():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    db = client["curso_python"]
    return db["usuarios"]