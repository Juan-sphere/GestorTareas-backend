from fastapi import FastAPI
from App.routers import auth, task

app = FastAPI(
    title="Gestor de Tareas",
    version="1.0",
    docs_url="/docs",  # Swagger
    redoc_url="/redoc"
)

app.include_router(auth.router)
app.include_router(task.router)

if __name__ == "__main__":
    from App.core.config import settings
    print(settings.DATABASE_URL)
    print(settings.SECRET_KEY)
