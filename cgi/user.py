import mysql.connector


class User:
    queries = {"create": "Insert Into user (email,password) values(?,?);"}

    def __init__(self, connection: mysql.connector.MySQLConnection):
        self.connection = connection

    def create(self, email: str, password: str):
        with self.connection.cursor() as cursor:
            cursor.execute(self.queries["create"], params=[email, password])
