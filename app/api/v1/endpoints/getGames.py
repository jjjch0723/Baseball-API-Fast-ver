from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from app.db.connection import get_connection
from app.core.config import settings
import resources.getBaseBallRating as gbr # 예상결과
import resources.getCurKBOrslt as gckr # 최근 kbo경기 결과
import resources.getCurMLBrslt as gcmr # 최근 mlb경기 결과
import resources.getTodayKBOgame as gtkg # 오늘 kbo경기 일정
import resources.getTodayMLBgame as gtmg # 내일 mlb경기 일정

import logging

logger = logging.getLogger(__name__)

router = APIRouter()

#현재 버전 가져오기
@router.get("/version", response_model=dict)
async def get_version():
    return{"Application version" : settings.appVer}

#경기 일정 가져오기
@router.get("/schedule/process", response_model=dict)
async def processSchedule():
    kbo_list = gtkg.get_today_kbo_schedule()
    mlb_list = gtmg.get_today_mlb_schedule()

    fullScheule = []

    # 데이터 검증
    if kbo_list :
        fullScheule.extend(kbo_list)
    if mlb_list :
        fullScheule.extend(mlb_list)

    print(fullScheule)
    logger.info(fullScheule)

    if not fullScheule:
        return JSONResponse(content={"cheduled_matches": fullScheule}, status_code=200)
    
    return JSONResponse(content={"scheduled_matches":fullScheule}, status_code=200)

#경기 결과 가져오기
@router.get("/results/process", response_model=dict)
async def processResults():
    kbo_list = gckr.get_yesterday_kbo_results()
    mlb_list = gcmr.get_yesterday_mlb_results()

    fullResults = []
    
    # 데이터 검증
    if kbo_list : 
        fullResults.extend(kbo_list)
    if mlb_list : 
        fullResults.extend(mlb_list)

    print(fullResults)
    logger.info(fullResults)

    if not fullResults : 
        return JSONResponse(content={"matches_results": fullResults}, status_code=200)
    
    return JSONResponse(content={"matches_results": fullResults}, status_code=200)