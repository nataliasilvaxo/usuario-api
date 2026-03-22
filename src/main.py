from flask import Flask, jsonify, request
from conexion import coleccion
from models.usuario import Usuario
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({"prueba": "version nueva"})

if __name__ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)