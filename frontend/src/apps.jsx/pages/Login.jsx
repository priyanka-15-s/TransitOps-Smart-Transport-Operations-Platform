import Navbar from "../../components/navbar";

function Login() {
  return (
    <div>
      <Navbar />
      <div className="container">
        <div className="card">
          <h2>Login</h2>
          <form>
            <input type="email" placeholder="Email address" />
            <input type="password" placeholder="Password" />
            <button type="button">Sign In</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
