from config import FRONTEND_URL
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import tasks_router

app = FastAPI(
    title="Менеджер задач API",
    description="Учебный API-проект для взаимодействия с React-клиентом",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)