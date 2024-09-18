from pydantic import BaseModel

class Plant(BaseModel):
    family_name: str
    genus: str
    common_name: str
