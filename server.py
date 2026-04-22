#!/usr/bin/env python3
import http.server
import json
import os
import sys

PORT = 8765
DATA_FILE = 'reiskosten_data.json'

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/api/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    self.wfile.write(f.read().encode('utf-8'))
            else:
                self.wfile.write(b'{}')
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/data':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                json.loads(body)  # valideer JSON
                with open(DATA_FILE, 'w', encoding='utf-8') as f:
                    f.write(body.decode('utf-8'))
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"ok":true}')
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"ok":false,"error":"Ongeldige JSON"}')
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # geen log-output in terminal

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        httpd = http.server.HTTPServer(('localhost', PORT), Handler)
        print(f'✓ Reiskosten draait op http://localhost:{PORT}')
        print('  Sluit dit venster om de applicatie te stoppen.\n')
        httpd.serve_forever()
    except OSError:
        print(f'Poort {PORT} is al in gebruik. Is de app al gestart?')
        sys.exit(1)
