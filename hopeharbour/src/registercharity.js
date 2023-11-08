import React from 'react';
import { useState } from 'react';
import {useNavigate} from 'react-router-dom';
import image1 from './assets/images/registercharity/charityimage.png'

function RegisterCharity(){

    

    const [inputDetails, setInputDetails]=useState([]);

    const firstDiv ={
        backgroundColor:"#97B3DC",
        display:"flex",
        position:"relative"
    }

    const signUpForm={
        position:"relative",
        width:"500px",
        height:"500px",
        backgroundColor:"#569DDF",
        borderRadius:"50px",
        textAlign:"center",
        left:"10%",
        marginTop:"5%"

    }

    const infoSquare={
        position:"absolute",
        backgroundColor:"#D9D9D9",
        width:"300px",
        height:"300px",
        left:"75%",
        top:"50%",
    }
    
    const infoSquareText={
        position:'relative',
        fontFamily:"HeeboLight",
        fontSize:"20px",
        color:"white",
        marginTop:"30%"
    }

    const signUpHeader={
        marginTop:"10%",
        fontSize:"36px",
        fontFamily:"FaunaOne",
        fontWeight:"Bold",
        color:"white"
    }


    const signUpHeader2={
        marginTop:"1%",
        fontSize:"16px",
        fontFamily:"FaunaOne",
        fontWeight:"Bold",
        color:"white"
    }

    const inputContainer={

    }

    const inputField={
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

    const signUpButtonStyle={
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
        <div className='container-fluid' style={firstDiv}>
            <div className='container' style={signUpForm}>
                <h4 style={signUpHeader}>Register Charity </h4>
                <div className='container' style={inputContainer}>
                    <input style={inputField} type='text' placeholder='Name of your organisation'></input>
                    <input style={inputField} type='text' placeholder='Email'></input>
                    <input style={inputField} type='password' placeholder='Password'></input>
                </div>
                <div className='container' style={{paddingTop:"30px", marginLeft:"0%"}}>
                    <button style={signUpButtonStyle}>Apply</button>
                </div>
                
            </div>
            <img src={image1}></img>
            <div className='container' style={infoSquare}>
                    <p style={infoSquareText}>We only partner with High impact charities. Apply here for evaluation</p>
            </div>
            </div>
    )
}

export default RegisterCharity