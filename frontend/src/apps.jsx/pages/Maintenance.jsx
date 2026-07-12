import Navbar from "../../components/navbar";

function Maintenance() {
  return (
    <div>
      <Navbar />
      <div className="container">
        <div className="card">
          <h2>Maintenance</h2>
          <table>
            <thead>
              <tr>
                <th>Vehicle</th>
                <th>Issue</th>
                <th>Due</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>XYZ-789</td>
                <td>Brake inspection</td>
                <td>2026-07-15</td>
              </tr>
              <tr>
                <td>ABC-123</td>
                <td>Oil change</td>
                <td>2026-07-18</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Maintenance;
