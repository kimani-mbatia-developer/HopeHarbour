import os
import stripe
import paypalrestsdk
from flask import Blueprint, request, jsonify
from backend.models.common import db
from backend.models.payment_method import PaymentMethod
from flask_restx import Resource, Namespace, fields

payments_bp = Blueprint("payments", __name__)
payments_ns = Namespace("payments", description="Payment methods operations")

# Configure Stripe API key
stripe.api_key = 'sk_test_51O7H7eJUCyTsYNvWfqtyJCUxIAuoVi6a5w8hNCjHlpEDktqKKVR61uO9MMK8Ps5slC1O042VkaUPRMcln3G67Hl000NsHH1TWc'

# Configure PayPal API credentials (sandbox mode)
paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": "AXS3g0Fpytz0A91KUvNp-MZCTK8-_TBN08ySwgGCt4-sAKMV9_SmsukL1cNqc_c7n92gSLSkdzCuRWG0",
    "client_secret": "EEJzJlfqRElUkmssyF3x3SZxeL2erkUiSaC_ThwuWHMz3Hz4U04ecE3P65pAA18ls2bZFdvsk1gAgNiU"
})

payment_method_model = payments_ns.model(
    "PaymentMethodModel",
    {
        "payment_type": fields.String(required=True, description="Payment type (stripe/paypal)"),
        "card_number": fields.String(description="Card number (for stripe payment)"),
        "expiration_date": fields.String(description="Expiration date (for stripe payment)"),
        "security_code": fields.String(description="Security code (for stripe payment)"),
        "paypal_email": fields.String(description="PayPal email (for PayPal payment)"),
        "is_default": fields.Boolean(required=True, description="Is default payment method"),
        "donor_id": fields.Integer(required=True, description="Donor ID"),
    },
)

@payments_ns.route("/payment-methods")
class PaymentMethodsResource(Resource):
    @payments_ns.doc("Create a new payment method")
    @payments_ns.expect(payment_method_model)
    def post(self):
        data = request.json
        payment_type = data.get("payment_type")
        donor_id = data.get("donor_id")

        if payment_type == "stripe":
            # Handle Stripe payment creation
            card_number = data.get("card_number")
            expiration_date = data.get("expiration_date")
            security_code = data.get("security_code")
            
            # Create payment method in Stripe
            stripe_token = stripe.Token.create(
                card={
                    "number": card_number,
                    "exp_month": expiration_date.split("/")[0],
                    "exp_year": expiration_date.split("/")[1],
                    "cvc": security_code,
                },
            )

            # Save payment method details in your database
            payment_method = PaymentMethod(
                payment_type=payment_type,
                card_number=card_number,  # Save only last 4 digits or token for security
                expiration_date=expiration_date,
                security_code=security_code,  # Save only last 4 digits or token for security
                is_default=data.get("is_default"),
                donor_id=donor_id,
            )
            db.session.add(payment_method)
            db.session.commit()

            # Return success response
            return {"message": "Stripe payment method created successfully"}, 201

        elif payment_type == "paypal":
            # Handle PayPal payment creation
            paypal_email = data.get("paypal_email")
            
            # Save PayPal email in your database
            payment_method = PaymentMethod(
                payment_type=payment_type,
                paypal_email=paypal_email,
                is_default=data.get("is_default"),
                donor_id=donor_id,
            )
            db.session.add(payment_method)
            db.session.commit()

            # Return success response
            return {"message": "PayPal payment method created successfully"}, 201

        else:
            return {"message": "Invalid payment type"}, 400
