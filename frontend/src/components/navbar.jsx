import { Link } from "react-router-dom";

function Navbar() {

    return (

        <nav>

            <Link to="/dashboard">Dashboard</Link>

            <Link to="/vehicles">Vehicles</Link>

            <Link to="/drivers">Drivers</Link>

            <Link to="/trips">Trips</Link>

            <Link to="/maintenance">Maintenance</Link>

            <Link to="/fuel">Fuel</Link>

            <Link to="/reports">Reports</Link>

        </nav>

    );
}

export default Navbar;