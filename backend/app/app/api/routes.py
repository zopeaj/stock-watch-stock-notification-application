from fastapi import APIRouter
from app.api.controller.StockController import stockroutes
from app.api.controller.StockNotificationController import stocknotificationroutes
from app.api.controller.UserController import userroutes

api_router = APIRouter()

api_router.include_router(stockroutes, prefix="/stock", tags=["Stock"])
api_router.include_router(stocknotificationroutes, prefix="/stock-notification", tags=["Stock-Notification"])
api_router.include_router(userroutes, prefix="/user", tags=["User"])
