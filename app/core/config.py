from pydantic import BaseSettings

#.env와 변수명으로 매핑되어 설정값 찾음 
class Setting(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

    class Config:
        env_file = ".env" #루트 디렉토리의 환경변수(.env파일) 로드

settings = Setting() #객체 생성