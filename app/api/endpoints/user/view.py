from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.api.endpoints.user.controller import ctr_login

router = APIRouter()


@router.get("/login")
async def login():
    print('hmmmmmmmmmmmm')
    response_data = await ctr_login()
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    return {"user_name": response_data}
