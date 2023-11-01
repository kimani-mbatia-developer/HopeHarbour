import logo from './logo.svg';
import './App.css';
import Navbar from './navbar';
import Home from './home';
import SignUp from './signup';
import RegisterCharity from './registercharity';
import Login from './login';
import Footer from './footer';
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom'; 
import { useState } from 'react';

function App() {
  let [isLoggedIn, setIsLoggedIn] = useState(false)
  
  return (
    <div>

      <Navbar />
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/signup" element={<SignUp />}/>
        <Route path="/registercharity" element={<RegisterCharity />}/>
        <Route path="/login" element={<Login />}/>
      </Routes>
      <Footer />
    </div> 

  );
}

export default App;
