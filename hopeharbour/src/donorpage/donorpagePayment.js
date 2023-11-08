import React from "react";
import { useState } from "react";
import { CardElement } from "@stripe/react-stripe-js";

//Stripe imports
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

import mastercard from "../assets/images/pay/Rectangle 143.png"
import visa from "../assets/images/pay/Rectangle 144.png"

const stripePromise = loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

function DonorPagePayment({amount,selectedCharityId,selectedCharityName}){

    const options = {
        // passing the client secret obtained from the server
        clientSecret: '{{CLIENT_SECRET}}',
        fetch
      };
    

    const [donationMessage, setDonationMessage]=useState("")

    const CARD_ELEMENT_OPTIONS = {
        theme: 'stripe',

        style: {
          base: {
            'color': '#32325d',
            'fontFamily': '"Helvetica Neue", Helvetica, sans-serif',
            'fontSmoothing': 'antialiased',
            'fontSize': '20px',
            
            
            '::placeholder': {
              color: '#aab7c4',
            },
          },
          invalid: {
            color: '#fa755a',
            iconColor: '#fa755a',
          },
        },
      };

    const mainContainer={
        backgroundColor:"#E9E9E9",
        marginTop:"2%",
        width:"70%",
        height: "1000px",
        borderRadius:"30px"
    }

    const charityDisplay={
        marginTop:"10%",
        backgroundColor:"#97B3DC",
        borderRadius:"30px",
        display:"flex",
        width:"90%",
        height:"15%",
        fontSize:"32px",
    }

    const amountDisplay={
        textAlign:"center",
        backgroundColor:"#D9D9D9",
        width:"99%",
        height:"40%",
        borderRadius:"30px",
        fontFamily:"HeeboRegular"
    }

    const selectPaymentCont={
        marginTop:"5%",
        backgroundColor:"#D9D9D9",
        width:"45%",
        height:"5%",
        borderRadius:"30px"
    }

    const paymentModeContainer={
        marginTop:"5%",
        backgroundColor:"#FFFFFF",
        width:"50%",
        height:"40%",
        borderRadius:"30px"
    }

    const inputStyle={
        border:"none",
        backgroundColor:"#D9D9D9",
        borderRadius:"30px",
        width:"80%",
        height:"80px",
        marginTop:"10px",
        textAlign:"center"
    }


    const inputStyle2={
        border:"none",
        backgroundColor:"#D9D9D9",
        borderRadius:"30px",
        width:"30%",
        height:"80px",
        marginTop:"10px",
        textAlign:"center"
    }

    const submitButtonStyle={
        marginTop:"10%",
        border:"none",
        width:"30%",
        height:'50px',
        backgroundColor:"#97B3DC",
        borderRadius:"30px"

    }

    function makeDonation(){
        fetch('https://hopeharbour-api.onreder.com/donations/donate',{
            method:'POST',
            mode:'no-cors',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                amount:amount,
                charity_id: selectedCharityId,
            }),
        })
        .then(res=>res.json())
        .then(data=>{
            setDonationMessage(data.message)
            alert(donationMessage)
        })
    }

    return(
        <div className="container" style={mainContainer}>
            <div className="container" style={charityDisplay}>
                <div className="row" style={{width:"99%", paddingTop:"5%"}}>
                    <div className="col-5">
                        <h2 style={{fontFamily:"FaunaOne",fontWeight:"bold",fontSize:"28px"}}>{selectedCharityName}</h2>
                    </div>
                    <div className="col">
                        <p style={{fontFamily:"HeeboRegular", fontSize:"14px"}}>Amount:</p>
                    </div>
                    <div className="col">
                        <div className="container" style={amountDisplay}>
                            <h3>$ {amount}</h3>
                        </div>
                    </div>
                </div>
                
                {/* <h2>CharityId: {selectedCharityId}</h2> */}
                

                    {/* <button onClick={makeDonation}>Donate now</button> */}
                
            </div>
            <div className="container" style={selectPaymentCont}>
                    <select style={{marginTop:"2%",position:"relative",fontFamily:"HeeboRegular",border:"none", width:"99%"}}  name="paymentMode" id="paymentMode">
                        <option value="card">Card</option>
                        <option value="Paypal">Paypal</option>
                    </select>
            </div>

            <div className="container" style={paymentModeContainer}>
               <div className="container" style={{textAlign:"center"}}>
                    <div className="row" style={{paddingTop:"10%"}}>
                        <div className="col">
                            <img src={mastercard} style={{width:"104px",height:"80px"}}></img>
                        </div>
                        <div className="col">
                            <img src={visa} style={{width:"104px",height:"80px"}}></img>
                        </div>
                    </div>
                </div>
                <div className="container" style={{display:"block",textAlign:"center",marginTop:"10%"}}>
                    <Elements stripe={stripePromise} /* options={options} */>
                        <CardElement id="card-element"  options={CARD_ELEMENT_OPTIONS} />
                    </Elements>
                    <button style={submitButtonStyle}>Pay</button>

                </div>
               


{/*                 <div className="container" style={{display:"block",textAlign:"center"}}>
                    <input style={inputStyle} placeholder="Card Number"></input>
                    <input style={inputStyle} placeholder="Name of Card"></input>
                    <input type="month" style={inputStyle2} placeholder="Expiry Date"></input>
                    <input type="number" style={inputStyle2} placeholder="Expiry Date"></input>
                </div> */}


                
            </div>
            

            

           
        </div>
    )
}

export default DonorPagePayment