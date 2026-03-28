import psycopg2
from psycopg2 import pool
from app.core.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

connection_pool = None


def get_pool():
    global connection_pool
    if connection_pool is None:
        connection_pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=5,
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    return connection_pool


def get_connection():
    return get_pool().getconn()


def release_connection(conn):
    get_pool().putconn(conn)
