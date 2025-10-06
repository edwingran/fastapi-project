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
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return{"time": datetime.now(tz)}

#Reto: crear un nuevo endpoint que reciba una variable en formato get 
#Y que automaticamente se pueda hablitar el formato de hora. Por ejemplo devolver 
#la hora en formato de 24 horas si el usuario lo requiere.
