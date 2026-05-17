from pydantic import BaseModel

class Producto(BaseModel):
    descripcion: str
    cantidad: int
    precio: float
    precio_compra: float
    precio_venta: float
