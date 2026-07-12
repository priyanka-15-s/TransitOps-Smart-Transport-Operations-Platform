import Navbar from "../../components/navbar";

function Reports() {
  return (
    <div>
      <Navbar />
      <div className="container">
        <div className="card">
          <h2>Reports</h2>
          <table>
            <thead>
              <tr>
                <th>Report</th>
                <th>Period</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Vehicle Utilization</td>
                <td>Monthly</td>
                <td>Ready</td>
              </tr>
              <tr>
                <td>Fuel Consumption</td>
                <td>Weekly</td>
                <td>Review</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Reports;
