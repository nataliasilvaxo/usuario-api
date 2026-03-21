from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

from conexion import get_coleccion
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
        ruta = self.path.strip()
        print("RUTA RECIBIDA:", ruta, flush=True)

        if ruta == "/":
            self.responder({"mensaje": "API funcionando"})
            return

        if ruta.startswith("/insertar/"):
            try:
                partes = ruta.split("/")

                # ['', 'insertar', '99999', 'Natalia', 'silva_u.com']
                id_usuario = int(partes[2])
                nombre = partes[3]
                correo = partes[4]

                usuario = Usuario(id_usuario, nombre, correo)
                coleccion = get_coleccion()
                coleccion.insert_one(usuario.to_dict())

                self.responder({"mensaje": "Usuario guardado correctamente"})
            except Exception as e:
                print("ERROR:", str(e), flush=True)
                self.responder({"error": str(e)}, 500)
            return

        self.responder({"error": "Ruta no encontrada"}, 404)


if __name__ == "_main_":
    port = int(os.getenv("PORT", 8000))
    print("Servidor corriendo en puerto", port, flush=True)
    servidor = HTTPServer(("0.0.0.0", port), Servidor)
    servidor.serve_forever()