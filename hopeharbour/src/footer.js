import React from "react";
import logo from './assets/images/Hopeharbour.png'

function Footer(){
    const footerStyle={
        height:"300px",
        backgroundColor:"#E9E9E9",
        overflow:"hidden"
    }

    const footerTextStyle={
        fontFamily:"HeeboRegular",
        fontSize: "15px",
        color: "#C7C7C7",

    }

    const logoStyle2={
        fontFamily:"FaunaOne",
        fontWeight:"bold",
        //fontSize:"16pt",
        color:"#479FF0"
    }

    return(
        <div className="footer" style={footerStyle}>
            <div className="container" style={{position:"relative", left:"-35%", width:"300px"}}>
                <div className="row" style={{}}>
                    <div className="col" style={{paddingTop:"30px",borderRight:"4px solid grey", borderColor:"#D9D9D9", left:"0%", textAlign:"center"}}>
                        <br></br>
                        <h5 style={{fontFamily:"HeeboBold"}}>About</h5>
                        <p style={footerTextStyle}>Home</p>
                        <p style={footerTextStyle}>About Us</p>
                    </div>
                    <div className="col" style={{paddingTop:"30px",left:"1%", textAlign:"center"}}>
                        <br></br>
                        <h5 style={{fontFamily:"HeeboBold",}}>Users</h5>
                        <p style={footerTextStyle}>Login</p>
                        <p style={footerTextStyle}>Support</p>
                    </div>
                </div>
            </div>
            <div className="container" style={{position:"relative",left:"30%", bottom:"-15%"}}>
                {/* <img src={logo} style={logoStyle}></img> */}
                <h2 style={logoStyle2}>Hopeharbour</h2>
            </div>
        </div>
    )
}

export default Footer