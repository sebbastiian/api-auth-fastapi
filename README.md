# API de Autenticación con FastAPI

## 📌 Descripción

Este proyecto consiste en el desarrollo de un servicio web (API REST) para el registro y autenticación de usuarios.

Permite:

* Registrar usuarios
* Iniciar sesión (login)
* Validar credenciales

Este proyecto fue desarrollado como evidencia académica, aplicando buenas prácticas utilizadas en entornos profesionales.

---

## 🚀 Tecnologías utilizadas

* Python
* FastAPI
* MySQL
* SQLAlchemy
* Pydantic
* Uvicorn
* Passlib (hash de contraseñas)
* Git y GitHub

---

## 📁 Estructura del proyecto

```
app/
│
├── main.py
│
├── core/
│   └── config.py
│
├── db/
│   └── database.py
│
├── models/
│   └── user.py
│
├── schemas/
│   └── user_schema.py
│
├── routes/
│   └── auth.py
│
├── services/
│   └── auth_service.py
```

---

## ⚙️ Instalación

### 1. Clonar repositorio

```
git clone <URL_DEL_REPOSITORIO>
cd api-auth-fastapi
```

### 2. Crear entorno virtual

```
python -m venv venv
```

### 3. Activar entorno

Windows:

```
# Activar entorno virtual (Windows PowerShell)
venv\Scripts\Activate.ps1

# En caso de error de permisos
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. Instalar dependencias

```
pip install -r requirements.txt
pip install bcrypt
pip install "passlib[bcrypt]" bcrypt==4.0.1
```

---

## 🗄️ Base de datos

Se utiliza MySQL.

Crear base de datos:

```sql
CREATE DATABASE auth_db;
```

Configurar credenciales en archivo `.env`:

```
DATABASE_URL=mysql+pymysql://usuario:password@localhost/auth_db
```

---

## ▶️ Ejecución del proyecto

```
uvicorn app.main:app --reload
```

Acceder a la documentación:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Endpoints

### 1. Registro de usuario

**POST** `/auth/register`

Body:

```json
{
  "username": "usuario",
  "email": "correo@example.com",
  "password": "12345678"
}
```

Respuesta:

```json
{
  "id": 1,
  "username": "usuario",
  "email": "correo@example.com"
}
```

---

### 2. Inicio de sesión

**POST** `/auth/login`

Body:

```json
{
  "username": "usuario",
  "password": "12345678"
}
```

Respuesta:

```json
{
  "message": "Autenticación satisfactoria"
}
```

---

## 🔒 Seguridad

* Las contraseñas se almacenan encriptadas usando bcrypt
* No se guardan contraseñas en texto plano

---

## 🧪 Pruebas

Se pueden realizar pruebas usando:

* Swagger (`/docs`)
* Postman
* cURL

---

## 👨‍💻 Autor

Proyecto desarrollado por:

**Sebastian**

---

## 📌 Estado del proyecto

✅ Funcional
✅ Cumple requerimientos
✅ Listo para entrega
