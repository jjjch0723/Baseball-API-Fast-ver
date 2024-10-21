# Baseball-API-Fast-ver

## 목차
1. [Baseball API란](#11-baseball-api란)  
    1.1. [Baseball API란](#11-baseball-api란)  
2. [Baseball API 아키텍처 구조](#21-baseball-api-아키텍처-구조)  
    2.1. [Baseball API 프로젝트 구조](#22-baseball-api-프로젝트-구조)  
3. [상세 설명](#31-상세-설명)  
    3.1. [Python 스크립트](#31-python-스크립트)  
    3.2. [FastAPI 설명 및 사용법](#32-api-설명-및-사용법)  
    3.3. [팀코드](#33-팀코드)
4. [느낀점 및 보완점](#41-느낀점-및-보완점)  
    4.1. [느낀점](#41-느낀점)  
    4.2. [보완점](#42-보완점)


---

## 1.1 Baseball API란


---

## 1.1 Baseball API란

이 프로젝트는 Restful 로 설계된 현 baseball api를 Fast 로 바꾸는 리펙토링 프로젝트입니다. 

아래는 baseball api의 깃 주소입니다.<br>
[baseball api 링크](https://github.com/jjjch0723/BaseBall_API)

---

## 2.1 Baseball API 프로젝트 구조
```
Baseball-API-Fast-ver/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           ├── baseball.py         # API 엔드포인트 정의
│   │           └── __init__.py
│   ├── core/
│   │   ├── batch_config.py             # 배치 관련 설정
│   │   ├── config.py                   # 설정 파일 (BaseSettings 사용)
│   │   └── __init__.py
│   ├── db/
│   │   ├── connection.py               # PostgreSQL 연결 풀 설정
│   │   ├── session.py                  # DB 세션 관리
│   │   └── __init__.py
│   ├── service/
│   │   ├── batch.py                    # 배치 서비스 로직
│   │   ├── ml.py                       # AI 관련 서비스 로직
│   │   └── __init__.py
│   ├── util/
│   │   ├── json_manager.py             # JSON 파일 읽기/쓰기 유틸리티
│   │   └── __init__.py
│   ├── test/
│   │   ├── connection_test.py          # DB 연결 테스트 코드
│   │   └── __init__.py
│   └── main.py                         # FastAPI 애플리케이션의 진입점
├── .env                                # 환경 변수 파일
├── Dockerfile                          # Docker 설정 파일
├── requirements.txt                    # Python 의존성 목록
└── .gitignore                          # Git에서 제외할 파일 목록
```
