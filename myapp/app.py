from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello from my Python app!\n")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    print("Server started on port 8000")
    server.serve_forever()
# trigger
# trigger Чт 12 ноя 2026 23:11:38 MSK
