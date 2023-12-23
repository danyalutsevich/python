import mysql.connector

db_credentials = {"host": "127.0.0.1", "user": "danlutsevich", "database": "mysql"}
try:
    connection = mysql.connector.connect(
        **db_credentials
    )

    if connection.is_connected():
        print("Connection OK")

    sql = "SHOW DATABASES"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            print(cursor.column_names)
            for row in cursor:
                print(row)
    except mysql.connector.Error as err:
        print(err)

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
