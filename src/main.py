from flask import Flask, jsonify, request
from conexion import coleccion
from models.usuario import Usuario
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({"mensaje": "API funcionando"})

@app.route("/insertar", strict_slashes=False)
def insertar():
    id_usuario = int(request.args.get("id"))
    nombre = request.args.get("nombre")
    correo = request.args.get("correo")

    usuario = Usuario(id_usuario, nombre, correo)
    coleccion.insert_one(usuario.to_dict())

    return jsonify({"mensaje": "Usuario guardado"})

if __name__ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)