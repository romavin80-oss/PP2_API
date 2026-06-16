# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import os
import pyodbc
import psycopg2
from dotenv import load_dotenv

load_dotenv()

MS_USER = os.getenv("MS_SQL_USER")
MS_KEY = os.getenv("MS_SQL_KEY")
MS_SERVER = os.getenv("MS_SQL_SERVER")
MS_DB = os.getenv("MS_SQL_DATABASE")
MS_DRIVER = os.getenv("MS_SQL_DRIVER")


def connect_to_ms_sql():
    try:
        conn_str = (
            f"DRIVER={{{MS_DRIVER}}};"
            f"SERVER={MS_SERVER};"
            f"DATABASE={MS_DB};"
            f"UID={MS_USER};"
            f"PWD={MS_KEY};"
        )
        connection = pyodbc.connect(conn_str)
        print(" Успешное подключение к MS SQL Server!")
        return connection
    except Exception as e:
        print(f" Ошибка подключения к MS SQL: {e}")
        return None

PG_USER = os.getenv("POSTGRESQL_USER")
PG_DB = os.getenv("POSTGRES_DATABASE_DOCKER")
PG_PASSWORD = os.getenv("POSTGRES_PASSWORD_DOCKER")
PG_HOST = os.getenv("POSTGRESQL_HOST_DOCKER")
PG_PORT = os.getenv("POSTGRESQL_PORT_DOCKER")


def connect_to_postgres():
    try:
        connection = psycopg2.connect(
            host=PG_HOST,
            port=PG_PORT,
            database=PG_DB,
            user=PG_USER,
            password=PG_PASSWORD
        )
        print(f" Успешное подключение к PostgreSQL в Docker ({PG_HOST}:{PG_PORT})!")
        return connection
    except Exception as e:
        print(f" Ошибка подключения к PostgreSQL в Docker: {e}")
        return None

if __name__ == "__main__":
    print("Инициализация приложения...")

    if os.getenv("CACHE_ENABLED") == "True":
        print(f" Кэш включен. Локация: {os.getenv('CACHE_LOCATION')}")

    ms_sql_conn = connect_to_ms_sql()
    postgres_conn = connect_to_postgres()

    if ms_sql_conn:
        ms_sql_conn.close()
    if postgres_conn:
        postgres_conn.close()
