import React from 'react';
import Cliploader from "react-spinners/ClipLoader"
import { useState } from 'react';
import {useNavigate} from 'react-router-dom';
import image1 from './assets/images/registercharity/charityimage.png'

function RegisterCharity(){

    
    const [isLoading, setIsLoading]=useState(false)
    const [charityName, setCharityName]=useState("");
    const [charityEmail, setCharityEmail]=useState("");
    const [charityDescription, setCharityDescription]=useState("");
    const [applicationMessage, setApplicationMessage]=useState("");
    const [applicationSuccess, setApplicationSuccess]=useState(false)
    const [color, setColor] =useState("#ffffff")

    const firstDiv ={
        backgroundColor:"#97B3DC",
        display:"flex",
        position:"relative",
        opacity:"1"
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

    const infoSquare2={
        position:"fixed",
        backgroundColor:"#569DDF",
        width:"550px",
        height:"500px",
        left:"40%",
        top:"20%",
    }
    
    const infoSquareText2={
        position:'relative',
        fontFamily:"HeeboLight",
        fontSize:"22px",
        color:"white",
        marginTop:"30%",
        padding:"20px"
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

    const signUpButtonStyle2={
        fontFamily:"HeeboMedium",
        width:"170px",
        height:"60px",
        color:"white",
        backgroundColor:"#97B3DC",
        border:"none",
        borderRadius:"50px",
        fontSize:"12pt",
        marginTop:"10%",
        marginLeft:"30%"
    }

    const overlay={
        position:"fixed",
        width:"100%",
        height:"100%",
        top:"0",
        left: "0",
        right: "0",
        bottom: "0",
        backgroundColor: "rgba(0,0,0,0.7)",
        zIndex: "2"
    }

    function handleCharityName(event){
        setCharityName(event.target.value)
    }

    function handleCharityEmail(event){
        setCharityEmail(event.target.value)
    }

    function handleCharityDescription(event){
        setCharityDescription(event.target.value)
    }

    function submitCharityApplication(){
        setIsLoading(true)
        fetch('https://hopeharbour-api.onrender.com/charities/apply',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                name:charityName,
                description: charityDescription,
            }),
        })
        .then(res=>res.json())
        .then((data)=>{
            if (data.message=="Application submitted successfully"){
                setApplicationMessage(data.message)
                alert(applicationMessage)
                setApplicationSuccess(true)
                setIsLoading(false)
            }
            else{
                
            }
            
            
            
        })
    }

    return(
        <>
        <div className='container-fluid' style={firstDiv}>
            <div className='container' style={signUpForm}>
                <h4 style={signUpHeader}>Apply to become a partner </h4>
                <div className='container' style={inputContainer}>
                    <input style={inputField} type='text' placeholder='Name of your organisation' onChange={handleCharityName}></input>
                    <input style={inputField} type='text' placeholder='Email' onChange={handleCharityEmail}></input>
                    <input style={inputField} type='text' placeholder='Description' onChange={handleCharityDescription}></input>
                </div>
                <div className='container' style={{paddingTop:"30px", marginLeft:"0%"}}>
                    {isLoading?(<button style={signUpButtonStyle}>
                        <Cliploader color={color} />
                    </button>):(<button style={signUpButtonStyle} onClick={submitCharityApplication}>Apply</button>)}
                    
                </div>
                
            </div>
            <img src={image1}></img>
            <div className='container' style={infoSquare}>
                    <p style={infoSquareText}>We only partner with High impact charities. Apply here for evaluation</p>
            </div>


            </div>
        
            {applicationSuccess?(
                <div className='container-fluid' style={overlay}>
                    <div className='container' style={infoSquare2}>
                        <p style={infoSquareText2}>{applicationMessage}, One of our agents will get back to you soon</p>
                        <button style={signUpButtonStyle2}>Return To homepage</button>
                    </div>     
                </div>

            ):(<div></div>)}
            </>
    )
}

export default RegisterCharity