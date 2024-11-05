from fastapi import FastAPI
from app.api.v1.endpoints.getGames import router as get_game_router
from app.api.v1.endpoints.getTeamsInfo import router as get_teams_router
import uvicorn

app = FastAPI()

app.include_router(get_game_router, prefix="/api/v1", tags=["version", "schedule", "results"])
app.include_router(get_teams_router, prefix="/api/v1", tags=["teamsInfo", "teamInfo", "position"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
