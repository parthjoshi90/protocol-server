from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    debug=True,
    title="Protocol Server",
    description="Protocol Server to connect the client seller App to ONDC Network",
    version="0.1.0",
)


@app.get("/")
def helth():
    return {"msg": "Hello World!"}


app.include_router(router)
