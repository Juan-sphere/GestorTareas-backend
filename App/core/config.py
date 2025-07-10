from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

    def __str__(self):
        return f"DATABASE_URL: {self.DATABASE_URL}\nSECRET_KEY: {self.SECRET_KEY}"

settings = Settings()

# Ahora puedes hacer simplemente:
print(settings)
