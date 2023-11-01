from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, current_user
from sqlalchemy import func
from backend.models.charity import Charity
from backend.models.donation import Donation
from backend.models.common import db
from backend.models.selected_charity import SelectedCharity
from flask_restx import Namespace, Resource, reqparse, fields

donors_bp = Blueprint("donors", __name__, url_prefix="/donors")
donors_ns = Namespace("donors", description="Donor operations")

# Define a model for the response data
anonymous_donations_model = donors_ns.model(
    "AnonymousDonationsModel",
    {
        "total_anonymous_donations": fields.Float(
            description="Total amount donated by anonymous donors"
        ),
    },
)


# Route to choose a charity
@donors_ns.route("/choose-charity/<int:charity_id>")
class ChooseCharityResource(Resource):
    @donors_ns.doc(description="Choose a charity")
    @donors_ns.response(200, "Charity chosen successfully")
    @donors_ns.response(400, "Bad Request")
    @donors_ns.response(404, "Charity not found")
    @jwt_required()
    def post(self, charity_id):
        donor_id = current_user.id
        charity = Charity.query.get(charity_id)

        if not charity:
            return {"message": "Charity not found"}, 404

        # Check if the donor has already chosen a charity
        existing_association = SelectedCharity.query.filter_by(
            donor_id=donor_id
        ).first()
        if existing_association:
            # Update the donor's choice
            existing_association.charity_id = charity_id
        else:
            # Create a new association
            selected_charity = SelectedCharity(donor_id=donor_id, charity_id=charity_id)
            db.session.add(selected_charity)

        db.session.commit()
        return {"message": "Charity chosen successfully"}, 200


# Route to get the total amount donated by anonymous donors
@donors_ns.route("/donations/anonymous-amount")
class AnonymousDonationsAmountResource(Resource):
    @donors_ns.doc(description="Get the total amount donated by anonymous donors")
    @donors_ns.marshal_with(anonymous_donations_model)
    @jwt_required()
    def get(self):
        # Query and sum amounts donated by anonymous donors
        total_amount = (
            db.session.query(func.sum(Donation.amount))
            .filter(Donation.anonymous.is_(True), Donation.donor_id == current_user.id)
            .scalar()
        )

        if total_amount is not None:
            return {"total_anonymous_donations": total_amount}
        else:
            return {"total_anonymous_donations": 0.0}
