from fastapi import APIRouter
from backend.app.schemas.producto import Producto
from backend.app.services.producto_service import (
    obtener_productos, 
    agregar_producto, 
    busqueda_especifica, 
    modificar
)

router = APIRouter()

@router.get("/productos")
def route_obtener_productos():
    return obtener_productos()

@router.post("/productos")
def route_agregar_producto(producto: Producto):
    return agregar_producto(producto)

@router.get("/productos/{id}")    
def route_busqueda_id(id: int):   
    return busqueda_especifica(id)

@router.put("/productos/{id}")    
def route_modificar(producto_actualizado: Producto, id: int):
    return modificar(producto_actualizado, id)