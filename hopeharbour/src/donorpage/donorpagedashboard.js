import React from "react"
import Ellipse2 from '../assets/images/donordashboard/Ellipse 2.png'

function DonorPageDashboard(){

    const dashboardContainer1={
        position:"relative",
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

    return(
        <div className="container-fluid" style={{width:"1350px", height:"400px"}}>
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
        </div>
    )
}

export default DonorPageDashboard

