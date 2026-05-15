from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Base de datos en memoria
productos = []
contador_id = 1

class producto(BaseModel):
    descripcion: str
    cantidad:int
    precio:float
    precio_compra:float
    precio_venta:float
    cantidad_vendida:int

#Mostrar productos

app.get("/productos")
def obtener_productos():
    return productos


