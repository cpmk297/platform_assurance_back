from fastapi import FastAPI
from app.routers import main_route, visite_t_postgres
from database import engine, Base

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(main_route.router)
app.include_router(visite_t_postgres.router)
