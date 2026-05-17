from fastapi import APIRouter
from backend.app.schemas.producto import Producto
from backend.app.database.db import productos, contador_id

router = APIRouter()

@router.get("/productos")
def obtener_productos():
    return productos

@router.post("/productos")
def agregar_producto(producto: Producto):
    global contador_id
    nuevo = producto.model_dump()   # convierte a diccionario {"descripcion": "remera"} 
    nuevo["id"] = contador_id       # le agrega el id
    productos.append(nuevo)         # lo guarda en la lista
    contador_id += 1
    return nuevo
   