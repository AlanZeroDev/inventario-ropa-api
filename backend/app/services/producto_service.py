from backend.app.database.db import productos, contador_id
from backend.app.routes.productos import Producto

def obtener_productos():
    return productos

def agregar_producto(producto:Producto):
    global contador_id
    nuevo = producto.model_dump()
    nuevo["id"] = contador_id
    contador_id += 1
    productos.append(nuevo)
    return nuevo

def busqueda_especifica(id:str):
    for producto in productos:
        if producto["id"] == id :
            return producto
    return "No existe el estudiante"

def modificar(producto_actualizado:Producto , id =str):
    for producto in productos:
        if producto["id"] == id :
            producto["descripcion"] = producto_actualizado.descripcion
            producto["Precio"] = producto_actualizado.precio
            producto["precio_compra"] = producto_actualizado.precio_compra
            producto["precio_venta"] = producto_actualizado.precio_venta
    return "no existe el producto"
            