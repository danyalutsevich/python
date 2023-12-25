#!/usr/local/bin/python3

# uwsgi --ini app.ini

import mysql.connector
import json
import logging

db_credentials = {"host": "127.0.0.1", "user": "danlutsevich", "database": "python"}

logging.basicConfig(
    filename="log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def connect():
    try:
        connection = mysql.connector.connect(**db_credentials)

        if connection.is_connected():
            print("Connection OK")

        return connection

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")


def query_parser(query: str):
    result = {}
    key_value = query.split("&")

    for el in key_value:
        kw = el.split("=")
        result[kw[0]] = kw[1]
    return result


def show_databases(connection):
    sql = "SHOW DATABASES"
    dbs = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            # print(cursor.column_names)
            for row in cursor:
                dbs.append(row)
            return dbs
    except mysql.connector.Error as err:
        print(err)


def app(environ, start_response):
    # print(json.dumps(environ, indent=2))
    # print("Before parse: ", environ["QUERY_STRING"])
    # print("After: ", query_parser(environ["QUERY_STRING"]))
    logging.log(msg="LOGGER WORKS", level=logging.INFO)
    connection = connect()
    dbs = show_databases(connection)
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
                <h1>CGI Databases</h1>
                <ul>
                    {"".join(f"<li>{d}</li>" for d in dbs)}
                </ul>
                <h1>CGI Headers</h1>
                <ul>
                    {"".join(f"<li>{k} = {environ[k]}</li>" for k in param)}
                </ul>
              </body>
            </html>
            """,
            "UTF-8",
        )
    ]
