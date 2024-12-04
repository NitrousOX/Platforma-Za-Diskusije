import React from "react";
import "../styles/AdminPage.css";

const AdminPage = () => {
  // Dummy user data
  const users = [
    { id: 1, username: "john_doe", email: "john@example.com", role: "User" },
    { id: 2, username: "jane_doe", email: "jane@example.com", role: "User" },
    { id: 3, username: "admin_user", email: "admin@example.com", role: "Admin" },
  ];

  return (
    <div className="admin-container">
      <header className="admin-header">
        <h1>Administrator Dashboard</h1>
      </header>
      <main className="admin-main">
        <h2>Users List</h2>
        <table className="users-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Username</th>
              <th>Email</th>
              <th>Role</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.username}</td>
                <td>{user.email}</td>
                <td>{user.role}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </main>
    </div>
  );
};

export default AdminPage;
