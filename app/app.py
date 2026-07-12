from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI(title="TransitOps")

# ---------------- DATABASE ----------------

engine = create_engine(
    "sqlite:///transitops.db",
    connect_args={"check_same_thread": False}
)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    vehicle_no = Column(String)
    driver = Column(String)
    status = Column(String)


Base.metadata.create_all(engine)


# Add sample data
db = SessionLocal()

if db.query(Vehicle).count() == 0:
    db.add_all([
        Vehicle(vehicle_no="BUS-101",
                driver="Arun",
                status="Running"),

        Vehicle(vehicle_no="BUS-102",
                driver="Priya",
                status="Maintenance"),

        Vehicle(vehicle_no="BUS-103",
                driver="Kumar",
                status="Idle")
    ])

    db.commit()

db.close()


# ---------------- BACKEND API ----------------


@app.get("/vehicles")
def get_vehicles():

    db = SessionLocal()

    data = db.query(Vehicle).all()

    result=[]

    for v in data:
        result.append({
            "id":v.id,
            "vehicle":v.vehicle_no,
            "driver":v.driver,
            "status":v.status
        })

    db.close()

    return result



@app.post("/add_vehicle")
async def add_vehicle(request:Request):

    body = await request.json()

    db=SessionLocal()

    vehicle=Vehicle(
        vehicle_no=body["vehicle"],
        driver=body["driver"],
        status="Idle"
    )

    db.add(vehicle)
    db.commit()

    db.close()

    return {
        "message":"Vehicle Added"
    }



# ---------------- FRONTEND ----------------


@app.get("/",response_class=HTMLResponse)
def home():

    return """

<!DOCTYPE html>

<html>

<head>

<title>TransitOps Dashboard</title>


<style>

body{
font-family:Arial;
background:#f4f6f9;
margin:0;
}


header{

background:#0d47a1;
color:white;
padding:20px;
text-align:center;

}


.container{

padding:30px;

}


.cards{

display:flex;
gap:20px;

}


.card{

background:white;
padding:20px;
border-radius:10px;
width:200px;
box-shadow:0 2px 5px gray;

}


table{

background:white;
width:100%;
margin-top:30px;
border-collapse:collapse;

}


td,th{

padding:12px;
border:1px solid #ddd;

}


button{

background:#0d47a1;
color:white;
padding:10px;
border:none;
border-radius:5px;

}


input{

padding:10px;
margin:5px;

}

</style>


</head>


<body>


<header>

<h1>TransitOps</h1>

<p>Smart Transport Operations Platform</p>

</header>



<div class="container">


<div class="cards">


<div class="card">
<h3>Total Vehicles</h3>
<h2 id="count">0</h2>
</div>


<div class="card">
<h3>Active Routes</h3>
<h2>12</h2>
</div>


<div class="card">
<h3>Alerts</h3>
<h2>3</h2>
</div>


</div>



<h2>Vehicle Management</h2>


<input id="vehicle"
placeholder="Vehicle Number">


<input id="driver"
placeholder="Driver Name">


<button onclick="addVehicle()">
Add Vehicle
</button>



<table>


<thead>

<tr>

<th>ID</th>
<th>Vehicle</th>
<th>Driver</th>
<th>Status</th>

</tr>

</thead>


<tbody id="table">

</tbody>


</table>



</div>



<script>


async function loadVehicles(){

let res =
await fetch('/vehicles');


let data =
await res.json();



document.getElementById("count").innerHTML=data.length;



let rows="";


data.forEach(v=>{


rows += `

<tr>

<td>${v.id}</td>

<td>${v.vehicle}</td>

<td>${v.driver}</td>

<td>${v.status}</td>


</tr>

`;

});


document.getElementById("table").innerHTML=rows;


}



async function addVehicle(){


let vehicle=
document.getElementById("vehicle").value;


let driver=
document.getElementById("driver").value;



await fetch(
'/add_vehicle',
{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

vehicle:vehicle,

driver:driver

})

}

);


loadVehicles();


}



loadVehicles();


</script>



</body>

</html>

"""
