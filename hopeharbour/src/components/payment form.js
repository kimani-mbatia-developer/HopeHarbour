import React, { useState } from "react";
import { CardElement, useElements, useStripe } from "@stripe/react-stripe-js";
import axios from 'axios';

const CARD_OPTIONS = {
    iconStyle: "solid",
    style: {
        base: {
            iconColor: "#c4f0ff",
            color: "#fff",
            fontWeight: 500,
            fontSize: "16px",
            fontSmoothing: "antialiased",
            WebkitAutofill: { color: "#fce883" },
            "::placeholder": { color: "#87bbfd" },
        },
        invalid: {
            iconColor: "#ffc7ee",
            color: "#ffc7ee",
        },
    }
};

export default function PaymentForm() {
    const [success, setSuccess] = useState(false);
    const stripe = useStripe();
    const elements = useElements();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const { error, paymentMethod } = await stripe.createPaymentMethod({
            type: "card",
            card: elements.getElement(CardElement),
        });

        if (!error) {
            try {
                const { id } = paymentMethod;
                const response = await axios.post("https://harborservicedb.onrender.com/payment", {
                    amount: 1000,
                    id,
                });

                if (response.data.success) {
                    console.log("Successful payment");
                    setSuccess(true);
                }
            } catch (error) {
                console.error("Error", error);
            }
        } else {
            console.error(error.message);
        }
    };

    return (
        <>
            {!success ? (
                <form onSubmit={handleSubmit}>
                    <fieldset className="formGroup">
                        <div className="formRow">
                            <CardElement options={CARD_OPTIONS} />
                        </div>
                    </fieldset>
                    <button>Pay</button>
                </form>
            ) : (
                <div>
                    <h2>Welcome to Hope Harbor</h2>
                </div>
            )}
        </>
    );
}
