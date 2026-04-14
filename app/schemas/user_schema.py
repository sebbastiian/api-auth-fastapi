# Importamos BaseModel de Pydantic
from pydantic import BaseModel, EmailStr


# Esquema para crear usuario (registro)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Esquema para login
class UserLogin(BaseModel):
    username: str
    password: str


# Esquema para respuesta (opcional pero profesional)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True