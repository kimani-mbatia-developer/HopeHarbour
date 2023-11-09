import React, { useState,useEffect } from "react";
import { useNavigate } from "react-router-dom";
import DonorPagePayment from "./donorpagePayment";

function DonorPageDonate(){

    const [charityList,setCharityList]=useState([])
    const [amount, setAmount]=useState("")
    const [showPaymentSection, togglePaymentSection]=useState(false)
    const [selectedCharityId, setCharityId]= useState('')
    const [selectedCharityName, setCharityName] = useState('')

    const navigate=useNavigate()

    useEffect(()=>{
        fetch('https://hopeharbour-api.onrender.com/charities/')
        .then((response)=>response.json())
        .then(data=>{
            setCharityList(data)
        })
    },[])

    function navigatetoPay(event){
        if (amount == ""){
            alert("Please Put in a valid amount")
        }
        else{
            setCharityId(event.target.id)
            setCharityName(event.target.name)
            togglePaymentSection(true)
        }
        //alert(event.target.id)
    }

    function setDonationAmountEvent(event){
        setAmount(event.target.value)
    }

    const mainContainer={
        backgroundColor:"#E9E9E9",
        marginTop:"2%",
        width:"70%",
        height: "auto",
        borderRadius:"30px",
        textAlign:"center",
    }

    let charities =[
        {name:"Amref"},
        {name:"Doctors Without Borders"},
        {name:"Habitat for Humanity"},
        {name:"Hopeharbour Inc"}
    ]

    let inputStyle1={
        border:"none",
        borderRadius:"30px",
        backgroundColor:"#D9D9D9",
        width:"300px",
        height:"60px",
        textAlign:"center"
    }

    let buttonStyle1={
        border:"none",
        borderRadius:"30px",
        backgroundColor:"#D9D9D9",
        width:"100%",
        height:"60px",
        fontSize:"12px",
    }

    let buttonStyle2={
        border:"none",
        borderRadius:"30px",
        backgroundColor:"#97B3DC",
        width:"100%",
        height:"60px",
        fontSize:"12px"
    }

    let buttonStyle3={
        fontFamily:"HeeboBold",
        border:"none",
        borderRadius:"30px",
        backgroundColor:"#97B3DC",
        width:"250px",
        height:"60px",
        fontSize:"18px",
        color:"white"
    }

    function showID(event){
        
        
    }

    const listCharities = charityList.map((charity)=>
    <>   
        <div className="container-fluid" style={{display:"flex", marginTop:"100px"}}>
            <div className="container" style={{width:"400px", height:"400px", backgroundColor:'#D9D9D9', textAlign:"left", borderRadius:"30px"}}>
            </div>
            
        <div className="container" style={{width:"fit", textAlign:"center", width:"50%"}} >
            <h2 style={{fontFamily:"HeeboBold",marginBottom:"10%"}}>{charity.name}</h2>
            <input type="number" style={inputStyle1} placeholder="Amount" onChange={setDonationAmountEvent}></input>
            <div className="container" style={{height:"60px", width:"300px", marginTop:"50px"}}>
                <div className="row" style={{width:"300px"}}>
                    <div className="col">
                        <button style={buttonStyle1}>Become a frequent Donor</button>
                    </div>
                    <div className="col">
                        <button style={buttonStyle2}>One Time Donation</button>
                    </div>
                </div>
            </div>
            <div className="container" style={{marginTop:"50px",marginBottom:"50px"}}>

                
            </div>
            <button id={charity.id} name={charity.name} style={buttonStyle3} onClick={navigatetoPay}>Donate</button>
        </div>
        </div>

    </>

    )

    return(
        <>
        {showPaymentSection==true?(<DonorPagePayment amount={amount} selectedCharityId={selectedCharityId} selectedCharityName={selectedCharityName} />):(
                    <div className="container" style={mainContainer}>
                    <h3 style={{fontFamily:"HeeboBold",marginTop:"5%"}}>Make a Donation</h3>    
                    {listCharities}
                </div>
        )}



        </>

    )
}

export default DonorPageDonate