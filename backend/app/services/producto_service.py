from backend.app.database.db import productos, contador_id

def obtener_productos():
    return productos

def agregar_producto(producto):
    global contador_id
    nuevo = producto.model_dump()
    nuevo["id"] = contador_id
    contador_id += 1
    productos.append(nuevo)
    return nuevo

