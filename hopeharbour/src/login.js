import React, { useEffect } from "react";
import vector6 from './assets/images/login/Vector 6.png'
import vector13 from './assets/images/login/Vector 13.png'
import Cliploader from "react-spinners/ClipLoader"
import { useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";


function Login({setLoginStatus,setDonorCredentials}){

    const [email,setEmail]=useState("")
    const [password,setPassword]=useState("")
    const [loginAttempt, setLoginAttempt]=useState(false)
    const [loginMessage, setLoginMessage]=useState("")
    const [isLoading, setIsLoading]=useState(false)
    const [color, setColor] =useState("#ffffff")

    const navigate = useNavigate()


    function handleEmailInput(event){
        setEmail(event.target.value)
    }

    function handlePasswordInput(event){
        setPassword(event.target.value)
    }
    

    function handleLogin(){
        //event.preventDefault()

        /*
        try{
            const response = fetch('https://hopeharbour-api.onrender.com/auth/login',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                email:email,
                password: password,
            }),
        });

        if (response.ok){alert("Login Succesful", response.message)}

        }catch(error){
            alert('Error',error)
        }
        */

        setIsLoading(true)
         fetch('https://hopeharbour-api.onrender.com/auth/login',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                email:email,
                password: password,
            }),
        })
        .then(res=> res.json())
        .then((data)=>{
            //alert(data.message)
            setLoginMessage(data.message)
            //alert(loginStatus)
            setLoginAttempt(true)
            setIsLoading(false)
            if(data.message ==="Login successful"){
                const accessToken = data.data.access_token;
                localStorage.setItem('access_token', accessToken);
                
                if(accessToken){alert("access token found")}

                const userData = data.data.user_data;
                alert(userData.username);
                localStorage.setItem('user_data', JSON.stringify(userData));
                //setDonorCredentials(userData)
                setLoginStatus()
                navigate("/");
            }
        })
        //.then(setLoginAttempt(true))


    }

    const mainStyle={
        position:"relative",
        display:"flex",
        overflow: "hidden",
        backgroundColor:"#77C5D6"
    }

    const vector6Style={
        position:"relative",
    }

    const vector13Style={
        position:"relative",
        left:"30%",
        //width:"77%"
    }

    const infoSquare={
        position:"absolute",
        backgroundColor:"#569DDF",
        width:"300px",
        height:"300px",
        left:"23%",
        top:"45%",
    }
    
    const infoSquareText={
        textAlign: "justify",
        position:'relative',
        fontFamily:"HeeboLight",
        fontSize:"20px",
        color:"white",
        marginTop:"30%"
    }

    const loginHeader={
        position:"relative",
        top:"10%",
        fontSize:"36px",
        fontFamily:"FaunaOne",
        fontWeight:"Bold",
        color:"white"
    }

    const signUpHeader2={
        position:"relative",
        marginTop:"12%",
        fontSize:"16px",
        fontFamily:"FaunaOne",
        fontWeight:"Bold",
        color:"white"
    }

    const signUpHeader3={
        position:"relative",
        paddingTop:"10px",
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
        marginLeft:"20px",
        textAlign:"center"
    }
    
    const loadingIconStyle={
        position:"relative",
        fontFamily:"HeeboMedium",
        width:"170px",
        height:"60px",
        color:"white",
        backgroundColor:"#97B3DC",
        border:"none",
        borderRadius:"50px",
        fontSize:"12pt",
        marginLeft:"150px",
        textAlign:"center"
    }

    return(
        <div className="container-fluid" style={mainStyle}>
            <img src={vector13} style={vector13Style}></img>
            <div className='container' style={infoSquare}>
                    <p style={infoSquareText}>Sign in and get updated on the work our charities are doing</p>
            </div>
            <div className="container" style={{position:"relative", left:"-25%",marginTop:"5%"}}>
                <div className='container' style={loginForm}>
                    <h4 style={loginHeader}>Login</h4>
                    <h6 style={signUpHeader2}>as a Donor</h6>
                    <div className='container'>
                        <input style={inputField} type='text' placeholder='Email' onChange={handleEmailInput}></input>
                        <input style={inputField} type='password' placeholder='Password' onChange={handlePasswordInput}></input>
                    </div>
                    <div className='container' style={{paddingTop:"30px"}}>
                        {isLoading==true?(<div style={loadingIconStyle}>
                            <div className="container" style={{paddingTop:"5%"}}>
                            <Cliploader
                                color={color}

                            />
                            </div>

                        </div>)
                        :
                        (<button style={loginButtonStyle} onClick={handleLogin}>Login</button>)}
                        
                        <h6 style={signUpHeader3}>Don't have an account?</h6>
                        <button style={loginButtonStyle} >Sign Up</button>
                    </div>


                            {loginAttempt?(
                                <div className="container" style={{height:"90%",marginTop:"5%"}}>
                                    {loginMessage==="Login Failed"?(
                                         <div className="container" style={{height:"10%",borderRadius:"30px",backgroundColor:"green",marginTop:"5%"}}>
                                            <h6 style={signUpHeader3}>{loginMessage}</h6>
                                         </div>
                                        
                                        ):(
                                        <div className="container" style={{height:"10%",borderRadius:"30px",backgroundColor:"red",marginTop:"5%"}}>
                                            <h6 style={signUpHeader3}>{loginMessage}</h6>
                                         </div>
                                        )}

                                
                            </div>):(<div></div>)}
                    
                    
                </div>
            </div>
        </div>
    )
}

export default Login