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
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom'; 
import { useState,useEffect } from 'react';

function App() {
  let [isLoggedIn, setIsLoggedIn] = useState(false)
  let [donorCredentials, setDonorCredentials] = useState([])



/*   useEffect(function(){
    setDonorCredentials(false)
  }) */

  function setLoginStatus(){
    setIsLoggedIn(true)
  }

  return (
    <div>
       
        <Navbar isLoggedIn={isLoggedIn} />
        <Routes>
          <Route path="/" element={<Home />}/>
          <Route path="/signup" element={<SignUp />}/>
          <Route path="/registercharity" element={<RegisterCharity />}/>
          <Route path="/login" element={<Login setLoginStatus={setLoginStatus} />}/>
          <Route path="/donorMainPage" element={<DonorMainPage />}>
            <Route path="details" element={<DonorPageDetails />}></Route>
            <Route path="donate" element={<DonorPageDonate />}>
                <Route path='payment' element={ <DonorPagePayment />}></Route>
            </Route>
          </Route>
        </Routes>
        <Footer />
      
    </div> 

  );
}

export default App;
