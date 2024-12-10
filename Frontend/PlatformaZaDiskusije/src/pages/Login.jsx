import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/LoginPage.css";

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      // Connect to the WebSocket server
      const socket = new WebSocket("ws://localhost:6789");

      // Send login request when WebSocket is open
      socket.onopen = () => {
        const loginData = {
          action: "login",
          username,
          password,
        };
        socket.send(JSON.stringify(loginData));
      };

      // Handle server response
      socket.onmessage = (event) => {
        const response = JSON.parse(event.data);

        if (response.status === "success") {
          // Navigate based on user role
          const role = username === "admin" ? "admin" : "user";
          navigate(`/${role}`);
        } else {
          setError(response.message);
        }

        // Close WebSocket after receiving response
        socket.close();
      };

      // Handle WebSocket errors
      socket.onerror = (error) => {
        console.error("WebSocket Error:", error);
        setError("Connection error. Please try again.");
      };
    } catch (err) {
      console.error("Error:", err);
      setError("Unexpected error occurred.");
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h1>Login</h1>
        <form onSubmit={handleLogin}>
          <div className="input-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter your username"
            />
          </div>
          <div className="input-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter your password"
            />
          </div>
          {error && <p className="error-message">{error}</p>}
          <button type="submit" className="login-button">
            Login
          </button>
        </form>
        <div className="register-link">
          <p>
            Don’t have an account?{" "}
            <span
              className="create-account-link"
              onClick={() => navigate("/register")}
            >
              Create Account
            </span>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
