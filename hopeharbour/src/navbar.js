import React from 'react';
import logo from './assets/images/Hopeharbour.png'
import {useNavigate} from 'react-router-dom';

function Navbar(){

    const navigate = useNavigate()

    const navbarStyle={
        backgroundColor:"#E9E9E9",
        height:"120px",
        overflow:"hidden"
    }

    const logoContainer={
        position:"relative",
    }

    const logoStyle={
        width:"286px"
    }

    const navButtonStyle={
        fontFamily:"HeeboMedium",
        backgroundColor:"transparent",
        border:"none",
        fontSize:"12pt",
        marginLeft:"20px"
    }

    const signUpButtonStyle={
        fontFamily:"HeeboMedium",
        width:"100px",
        height:"50px",
        color:"white",
        backgroundColor:"#569DDF",
        border:"none",
        borderRadius:"50px",
        fontSize:"12pt",
        marginLeft:"20px"
    }

    return (
        <nav className='navbar' style={navbarStyle}>
            <div className='container-fluid'>
                    <div className='container-fluid' style={{position:"relative",left:"0%",top:"20px"}}>
                            <img src={logo} style={logoStyle}></img>
                    </div>
                        <div className='container-fluid' style={{position:"relative",left:"75%",top:"-30px"}}>
                            <button style={navButtonStyle} onClick={()=>navigate('/')}>Home</button>
                            <button style={navButtonStyle}>About Us</button>
                            <button style={navButtonStyle}>Login</button>
                            <button style={signUpButtonStyle} onClick={()=>navigate('signup')}>Sign Up</button>

                        </div>
            </div>
        </nav>
    )
}

export default Navbar