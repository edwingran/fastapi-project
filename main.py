from fastapi import FastAPI
from datetime import datetime
import zoneinfo

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


#Reto: crear un nuevo endpoint que reciba una variable en formato get 
#Y que automaticamente se pueda hablitar el formato de hora. Por ejemplo devolver 
#la hora en formato de 24 horas si el usuario lo requiere.
