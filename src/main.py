import os
from flask import Flask, jsonify
from conexion import coleccion
from models.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({"mensaje": "API funcionando"})

@app.route("/insertar/<int:id>/<nombre>/<correo>")
def insertar(id, nombre, correo):
    try:
        usuario = Usuario(id, nombre, correo)
        coleccion.insert_one(usuario.to_dict())
        return jsonify({"mensaje": "Usuario guardado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "_main_":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)