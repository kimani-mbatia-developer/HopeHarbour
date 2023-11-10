import React from "react";
import CharityPageNavBar from "./charitypagenavbar";
import CharityPageDetails from "./charitypagedetails";
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom'; 
import CharityPageDashboard from "./charitypagedashboard";

const stripePromise = loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

function CharityPageMain(){

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
            <CharityPageNavBar />
            <Routes>
                <Route path="" element={<CharityPageDashboard />}></Route>
                <Route path="details" element={<CharityPageDetails />}></Route>
            </Routes>


        </section>
    )
}

export default CharityPageMain