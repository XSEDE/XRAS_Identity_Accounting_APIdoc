from typing import List, Optional, Union
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_api_key, get_xa_requester

router = APIRouter(
    prefix="/action/api",
    tags=["actions"],
    dependencies=[Depends(get_api_key), Depends(get_xa_requester)],
    responses={},
)


class Resource(BaseModel):
    action_resource_id: Optional[int]
    resource_repository_key: str
    awarded_amount: int
    comments: str


class Role(BaseModel):
    request_people_role_id: Optional[int]
    role_type: str
    username: str
    begin_date: str
    end_date: str
    is_account_to_be_created: bool


class Action(BaseModel):
    action_id: Optional[int]
    action_type: str
    action_begin_date: str
    action_end_date: str
    request_id: str
    request_number: int
    request_type: str
    request_abstract: str
    request_title: str
    opportunity_id: int
    opportunity_type: str
    opportunity_name: str
    allocation_type: str
    award_date: str
    award_period: str
    resources: Union[List[Resource], None]
    roles: Union[List[Role], None]
    fos: str
    panels: str


@router.post("/actions/", response_model=Action)
async def create_action(action: Action):
    return {**action.dict(), "action_id": 1}
