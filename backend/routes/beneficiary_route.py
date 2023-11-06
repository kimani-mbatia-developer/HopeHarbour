from flask import Blueprint, request, jsonify
from backend.models.beneficiary import Beneficiary
from backend.models.charity import Charity
from backend.models.common import db
from flask_restx import Resource, Namespace, fields


beneficiaries_bp = Blueprint("beneficiaries", __name__, url_prefix="/beneficiary")
beneficiaries_ns = Namespace("beneficiaries", description="Beneficiary operations")


# Model for creating a beneficiary for a charity
create_beneficiary_model = beneficiaries_ns.model(
    "CreateBeneficiaryModel",
    {
        "name": fields.String(required=True, description="Name of the beneficiary"),
        "charity_id": fields.Integer(
            required=True,
            description="ID of the charity associated with the beneficiary",
        ),
    },
)

# Model for paginated list of beneficiaries
paginated_beneficiaries_model = beneficiaries_ns.model(
    "PaginatedBeneficiariesModel",
    {
        "beneficiaries": fields.List(
            fields.Nested(
                beneficiaries_ns.model(
                    "BeneficiaryModel",
                    {
                        "id": fields.Integer(description="Beneficiary ID"),
                        "name": fields.String(description="Name of the beneficiary"),
                        "charity_id": fields.Integer(
                            description="ID of the associated charity"
                        ),
                    },
                )
            ),
            description="List of beneficiaries",
        ),
        "page": fields.Integer(description="Current page number"),
        "total_pages": fields.Integer(description="Total number of pages"),
        "total_items": fields.Integer(description="Total number of beneficiaries"),
    },
)

# Common response model
beneficiary_response_model = beneficiaries_ns.model(
    "ResponseModel",
    {
        "message": fields.String(description="A message describing the response"),
        "data": fields.Raw(description="Response data, if applicable"),
    },
)


# Route to get all beneficiaries with pagination
@beneficiaries_ns.route("/", methods=["GET"])
class GetBeneficiaries(Resource):
    @beneficiaries_ns.doc("Get all beneficiaries with pagination")
    @beneficiaries_ns.marshal_with(
        paginated_beneficiaries_model, code=200, description="List of beneficiaries"
    )
    def get(self):
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)

        beneficiaries = Beneficiary.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        beneficiary_data = [
            {
                "id": beneficiary.id,
                "name": beneficiary.name,
                "charity_id": beneficiary.charity_id,
            }
            for beneficiary in beneficiaries.items
        ]

        return {
            "beneficiaries": beneficiary_data,
            "page": beneficiaries.page,
            "total_pages": beneficiaries.pages,
            "total_items": beneficiaries.total,
        }


# Route to create a beneficiary for a charity
@beneficiaries_ns.route("/create", methods=["POST"])
class CreateBeneficiary(Resource):
    @beneficiaries_ns.doc("Create a beneficiary for a charity")
    @beneficiaries_ns.expect(create_beneficiary_model)
    @beneficiaries_ns.marshal_with(
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
