from fastapi import FastAPI
from app.api.endpoints import router as v1_router

app = FastAPI()

app.include_router(router=v1_router.router, prefix="/api/v1")
