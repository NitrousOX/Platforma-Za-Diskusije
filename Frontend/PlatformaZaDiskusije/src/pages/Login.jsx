import React from "react";
import "../styles/LoginPage.css";

const LoginPage = () => {
  return (
    <div className="login-container">
      <header className="login-header">
        <h1>Platforma za diskusije</h1>
      </header>
      <div className="login-box">
        <h2>Welcome Back</h2>
        <form>
          <div className="input-group">
            <label htmlFor="username">Username</label>
            <input type="text" id="username" placeholder="Enter your username" />
          </div>
          <div className="input-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              placeholder="Enter your password"
            />
          </div>
          <button type="submit" className="login-button">
            Login
          </button>
        </form>
        <div className="register-link">
          <p>
            Don't have an account? <a href="/register">Register now</a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
