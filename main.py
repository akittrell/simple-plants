from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from models.plant import Plant, PlantCreate
from db.models.base import SessionLocal
import queries.query_plants as query

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/plants/{plant_id}", response_model=Plant)
def get_plant(plant_id: str, db: Session = Depends(get_db)):
    plant = query.get_plant(db, plant_id)
    if plant is None:
        raise HTTPException(status_code=404, detail="Plant does not exist")
    return plant

@app.post("/plants", response_model=Plant)
def create_plant(new_plant: PlantCreate, db: Session = Depends(get_db)):
    plant = query.create_plant(db, new_plant)
    return plant


@app.delete("/plants/{plant_id}")
def delete_plant(plant_id: str, db: Session = Depends(get_db)):
    query.delete_plant(db, plant_id)
