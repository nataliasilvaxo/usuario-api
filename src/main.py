from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
import os

from conexion import coleccion
from models.usuario import Usuario


class Servidor(BaseHTTPRequestHandler):

    def responder(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        ruta = parsed.path
        params = parse_qs(parsed.query)

        if ruta == "/":
            self.responder({"mensaje": "API funcionando. Usa /insertar"})

        elif ruta == "/insertar":
            try:
                id = int(params["id"][0])
                nombre = params["nombre"][0]
                correo = params["correo"][0]

                usuario = Usuario(id, nombre, correo)
                coleccion.insert_one(usuario.to_dict())

                self.responder({"mensaje": "Usuario guardado"})

            except Exception as e:
                self.responder({"error": str(e)}, 500)

        else:
            self.responder({"error": "Ruta no encontrada"}, 404)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    servidor = HTTPServer(("0.0.0.0", port), Servidor)
    print("Servidor corriendo...")
    servidor.serve_forever()