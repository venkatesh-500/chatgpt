"""Main app handler"""
from fastapi import FastAPI
import fake_user
import use_headers
import using_openai

app = FastAPI()

app.include_router(router=fake_user.router, prefix='/fake_user')
app.include_router(router=use_headers.router, prefix='/using_headers')
app.include_router(router=using_openai.router, prefix='/openai')
