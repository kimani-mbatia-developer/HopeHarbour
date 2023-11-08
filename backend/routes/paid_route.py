from flask import Flask, request
from flask import Blueprint, jsonify
from flask_restx import Api, Resource, fields

import stripe

stripe.api_key = "sk_test_51O9wNVBwM0XCzFWG6cGF6RRDbiDdAMt3AIGlEaRnILSNfSzjXSxAQqJVD94sRKF7yT704oTEnjtMrqYBQPJdipD600mzOc0VKw"

app = Flask(__name__)

onetimepay = Blueprint("email", __name__)

api = Api(
    onetimepay,
    doc="/doc",
    title="Stripe Payment API",
    description="API for making one-time payments with Stripe",
)

# Request and response models
payment_model = api.model(
    "Payment",
    {
        "email": fields.String(description="Email of the recipient", required=True),
    },
)

response_model = api.model(
    "PaymentResponse",
    {
        "client_secret": fields.String(
            description="Stripe Payment Intent Client Secret"
        ),
    },
)


@onetimepay.route("/pay", methods=["POST"])
class PaymentResource(Resource):
    @api.expect(payment_model, validate=True)
    @api.marshal_with(response_model, code=200)
    def post(self):
        """
        Make a one-time payment with Stripe
        """
        email = request.json.get("email", None)

        if not email:
            return "You need to send an Email!", 400

        intent = stripe.PaymentIntent.create(
            amount=5000, currency="usd", receipt_email=email
        )

        return {"client_secret": intent["client_secret"]}, 200


app.register_blueprint(onetimepay)

if __name__ == "__main__":
    app.run(debug=True)
