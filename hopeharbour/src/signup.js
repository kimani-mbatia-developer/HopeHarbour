import React from 'react';
import { useState } from 'react';
import {useNavigate} from 'react-router-dom';
import Cliploader from "react-spinners/ClipLoader"
import image4 from './assets/images/signup/image4.png'

function SignUp(){
    const navigate = useNavigate()

    const [userName,setUserName]=useState("")
    const [email,setEmail]=useState("")
    const [password,setPassword]=useState("")
    const [signUpAttempt, setSignUpAttempt]=useState(false)
    const [signUpMessage, setSignUpMessage]=useState("")
    const [isLoading, setIsLoading]=useState(false)
    const [color, setColor] =useState("#ffffff")


    const [inputDetails, setInputDetails]=useState({
        userName:'',
        email:'',
        password:'',
        role:'donor'
    });
    
    function handleSubmit(event){
        event.preventDefault()
        const input ={
            userName: userName,
            email:email,
            password:password,
            role: "donor"
        }
        setIsLoading(true)
        setInputDetails(input)

        alert(inputDetails.password)
        fetch('https://hopeharbour-api.onrender.com/auth/register',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                username:userName,
                email: email,
                password: password,
                role: "donor"
            }),
        })
        .then(response=>response.json())
        .then((data)=>{
            setSignUpMessage(data.message)
            setSignUpAttempt(true)
            setIsLoading(false)
        })

    }
    
    function handleUserNameChange(event){
        setUserName(event.target.value)
        //alert(inputDetails.email)
    }

    function handleEmailChange(event){
        setEmail(event.target.value)
        //alert(inputDetails.email)
    }

    function handlePasswordChange(event){
        setPassword(event.target.value)
        //alert(inputDetails.email)
    }

/*     setInputDetails({
        [event.target.name]: event.target.value
    }) */


    const firstDiv ={
        backgroundColor:"#97B3DC",
        display:"flex",
        position:"relative"
    }

    const signUpForm={
        position:"relative",
        width:"500px",
        height:"570px",
        backgroundColor:"#569DDF",
        borderRadius:"50px",
        textAlign:"center",
        left:"-10%",
        marginTop:"5%"

    }

    const infoSquare={
        position:"absolute",
        backgroundColor:"#77C5D6",
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

    const signUpHeader3={
        position:"relative",
        paddingTop:"10px",
        fontSize:"16px",
        fontFamily:"FaunaOne",
        fontWeight:"Bold",
        color:"white"
    }



    return(
        <div className='container-fluid' style={firstDiv}>
            <img src={image4}></img>
            <div className='container' style={signUpForm}>
                <h4 style={signUpHeader}>Sign Up</h4>
                <h6 style={signUpHeader2}>as a Donor</h6>
                <div className='container' style={inputContainer}>
                    <form onSubmit={handleSubmit}>
                        <input name='userName' style={inputField} type='text' placeholder='Username' onChange={handleUserNameChange}></input>
                        <input name='email' style={inputField} type='email' placeholder='Email' onChange={handleEmailChange}></input>
                        <input name='password' style={inputField} type='password' placeholder='Password'onChange={handlePasswordChange}></input>
                    </form>

                </div>
                <div className='container' style={{display:"flex", paddingTop:"30px", marginLeft:"5%"}}>
                    {isLoading?(<div className='container' style={signUpButtonStyle}>
                    <Cliploader
                                color={color}

                            />
                    </div>):(
                         <button type='submit' style={signUpButtonStyle} onClick={handleSubmit}>Sign Up</button>
                    )}
                   
                    <button style={signUpButtonStyle} onClick={()=>navigate('/registercharity')}>Register Charity</button>
                </div>

                {signUpAttempt?(
                                <div className="container" style={{height:"90%",marginTop:"5%"}}>
                                    {signUpMessage?(
                                         <div className="container" style={{height:"10%",borderRadius:"30px",backgroundColor:"green",marginTop:"5%"}}>
                                            <h6 style={signUpHeader3}>{signUpMessage}</h6>
                                         </div>
                                        
                                        ):(
                                        <div className="container" style={{height:"10%",borderRadius:"30px",backgroundColor:"red",marginTop:"5%"}}>
                                            <h6 style={signUpHeader3}>{signUpMessage}</h6>
                                         </div>
                                        )}

                                
                            </div>):(<div></div>)}

            </div>
            <div className='container' style={infoSquare}>
                    <p style={infoSquareText}>Join Hopeharbour's network of charities, ranked among the most impactful globally</p>
            </div>

            </div>
    )
}

export default SignUp