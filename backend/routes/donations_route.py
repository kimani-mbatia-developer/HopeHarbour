from flask import Blueprint, request, jsonify
from flask_jwt_extended import current_user
from backend.models.charity import Charity
from backend.models.donation import Donation
from backend.models.common import db
from flask_restx import Resource, Namespace, fields

donations_bp = Blueprint("donations", __name__, url_prefix="/donations")
donations_ns = Namespace("donations", description="Donation operations")


# Model for creating a donation
donation_model = donations_ns.model(
    "DonationModel",
    {
        "amount": fields.Float(required=True, description="Donation amount"),
        "charity_id": fields.Integer(
            required=True, description="ID of the charity to donate to"
        ),
        "frequency": fields.String(required=True, description="Donation frequency"),
        "payment_methods": fields.List(
            fields.String(description="Payment methods used for the donation")
        ),
    },
)

# Model for paginated list of donations
paginated_donations_model = donations_ns.model(
    "PaginatedDonationsModel",
    {
        "donations": fields.List(
            fields.Nested(
                donations_ns.model(
                    "DonationModel",
                    {
                        "id": fields.Integer(description="Donation ID"),
                        "amount": fields.Float(description="Donation amount"),
                        "charity_id": fields.Integer(description="ID of the charity"),
                    },
                )
            ),
            description="List of donations",
        ),
        "page": fields.Integer(description="Current page number"),
        "total_pages": fields.Integer(description="Total number of pages"),
        "total_items": fields.Integer(description="Total number of donations"),
    },
)

# Common response model
donations_response_model = donations_ns.model(
    "ResponseModel",
    {
        "message": fields.String(description="A message describing the response"),
        "data": fields.Raw(description="Response data, if applicable"),
    },
)


# Route to get all donations with pagination
@donations_ns.route("/", methods=["GET"])
class GetDonations(Resource):
    @donations_ns.doc("Get all donations with pagination")
    @donations_ns.marshal_with(
        paginated_donations_model, code=200, description="List of donations"
    )
    def get(self):
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)

        donations = Donation.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        donation_data = [
            {
                "id": donation.id,
                "amount": donation.amount,
                "charity_id": donation.charity_id,
            }
            for donation in donations.items
        ]

        return jsonify(
            {
                "donations": donation_data,
                "page": donations.page,
                "total_pages": donations.pages,
                "total_items": donations.total,
            }
        )


# Route to make a donation to a charity
@donations_ns.route("/donate", methods=["POST"])
class CreateDonation(Resource):
    @donations_ns.doc("Make a donation to a charity")
    @donations_ns.expect(donation_model)
    @donations_ns.marshal_with(
        donations_response_model, code=201, description="Donation made successfully"
    )
    def post(self):
        data = request.get_json()
        amount = data.get("amount")
        charity_id = data.get("charity_id")
        frequency = data.get("frequency")
        payment_methods = data.get("payment_methods")

        if amount is None or not isinstance(amount, (int, float)) or amount <= 0:
            return {"message": "Invalid donation amount"}, 400

        # Check if the charity exists
        charity = Charity.query.get(charity_id)
        if not charity:
            return {"message": "Charity not found"}, 404

        # Create a new donation with frequency
        donation = Donation(
            amount=amount,
            donor_id=current_user.id,
            charity_id=charity_id,
            frequency=frequency,
            payment_methods=payment_methods,
        )

        db.session.add(donation)
        db.session.commit()

        return {"message": "Donation made successfully"}, 201
