import logo from './logo.svg';
import './App.css';
import Navbar from './navbar/navbar'
import Home from './home';
import SignUp from './signup';
import RegisterCharity from './registercharity';
import DonorMainPage from './donorpage/donorpagemain';
import DonorPageDetails from './donorpage/donorpagedetails';
import DonorPageDonate from './donorpage/donorpagedonate';
import DonorPagePayment from './donorpage/donorpagePayment';
import Login from './login';
import Footer from './footer';
//Stripe Elements
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom'; 
import { useState,useEffect } from 'react';

const stripePromise = loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

function App() {
  let [isLoggedIn, setIsLoggedIn] = useState(true);
  const [clientSecret, setClientSecret] = useState("");
  let [donorCredentials, setDonorCredentials] = useState([]);
  const [emailAddress, setEmailAddress]=useState("kimani.mbatia@student.moringaschool.com");


        useEffect(() => {
        // Create PaymentIntent as soon as the page loads
        fetch("https://hopeharbour-api.onrender.com/onetimepay/pay", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: emailAddress}),
        })
          .then((res) => res.json())
          .then((data) => {
            //console.log(typeof data.client_secret)
            //console.log(data.client_secret)
            setClientSecret(data.client_secret)
            alert(clientSecret)
          } )
          .catch(error=>{alert(error)})
      }, []);

/*   useEffect(function(){
    setDonorCredentials(false)
  }) */


  function setLoginStatus(){
    setIsLoggedIn(true)
  }

  const appearance = {
    theme: 'stripe',
  };
  const options = {
    clientSecret,
    appearance,
  };

  return (
    <div>
      {clientSecret &&(
              <Elements options={options} stripe={stripePromise}>
              <Navbar isLoggedIn={isLoggedIn} />
              <Routes>
                <Route path="/" element={<Home />}/>
                <Route path="/signup" element={<SignUp />}/>
                <Route path="/registercharity" element={<RegisterCharity />}/>
                <Route path="/login" element={<Login setLoginStatus={setLoginStatus} />}/>
                <Route path="/donorMainPage" element={<DonorMainPage />}>
                  <Route path="details" element={<DonorPageDetails />}></Route>
                  <Route path="donate" element={<DonorPageDonate />}>
                    <Route path='payment' element={<DonorPagePayment />}>
                      </Route>
                  </Route>
                </Route>
              </Routes>
              <Footer />
             </Elements>
      )}

    </div> 

  );
}

export default App;
