from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from app.db.connection import get_connection
from app.core.config import settings
from app.db.queries import teamsInfo
from app.db.queries import teamInfo as ti
from app.db.queries import position
from app.db.queries import players
from app.db.queries import teamPos
from app.db.queries import bat_status
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
    
#특정 팀 특정포지션
@router.get("/teamInfo/position", response_model=dict)
async def get_teamPosition(teamcode: str, pos: str):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(teamPos, (teamcode, pos))
            team_positions = cursor.fetchall()

            if not team_positions:
                return JSONResponse(status_code=404, content={"message": "Check the teamcode and position"})

            result = []
            for teamPos_ in team_positions:
                teamPos_ = list(teamPos_)

                # 포지션에 따른 변환
                if teamPos_[2] == 'P':
                    teamPos_[2] = "Pitcher"
                elif teamPos_[2] == 'LF':
                    teamPos_[2] = "Left Fielder"
                elif teamPos_[2] == 'CF':
                    teamPos_[2] = "Center Fielder"
                elif teamPos_[2] == 'RF':
                    teamPos_[2] = "Right Fielder"
                elif teamPos_[2] == '1B':
                    teamPos_[2] = "First Baseman"
                elif teamPos_[2] == '2B':
                    teamPos_[2] = "Second Baseman"
                elif teamPos_[2] == '3B':
                    teamPos_[2] = "Third Baseman"
                elif teamPos_[2] == 'SS':
                    teamPos_[2] = "Shortstop"
                elif teamPos_[2] == 'C':
                    teamPos_[2] = "Catcher"

                # 결과에 추가
                result.append({
                    "리그명": teamPos_[0],
                    "이름": teamPos_[1],
                    "포지션": teamPos_[2],
                    "팀명": teamPos_[3]
                })

            return {"result": result}
    except Exception as e:
        logger.error(f"error : {e}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching position information.")


@router.get("/teamInfo/status/bat", response_model=dict)
async def get_status(league : str, year : str):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(bat_status, (league, year))
            batStatus = cursor.fetchall()

            if not batStatus:
                return JSONResponse(status_code=404, content={"message": "Check the teamcode and position"})

            result = []

            for row in batStatus:
                result.append({
                    "팀명_KR": row[0],
                    "팀명_US": row[1],
                    "타석": row[2],
                    "안타": row[3],
                    "2루타": row[4],
                    "3루타": row[5],
                    "홈런": row[6],
                    "타점": row[7],
                    "도루": row[8],
                    "도루실패": row[9],
                    "볼넷": row[10],
                    "삼진": row[11],
                    "타율": row[12],
                    "출루율": row[13],
                    "장타율": row[14]
                })

            return {"result": result}
    except Exception as e:
        logger.error(f"error : {e}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching position information.")
