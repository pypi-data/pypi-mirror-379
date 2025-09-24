from time import sleep

from fastapi import FastAPI

from fastapi_yieldable_response import yieldable_response

app = FastAPI(title="FastAPI Express", version="0.1.0")


@app.get("/")
@yieldable_response
async def root():
    yield {"message": "Hello!"}
    sleep(2)
    print("ciao!")


@app.get("/{route}")
@yieldable_response
def route(route: str):
    yield {"message": f"Hello, you're visiting {route}!"}
    sleep(2)
    print("ciao!")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
