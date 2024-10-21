import psycopg2
from psycopg2 import pool
from contextlib import contextmanager
from app.core.config import settings as db

#Postgresql 커넥션 풀 설정
try: 
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        minconect = 1,
        maxconect = 10,
        user = db.db_username,
        password = db.db_password,
        host = db.db_host,
        port = db.db_port,
        database = db.db_name
    )
    if connection_pool:
        print("db연결 성공")
except Exception as err:
    print("DB 체크 부탁", err)
    raise