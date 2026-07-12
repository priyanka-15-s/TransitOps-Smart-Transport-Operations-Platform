from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Vehicle
from schemas import VehicleCreate



router=APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)



@router.post("/")
def add_vehicle(
    vehicle:VehicleCreate,
    db:Session=Depends(get_db)
):

    new_vehicle=Vehicle(

        vehicle_number=vehicle.vehicle_number,
        vehicle_type=vehicle.vehicle_type,
        capacity=vehicle.capacity,
        status=vehicle.status
    )


    db.add(new_vehicle)

    db.commit()

    db.refresh(new_vehicle)


    return new_vehicle



@router.get("/")
def get_vehicle(
    db:Session=Depends(get_db)
):

    return db.query(Vehicle).all()