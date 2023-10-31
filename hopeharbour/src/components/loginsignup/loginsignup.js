import React from 'react';
import './LoginSignup.css';

const LoginSignup = () => {
  const [action,setAction]=useState("sign up")  
    return (
        <div className='container'>
            <div className="header">
                <div className="text">{action}</div>
                <div className="underline"></div>
            </div>
            <div className="inputs">
                {action==="login"?<div></div>:<div className="input">
                    <img src={user_icon} alt=""/>
                    <input type="text"placeholder="Name"/>
                </div>}

                <div className="input">
                    <img src={user_icon} alt=""/>
                    <input type="text"placeholder="Name"/>
                </div>
                <div className="input">
                    <img src={email_icon} alt=""/>
                    <input type="email"placeholder="Email Id"/>
                </div>
                <div className="input">
                    <img src={password_icon} alt=""/>
                    <input type="password"placeholder="password"/>
                </div>
            </div>
            {action==="sign up"?<div></div>:<div className="forgot-password">lost password? <span>click Here!</span></div>}

            <div className="forgot-password">lost password? <span>click Here!</span></div>
            <div className="submit-container">
                <div className={action==="login"?"submit gray":"submit"}onClick={()=>{setAction("sign up")}}>signup</div>
                <div className={action==="sign up"?"submit gray":"submit"}onClick={()=>{setAction("login")}}>login</div>
            </div>
        </div>
    );
};

export default LoginSignup;
