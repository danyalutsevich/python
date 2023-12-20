#!/usr/local/bin/python3

# import os
# envs = os.environ


def app(environ, start_response):
    start_response("200 OK", [("Content-type", "text/html")])
    return [
        b"<html><head><title>Simple CGI App</title></head><body><h1>Hello, CGI World!</h1><p>This is a simple CGI application.</p></body></html>"
    ]
