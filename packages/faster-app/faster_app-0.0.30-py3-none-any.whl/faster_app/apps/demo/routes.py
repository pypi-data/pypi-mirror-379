from fastapi import APIRouter, Depends
from faster_app.settings import configs
from pydantic import BaseModel, Field
from faster_app.settings import logger
from faster_app.apps.demo.models import DemoModel
from tortoise_pagination import Pagination, Page
from tortoise.contrib.pydantic import pydantic_model_creator
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/demo", tags=["demo"])

# 创建 Pydantic 模型用于序列化
DemoModelPydantic = pydantic_model_creator(DemoModel, name="DemoModel")


class DemoRequest(BaseModel):
    message: str = Field(default="world")


@router.post("/")
async def demo(request: DemoRequest):
    logger.info(f"demo request: {request}")
    return JSONResponse(
        content={
            "message": f"Make {configs.PROJECT_NAME}",
            "version": configs.VERSION,
            "hello": request.message,
        },
        status_code=200,
    )


@router.get("/models")
async def pagination(
    pagination: Pagination = Depends(Pagination.from_query),
) -> Page[DemoModelPydantic]:
    return await pagination.paginated_response(DemoModel.all(), DemoModelPydantic)
