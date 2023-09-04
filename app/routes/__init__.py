from fastapi import APIRouter
from .retail import router as retail_routes
from .logistic import router as logistic_routes

router = APIRouter(prefix="/protocol")


router.include_router(retail_routes)
router.include_router(logistic_routes)
