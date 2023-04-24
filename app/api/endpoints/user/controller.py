from sqlalchemy import select
from sqlalchemy.orm import Session
from app.third_parties.sqlite.model.user import User
from fastapi import HTTPException
session = Session()

async def ctr_login():
    print("hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
    try:
        print("1")
        data_response = session.execute(
            select(
                User
            )
        ).all()
    except Exception as e:
        print("2")
        return HTTPException(status_code=404, detail=e)
    return {
        "data": data_response
    }
