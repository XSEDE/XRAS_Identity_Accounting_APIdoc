from fastapi import FastAPI
from app.routers import usage
from app.routers import action
from app.routers import date
from app.routers import request
from app.routers import role

import uvicorn

app = FastAPI()

app.include_router(usage.router)
app.include_router(action.router)
app.include_router(date.router)
app.include_router(request.router)
app.include_router(role.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
