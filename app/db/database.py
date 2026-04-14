# Importamos el motor de SQLAlchemy
from sqlalchemy import create_engine
# Importamos sessionmaker para crear sesiones de base de datos
from sqlalchemy.orm import sessionmaker
# Importamos Base para los modelos
from sqlalchemy.orm import declarative_base
# Importamos la configuración que ya hicimos
from app.core.config import settings


# Crear el motor de conexión a la base de datos
engine = create_engine(
    settings.DATABASE_URL,
    echo=True  # Muestra las consultas SQL en consola (útil para desarrollo)
)


# Crear la sesión de conexión a la base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base para los modelos (clases que representan tablas)
Base = declarative_base()


# Dependencia para obtener la sesión en las rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()