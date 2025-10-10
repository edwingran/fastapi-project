# 🚀 FastAPI Learning Project

Este proyecto fue desarrollado como parte de mi proceso de aprendizaje con **FastAPI**.  
Aquí practico conceptos fundamentales de desarrollo backend con Python, creación de endpoints, validaciones con Pydantic y manejo básico de datos en memoria.

---

## 📁 Estructura del proyecto

curso-fastapi-project/

├── main.py # Archivo principal con los endpoints

├── models.py # Modelos de datos con Pydantic

├── requirements.txt # Dependencias del proyecto

└── README.md # Documentación del proyecto


---

## ⚙️ Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/edwingran/fastapi-project.git
cd fastapi-project
```

### 2️⃣ Crear y activar entorno virtual
🪟 Windows (PowerShell o Git Bash)

- python -m venv venv
- venv\Scripts\activate

🍎 macOS / 🐧 Linux

- python3 -m venv venv
- source venv/bin/activate

### 3️⃣ Instalar dependencias

pip install -r requirements.txt

### 4️⃣ Ejecutar el servidor de desarrollo

  Opción 1: 
  - fastapi dev main.py

  Opción 2:
  - uvicorn main:app --reload

Luego abre en tu navegador:
👉 http://localhost:8000/docs


### 📡 Endpoints disponibles

| Método   | Endpoint           | Descripción                                                     |
| :------- | :----------------- | :-------------------------------------------------------------- |
| **GET**  | `/`                | Mensaje de bienvenida                                           |
| **GET**  | `/time/{iso_code}` | Devuelve la hora actual según el país (soporta formato 12h/24h) |
| **POST** | `/customers`       | Crea un nuevo cliente                                           |
| **GET**  | `/customers`       | Lista todos los clientes registrados                            |
| **POST** | `/transactions`    | Registra una transacción                                        |
| **POST** | `/invoices`        | Crea una factura con cliente y transacciones                    |

🧩 Modelos principales
- Customer
```python
class Customer(BaseModel):
    id: int | None = None
    name: str
    description: str | None
    email: EmailStr
    age: int
```
- Transaction
```python
class Transaction(BaseModel):
    id: int
    ammount: int
    description: str
```

- Invoice
```python
class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int
```


#### 🧠 Conceptos aprendidos hasta ahora

- Creación de endpoints con FastAPI (@app.get, @app.post).

- Uso de modelos Pydantic para validación automática de datos.

- Manejo básico de listas como base de datos temporal.

- Validación de emails con EmailStr.

- Enrutamiento con parámetros de ruta y query params.

- Organización modular (main.py y models.py).

- Control de versiones con Git y GitHub.

#### 🧭 Próximos pasos

- Conectar FastAPI con una base de datos real (MySQL o PostgreSQL).

- Implementar operaciones CRUD completas.

- Añadir autenticación básica con JWT.

- Desplegar el proyecto en Render o Railway.

### ✨ Autor

👨‍💻 Edwin Granada
📍 Ingeniero Físico | En formación como Desarrollador Backend con Python
🔗 GitHub

💡 ***Este proyecto forma parte de mi ruta de aprendizaje profesional en desarrollo backend con Python y FastAPI.***