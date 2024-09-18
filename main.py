from fastapi import FastAPI

app = FastAPI()


@app.get("/plants/{plant_id}")
async def get_plant(plant_id: str):
    return {"message": f"You requested a plant with plant_id {plant_id}"}

