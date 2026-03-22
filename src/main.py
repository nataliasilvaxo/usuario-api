from flask import Flask, jsonify, request
from conexion import coleccion
from models.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def inicio():
    id_usuario = request.args.get("id")
    nombre = request.args.get("nombre")
    correo = request.args.get("correo")

    if id_usuario and nombre and correo:
        try:
            usuario = Usuario(int(id_usuario), nombre, correo)
            coleccion.insert_one(usuario.to_dict())
            return jsonify({"mensaje": "Usuario guardado"})
        except Exception as e:
            return jsonify({"error": str(e)})

    return jsonify({"mensaje": "API funcionando"})

if __name__ == "_main_":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)