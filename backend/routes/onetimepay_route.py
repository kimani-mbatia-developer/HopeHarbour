from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
import stripe


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


@onetimepay_ns.route("/pay")
class PaymentResource(Resource):
    @onetimepay_ns.doc(description="Facilitate a onetime payment")
    @onetimepay_ns.expect(payment_model, validate=True)
    @onetimepay_ns.marshal_with(response_model, code=200)
    def post(self):
        """
        Make a one-time payment with Stripe
        """
        email = onetimepay_ns.payload.get("email", None)

        if not email:
            return "You need to send an Email!", 400

        intent = stripe.PaymentIntent.create(
            amount=5000, currency="usd", receipt_email=email
        )

        return {"client_secret": intent["client_secret"]}, 200
