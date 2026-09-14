"""Dependency-free demo server used when Flask is unavailable locally."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

from app.interface import Interface


class Handler(BaseHTTPRequestHandler):
    def _send(self, payload, status=200):
        body = payload.encode() if isinstance(payload, str) else json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/get_test":
            self._send("Hello World", 200)
        elif path == "/tasks":
            self._send(Interface.get_all_tasks())
        elif path == "/projects":
            self._send(Interface.get_all_projects())
        elif path == "/users":
            self._send(Interface.get_all_users())
        elif path == "/":
            self._send({"name": "TaskApp", "status": "running", "routes": ["/tasks", "/projects", "/users"]})
        else:
            self._send({"error": "Not found"}, 404)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        try:
            data = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            data = {}
        path = urlparse(self.path).path
        if path == "/task":
            task = Interface.create_task(data.get("title", ""), data.get("description", ""), data.get("priority", "Normal"), data.get("projectParent", ""), data.get("deadline", ""))
            self._send(task, 201)
        elif path == "/invite":
            username = data.get("username", "").strip()
            self._send({"error": "Username cannot be empty"}, 400) if not username else self._send({"message": f"Invited {username} to project {data.get('projectId', 'p1')}"})
        elif path in ("/post_test", "/register"):
            self._send({}, 201)
        else:
            self._send({"error": "Not found"}, 404)

    def log_message(self, fmt, *args):
        print("[TaskApp] " + (fmt % args))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()
    print(f"TaskApp demo running at http://127.0.0.1:{args.port}")
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
