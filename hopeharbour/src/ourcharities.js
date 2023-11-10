import React from "react";
import { useState, useEffect } from "react";

function OurCharities(){

    const [charityList, setCharityList]=useState([])


    useEffect(function(){
        fetch('https://hopeharbour-api.onrender.com/charities/')
        .then((response)=>response.json())
        .then((data)=>{
            setCharityList(data)
        })
    })


    function CharityDisplay(){
        let items =charityList.map((charity)=>(
            <div className='container' style={charityContainer}>
            <h3 style={{fontFamily:"HeeboLight",color:"white", fontSize:"30px", marginTop:"30%"}}>{charity.name}</h3>    
        </div>
            ))

            return items
        }

    const charityContainer={
        margin:"15px",
        backgroundColor:"#CEDC97",
        width:"250px",
        height:"250px",
        textAlign:"center"
    }

    const header2={
        fontSize:"48px",
        fontFamily:"FaunaOne",
        fontWeight:"Bold",
        color:"white"
    }

    
    return(
        <div className='container-fluid' style={{backgroundColor:"#569DDF",height:'430px'}}>
        <div className='container' style={{position:"relative", paddingTop:"50px",textAlign:'center'}}>
            <h2 style={header2}>Our Charities</h2>
            <div className='container' style={{ marginLeft:"2px",textAlign:"center",display:"flex"}}>
                <CharityDisplay />
            </div>

        </div>
    </div>    
    )
}
export default OurCharities