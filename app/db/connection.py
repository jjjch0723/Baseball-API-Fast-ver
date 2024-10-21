import psycopg2
from psycopg2 import pool
from contextlib import contextmanager
from app.core.config import settings

#Postgresql 커넥션 풀 설정
try:
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        user=settings.db_username,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port,
        database=settings.db_name
    )
    if connection_pool:
        print("db연결 성공")
except Exception as err:
    print("DB 체크 부탁", err)
    raise

#컨텍스트 매니져로 DB연결 관리
@contextmanager
def get_connection():
    connection = None
    try:
        connection = connection_pool.getconn()
        yield connection
    except Exception as err:
        print("DB연결 중에 오류 발생", err)
        raise
    finally:
        if connection is True:
            connection_pool.putconn(connection)

#커넥션 풀 종료
def close_conncetion():
    if connection_pool:
        connection_pool.closeall()
    
