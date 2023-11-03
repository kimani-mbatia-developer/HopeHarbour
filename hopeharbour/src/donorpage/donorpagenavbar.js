import React from "react";

function DonorPageNavBar(){

    const navbarStyle={
        position:"relative",
        left:"2px",
        width:"15%",
        height:"auto",
        backgroundColor:"#569DDF",
        borderRadius:"30px",
        textAlign:"center"
    }

    const navbarStyle2={
        position:"relative",
        height:"100%",
        width:"100%",
        top:"10%",
        borderRadius:"30px",
        textAlign:"center"
    }

    const navLinkStyle ={
        position:"relative",
        backgroundColor:"transparent",
        border: "3px solid white",
        borderRadius:"30px",
        fontFamily:"HeeboBold",
        fontSize:"20px",
        color:"white",
        height:'15%',
        width:"100%",
        marginTop:"10%"
    }

    return(
        <div className="container" style={navbarStyle}>
            <div className="container" style={navbarStyle2}>
                <button style={navLinkStyle}>Dashboard</button>
                <button style={navLinkStyle}>Personal Details</button>
                <button style={navLinkStyle}>Payment Info</button>
                <button style={navLinkStyle}>Make a Donation</button>
            </div>

        </div>
    )
}

export default DonorPageNavBar