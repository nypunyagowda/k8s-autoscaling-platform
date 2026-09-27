
from http.server import BaseHTTPRequestHandler, HTTPServer
import hashlib
import os
import socket


class AppHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.respond(
                200,
                f"Hello from Kubernetes! Pod: {socket.gethostname()}"
            )

        elif self.path == "/health":
            self.respond(200, "Healthy")

        elif self.path == "/work":
            result = b"autoscaling-demo"

            # CPU-intensive task to generate load
            for _ in range(250_000):
                result = hashlib.sha256(result).digest()

            self.respond(
                200,
                f"Work completed by pod: {socket.gethostname()}"
            )

        else:
            self.respond(404, "Not Found")

    def respond(self, status, message):
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), AppHandler)
    print(f"Server running on port {port}")
    server.serve_forever()