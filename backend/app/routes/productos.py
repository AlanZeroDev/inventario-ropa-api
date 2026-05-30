from fastapi import APIRouter
from backend.app.schemas.producto import Producto
from backend.app.services.producto_service import (
    obtener_productos, 
    agregar_producto, 
    busqueda_id, 
    modificar,
    busqueda_descripcion,
    eliminar,
    agregar_stock,
    eliminar_stock
)

router = APIRouter()

@router.get("/productos")
def route_obtener_productos():
    return obtener_productos()

@router.post("/productos")
def route_agregar_producto(producto: Producto):
    return agregar_producto(producto)

@router.get("/productos/id/{id}")    
def route_busqueda_id(id: int):   
    return busqueda_id(id)

@router.get("/productos/descripcion/{info}")
def route_busqueda_descripcion(info: str):
    return busqueda_descripcion(info)

@router.put("/productos/{id}")    
def route_modificar(producto_actualizado: Producto, id: int):
    return modificar(producto_actualizado, id)

@router.delete("/productos/{id}")
def route_eliminar(id: int):
    return eliminar(id)

@router.patch("/productos/{id}/agregar")
def route_agregar(cantidad:int , id:int):
    return agregar_stock(cantidad,id)

@router.patch("/productos/{id}/eliminar-stock")
def route_eliminar_stock(cantidad_eliminar: int , id: int):
    return eliminar_stock(cantidad_eliminar,id)

