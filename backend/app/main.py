from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routes import signup, login, shop, home
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
                   )
app.include_router(home.router)
app.include_router(signup.router)
app.include_router(login.router)
app.include_router(shop.router)
