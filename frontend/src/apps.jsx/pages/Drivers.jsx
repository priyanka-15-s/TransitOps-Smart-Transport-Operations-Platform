import Navbar from "../../components/navbar";

function Drivers() {
  return (
    <div>
      <Navbar />
      <div className="container">
        <div className="card">
          <h2>Drivers</h2>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>License</th>
                <th>Assigned Vehicle</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Mark Allen</td>
                <td>Class A</td>
                <td>ABC-123</td>
              </tr>
              <tr>
                <td>Sarah Kim</td>
                <td>Class B</td>
                <td>XYZ-789</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Drivers;
