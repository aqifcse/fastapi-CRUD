from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.middleware('http')
async def hello_from_middleware(request: Request, call_next):
    response = await call_next(request)
    print("Hello! from middleware!!")
    return response


@app.exception_handler(404)
async def exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "message": "Oops! The page you're looking for does not exist."
        },
    )


@app.get('/')
async def hello_message():
    return {"message": "Hello World!!!"}
