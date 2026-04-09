from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class VisiteInfo(BaseModel):
    centre: Optional[str] = Field(default=None, description="à droite de CENTRE dans le document")
    mtt: Optional[str] = Field(default=None, description="à droite de MTT dans le document")
    cat: Optional[str] = Field(default=None, description="à droite CAT dans le document")
    kms: Optional[str] = Field(default=None, description="à droite de KMS dans le document")
    stat: Optional[str] = Field(default=None, description="à droite de STAT dans le document")
    ville: Optional[str] = Field(default=None, description="Le nom de la ville")
    immatriculation: Optional[str] = Field(default=None, description="Juste en dessous de Immatriculation")
    expiration: Optional[date] = Field(default=None, description="date d'expiration juste en dessous de Expiration")
    marque: Optional[str] = Field(default=None, description="à droite de MARQUE")
    type: Optional[str] = Field(default=None, description="à droite de TYPE")
    numero_serie: Optional[str] = Field(default=None, description="à droite de N° SERIE")
    puis_fis_cv: Optional[str] = Field(default=None, description="à droite de PUIS.FIS.(CV) juste au dessus de MISE EN CIRC.")
    mise_en_circulation: Optional[date] = Field(default=None, description="la date à droite de MISE EN CIRC")
    observations: Optional[str] = Field(default=None, description="à droite de OBSERVATIONS")
    quotite: Optional[str] = Field(default=None, description="Juste en dessous de QUOTITE")
    numero_vignette: Optional[str] = Field(default=None, description="Juste en dessous de N° VIGNETTE")
    ncc: Optional[str] = Field(default=None, description="Juste en dessous de NCC (peut être vide)")
    responsable: Optional[str] = Field(default=None, description="Juste en dessous de RESPONSABLE")


