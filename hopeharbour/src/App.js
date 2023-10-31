import logo from './logo.svg';
import './App.css';
import Navbar from './navbar';
import Home from './home';
import SignUp from './signup';
import RegisterCharity from './registercharity';
import Footer from './footer';
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom'; 

function App() {
  return (
    <div>

      <Navbar />
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/signup" element={<SignUp />}/>
        <Route path="/registercharity" element={<RegisterCharity />}/>
      </Routes>
      <Footer />
    </div> 

  );
}

export default App;
