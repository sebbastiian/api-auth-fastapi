# Importamos FastAPI
from fastapi import FastAPI

# Importamos el motor y Base
from app.db.database import engine, Base

# Importamos las rutas
from app.routes import auth


# Crear la aplicación
app = FastAPI()


# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)


# Incluir rutas de autenticación
app.include_router(auth.router, prefix="/auth", tags=["Auth"])


# Ruta de prueba (opcional)
@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}