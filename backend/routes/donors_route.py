from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, current_user
from sqlalchemy import func
from backend.models.charity import Charity
from backend.models.donation import Donation
from backend.models.common import db
from backend.models.selected_charity import SelectedCharity
from flask_restx import Namespace, Resource, reqparse, fields

from backend.models.story import Story

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


# Common response model
stories_response_model = donors_ns.model(
    "ResponseModel",
    {
        "message": fields.String(description="A message describing the response"),
        "data": fields.Raw(description="Response data, if applicable"),
    },
)


# donations response model
donation_model = donors_ns.model(
    "DonationModel",
    {
        "id": fields.Integer(description="Donation ID"),
        "amount": fields.Float(description="Donation Amount"),
        "charity_name": fields.String(description="Charity Name"),
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


# Get stories of beneficiaries
@donors_ns.route("/stories/<int:charity_id>")
class StoryListByCharity(Resource):
    @donors_ns.doc("Get stories by charity ID")
    @donors_ns.marshal_with(
        stories_response_model, code=200, description="Success", as_list=True
    )
    def get(self, charity_id):
        stories = Story.query.filter_by(charity_id=charity_id).all()
        story_data = [
            {"id": story.id, "title": story.title, "content": story.content}
            for story in stories
        ]
        return {"message": "Success", "data": story_data}, 200


# Get donations a donor has made
@donors_ns.route("/contributions/<int:donor_id>")
class GetContribution(Resource):
    @donors_ns.doc("Get a donor's contributions")
    @donors_ns.marshal_list_with(donation_model)
    def get(self, donor_id):
        # Query donations made by the donor with the specified donor_id
        donations = (
            db.session.query(
                Donation.id, Donation.amount, Charity.name.label("charity_name")
            )
            .join(Charity, Donation.charity_id == Charity.id)
            .filter(Donation.donor_id == donor_id)
            .all()
        )

        # Format the donations as a list of dictionaries
        donation_data = [
            {
                "id": donation.id,
                "amount": donation.amount,
                "charity_name": donation.charity_name,
            }
            for donation in donations
        ]

        return donation_data, 200
