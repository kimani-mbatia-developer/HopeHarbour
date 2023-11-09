import React from "react";

function OurCharities(){

    const charityContainer={
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
            <div className='container' style={{marginLeft:"2px",textAlign:"center",display:"flex"}}>
                <div className='container' style={charityContainer}>
                    <h3 style={{fontFamily:"HeeboLight",color:"white", fontSize:"30px", marginTop:"30%"}}>Doctors without borders</h3>    
                </div>
                <div className='container' style={charityContainer}>
                    <h3 style={{fontFamily:"HeeboLight",color:"white", fontSize:"30px", marginTop:"30%"}}>Doctors without borders</h3>    
                </div>
                <div className='container' style={charityContainer}>
                    <h3 style={{fontFamily:"HeeboLight",color:"white", fontSize:"30px", marginTop:"30%"}}>Doctors without borders</h3>    
                </div>    
            </div>

        </div>
    </div>    
    )
}
export default OurCharities