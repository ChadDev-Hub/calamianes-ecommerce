from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routes import user_route


app = FastAPI()

app.include_router(user_route.router)
