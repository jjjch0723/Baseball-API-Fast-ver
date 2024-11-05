from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from app.db.connection import get_connection
from app.core.config import settings
from app.db.queries import teamsInfo
from app.db.queries import teamInfo as ti
from app.db.queries import position
from app.db.queries import players
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

# 전체 팀정보
@router.get("/teamsInfo",response_model=dict)
async def get_teams():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(teamsInfo)
            team_list = cursor.fetchall()
        result = [
            {
                "리그명": row[0],
                "팀명": row[1],
                "영어팀명": row[2],
                "과거팀명": row[3]
            }
            for row in team_list
        ]
        if not result:
            return JSONResponse(status_code=204, content={"message": "No teams found!"})
        
        return {"teams" : result}
    except Exception as e:
        logger.error(f"Error fetching teams: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching teams.")

# 특정 팀정보
@router.get("/teamInfo", response_model=dict)
async def get_teamInfo(teamcode : str):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(ti, (teamcode, ))
            team = cursor.fetchone()

        if not team:
            return JSONResponse(status_code=404, content={"message": "Team not found!"})

        result = {
            "리그명": team[0],
            "팀명": team[1],
            "영어팀명": team[2],
            "과거팀명": team[3]
        }
        return {"team": result}
    except Exception as e:
        logger.error(f"Error fetching team info for teamcode {teamcode}: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching team information.")

#포지션별 선수 모음
@router.get("/positionInfo", response_model=dict)
async def get_positionInfo(pos : str):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(position, (pos, ))
            posPlayers = cursor.fetchall()

        if not posPlayers:
            return JSONResponse(status_code=404, content={"message": "No players"})

        result = [
            {
                "리그명": row[0],
                "포지션": row[1],
                "이름": row[2],
                "팀명": row[3],
                "팀코드": row[4]
            }
            for row in posPlayers
        ]
        return {"players": result}
    except Exception as e:
        logger.error(f"Error fetching team info for position {pos}: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching position information.")
    
# 팀 26인로스터 정보
@router.get("/roster", response_model=dict)
async def get_roster(teamcode : str):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(players, (teamcode, ))
            roster = cursor.fetchall()

        if not roster:
            return JSONResponse(status_code=404, content={"message": "No players"})

        result = [
            {
                "리그명": row[0],
                "포지션": row[1],
                "이름": row[2],
                "팀명": row[3],
                "팀코드": row[4]
            }
            for row in roster
        ]
        return {"roster": result}
    except Exception as e:
        logger.error(f"Error fetching team info for position {teamcode}: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching position information.")
    