from backend.app.database.db import productos, contador_id
from backend.app.schemas.producto import Producto

def obtener_productos():
    return productos

def agregar_producto(producto:Producto):
    global contador_id
    nuevo = producto.model_dump()
    nuevo["id"] = contador_id
    contador_id += 1
    productos.append(nuevo)
    return "producto agregado"

def busqueda_id(id:int):
    for producto in productos:
        if producto["id"] == id :
            return producto
    return "No existe el id"

def busqueda_descripcion(dato:str):
    for producto in productos:
        if producto["descripcion"] == dato:
            return producto
    return "No existe la descripcion"

def modificar(producto_actualizado: Producto, id: int):
    for producto in productos:
        if producto["id"] == id:
            producto["descripcion"] = producto_actualizado.descripcion
            producto["cantidad"] = producto_actualizado.cantidad
            producto["precio"] = producto_actualizado.precio
            producto["precio_compra"] = producto_actualizado.precio_compra
            producto["precio_venta"] = producto_actualizado.precio_venta
            return "producto modificado"
    return "no existe el producto"

def eliminar(id:int):
    for producto in productos:
        if producto["id"] == id:
            productos.remove(producto)
            return "producto eliminado"
    return "id no existe"