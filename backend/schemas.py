from pydantic import BaseModel



class UserCreate(BaseModel):

    username:str
    email:str
    password:str
    role:str



class VehicleCreate(BaseModel):

    vehicle_number:str
    vehicle_type:str
    capacity:int
    status:str



class DriverCreate(BaseModel):

    name:str
    phone:str
    license_number:str



class TripCreate(BaseModel):

    vehicle_id:int
    driver_id:int
    source:str
    destination:str
    distance:float