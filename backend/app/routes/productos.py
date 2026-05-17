from fastapi import APIRouter
from backend.app.schemas.producto import Producto
from backend.app.database.db import productos, contador_id

router = APIRouter()

@router.get("/productos")
def obtener_productos():
    return obtener_productos

@router.post("/productos")
def agregar_producto(producto: Producto):
    return agregar_producto(producto)
  