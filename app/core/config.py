from pydantic import BaseSettings

#.env와 변수명으로 매핑되어 설정값 찾음 
class Setting(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    appVer: str = "0.0.1" #앱 버전 추가

    class Config:
        env_file = ".env" #루트 디렉토리의 환경변수(.env파일) 로드

 #객체 생성
settings = Setting()

