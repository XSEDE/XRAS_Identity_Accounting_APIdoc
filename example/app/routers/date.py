from typing import List, Union

import databases
import sqlalchemy
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/v1/dates/requests",
    tags=["dates"],
    dependencies=[],
    responses={},
)


class Date(BaseModel):
    request_number: int
    request_begin_date: str
    request_end_date: str


dates = [Date(request_number=1, request_begin_date="1994-06-05", request_end_date="1997-08-05"),
         Date(request_number=2, request_begin_date="1996-08-05", request_end_date="1998-08-05"),
         Date(request_number=3, request_begin_date="1998-08-05", request_end_date="1999-08-05"),
         Date(request_number=4, request_begin_date="1997-05-03", request_end_date="1999-08-05"),
         Date(request_number=5, request_begin_date="2008-08-05", request_end_date="2009-08-05")]


@router.get("/", response_model=List[Date])
async def read_dates(request_numbers: Union[str, None] = None):
    results = []
    if request_numbers:
        request_numbers = [int(x) for x in request_numbers.split(',') if x.strip().isdigit()]
        # replace this with a call to the right table
        results = [r for r in dates if(r.request_number in request_numbers)]
    return results
