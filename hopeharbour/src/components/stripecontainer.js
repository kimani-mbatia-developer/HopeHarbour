import React from 'react';
import { loadStripe } from '@stripe/stripe-js';
import PaymentForm from './payment form';

const public_key = ""; // Replace with your actual public key

const stripeTestPromise = loadStripe(public_key);

const paymentform = () => (
  <div>
    {/* Your payment form component code goes here */}
  </div>
);

const StripeContainer = () => (
  <Elements stripe={stripeTestPromise}>
    <PaymentForm />
  </Elements>
);

export default StripeContainer;
