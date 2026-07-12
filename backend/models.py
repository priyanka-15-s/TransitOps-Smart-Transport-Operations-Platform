from sqlalchemy import Column,Integer,String,Date,Float,ForeignKey
from database import Base



class User(Base):

    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)

    username=Column(String(50))

    email=Column(String(100),unique=True)

    password=Column(String(200))

    role=Column(String(20))



class Vehicle(Base):

    __tablename__="vehicles"


    id=Column(Integer,primary_key=True)

    vehicle_number=Column(String(50))

    vehicle_type=Column(String(50))

    capacity=Column(Integer)

    status=Column(String(30))



class Driver(Base):

    __tablename__="drivers"


    id=Column(Integer,primary_key=True)

    name=Column(String(100))

    phone=Column(String(20))

    license_number=Column(String(50))



class Trip(Base):

    __tablename__="trips"


    id=Column(Integer,primary_key=True)

    vehicle_id=Column(Integer)

    driver_id=Column(Integer)

    source=Column(String(100))

    destination=Column(String(100))

    distance=Column(Float)



class Maintenance(Base):

    __tablename__="maintenance"


    id=Column(Integer,primary_key=True)

    vehicle_id=Column(Integer)

    issue=Column(String(200))

    cost=Column(Float)



class Fuel(Base):

    __tablename__="fuel"


    id=Column(Integer,primary_key=True)

    vehicle_id=Column(Integer)

    liters=Column(Float)

    amount=Column(Float)