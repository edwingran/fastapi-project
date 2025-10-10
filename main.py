from fastapi import FastAPI
from datetime import datetime
import zoneinfo
from models import Customer, CustomerCreate, Transaction, Invoice

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenido a mi App!"}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima"
}

@app.get("/time/{iso_code}")
async def time(iso_code: str, format: str = "24h"): # Parámetro tipo query
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    if not timezone_str:
        return {"error": "Código de país no válido"}
    
    tz = zoneinfo.ZoneInfo(timezone_str)
    current_time = datetime.now(tz)
    
    # Definimos la lógica del formato
    if format == "12h":
        formatted_time = current_time.strftime("%I:%M:%S %p") #Ej: 07:30:15 PM
    else:
        formatted_time = current_time.strftime("%H:%M:%S") #Ej 19:30:15
        
    return {
        "country": iso,
        "time": formatted_time,
        "format": format
    }
# Base de datos tipo lista inicializada en vacío
db_customers: list[Customer] = []

@app.post("/customers", response_model = Customer)
async def create_customer(customer_data: CustomerCreate):
    customer = Customer.model_validate(customer_data.model_dump())
    # Asumiendo que se hace en la base de datos
    customer.id = len(db_customers)
    db_customers.append(customer)

    return customer

@app.get("/customers", response_model = list[Customer])
async def list_customers():
    return db_customers

@app.post("/transactions")
async def create_transaction(transaction_data: Transaction):
    
    return transaction_data

@app.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    
    return invoice_data

