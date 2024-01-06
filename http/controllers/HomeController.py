from http_server import MainHandler
import inspect
import appsettings
import os


class HomeController:
    def __init__(self, server: MainHandler) -> None:
        self.server = server
        self.short_name = self.__class__.__name__.removesuffix("Controller").lower()

    def index(self):
        view_path = f"{appsettings.VIEWS_PATH}/{self.short_name}/{inspect.currentframe().f_code.co_name}.html"
        self.return_view(view_path)

    def privacy(self):
        view_path = f"{appsettings.VIEWS_PATH}/{self.short_name}/{inspect.currentframe().f_code.co_name}.html"
        self.return_view(view_path)

    def return_view(self, action_name):
        layout_name = f"{appsettings.VIEWS_PATH}/_layout.html"
        if not os.path.isfile(action_name) or not os.path.isfile(layout_name):
            print("File not found")
            self.server.send_404()
            return

        with open(action_name) as action:
            with open(layout_name) as layout:
                self.server.send_response(200)
                self.server.send_header("Content-Type", "text/html")
                for k, v in self.server.response_headers.items():
                    self.server.send_header(k, v)

                self.server.end_headers()
                page = (
                    layout.read()
                    .replace("<render-body />", action.read())
                    .encode("UTF-8")
                )
                # print(page)
                self.server.wfile.write(page)
