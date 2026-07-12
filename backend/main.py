from fastapi import FastAPI
from database import engine
from models import Base


from routers import (
    users,
    vehicles,
    drivers,
    trips,
    maintenance,
    fuel,
    reports
)


app=FastAPI(
    title="TransitOps API"
)



Base.metadata.create_all(
    bind=engine
)



app.include_router(users.router)
app.include_router(vehicles.router)
app.include_router(drivers.router)
app.include_router(trips.router)
app.include_router(maintenance.router)
app.include_router(fuel.router)
app.include_router(reports.router)



@app.get("/")
def home():

    return {
        "message":
        "TransitOps Backend Running"
    }