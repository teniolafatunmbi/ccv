import uvicorn, logging, traceback
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from api.cvv.router import router as cvv

from decouple import config

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

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
    return {"message": "Credit Card Validation API", "url": "http://127.0.0.1/docs"}


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    if isinstance(exc, HTTPException):
        raise exc
    logger.error(exc, exc_info=True)
    traceback_str = traceback.format_exc()
    logger.error(traceback_str)
    message = f"Error: {exc}\n\nTraceback:\n```{traceback_str}```\n"

    logger.error(message)
    print(exc)
    resp = { "detail": f"Internal server error" }
    ''
    if config('APP_ENV') != "production" and isinstance(exc, HTTPException):
        resp['context'] = exc.errors()
    return JSONResponse(content=resp, status_code=500)


if __name__ == "__main__":
    uvicorn.run("main:app", port=int(config('PORT')), reload=True)
