from pydantic import BaseModel

class Plant(BaseModel):
    id: str
    family_name: str
    genus: str
    common_name: str

class PlantCreate(BaseModel):
    family_name: str
    genus: str
    common_name: str