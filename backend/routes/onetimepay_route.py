from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
import stripe
import os
import logging

# Your Stripe webhook secret (retrieve it from your Stripe dashboard)
STRIPE_WEBHOOK_SECRET = 'your_webhook_secret_here'

onetimepay_bp = Blueprint("onetimepay", __name__)
onetimepay_ns = Namespace("onetimepay", description="Onetime payment operations")

# Request and response models
payment_model = onetimepay_ns.model(
    "Payment",
    {
        "email": fields.String(description="Email of the recipient", required=True),
    },
)

response_model = onetimepay_ns.model(
    "PaymentResponse",
    {
        "client_secret": fields.String(
            description="Stripe Payment Intent Client Secret"
        ),
    },
)

class PaymentResource(Resource):
    @onetimepay_ns.expect(payment_model, validate=True)
    @onetimepay_ns.marshal_with(response_model, code=200)
    def post(self):
        """
        Make a one-time payment with Stripe
        """
        try:
            email = onetimepay_ns.payload.get("email", None)

            if not email:
                raise ValueError("Missing email parameter")

            logging.info(f"Creating payment intent for email: {email}")

            intent = stripe.PaymentIntent.create(
                amount=5000, currency="usd", receipt_email=email, payment_method_types=["card"],
            )

            return {"client_secret": intent["client_secret"]}, 200
        except Exception as e:
            logging.error(f"Payment error: {str(e)}")
            return str(e), 400

onetimepay_ns.add_resource(PaymentResource, '/pay')

@onetimepay_bp.route("/stripe-webhook", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        logging.error(f"Invalid webhook event: {str(e)}")
        return str(e), 400
    except stripe.error.SignatureVerificationError as e:
        logging.error(f"Invalid webhook signature: {str(e)}")
        return str(e), 400

    # Handle the specific webhook event 
    if event.type == "payment_intent.succeeded":
        # Handle successful payment
        payment_intent = event.data.object
        logging.info(f"Payment succeeded for payment_intent_id: {payment_intent.id}")

        # Update payment status in your database or customer management system
        # ...

    return "", 200


    
# @app.route('/sub', methods=['POST'])
# def sub():
#     email = request.json.get('email', None)
#     payment_method = request.json.get('payment_method', None)

#     if not email:
#         return 'You need to send an Email!', 400
#     if not payment_method:
#         return 'You need to send an payment_method!', 400

#     # This creates a new Customer and attaches the default PaymentMethod in one API call.
#     customer = stripe.Customer.create(
#         payment_method=payment_method,
#         email=email,
#         invoice_settings={
#             'default_payment_method': payment_method,
#         },
#     )
#     # Creates a subscription and attaches the customer to it
#     subscription = stripe.Subscription.create(
#         customer=customer['id'],
#         items=[
#             {
#             'plan': 'si_OyDPlcyq8R6i5h',
#             },
#         ],
#         expand=['latest_invoice.payment_intent'],
#     )

#     status = subscription['latest_invoice']['payment_intent']['status'] 
#     client_secret = subscription['latest_invoice']['payment_intent']['client_secret']

#     user_info['customer_id'] = customer['id']
#     user_info['email'] = email
    
#     return {'status': status, 'client_secret': client_secret}, 200