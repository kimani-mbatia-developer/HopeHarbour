import React from "react";
import DonorPageNavBar from "./donorpagenavbar";
import DonorPageDashboard from "./donorpagedashboard";
import DonorPageDetails from "./donorpagedetails";
import DonorPageDonate from "./donorpagedonate";
import DonorPagePayment from "./donorpagePayment";
import DonorPageSuccess from "./donorpagesuccess";
//

import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom'; 

const stripePromise = loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

function DonorMainPage({donorCredentials}){

    const sectionStyle={
        backgroundColor:"#97B3DC",
        display:"flex"
    }

    const appearance = {
        theme: 'stripe',
      };
      const options = {
        //clientSecret,
        appearance,
      };
    



    return(
        <section style={sectionStyle}>
            <DonorPageNavBar />
            <Routes>
                <Route path="" element={<DonorPageDashboard donorCredentials={donorCredentials} />}></Route>
                <Route path="details" element={<DonorPageDetails donorCredentials={donorCredentials} />}></Route>
                <Route path="donate" element={<DonorPageDonate />}>
                    <Route path="payment" element={<DonorPagePayment />}>
                    </Route>
                    <Route path="success" element={<DonorPageSuccess />} ></Route>   
                </Route>
            </Routes>


        </section>
    )
}

export default DonorMainPage