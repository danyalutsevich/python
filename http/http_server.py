from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys
import importlib
import appsettings
import uuid
import json
import time

sys.path.append(appsettings.CONTROLLERS_PATH)
# import HomeController


class MainHandler(BaseHTTPRequestHandler):
    sessions = dict()

    # def __init__(self):
    # self.load_sessions()
    # print(self.sessions)

    def send_file(self, path):
        if ".." in path:
            self.send_404()
            return

        if os.path.isfile(path):
            ext = path.split(".")[-1] if "." in path else ""
            if ext in ("html", "css"):
                content_type = "text/" + ext
            elif ext == "js":
                content_type = "text/javascript"
            elif ext in ("png", "bmp", "gif"):
                content_type = "image/" + ext
            elif ext == "ico":
                content_type = "image/x-icon"
            elif ext in ("py", "env", "php", "exe", "log", "sql", "bat", "sh"):
                self.send_404()
                return
            else:
                content_type = "application/octet-stream"

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            with open(path, mode="rb") as file:
                self.wfile.write(file.read())
            return "file sent"

    def do_GET(self) -> None:
        url_parts = self.path.split("?")
        if len(url_parts) > 2:
            self.send_404()
            return
        path = url_parts[0]
        query = url_parts[1] if len(url_parts) > 1 else None

        path_parts = self.path.split("/")

        controller_name = (
            path_parts[1].capitalize() if path_parts[1] != "" else "Home"
        ) + "Controller"
        action_name = (
            path_parts[2].lower()
            if len(path_parts) > 2 and path_parts[2] != ""
            else "index"
        )
        # print(controller_name, action_name)
        try:
            # controller_module = getattr(sys.modules[__name__], controller_name)
            controller_module = importlib.import_module(controller_name)
            controller_class = getattr(controller_module, controller_name)
            controller_object = controller_class(self)
            controller_action = getattr(controller_object, action_name)
        except:
            controller_action = None

        self.response_headers = {}

        self.cookies = (
            dict((cookie.split("=") for cookie in self.headers["Cookie"].split("; ")))
            if "Cookie" in self.headers
            else {}
        )
        print(self.cookies)

        session_id = (
            self.cookies["session-id"]
            if "session-id" in self.cookies
            else str(uuid.uuid1())
        )
        if not session_id in MainHandler.sessions:
            MainHandler.sessions[session_id] = {
                "timestamp": time.time(),
                "session-id": session_id,
            }
            self.response_headers["Set-Cookie"] = f"session-id={session_id}"

        self.session = MainHandler.sessions[session_id]

        print(self.session)

        file = self.send_file(appsettings.PUBLIC_PATH + self.path)
        if file:
            return
        if controller_action:
            controller_action()
            return
        else:
            self.send_404()
            return

    def send_404(self):
        self.send_response(404)
        self.send_header("Status", "404 Not Found")
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Requested content dont exist")


def load_sessions():
    print("Loading sessions")
    with open(appsettings.SESSIONS_FILE_PATH, "r") as file:
        loaded = json.load(file)
        print(loaded)


def save_sessions(sessions):
    print("Saving sessions")
    with open(appsettings.SESSIONS_FILE_PATH, "w") as file:
        json.dump(sessions, file)


def main():
    load_sessions()
    server = HTTPServer(("127.0.0.1", 4343), MainHandler)
    try:
        print("Starting server on http://127.0.0.1:4343")
        server.serve_forever()
    except:
        save_sessions(MainHandler.sessions)
        print("Server stoped")


if __name__ == "__main__":
    main()
