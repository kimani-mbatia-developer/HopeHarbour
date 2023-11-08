from flask import Flask, request
from flask import Blueprint, jsonify
import stripe
stripe.api_key = 'sk_test_51O9wNVBwM0XCzFWG6cGF6RRDbiDdAMt3AIGlEaRnILSNfSzjXSxAQqJVD94sRKF7yT704oTEnjtMrqYBQPJdipD600mzOc0VKw'

onetimepay = Blueprint('email', __name__)


@onetimepay.route('/pay', methods=['POST'])
def pay():
    email = request.json.get('email', None)

    if not email:
        return 'You need to send an Email!', 400

    intent = stripe.PaymentIntent.create(
        amount=5000,
        currency='usd',
        receipt_email=email
    )

    return {"client_secret": intent['client_secret']}, 200