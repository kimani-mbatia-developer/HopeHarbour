import React from "react"
import Ellipse2 from '../assets/images/donordashboard/Ellipse 2.png'
import { useState } from "react"

function DonorPageDashboard(){

    const[yourDonations, setYourDonations]=useState([])

    const dashboardContainer1={
        //position:"relative",
        marginTop:"5%",
        backgroundColor:"#569DDF",
        width:"1350px",
        height:"400px",
        borderRadius:"30px"
    }

    const dashboardContainer1Text={
        fontFamily:"HeeboBold",
        color:"white",
        paddingTop:"3%",
        paddingLeft:"5%"
    }

    const dashboardContainer2={
        marginTop:"5%",
        backgroundColor:"white",
        width:"1350px",
        height:"400px",
        borderRadius:"30px"
    }

    const dashboardContainer2Heading={
        fontFamily:"HeeboBold",
        color:"white",
        paddingTop:"3%",
        paddingLeft:"5%",

    }

    const charityContainer={
        position:"relative",
        top:"10%",
        backgroundColor:"#E9E9E9",
        width:"70%",
        height:"15%",
        borderRadius:"30px"
    }

    return(
        <div className="container">
            <div className="container" style={dashboardContainer1}>
                <div className="row">
                    <div className="col" style={dashboardContainer1Text}>
                        <p style={{fontSize:"20px",fontFamily:"HeeboRegular", marginTop:"5%"}}>October 25 2023</p>
                        <h5 style={{ fontSize:"32px", marginTop:"5%"}}>Welcome back, Carlton</h5>
                        <p style={{fontFamily:"HeeboRegular", marginTop:"5%"}}>Stay updated on your beneficiaries</p>
                    </div>
                    <div className="col" style={{paddingTop:"1%"}}>
                        <img src={Ellipse2} style={{width:"350px",height:"350px"}}></img>
                    </div>
                </div>
            </div>
            <h3 style={dashboardContainer2Heading}>Your beneficiaries</h3>
                <div className="container" style={dashboardContainer2}>
                <div className="container" style={charityContainer}>
                    <div className="container" style={{display:"flex"}}>
                        <p>Charity Name</p>
                        <button>Donate Now</button>
                    </div>
                </div>
                </div>
            <h3 style={dashboardContainer2Heading}>Support new charities</h3>
            <div className="container" style={dashboardContainer2}>
                <div className="container" style={charityContainer}>
                    <div className="container" style={{display:"flex"}}>
                        <p>Charity Name</p>
                        <button>Donate Now</button>
                    </div>
                </div>
            </div>
        </div>    
    )
}

export default DonorPageDashboard

