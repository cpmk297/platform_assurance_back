from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi.routing import APIRouter
import app.schemas as schemas, app.models as models

router = APIRouter(prefix='/cni-recto-postgres', tags=['formulaire cni recto'])

@router.post('/create_cni_recto_postgres')
def create_cni_recto_postgres(cni_recto_postgres: schemas.CniInfoRecto, db: Session = Depends(get_db)):
    db_cni_recto_postgres = models.CniInfoRecto(**cni_recto_postgres.dict())
    db.add(db_cni_recto_postgres)
    db.commit()
    db.refresh(db_cni_recto_postgres)
    return db_cni_recto_postgres