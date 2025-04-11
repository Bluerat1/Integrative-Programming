import logo from './logo.svg';
import { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {

  const [posts, setPosts] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/api/v1/article/').then(response => {
      setPosts(response.data);
    })
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit !<code>src/App.js</code> and save to reload.
        </p>
        {
          posts.map((obj,index) => <p key={index}>{obj.title}</p>)
        }
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
