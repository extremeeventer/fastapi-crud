from fastapi import FastAPI

from fastapi_crud.router.main import router

app = FastAPI()
app.include_router(router)
