from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
import os

from conexion import coleccion
from models.usuario import Usuario


class Servidor(BaseHTTPRequestHandler):

    def responder(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        print("PATH COMPLETO:", repr(self.path), flush=True)

        if self.path == "/" or self.path == "":
            self.responder({"mensaje": "API funcionando. Usa /insertar"})
            return

        if self.path.startswith("/insertar"):
            try:
                parsed = urlparse(self.path)
                params = parse_qs(parsed.query)

                print("PARAMS:", params, flush=True)

                id = int(params["id"][0])
                nombre = params["nombre"][0]
                correo = params["correo"][0]

                usuario = Usuario(id, nombre, correo)
                coleccion.insert_one(usuario.to_dict())

                self.responder({"mensaje": "Usuario guardado"})
            except Exception as e:
                self.responder({"error": str(e)}, 500)
            return

        self.responder({"error": f"Ruta no encontrada: {self.path}"}, 404)


if __name__ == "_main_":
    port = int(os.getenv("PORT", 8000))
    servidor = HTTPServer(("0.0.0.0", port), Servidor)
    print("Servidor corriendo...", flush=True)
    servidor.serve_forever()