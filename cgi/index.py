#!/usr/local/bin/python3
# uwsgi --ini app.ini

import mysql.connector
import json
import logging
import router
from user import *

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


def show_databases(connection: mysql.connector.MySQLConnection):
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
    connection = connect()
    # dbs = show_databases(connection)
    # return router.router(environ)
    return router.router(environ, start_response)

   
    # with open("index.html", mode="r") as file:
        # return [bytes(file.read().replace("headers", str(environ)), "UTF-8")]
