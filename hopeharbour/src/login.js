import React from "react";
import vector6 from './assets/images/login/Vector 6.png'
import vector13 from './assets/images/login/Vector 13.png'

function Login(){

    const mainStyle={
        position:"relative",
        display:"flex",
        overflow: "hidden"
    }

    const vector6Style={
        position:"relative",
    }

    const vector13Style={
        position:"relative",
        left:"-20%",
        width:"77%"
    }

    const infoSquare={
        position:"absolute",
        backgroundColor:"#569DDF",
        width:"300px",
        height:"300px",
        left:"33%",
        top:"50%",
    }
    
    const infoSquareText={
        position:'relative',
        fontFamily:"HeeboLight",
        fontSize:"20px",
        color:"white",
        marginTop:"30%"
    }

    const loginHeader={
        position:"relative",
        marginTop:"10%",
        fontSize:"36px",
        fontFamily:"FaunaOne",
        fontWeight:"Bold",
        color:"white"
    }


    const signUpHeader2={
        position:"relative",
        marginTop:"1%",
        fontSize:"16px",
        fontFamily:"FaunaOne",
        fontWeight:"Bold",
        color:"white"
    }

    const loginForm={
        position:"relative",
        width:"500px",
        height:"570px",
        backgroundColor:"#569DDF",
        borderRadius:"50px",
        textAlign:"center",
        left:"-60%",
        marginTop:"5%"
    }

    const inputField={
        position:"relative",
        fontFamily:"HeeboBold",
        textAlign:"center",
        borderRadius:"30px",
        border:"none",
        width:"370px",
        height:"60px",
        marginTop:"15px",
        fontSize:"16px",
        color:"black",
        backgroundColor:"#E9E9E9"
    }

    const loginButtonStyle={
        position:"relative",
        fontFamily:"HeeboMedium",
        width:"170px",
        height:"60px",
        color:"white",
        backgroundColor:"#97B3DC",
        border:"none",
        borderRadius:"50px",
        fontSize:"12pt",
        marginLeft:"20px"
    }

    return(
        <div className="container-fluid" style={mainStyle}>
            <img src={vector6} style={vector6Style}></img>
            <img src={vector13} style={vector13Style}></img>
            <div className='container' style={infoSquare}>
                    <p style={infoSquareText}>Join Hopeharbour's network of charities, ranked among the most impactful globally</p>
            </div>
            <div className='container' style={loginForm}>
                <h4 style={loginHeader}>Login</h4>
                <h6 style={signUpHeader2}>as a Donor</h6>
                <div className='container'>
                    <input style={inputField} type='text' placeholder='Email'></input>
                    <input style={inputField} type='text' placeholder='Password'></input>
                </div>
                <div className='container' style={{paddingTop:"30px"}}>
                    <button style={loginButtonStyle}>Login</button>
                </div>
                <div className='container' style={{paddingTop:"30px"}}>
                    <h6 style={signUpHeader2}>Don't have an account?</h6>
                    <button style={loginButtonStyle}>Sign Up</button>
                </div>
                
            </div>
        </div>
    )
}

export default Login