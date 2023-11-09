import React from "react";
import { useNavigate } from "react-router-dom";

function DonorPageNavBar(){

    const navigate = useNavigate()

    const navbarStyle={
        position:"relative",
        marginTop:"2%",
        left:"2px",
        width:"16%",
        height:"1300px",
        backgroundColor:"#569DDF",
        borderRadius:"30px",
        textAlign:"center"
    }

    const navbarStyle2={
        position:"relative",
        height:"100%",
        width:"100%",
        top:"1%",
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
        height:'5%',
        width:"100%",
        marginTop:"10%"
    }

    const navLinkStyle2 ={
        position:"relative",
        backgroundColor:"transparent",
        border: "none",
        borderRadius:"30px",
        fontFamily:"HeeboBold",
        fontSize:"20px",
        color:"white",
        height:'5%',
        width:"100%",
        marginTop:"1%"
    }

    function logout(){
        fetch('https://hopeharbour-api.onrender.com/auth/logout',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },

        })
        .then(res=> res.json())
        .then((data)=>{alert(data.message)},
        navigate("/")
        )
    }

    return(
        <div className="container" style={navbarStyle}>
            <div className="container" style={navbarStyle2}>
                <button style={navLinkStyle} onClick={()=>navigate('/donorMainPage')}>Dashboard</button>
                <button style={navLinkStyle} onClick={()=>navigate('details')}>Personal Details</button>
                <button style={navLinkStyle}>Payment Info</button>
                <button style={navLinkStyle} onClick={()=>navigate('donate')}>Make a Donation</button>
            </div>
            <div className="container" style={{border:"3px solid white", marginTop:"-50%", borderRadius:"30px"}}>
                <button style={navLinkStyle2} onClick={()=>{logout()}}>Logout</button>
            </div>

        </div>
    )
}

export default DonorPageNavBar