import uvicorn, traceback
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from api.cvv.router import router as cvv

from decouple import config

def get_application():
    _app = FastAPI(title="Credit Card Validator")

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app

app = get_application()

app.mount("/app", StaticFiles(directory="./frontend", html=True), name="frontend")


app.include_router(cvv)

@app.get("/", tags=['Home'])
async def root():
    return {"message": "Credit Card Validation API", "url": "http://localhost:7001/docs"}


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    if isinstance(exc, HTTPException):
        raise exc

    print(exc)
    resp = { "detail": f"Internal server error" }
    return JSONResponse(content=resp, status_code=500)


if __name__ == "__main__":
    uvicorn.run("main:app", port=7001, reload=True)
