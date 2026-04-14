# Importamos APIRouter y dependencias
from fastapi import APIRouter, Depends, HTTPException

# Importamos la sesión de base de datos
from sqlalchemy.orm import Session

# Importamos la dependencia de DB
from app.db.database import get_db

# Importamos esquemas
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse

# Importamos lógica de negocio
from app.services.auth_service import create_user, authenticate_user, get_user_by_username


# Creamos el router
router = APIRouter()


# 📝 Registro de usuario
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    existing_user = get_user_by_username(db, user.username)

    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Crear usuario
    new_user = create_user(db, user)

    return new_user


# 🔐 Login de usuario
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(db, user.username, user.password)

    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {"message": "Autenticación satisfactoria"}