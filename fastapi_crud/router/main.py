from fastapi.routing import APIRouter

from . import auth, user

router = APIRouter()
router.include_router(auth.router, tags=["Auth"])
router.include_router(user.router, prefix="/profile", tags=["User"])
