def body_parser(environ):
    content_length = int(environ.get("CONTENT_LENGTH", 0))
    body = environ["wsgi.input"].read(content_length).decode("utf-8")
    return body
