import os
from pymongo import MongoClient

def get_coleccion():
    uri = os.getenv("MONGO_URI")
    if not uri:
        raise Exception("No existe la variable de entorno MONGO_URI")

    client = MongoClient(uri)
    db = client["curso_python"]
    return db["usuarios"]