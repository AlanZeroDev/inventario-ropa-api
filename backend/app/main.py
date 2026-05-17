from fastapi import FastAPI
from backend.app.routes.productos import router as productos_router

# 1. Crear la app
app = FastAPI()

# 2. Registrar los routers
app.include_router(productos_router)

