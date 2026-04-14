# Importamos sesión de base de datos
from sqlalchemy.orm import Session

# Importamos el modelo User
from app.models.user import User

# Importamos esquemas
from app.schemas.user_schema import UserCreate

# Importamos herramientas de encriptación
from passlib.context import CryptContext


# Configuración de encriptación
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 🔐 Función para hashear contraseña
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# 🔐 Función para verificar contraseña
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# 👤 Crear usuario (registro)
def create_user(db: Session, user: UserCreate):
    # Encriptar contraseña
    hashed_password = hash_password(user.password)

    # Crear instancia del usuario
    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    # Guardar en la base de datos
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# 🔎 Buscar usuario por username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


# 🔑 Autenticación (login)
def authenticate_user(db: Session, username: str, password: str):
    # Buscar usuario
    user = get_user_by_username(db, username)

    if not user:
        return None

    # Verificar contraseña
    if not verify_password(password, user.password):
        return None

    return user