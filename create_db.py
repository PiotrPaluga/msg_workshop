from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable


def connect_db(command, user="postgres", password="coderslab", host="localhost", db=""):
    try:
        cnx = connect(user=user, password=password, host=host, database=db)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(command)
        cursor.close()
        cnx.close()
    except OperationalError as error:
        print(f"An error occured: {error}")


def create_db(cmd):
    try:
        connect_db(cmd, db="msg_workshop")
        print("Database created!")
    except DuplicateDatabase:
        print("Database already exist!")


def create_tbl(cmd):
    try:
        connect_db(cmd, db="msg_workshop")
        print("Table created!")
    except DuplicateTable:
        print("Table already exist!")


sql_cmd = "CREATE DATABASE msg_workshop;"

sql_cmd_2 = """CREATE TABLE users (
id SERIAL PRIMARY KEY,
username VARCHAR(255),
hashed_password VARCHAR(80)
);"""

sql_cmd_3 = """CREATE TABLE messages (
id SERIAL PRIMARY KEY,
from_id INT NOT NULL,
FOREIGN KEY (from_id) REFERENCES users(id),
to_id INT NOT NULL,
FOREIGN KEY(to_id) REFERENCES users(id),
creation_date TIMESTAMP,
text VARCHAR(255)
);"""

create_db(sql_cmd)
create_tbl(sql_cmd_2)
create_tbl(sql_cmd_3)
