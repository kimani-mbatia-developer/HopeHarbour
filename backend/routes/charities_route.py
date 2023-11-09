from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, current_user
from flask_restx import Namespace, Resource, fields, reqparse
from sqlalchemy import func
from backend.models import charity
from backend.models.application import Application
from backend.models.beneficiary import Beneficiary
from backend.models.charity import Charity
from backend.models.common import db
from backend.models.donation import Donation
from backend.models.story import Story

charities_bp = Blueprint("charities", __name__, url_prefix="/charities")
charities_ns = Namespace("charities", description="Charity operations")

# Define models for request and response data
charity_model = charities_ns.model(
    "Charity",
    {
        "id": fields.Integer(readOnly=True, description="The charity ID"),
        "name": fields.String(required=True, description="The name of the charity"),
        "description": fields.String(description="The description of the charity"),
    },
)


charities_response_model = charities_ns.model(
    "ResponseModel",
    {
        "message": fields.String(description="A message describing the response"),
        "data": fields.Raw(description="Response data, if applicable"),
    },
)


total_donation_model = charities_ns.model(
    "TotalDonationAmount",
    {
        "total_donation_amount": fields.Float(
            description="The total donation amount for the charity"
        ),
    },
)


# Model for creating a beneficiary for a charity
create_beneficiary_model = charities_ns.model(
    "CreateBeneficiaryModel",
    {
        "name": fields.String(required=True, description="Name of the beneficiary"),
        "charity_id": fields.Integer(
            required=True,
            description="ID of the charity associated with the beneficiary",
        ),
    },
)


beneficiary_response_model = charities_ns.model(
    "ResponseModel",
    {
        "message": fields.String(description="A message describing the response"),
        "data": fields.Raw(description="Response data, if applicable"),
    },
)


# Route to get a list of charities
@charities_ns.route("/")
class CharitiesResource(Resource):
    @charities_ns.doc(description="Get a list of charities with Approved status")
    @charities_ns.expect(
        charities_ns.parser()
        .add_argument("page", type=int, help="Page number", default=1)
        .add_argument("per_page", type=int, help="Items per page", default=10)
    )
    @charities_ns.marshal_with(charity_model, as_list=True)
    def get(self):
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)

        # Query all "Approved" applications
        approved_applications = Application.query.filter(
            Application.status == "Approved"
        ).all()

        # Extract the charity IDs from approved applications
        charity_ids = [application.charity_id for application in approved_applications]

        # Filter charities based on the charity IDs
        charities = Charity.query.filter(Charity.id.in_(charity_ids)).paginate(
            page=page, per_page=per_page, error_out=False
        )

        charity_data = [
            {"id": charity.id, "name": charity.name} for charity in charities.items
        ]

        return charity_data, 200


# Route to view the total amount donated to the charity
@charities_ns.route("/total-donations/<int:charity_id>")
class TotalDonationsResource(Resource):
    @charities_ns.doc(description="View the total amount donated to the charity")
    @charities_ns.response(
        200, "Success", total_donation_model
    )  # Document the "Success" response
    @charities_ns.response(
        404, "Charity not found"
    )  # Document the "Charity not found" response
    @jwt_required()
    def get(self, charity_id):
        charity = Charity.query.get(charity_id)
        if charity is None:
            return {"message": "Charity not found"}, 404

        total_donation_amount = charity.calculate_total_donation()
        return {"total_donation_amount": total_donation_amount}, 200


# Route to submit a charity application
@charities_ns.route("/apply")
class ApplyCharityResource(Resource):
    @charities_ns.doc(description="Submit a charity application")
    @charities_ns.expect(
        charities_ns.model(
            "CharityApplication",
            {
                "name": fields.String(
                    required=True, description="The name of the charity"
                ),
                "description": fields.String(
                    description="The description of the charity"
                ),
            },
        )
    )
    @charities_ns.marshal_with(
        charities_response_model,
        code=201,
        description="Application submitted successfully",
    )
    @jwt_required()
    def post(self):
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")

        # Create a new application
        application = Application(charity_name=name)
        db.session.add(application)
        db.session.commit()

        return {"message": "Application submitted successfully", "data": None}, 201


# Route to get details of a specific charity
@charities_ns.route("/<int:charity_id>")
class GetCharityResource(Resource):
    @charities_ns.doc(description="Get details of a specific charity")
    @charities_ns.response(
        200, "Success", charity_model
    )  # Document the "Success" response
    @charities_ns.response(
        404, "Charity not found"
    )  # Document the "Charity not found" response
    def get(self, charity_id):
        charity = Charity.query.get(charity_id)
        if not charity:
            return {"message": "Charity not found"}, 404

        return {
            "id": charity.id,
            "name": charity.name,
            "description": charity.description,
        }, 200


# Route to set up charity details
@charities_ns.route("/setup/<int:charity_id>")
class SetupCharityResource(Resource):
    @charities_ns.doc(description="Set up charity details")
    @charities_ns.expect(charity_model)
    @charities_ns.response(
        200, "Charity details updated successfully"
    )  # Document the "Success" response
    @charities_ns.response(
        404, "Charity not found"
    )  # Document the "Charity not found" response
    @jwt_required()
    def put(self, charity_id):
        charity = Charity.query.get(charity_id)
        if charity:
            data = request.get_json()
            # Updating charity details here
            charity.name = data.get("name")
            charity.description = data.get("description")
            # Saving the changes to the database
            db.session.commit()
            return {"message": "Charity details updated successfully"}, 200
        return {"message": "Charity not found"}, 404


# Route to view donors and their donations (including anonymous donors)
@charities_ns.route("/donors/<int:charity_id>")
class ViewDonorsResource(Resource):
    @charities_ns.doc(description="View donors and their donations")
    @charities_ns.response(200, "Success")  # Document the "Success" response
    @charities_ns.response(
        404, "Charity not found"
    )  # Document the "Charity not found" response
    @jwt_required()
    def get(self, charity_id):
        charity = Charity.query.get(charity_id)
        if charity is None:
            return {"message": "Charity not found"}, 404

        all_donors = (
            charity.donors
        )  # This includes both anonymous and non-anonymous donors

        # Creating a list of donor details and their donations
        donor_details = []
        for donor in all_donors:
            donor_info = {
                "donor_name": donor.name if not donor.anonymous else "Anonymous",
                "donations": [
                    {"amount": donation.amount, "donation_date": donation.donation_date}
                    for donation in donor.donations
                ],
            }
            donor_details.append(donor_info)

        return donor_details, 200


# Route to create and post a story about beneficiaries
@charities_ns.route("/stories/create")
class CreateStoryResource(Resource):
    @charities_ns.doc(description="Create and post a story about beneficiaries")
    @charities_ns.expect(
        charities_ns.model(
            "Story",
            {
                "title": fields.String(required=True, description="Title of the story"),
                "content": fields.String(
                    required=True, description="Content of the story"
                ),
            },
        )
    )
    @charities_ns.response(
        201, "Story posted successfully"
    )  # Document the "Success" response
    @jwt_required()
    def post(self):
        data = request.get_json()
        title = data.get("title")
        content = data.get("content")

        # Create a new story for the charity
        story = Story(title=title, content=content, charity_id=charity.id)
        db.session.add(story)
        db.session.commit()

        return {"message": "Story posted successfully"}, 201


# Define the /donations/anonymous-amount route within the charities_bp Blueprint
@charities_ns.route("/anonymous-amount")
class AnonymousDonationsAmountResource(Resource):
    @charities_ns.doc(description="Get the total amount donated by anonymous donors")
    @charities_ns.response(200, "Success")  # Document the "Success" response
    @jwt_required()
    def get(self):
        # Query and sum amounts donated by anonymous donors
        total_amount = (
            db.session.query(func.sum(Donation.amount))
            .filter(
                Donation.anonymous.is_(True),
                Donation.charity_id == current_user.charity.id,
            )
            .scalar()
        )

        if total_amount is not None:
            return {"total_anonymous_donations": total_amount}, 200
        else:
            return {"total_anonymous_donations": 0}, 200


# Route to create a beneficiary for a charity
@charities_ns.route("/create-beneficiary", methods=["POST"])
class CreateCharityBeneficiary(Resource):
    @charities_ns.doc("Create a beneficiary for a charity")
    @charities_ns.expect(create_beneficiary_model)
    @charities_ns.marshal_with(
        beneficiary_response_model,
        code=201,
        description="Beneficiary created successfully",
    )
    def post(self):
        data = request.get_json()
        name = data.get("name")
        charity_id = data.get("charity_id")

        # Check if the charity exists
        charity = Charity.query.get(charity_id)
        if not charity:
            return {"message": "Charity not found"}, 404

        # Create a new beneficiary
        beneficiary = Beneficiary(name=name, charity_id=charity_id)

        db.session.add(beneficiary)
        db.session.commit()

        return {"message": "Beneficiary created successfully"}, 201
