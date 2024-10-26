from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
from app.db.connection import get_connection
from app.core.config import settings