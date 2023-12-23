#!/usr/local/bin/python3
import mysql.connector
import json


def query_parser(query: str):
    result = {}
    key_value = query.split("&")

    for el in key_value:
        kw = el.split("=")
        result[kw[0]] = kw[1]
    return result


def show_databases():
    pass


def app(environ, start_response):
    # print(json.dumps(environ, indent=2))
    # print("Before parse: ", environ["QUERY_STRING"])
    # print("After: ", query_parser(environ["QUERY_STRING"]))

    param = [
        "REQUEST_URI",
        "QUERY_STRING",
        "REQUEST_METHOD",
        "REMOTE_ADDR",
        "REQUEST_SCHEME",
    ]

    start_response("200 OK", [("Content-type", "text/html")])
    return [
        bytes(
            f"""
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>CGI</title>
              </head>
              <body>
                <h1>CGI works</h1>
                <ul>
                    {"".join(f"<li>{k} = {environ[k]}</li>" for k in param)}
                </ul>
              </body>
            </html>
            """,
            "UTF-8",
        )
    ]
