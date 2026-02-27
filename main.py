from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.controllers.health_controller import health_controller_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    pass
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(health_controller_router, prefix="/api")