from fastapi import FastAPI
from app.db import Base, engine
from app.api.v1 import user, company, settings, asdf, staff
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

app.include_router(asdf)
app.include_router(user)
app.include_router(company)
app.include_router(staff)
app.include_router(settings)