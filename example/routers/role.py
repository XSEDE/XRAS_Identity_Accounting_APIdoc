from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/v1/roles",
    tags=["role"],
    dependencies=[],
    responses={},
)


@router.post("/{requestNumber}/pi/{username}", status_code=status.HTTP_200_OK)
async def set_pi(*, requestNumber: int, username: str):
    if requestNumber is None or username is None:
        raise HTTPException(status_code=400)
    return ""


@router.post("/{requestNumber}/co_pi/{username}", status_code=status.HTTP_200_OK)
async def set_co_pi(*, requestNumber: int, username: str):
    if requestNumber is None or username is None:
        raise HTTPException(status_code=400)
    return ""


@router.delete("/{requestNumber}/co_pi/{username}", status_code=status.HTTP_200_OK)
async def remove_co_pi(*, requestNumber: int, username: str):
    if requestNumber is None or username is None:
        raise HTTPException(status_code=400)
    return ""


@router.post("/{requestNumber}/allocation_manager/{username}", status_code=status.HTTP_200_OK)
async def add_allocation_manager(*, requestNumber: int, username: str):
    if requestNumber is None or username is None:
        raise HTTPException(status_code=400)
    return ""


@router.delete("/{requestNumber}/allocation_manager/{username}", status_code=status.HTTP_200_OK)
async def remove_allocation_manager(*, requestNumber: int, username: str):
    if requestNumber is None or username is None:
        raise HTTPException(status_code=400)
    return ""
