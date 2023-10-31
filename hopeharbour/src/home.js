import React from 'react';

import shape1 from './assets/images/home/Vector 1.png'
import image2 from './assets/images/home/image2.png'
import vector3 from './assets/images/home/Vector 3.png'
import vector4 from './assets/images/home/Vector 4.png'


const homeStyle={
    backgroundColor:"#97B3DC",
    display:"inline-block",
    overflow:"hidden"
}

const firstDiv={
    display:"flex",
    position:"relative",
    overflow:"hidden"
}

const header1Container={
    position:"absolute",
    left:"5%",
    top:"20%",
    width:"600px"
}

const header1={
    fontFamily:"HeeboBold",
    fontSize:"40px"
}

const header1Text={
    fontFamily:"HeeboLight",
    fontSize:"24px"
}

const header1Button={
    backgroundColor:"#569DDF",
    fontFamily:"HeeboBold",
    width:"250px",
    height:"62px",
    border:"none",
    color:"white",
    borderRadius:"30px"
}

const infoSquare={
    position:"absolute",
    backgroundColor:"#569DDF",
    width:"300px",
    height:"300px",
    left:"70%",
    top:"30%",
}

const infoSquareText={
    position:'relative',
    fontFamily:"HeeboLight",
    fontSize:"20px",
    color:"white",
    marginTop:"30%"
}

const FactBox={
    width:"750px",
    height:"400px",
    backgroundColor:"#569DDF",
    borderRadius:"50px"
}

const altButtonStyle={
    width:"300px",
    height:"50px",
    borderRadius:"30px",
    backgroundColor:"#77C5D6",
    textAlign:"center",
    border:'none',
    fontFamily:"HeeboBold",
    fontSize:"20px",
    color:"white"
}

const header2={
    fontSize:"40px",
    fontFamily:"FaunaOne",
    fontWeight:"Bold",
    color:"white"
}

const header3Container={
    position:"absolute",
    right:"5%",
    top:"20%",
    width:"600px",
    zIndex:"9"
}

const quickFacts = [
    {
        title: "$50",
        content: "Can Feed a Child for a day"
    },
    {
        title: "$200",
        content: "Can Support a family for a month"
    },
    {
        title: "$1000", 
        content: "Can Give a village clean water"
    },
]

function Home(){
    return(
        <section style={homeStyle}>
            <div className='container-fluid' style={firstDiv}>
                <img src={shape1} style={{position:"relative" ,width:"50%", height:"732px" ,left:"-3%"}}></img>
                <div className='container' style={header1Container}>
                    <h4 style={header1}>Keep moving your mission foward</h4>
                    <p style={header1Text}>Hopeharbour has chosen to partner with the most impactful  charities around the world to ensure that those in need receive every penny.</p>
                    <button style={header1Button}>Learn More</button>
                </div>
                <img src={image2} style={{width:"60%", height:"612px", position:"relative",marginLeft:"-3%"}}></img>
                <div className='container' style={infoSquare}>
                    <p style={infoSquareText}>Join Hopeharbour's network of charities, ranked among the most impactful globally</p>
                </div>
            </div>

            <div className='container' style={FactBox}>
                {quickFacts.map(function(fact){
                    return(
                        <div className='row' style={{padding:"20px"}}>
                            <div className='col'>
                                <div className='container' style={{width:"170px",height:"60px", borderRadius:"30px", backgroundColor:"#77C5D6", textAlign:"center"}}>
                                    <p style={{position: "relative", fontFamily:"HeeboRegular", color:"white", top:"10px", fontSize:"24px"}}>{fact.title}</p>
                                </div>
                            </div>
                            <div className='col'>
                                <div className='container' style={{textAlign:"center"}}>
                                        <h6 style={{position: "relative", fontFamily:"HeeboBold", color:"white", top:"10px", fontSize:"20px"}}>{fact.content}</h6>
                                </div>
                            </div>
                    </div>
                    )

                })}
                <div className='container' style={{textAlign:"center"}}>
                    <button style={altButtonStyle}> Sign Up as a Benefactor</button>
                </div>
               
            </div>

            <div className='container' style={{position:"relative", left:"30%", paddingTop:"50px"}}>
                <h2 style={header2}>Our Charities</h2>    
            </div>

            <div className='container-fluid' style={firstDiv}>
                <img src={vector4} style={{width:"70%",position:"relative",left:"-3%"}}></img>
                <div className='container' style={header3Container}>
                    <h4 style={header1}>Sign up to our Newsletter</h4>
                    <p style={header1Text}>Get the latest news on our charities, their works and their progress. Knowledge and accountability are important to us.</p>
                    <button style={header1Button}>Learn More</button>
                </div>
                <img src={vector3} style={{width:"70%",position:"relative",right:"21%"}}></img>
            </div>    
        </section>
    )
}

export default Home