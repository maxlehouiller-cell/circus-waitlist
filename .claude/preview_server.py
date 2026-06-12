#!/usr/bin/env python3
# Minimal static server that serves the project folder by ABSOLUTE path.
# Avoids `os.getcwd()` (blocked by the preview sandbox) by passing `directory=` explicitly.
import functools
import http.server
import socketserver

PORT = 8765
ROOT = "/Users/maxwelllehouiller/Desktop/Circus Website"

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)


class Server(socketserver.TCPServer):
    allow_reuse_address = True


with Server(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving {ROOT} at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
