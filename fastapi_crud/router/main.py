from fastapi.routing import APIRouter

from . import auth

router = APIRouter()
router.include_router(auth.router, tags=["Auth"])