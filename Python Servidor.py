from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)

        filename = os.path.join("C:\\Users\\Magnetist\\Desktop\\files", os.path.basename(self.path))

        with open(filename, "wb") as file:
            file.write(data)

        self.send_response(200)
        self.end_headers()

def run_server():
    server_address = ('', 1234)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    print('Servidor iniciado en el puerto 8000...')
    httpd.serve_forever()

run_server()
