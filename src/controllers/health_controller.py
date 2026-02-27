from fastapi import APIRouter
from fastapi.responses import JSONResponse

health_controller_router = APIRouter()

@health_controller_router.get("/health")
async def chat():
    return JSONResponse(status_code=200, content={"content": "API is running."})