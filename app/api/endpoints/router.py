from fastapi import APIRouter
from app.api.endpoints.user import view as router_user

router = APIRouter()

router.include_router(router=router_user.router)
