from fastapi import FastAPI
import uvicorn
from app.config.db.config_db import Base, engine

from app.routers import router

app = FastAPI()

Base.metadata.create_all(engine)


app.include_router(router.router)
