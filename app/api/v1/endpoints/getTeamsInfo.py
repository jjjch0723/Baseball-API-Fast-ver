from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from app.db.connection import get_connection
from app.core.config import settings
from app.db.queries import teamsInfo
from app.db.queries import teamInfo as ti
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

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