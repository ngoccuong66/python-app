from fastapi import APIRouter
from sqlalchemy.orm import Session
router = APIRouter()


@router.get("/login")
async def login():
    return {"user_name": "password"}
