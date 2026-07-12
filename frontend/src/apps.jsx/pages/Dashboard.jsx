import Navbar from "../../components/navbar";

function Dashboard() {
  return (
    <div>
      <Navbar />
      <div className="container">
        <div className="card">
          <h2>Fleet Dashboard</h2>
          <div className="dashboard-grid">
            <div className="dashboard-card">
              <h3>Vehicles</h3>
              <p>24</p>
            </div>
            <div className="dashboard-card">
              <h3>Drivers</h3>
              <p>18</p>
            </div>
            <div className="dashboard-card">
              <h3>Trips</h3>
              <p>47</p>
            </div>
            <div className="dashboard-card">
              <h3>Fuel</h3>
              <p>328L</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
