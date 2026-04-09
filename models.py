from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class VisiteInfo(Base):

    __tablename__ = "visite_info"
    id = Column(Integer, primary_key=True, index=True)
    centre = Column(String, nullable=True)
    mtt = Column(String, nullable=True)     
    cat = Column(String, nullable=True)
    kms = Column(String, nullable=True)
    stat = Column(String, nullable=True)
    ville = Column(String, nullable=True)
    immatriculation = Column(String, nullable=True)
    expiration = Column(Date, nullable=True)
    marque = Column(String, nullable=True)
    type = Column(String, nullable=True)
    numero_serie = Column(String, nullable=True)
    puis_fis_cv = Column(String, nullable=True)
    mise_en_circulation = Column(Date, nullable=True)
    observations = Column(String, nullable=True)
    quotite = Column(String, nullable=True)
    numero_vignette = Column(String, nullable=True)
    ncc = Column(String, nullable=True)
    responsable = Column(String, nullable=True)
