from flask import Blueprint, request, jsonify
from backend.models.application import Application
from backend.models.common import db
from flask_restx import Resource, Namespace, fields


applications_bp = Blueprint("applications", __name__)
applications_ns = Namespace("applications", description="Applications operations")

# Model for submitting a charity application
submit_application_model = applications_ns.model(
    "SubmitApplicationModel",
    {
        "charity_name": fields.String(
            required=True, description="Name of the charity applying"
        ),
    },
)

# Model for paginated list of pending charity applications
paginated_applications_model = applications_ns.model(
    "PaginatedApplicationsModel",
    {
        "applications": fields.List(
            fields.Nested(
                applications_ns.model(
                    "ApplicationModel",
                    {
                        "id": fields.Integer(description="Application ID"),
                        "charity_name": fields.String(
                            description="Name of the charity"
                        ),
                        "status": fields.String(description="Application status"),
                    },
                )
            ),
            description="List of pending charity applications",
        ),
        "page": fields.Integer(description="Current page number"),
        "total_pages": fields.Integer(description="Total number of pages"),
        "total_items": fields.Integer(
            description="Total number of pending applications"
        ),
    },
)

# Common response model
applications_response_model = applications_ns.model(
    "ResponseModel",
    {
        "message": fields.String(description="A message describing the response"),
        "data": fields.Raw(description="Response data, if applicable"),
    },
)


# Route to get all pending charity applications with pagination
@applications_ns.route("", methods=["GET"])
class GetApplications(Resource):
    @applications_ns.doc("Get all pending charity applications with pagination")
    @applications_ns.marshal_with(
        paginated_applications_model,
        code=200,
        description="List of pending applications",
    )
    def get(self):
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)

        applications = Application.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        application_data = [
            {"id": app.id, "charity_name": app.charity.name, "status": app.status}
            for app in applications.items
        ]

        return {
            "applications": application_data,
            "page": applications.page,
            "total_pages": applications.pages,
            "total_items": applications.total,
        }


# Route to get all pending charity applications
@applications_ns.route("/pending", methods=["GET"])
class GetPendingApplications(Resource):
    @applications_ns.doc("Get all pending charity applications")
    @applications_ns.marshal_with(
        paginated_applications_model,
        code=200,
        description="List of pending applications",
    )
    def get(self):
        pending_applications = Application.query.filter_by(status="Pending").all()
        application_data = [
            {"id": app.id, "charity_name": app.charity.name, "status": app.status}
            for app in pending_applications
        ]
        return {
            "applications": application_data,
            "total_items": len(application_data),
        }
