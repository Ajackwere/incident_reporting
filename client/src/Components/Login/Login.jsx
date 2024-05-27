import React from "react";
import "./login.css";

function Login() {
  return (
    <div className="login-cnt">
      <form
        onSubmit={(e) => {
          e.preventDefault();
        }}
      >
        <h1>Reporter</h1>
        <h2>Sign in</h2>
        <input type="text" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <div className="singup-sec">
          or <span>Signup</span>
        </div>
        <button>Submit</button>
      </form>
    </div>
  );
}

export default Login;
