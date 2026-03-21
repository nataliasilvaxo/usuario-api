class Usuario:
    def _init_(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    def to_dict(self):
        return {
            "_id": self.id,
            "nombre": self.nombre,
            "correo": self.correo
        }