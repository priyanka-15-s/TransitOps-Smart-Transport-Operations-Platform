import Navbar from "../../components/navbar";

function Trips() {
  return (
    <div>
      <Navbar />
      <div className="container">
        <div className="card">
          <h2>Trips</h2>
          <table>
            <thead>
              <tr>
                <th>Route</th>
                <th>Driver</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Hub to North</td>
                <td>Mark Allen</td>
                <td>Completed</td>
              </tr>
              <tr>
                <td>Hub to East</td>
                <td>Sarah Kim</td>
                <td>In Transit</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Trips;
