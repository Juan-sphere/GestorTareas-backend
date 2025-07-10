from fastapi import FastAPI
from app.routers import auth, task

app = FastAPI(
    title="Gestor de Tareas",
    version="1.0",
    docs_url="/docs",  # Swagger
    redoc_url="/redoc"
)

app.include_router(auth.router)
app.include_router(task.router)
