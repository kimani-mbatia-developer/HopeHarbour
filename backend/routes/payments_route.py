from flask import Blueprint, request, jsonify
from backend.models.common import db
from backend.models.payment_method import PaymentMethod
from flask_restx import Resource, Namespace, fields

payments_bp = Blueprint("payments", __name__)
payments_ns = Namespace("payments", description="Payment methods operations")

payment_method_model = payments_ns.model(
  "PaymentsMethodModel",
  {
      "payment_type": fields.String(required=True, description="Payment Type"),
      "card_number": fields.String(required=True, description="Card number"),
      "expiration_date": fields.String(required=True, description="Expiration Date"),
      "security_code": fields.String(required=True, description="Security Code"),
      "is_default": fields.String(required=True, description="This is a default payment method"),
      "donor_id": fields.String(required=True, description="Donor ID"),
  },   
)

@payments_ns.route("/payment-methods")
class PaymentMethodResource(Resource):
    @payments_ns.doc("Create a new payment method")
    @payments_ns.expect(payment_method_model)
    def post(self):
        data = request.json
        payment_method = PaymentMethod(
            payment_type=data["payment_type"],
            card_number=data["card_number"],
            expiration_date=data["expiration_date"],
            security_code=data["security_code"],
            is_default=data["is_default"],
            donor_id=data["donor_id"]
        )
        db.session.add(payment_method)
        db.session.commit()
        return {"message": "Payment method created successfully!"}, 201

@payments_ns.route("/payment-methods/<int:payment_method_id>")
class PaymentMethodResource(Resource):
    @payments_ns.doc("UPdate a payment method")
    @payments_ns.expect(payment_method_model)
    def put(self, payment_method_id):
        data = request.json
        payment_method = PaymentMethod.query.get(payment_method_id)
        if payment_method:
            payment_method.payment_type=data["payment_type"]
            payment_method.card_number=data["card_number"]
            payment_method.expiration_date=data["expiration_date"]
            payment_method.security_code=data["security_code"]
            payment_method.is_default=data["is_default"]
            payment_method.donor_id=data["donor_id"]
            db.session.commit()
            return {"message": "Payment method updated successfully!"}, 200
        return{"message": "Payment method not found."}, 404
    
    @payments_ns.doc("Delete a payment method")
    def delete(self, payment_method_id):
        payment_method = PaymentMethod.query.get(payment_method_id)
        if payment_method:
            db.session.delete(payment_method)
            db.session.commit()
            return {"message": "Payment method deleted successfully!"}, 200
        return {"message": "Payment method not found"}, 404


