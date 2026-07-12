import Navbar from "../../components/navbar";

function Fuel() {
  return (
    <div>
      <Navbar />
      <div className="container">
        <div className="card">
          <h2>Fuel Logs</h2>
          <div className="dashboard-grid">
            <div className="dashboard-card">
              <h3>Today</h3>
              <p>74L</p>
            </div>
            <div className="dashboard-card">
              <h3>This Week</h3>
              <p>318L</p>
            </div>
            <div className="dashboard-card">
              <h3>Average Cost</h3>
              <p>$4.73</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Fuel;
