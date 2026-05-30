from backend.app.database.db import productos, contador_id
from backend.app.schemas.producto import Producto
from fastapi import HTTPException


def obtener_productos():
    return productos


def agregar_producto(producto: Producto):
    global contador_id

    nuevo = producto.model_dump()
    nuevo["id"] = contador_id

    contador_id += 1

    productos.append(nuevo)

    return "Producto agregado"


def busqueda_id(id: int):

    for producto in productos:
        if producto["id"] == id:
            return producto
    raise HTTPException(
        status_code=404,
        detail="Id no encontrado"
    )


def busqueda_descripcion(dato: str):

    for producto in productos:
        if producto["descripcion"] == dato:
            return producto
    raise HTTPException(
        status_code=404,
        detail="Descripcion no encontrada"
    )


def modificar(producto_actualizado: Producto, id: int):

    for producto in productos:
        if producto["id"] == id:
            producto["descripcion"] = producto_actualizado.descripcion
            producto["cantidad"] = producto_actualizado.cantidad
            producto["precio"] = producto_actualizado.precio
            producto["precio_compra"] = producto_actualizado.precio_compra
            producto["precio_venta"] = producto_actualizado.precio_venta
            return "Producto modificado"
    raise HTTPException(
        status_code=404,
        detail="Id no encontrado"
    )


def eliminar(id: int):

    for producto in productos:
        if producto["id"] == id:
            productos.remove(producto)
            return "Producto eliminado"
    raise HTTPException(
        status_code=404,
        detail="Id no encontrado"
    )


def agregar_stock(cantidad: int, id: int):

    if cantidad <= 0:
        raise HTTPException(
            status_code=400,
            detail="La cantidad debe ser mayor a 0"
        )
    for producto in productos:
        if producto["id"] == id:
            stock_actual = producto["cantidad"]
            producto["cantidad"] = stock_actual + cantidad
            return producto
    raise HTTPException(
        status_code=404,
        detail="Id no encontrado"
    )


def eliminar_stock(cantidad_eliminar: int, id: int):
    if cantidad_eliminar <= 0:
        raise HTTPException(
            status_code=400,
            detail="La cantidad a eliminar debe ser mayor a 0"
        )
    for producto in productos:
        if producto["id"] == id:
            if producto["cantidad"] < cantidad_eliminar:
                raise HTTPException(
                    status_code=400,
                    detail="Cantidad excede stock disponible"
                )
            stock_actual = producto["cantidad"]
            producto["cantidad"] = stock_actual - cantidad_eliminar
            return producto
    raise HTTPException(
        status_code=404,
        detail="Id no encontrado"
    )