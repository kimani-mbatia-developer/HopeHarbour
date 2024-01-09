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

import DonorPageSuccess from './donorpage/donorpagesuccess';

import CharityPageMain from './charitypage/charitypagemain';
import CharityPageDetails from './charitypage/charitypagedetails';

import AdminPageDashboard from './admin';

import Login from './login';
import Footer from './footer';

//Stripe Elements
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom'; 
import { useState,useEffect } from 'react';


//const stripePromise = loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

// const stripePromise = loadStripe('pk_test_51O9wNVBwM0XCzFWGs1UJCn7IqgvQM8pEx0dJSQ0tszXRi8v4YlekI3vvQVP7iEghQ2msfEbXDn9r3xx6NNdym0yG00HHan0JyP')



function App() {
  let [isLoggedIn, setIsLoggedIn] = useState(false);
  const [clientSecret, setClientSecret] = useState("1234");
  let [donorCredentials, setDonorCredentials] = useState([]);
  // const [emailAddress, setEmailAddress]=useState("kimani.mbatia@student.moringaschool.com");


      //   useEffect(() => {
      //   // Create PaymentIntent as soon as the page loads
      //   fetch("https://hopeharbour-api.onrender.com/onetimepay/pay", {
      //     method: "POST",
      //     headers: { "Content-Type": "application/json" },
      //     body: JSON.stringify({ email: emailAddress}),
      //   })
      //     .then((res) => res.json())
      //     .then((data) => {
      //       //console.log(typeof data.client_secret)
      //       //console.log(data.client_secret)
      //       setClientSecret(data.client_secret)
      //       console.log(clientSecret)
      //       //alert(clientSecret)
      //     } )
      //     .catch(error=>{alert(error)})
      // }, []);

/*   useEffect(function(){
    setDonorCredentials(false)
  }) */


  function setLoginStatus(){
    setIsLoggedIn(true)
    let temp =JSON.parse(localStorage.getItem('user_data'))
    setDonorCredentials(temp)
    alert(temp)
    alert(donorCredentials)
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
              // <Elements options={options} stripe={stripePromise}>
              <>
                <Navbar isLoggedIn={isLoggedIn} donorCredentials={donorCredentials} />
              <Routes>
                <Route path="/" element={<Home />}/>
                <Route path="/signup" element={<SignUp />}/>
                <Route path="/registercharity" element={<RegisterCharity />}/>
                <Route path="/login" element={<Login setDonorCredentials={setDonorCredentials} setLoginStatus={setLoginStatus} />}/>
                {isLoggedIn? (
                  <>
                                <Route path="/donorMainPage" element={<DonorMainPage donorCredentials={donorCredentials}  />}>
                                  <Route path="details" element={<DonorPageDetails />}></Route>
                                  <Route path="donate" element={<DonorPageDonate />}>
                                    <Route path='payment' element={<DonorPagePayment />}>
                                      </Route>
                                  </Route>
                                </Route>
                                <Route path='/success' element={<DonorPageSuccess />}></Route>
                              {donorCredentials.role =="charity"}
                                <Route path="/charityMainPage" element={<CharityPageMain />}>
                                  <Route path="details" element={<CharityPageDetails />}></Route>
                                </Route>
                  </>

                ):(
                  <></>
                )}

                <Route path="/admin" element={<AdminPageDashboard/>}></Route>
              </Routes>
              <Footer />
              </>
              
            //  </Elements>
      )}

    </div> 

  );
}

export default App;
