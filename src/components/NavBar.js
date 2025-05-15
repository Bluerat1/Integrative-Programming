import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { setAuthToken } from '../api';

export default function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem('token');
  const logout = () => {
    localStorage.removeItem('token');
    setAuthToken(null);
    navigate('/login');
  };
  return (
    <nav className="bg-white shadow p-4 flex justify-between">
      <Link to="/" className="font-bold">Integrative Programming</Link>
      <div>
        {token ? (
          <button onClick={logout} className="text-red-500">Logout</button>
        ) : (
          <>          
            <Link to="/login" className="mr-4">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
}
