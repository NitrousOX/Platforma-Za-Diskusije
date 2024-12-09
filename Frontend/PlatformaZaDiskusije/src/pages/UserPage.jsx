import React from "react";
import "../styles/UserPage.css";

const UserPage = ({ user }) => {
  return (
    <div className="user-page-container">
      <header className="user-header">
        <h1>Welcome, {user?.username || "User"}!</h1>
      </header>
      <main className="user-content">
        <h2>Your Profile</h2>
        <div className="user-info">
          <p>
            <strong>Username:</strong> {user?.username || "Not available"}
          </p>
          <p>
            <strong>Email:</strong> {user?.email || "Not available"}
          </p>
          <p>
            <strong>Role:</strong> {user?.role || "User"}
          </p>
        </div>
      </main>
    </div>
  );
};

export default UserPage;
