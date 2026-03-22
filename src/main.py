from flask import Flask, jsonify, request
from conexion import coleccion
from models.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({"mensaje": "API funcionando"})

@app.route("/insertar")
def insertar():
    id_usuario = int(request.args.get("id"))
    nombre = request.args.get("nombre")
    correo = request.args.get("correo")

    usuario = Usuario(id_usuario, nombre, correo)
    coleccion.insert_one(usuario.to_dict())

    return jsonify({"mensaje": "Usuario guardado"})