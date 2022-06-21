from fastapi import APIRouter, HTTPException
from typing import List, Union
from pydantic import BaseModel

router = APIRouter(
    prefix="/v1/usage",
    tags=["usage"],
    dependencies=[],
    responses={},
)


class Resource(BaseModel):
    resourceRepositoryKey: int
    usage: Union[List[str], None]


class Result(BaseModel):
    dates: Union[List[str], None]
    resource: Resource


class Response(BaseModel):
    message: str
    result: Result


@router.get("/by_month/{requestNumber}/{firstDate}/{lastDate}")
async def get_monthly_usage(*, requestNumber: int, firstDate: str, lastDate: str):
    if requestNumber == 0 or firstDate == "" or lastDate == "":
        raise HTTPException(status_code=404)
    resource = Resource(resourceRepositoryKey=11, usage=["0", "61.1", "0"])
    result = Result(dates=[firstDate, "date in between", lastDate], resource=resource)
    response = Response(message="", result=result)
    return response
