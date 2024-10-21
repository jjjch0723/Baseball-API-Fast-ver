import sys
import os

# 프로젝트의 루트 경로를 모듈 경로에 추가
project_root = r"E:\prj\Baseball-API-Fast-ver"
sys.path.append(project_root)

# 이제 app 모듈을 임포트할 수 있음
from app.db.connection import get_connection

def test_query():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("select now();")
            result = cursor.fetchall()
            cursor.close()
            print("현재 시각 : ", result)
    except Exception as err:
        print("db체크 드가자;", err)

if __name__ == "__main__":
    test_query()