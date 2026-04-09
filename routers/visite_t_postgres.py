from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi.routing import APIRouter
import app.schemas as schemas, app.models as models


router = APIRouter(prefix= "/Visite_technique_formulaire", tags= ["formulaire visite technique"])
@router.post('/bdd_visite_tech')
def create_visite_info(request: schemas.VisiteInfo, db: Session= Depends(get_db)):
    visite_info = models.VisiteInfo(**request.dict())
    db.add(visite_info)
    db.commit()
    db.refresh(visite_info)
    return visite_info


