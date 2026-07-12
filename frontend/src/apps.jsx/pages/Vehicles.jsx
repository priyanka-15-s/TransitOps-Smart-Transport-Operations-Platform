import Navbar from "../../components/navbar";

function Vehicles() {
  return (
    <div>
      <Navbar />
      <div className="container">
        <div className="card">
          <h2>Vehicles</h2>
          <table>
            <thead>
              <tr>
                <th>Plate</th>
                <th>Type</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>ABC-123</td>
                <td>Truck</td>
                <td>Active</td>
              </tr>
              <tr>
                <td>XYZ-789</td>
                <td>Van</td>
                <td>Maintenance</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Vehicles;
