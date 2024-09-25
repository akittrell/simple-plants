from sqlalchemy.orm import Session
from models.plant import PlantCreate
from db.models.plant import PlantDB


#CRUD
def create_plant(db: Session, plant: PlantCreate):
    new_plant = PlantDB(
        family_name=plant.family_name,
        common_name=plant.common_name,
        genus=plant.genus
    )
    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)
    return new_plant

def get_plant(db: Session, plant_id: str):
    return db.get(PlantDB, plant_id)

def update_plant(db: Session):
    # Probably not accessible to user. Still needed for maintenance.
    pass

def delete_plant(db: Session, plant_id: str):
    pass

def list_plants(db: Session):
    # Probably assign this to a user eventually rather than just listing
    # all plants everywhere
    pass