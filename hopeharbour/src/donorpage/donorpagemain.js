import React from "react";
import DonorPageNavBar from "./donorpagenavbar";
import DonorPageDashboard from "./donorpagedashboard";
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
                <Route path="/" element={<DonorPageDashboard />}></Route>
            </Routes>


        </section>
    )
}

export default DonorMainPage