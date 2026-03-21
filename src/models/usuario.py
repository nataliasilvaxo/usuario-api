from pymongo import MongoClient

class Usuario:

    def __init__(self,id, nombre, correo):
        self._id = id
        self.nombre = nombre
        self.correo = correo

        client = MongoClient("mongodb://localhost:27017/")
        db = client["curso_python"]
        self.coleccion = db["usuarios"]

    def al_dict(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "correo": self.correo
        }

    def crearUsuario(self):
        self.coleccion.insert_one(self.al_dict())
        print("Usuario creado")

    def leerUsuario(self):
        usuarios = self.coleccion.find({})
        for u in usuarios:
            print(u)

    def eliminarUsuario(self):
        self.coleccion.delete_one({"_id": self._id})
        print("Usuario eliminado")