from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["curso_python"]
coleccion = db["usuarios"]

print("Conexión exitosa")