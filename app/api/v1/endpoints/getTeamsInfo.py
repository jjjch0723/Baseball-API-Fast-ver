from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from app.db.connection import get_connection
from app.core.config import settings
from app.db.queries import teamsInfo
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
