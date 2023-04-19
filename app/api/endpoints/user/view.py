from fastapi import APIRouter

router = APIRouter()


@router.get("/login")
async def login():
    return {"user_name": "password"}


@router.post("/login")
async def login():
    return {"user_name": "password"}
