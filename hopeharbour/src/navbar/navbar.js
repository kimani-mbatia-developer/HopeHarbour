import React from 'react';
import logo from '../assets/images/Hopeharbour.png'
import userImageCont from '../assets/images/navbar/Ellipse 9.png'
import {useNavigate} from 'react-router-dom';

function Navbar({isLoggedIn, donorCredentials}){

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

    function showRole(){
        alert(donorCredentials.role)
    }


    return (
        <nav className='navbar' style={navbarStyle}>
            <div className='container-fluid'>
                    <div className='container-fluid' style={{position:"relative",left:"0%",top:"20px"}}>
                            <img src={logo} style={logoStyle}></img>
                    </div>
                {isLoggedIn?(
                <div className='container-fluid' style={{position:"relative",left:"75%",top:"-30px"}}>
                    {/*  <button onClick={showRole}>ShowRole</button>  */}
                    <button style={navButtonStyle} onClick={()=>navigate('/')}>Home</button>
                    <button style={navButtonStyle}>About Us</button>
                    {donorCredentials.role=="donor"?(<button style={signUpButtonStyle} onClick={()=>navigate('/donorMainPage')}>Dashboard</button>)
                    :
                    (<button style={signUpButtonStyle} onClick={()=>navigate('/charityMainPage')}>Dashboard</button>)}
                    
                    <img src={userImageCont} style={{width:"70px",height:"70px", position:"relative", left:"1%" }}></img>
                    <p style={{marginLeft:"18%"}}>{donorCredentials.username}</p>
                                   
                </div>
        ):(        
                <div className='container-fluid' style={{position:"relative",left:"75%",top:"-30px"}}>
                    <button style={navButtonStyle} onClick={()=>navigate('/')}>Home</button>
                    <button style={navButtonStyle}>About Us</button>
                    <button style={navButtonStyle} onClick={()=>navigate('/login')}>Login</button>
                    <button style={signUpButtonStyle} onClick={()=>navigate('signup')}>Sign Up</button>
                </div>
        )}
            </div>
        </nav>
    )
}

export default Navbar