import React from "react";
import DonorPageNavBar from "./donorpagenavbar";
import DonorPageDashboard from "./donorpagedashboard";
import DonorPageDetails from "./donorpagedetails";
import DonorPageDonate from "./donorpagedonate";
import DonorPagePayment from "./donorpagePayment";
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom'; 

function DonorMainPage(){

    const sectionStyle={
        backgroundColor:"#97B3DC",
        display:"flex"
    }



    return(
        <section style={sectionStyle}>
            <DonorPageNavBar />
            <Routes>
                <Route path="" element={<DonorPageDashboard />}></Route>
                <Route path="details" element={<DonorPageDetails />}></Route>
                <Route path="donate" element={<DonorPageDonate />}>
                    <Route path="payment" element={<DonorPagePayment />}></Route>
                </Route>
            </Routes>


        </section>
    )
}

export default DonorMainPage