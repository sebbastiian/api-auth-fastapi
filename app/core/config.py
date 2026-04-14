# Importamos la librería para leer variables de entorno
import os

# Importamos load_dotenv para cargar el archivo .env
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()


# Clase de configuración
class Settings:
    # Variables de conexión a la base de datos
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")

    # Construcción de la URL de conexión a MySQL
    DATABASE_URL: str = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


# Instancia única de configuración
settings = Settings()