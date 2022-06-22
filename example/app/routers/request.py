from typing import List, Optional, Union

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from app.dependencies import get_api_key, get_xa_requester

router = APIRouter(
    prefix="/v1/requests",
    tags=["requests"],
    dependencies=[Depends(get_api_key), Depends(get_xa_requester)],
    responses={},
)


class Fos(BaseModel):
    xrasFosTypeId: int
    isPrimary: bool


class ProjectStates(BaseModel):
    date: str
    state: str


class SiteResource(BaseModel):
    resourceId: int
    resourceName: str
    resourceIsActive: bool
    projectOnResourceState: Optional[str] = None
    accountOnResourceState: Optional[str] = None


class AllocationOther(BaseModel):
    allocationId: int
    accountId: int
    requestId: int
    resourceId: int
    resourceName: str
    chargeNumber: str
    grantNumber: int
    proposalNumber: int
    siteResources: Union[List[SiteResource], None]


class Action(BaseModel):
    orderApplied: str
    actionType: str
    amount: int
    endDate: str
    dateApplied: str
    xrasActionId: int
    xrasActionResourceId: int


class AccountState(BaseModel):
    date: str
    state: str


class AccountOther(BaseModel):
    personId: int
    siteResources: Union[List[SiteResource], None]


class Account(BaseModel):
    usernames: str
    firstName: str
    middleName: str
    lastName: str
    roles: Union[List[str], None]
    usage: float
    accountStates: Union[List[AccountState], None]
    accountOther: Union[List[AccountOther], None]
    siteResources: Union[List[SiteResource], None]


class Allocation(BaseModel):
    actionType: str
    allocationBeginDate: str
    allocationEndDate: str
    allocatedAmount: float
    remainingAmount: float
    resourceRepositoryKey: str
    projectStates: Union[List[ProjectStates], None]
    allocationOther: Union[List[AllocationOther], None]
    xrasActionResourceId: int
    actions: Union[List[Action], None]
    accounts: Union[List[Account], None]


class Request(BaseModel):
    projectId: int
    requestType: str
    requestBeginDate: str
    requestEndDate: str
    allocationType: str
    projectTitle: str
    xrasActionIds: Union[List[int], None]
    fos: Union[List[Fos], None] = None
    allocations: Union[List[Allocation], None] = None


class Master(BaseModel):
    requestNumber: int
    requests: Union[List[Request], None]


class Project(BaseModel):
    projectIdLabel: str
    masters: Union[List[Master], None]


class Result(BaseModel):
    message: str = ""
    result: Project


@router.get("/request/{requestNumber}", response_model=Result)
async def read_field(*, requestNumber: int):
    if requestNumber > 100:
        return Project(projectIdLabel="project id", masters=[])

    fos = Fos(xrasFosTypeId=1, isPrimary=False)
    project_state = ProjectStates(date="date", state="state")
    action = Action(orderApplied="order", actionType="action", amount=10, endDate="date",
                    dateApplied="date", xrasActionId=1, xrasActionResourceId=1)
    site_resource = SiteResource(resourceId=1, resourceName="name", resourceIsActive=False,
                                 projectOnResourceState="project state")
    account_site_resource = SiteResource(resourceId=10, resourceName="name", resourceIsActive=False,
                                         accountOnResourceState="account state")
    allocation_other = AllocationOther(allocationId=1, accountId=1, requestId=1,
                                       resourceId=1, resourceName="name", chargeNumber="charge",
                                       grantNumber=1, proposalNumber=1, siteResources=[site_resource])
    account_state = AccountState(date="date", state="state")
    account_other = AccountOther(personId=1, siteResources=[account_site_resource])
    account = Account(usernames="jondoe", firstName="first name",
                      middleName="middle name", lastName="last name",
                      roles=["roles"], usage=33.3, accountStates=[account_state],
                      accountOther=[account_other], siteResources=[site_resource])
    allocation = Allocation(actionType="action", allocationBeginDate="date",
                            allocationEndDate="date", allocatedAmount=1.0,
                            remainingAmount=2.0, resourceRepositoryKey="key",
                            projectStates=[project_state], allocationOther=[allocation_other],
                            xrasActionResourceId=1, actions=[action], accounts=[account])
    request = Request(projectId=requestNumber, requestType="type", requestBeginDate="date",
                      requestEndDate="date", allocationType="allocation", projectTitle="title",
                      xrasActionIds=[1, 2, 3], fos=[fos], allocations=[allocation])
    master = Master(requestNumber=requestNumber, requests=[request])
    project = Project(projectIdLabel="id label", masters=[master])
    result = Result(message="", result=project)
    return result


@router.get("/role/pi/{username}", response_model=Result)
async def read_field(*, username: str):
    if username != "jondoe":
        raise HTTPException(status_code=404, detail=f"username={username} not found")

    account = Account(usernames="jondoe", firstName="Jon",
                      middleName="Donald", lastName="Doe",
                      roles=["roles"], usage=33.3, accountStates=[],
                      accountOther=[], siteResources=[])
    allocation = Allocation(actionType="action type", allocationBeginDate="date",
                            allocationEndDate="date", allocatedAmount=1.0,
                            remainingAmount=2.0, resourceRepositoryKey="key",
                            projectStates=[], allocationOther=[],
                            xrasActionResourceId=1, actions=[], accounts=[account])
    request = Request(projectId=5, requestType="type", requestBeginDate="date",
                      requestEndDate="date", allocationType="allocation", projectTitle="title",
                      xrasActionIds=[1, 2, 3], fos=[], allocations=[allocation])
    master = Master(requestNumber=5, requests=[request])
    project = Project(projectIdLabel="id label", masters=[master])
    result = Result(message="", result=project)
    return result


@router.get("/role/co_pi/{username}", response_model=Result)
async def read_field(*, username: str):
    if username != "jondoe":
        raise HTTPException(status_code=404, detail=f"username={username} not found")

    account = Account(usernames="jondoe", firstName="Jon",
                      middleName="Donald", lastName="Doe",
                      roles=["roles"], usage=33.3, accountStates=[],
                      accountOther=[], siteResources=[])
    allocation = Allocation(actionType="action type", allocationBeginDate="date",
                            allocationEndDate="date", allocatedAmount=1.0,
                            remainingAmount=2.0, resourceRepositoryKey="key",
                            projectStates=[], allocationOther=[],
                            xrasActionResourceId=1, actions=[], accounts=[account])
    request = Request(projectId=5, requestType="type", requestBeginDate="date",
                      requestEndDate="date", allocationType="allocation", projectTitle="title",
                      xrasActionIds=[1, 2, 3], fos=[], allocations=[allocation])
    master = Master(requestNumber=5, requests=[request])
    project = Project(projectIdLabel="id label", masters=[master])
    result = Result(message="", result=project)
    return result


@router.get("/role/allocation_manager/{username}", response_model=Result)
async def read_field(*, username: str):
    if username != "jondoe":
        raise HTTPException(status_code=404, detail=f"username={username} not found")

    project = Project(projectIdLabel="Jon Doe's project", masters=[])
    result = Result(message="", result=project)
    return result


@router.get("/user/{username}", response_model=Result)
async def read_field(*, username: str):
    if username != "jondoe":
        raise HTTPException(status_code=404, detail=f"username={username} not found")

    account = Account(usernames="jondoe", firstName="Jon",
                      middleName="Donald", lastName="Doe",
                      roles=["roles"], usage=33.3, accountStates=[],
                      accountOther=[], siteResources=[])
    allocation = Allocation(actionType="action type", allocationBeginDate="date",
                            allocationEndDate="date", allocatedAmount=1.0,
                            remainingAmount=2.0, resourceRepositoryKey="key",
                            projectStates=[], allocationOther=[],
                            xrasActionResourceId=1, actions=[], accounts=[account])
    request = Request(projectId=5, requestType="type", requestBeginDate="date",
                      requestEndDate="date", allocationType="allocation", projectTitle="title",
                      xrasActionIds=[1, 2, 3], fos=[], allocations=[allocation])
    master = Master(requestNumber=5, requests=[request])
    project = Project(projectIdLabel="id label", masters=[master])
    result = Result(message="", result=project)
    return result
