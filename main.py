from fastapi import FastAPI
from app.routers import main_route, visite_t_postgres, facture_postgres, cni_recto_postgres, permis_cond_postgres
from app.database import engine, Base

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(main_route.router)
app.include_router(visite_t_postgres.router)
app.include_router(facture_postgres.router)
app.include_router(cni_recto_postgres.router)
app.include_router(permis_cond_postgres.router)
