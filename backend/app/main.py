from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routes import signup, login, shop, home


app = FastAPI()
app.include_router(home.router)

app.include_router(signup.router)
app.include_router(login.router)
app.include_router(shop.router)
