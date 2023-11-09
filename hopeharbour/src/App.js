import logo from './logo.svg';
import './App.css';
import Navbar from './navbar/navbar'
import Home from './home';
import SignUp from './signup';
import RegisterCharity from './registercharity';
import DonorMainPage from './donorpage/donorpagemain';
import Login from './login';
import Footer from './footer';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'; 
import { useState, useEffect } from 'react';
import paypal from './components/paypal';
import StripeCheckout from 'react-stripe-checkout';

function App() {
 const [checkout, setCheckout] = useState(false);

 let [isLoggedIn, setIsLoggedIn] = useState(false);
 let [donorCredentials, setDonorCredentials] = useState([]);

 const handleToken = (token) => {
    // Handle the token received from Stripe
    console.log(token);
 };

 useEffect(() => {
    setDonorCredentials(false);
 }, []);

 return (
    <div className="App">
      {checkout ? (
        <paypal />
      ) : (
        <>
          <StripeCheckout
            token={handleToken}
            stripeKey="my_PUBLISHABLE_stripekey"
          />
          <button
            onClick={() => {
              setCheckout(true);
            }}
          >
            checkout
          </button>
        </>
      )}

      <Navbar isLoggedIn={isLoggedIn} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/registercharity" element={<RegisterCharity />} />
        <Route path="/login" element={<Login />} />
        <Route path="/donorMainPage" element={<DonorMainPage />} />
      </Routes>
      <Footer />
    </div>
 );
}

export default App;