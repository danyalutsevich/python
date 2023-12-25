import auth
import static


def router(environ, start_response):
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]
    start_response("200 OK", [("Content-type", "text/html")])
    match path:
        case "/auth":
            auth.routing(environ)
        case _:
            return static.static(environ)
