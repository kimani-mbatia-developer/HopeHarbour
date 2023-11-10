import React from "react";
import { useNavigate } from "react-router-dom";

function DonorPageSuccess(){

    const navigate= useNavigate()

    const dashboardContainer1={
        //position:"relative",
        marginTop:"5%",
        backgroundColor:"#569DDF",
        width:"350px",
        height:"400px",
        //borderRadius:"30px"
    }

    const dashboardContainer1Text={
        marginTop:"20%",
        fontFamily:"HeeboBold",
        color:"white",
        paddingTop:"3%",
        paddingLeft:"5%"
    }

    const returnStyle={
        border:"none",
        marginTop:"30%",
        backgroundColor:"#CEDC97",
        borderRadius:"30px",
        color:"white",
        width:"80%",
        height:"20%"
    }

    return(    <div className="container" style={dashboardContainer1}>
    <div className="row">
        <div className="col" style={dashboardContainer1Text}>
            <p style={{fontSize:"20px",fontFamily:"HeeboRegular", marginTop:"5%"}}>October 25 2023</p>
            <h5 style={{ fontSize:"32px", marginTop:"5%"}}>Payment Successful!</h5>
            <button style={returnStyle} onClick={()=>{navigate('/donorMainPage')}}>Return To Dashboard</button>
        </div>
    </div>
</div>)

}

export default DonorPageSuccess