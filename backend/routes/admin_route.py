from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from backend.models.application import Application
from backend.models.charity import Charity
from backend.models.common import db
from flask_restx import Resource, Namespace, fields

admin_ns = Namespace("admin", description="Admin operations")
admin_bp = Blueprint("admin", __name__)

# Common response model
admin_response_model = admin_ns.model(
    "ResponseModel",
    {
        "message": fields.String(description="A message describing the response"),
        "data": fields.Raw(description="Response data, if applicable"),
    },
)


# Resource for pending applications
@admin_ns.route("/applications")
class ApplicationsList(Resource):
    @admin_ns.doc("Get all pending charity applications")
    @admin_ns.marshal_with(
        admin_response_model, code=200, description="Success", as_list=True
    )
    def get(self):
        pending_applications = Application.query.filter_by(status="Pending").all()

        # Serialize applications to JSON
        applications = [
            {
                "id": app.id,
                "charity_name": app.charity.name,
                "status": app.status,
            }
            for app in pending_applications
        ]

        return {"message": "Success", "data": applications}, 200


# Resource for approving applications
@admin_ns.route("/applications/approve/<int:application_id>")
class ApproveApplication(Resource):
    @admin_ns.doc("Approve a charity application")
    @admin_ns.marshal_with(admin_response_model, code=200, description="Success")
    @admin_ns.marshal_with(
        admin_response_model, code=404, description="Application not found"
    )
    def put(self, application_id):
        application = Application.query.get(application_id)
        if application:
            if application.status != "Approved":
                application.status = "Approved"
                # Create and save the associated charity
                new_charity = Charity(
                    name=application.charity_name,
                    description=application.description,
                    user_id=application.user_id,
                    total_donation_amount=application.total_donation_amount,
                )
                db.session.add(new_charity)

                # Save the changes to the database
                db.session.commit()
            return {"message": "Application approved successfully", "data": None}, 200
        return {"message": "Application not found", "data": None}, 404


# Resource for rejecting charity applications
@admin_ns.route("/applications/reject/<int:application_id>")
class RejectApplication(Resource):
    @admin_ns.doc("Reject a charity application")
    @admin_ns.marshal_with(admin_response_model, code=200, description="Success")
    @admin_ns.marshal_with(
        admin_response_model,
        code=400,
        description="Application has already been processed",
    )
    @admin_ns.marshal_with(
        admin_response_model, code=404, description="Application not found"
    )
    def put(self, application_id):
        application = Application.query.get(application_id)
        if application:
            if application.status != "Pending":
                return {
                    "message": "Application is being processed",
                    "data": None,
                }, 400

            application.status = "Rejected"
            # Save the changes to the database
            db.session.commit()
            return {"message": "Application rejected successfully", "data": None}, 200
        return {"message": "Application not found", "data": None}, 404


# Resource for deleting charities
@admin_ns.route("/charities/delete/<int:charity_id>")
class DeleteCharity(Resource):
    @admin_ns.doc("Delete a charity")
    @admin_ns.marshal_with(admin_response_model, code=200, description="Success")
    @admin_ns.marshal_with(
        admin_response_model, code=404, description="Charity not found"
    )
    def delete(self, charity_id):
        charity = Charity.query.get(charity_id)
        if charity:
            # Optionally, delete associated data (donations, beneficiaries, stories)
            db.session.delete(charity)
            # Save the changes to the database
            db.session.commit()
            return {"message": "Charity deleted successfully", "data": None}, 200
        return {"message": "Charity not found", "data": None}, 404


# Route for administrator to review and process charity applications
@admin_ns.route("/charities/applications/<int:application_id>")
class ReviewCharityApplicationResource(Resource):
    @admin_ns.doc(description="Review and process a charity application")
    @admin_ns.response(200, "Application approved")
    @admin_ns.response(204, "Application deleted")
    @admin_ns.response(404, "Application not found")
    @jwt_required()  # Ensure only administrators can access this route
    def put(self, application_id):
        application = Application.query.get(application_id)
        if not application:
            return {"message": "Application not found"}, 404

        # You can implement logic to review and set the application to "Pending" or "Delete" here
        # For example, if application.status == "Pending", you can set it to "Approved"

        if application.status == "Pending":
            application.status = "Approved"

        elif application.status == "Delete":
            pass

        db.session.commit()

        if application.status == "Pending":
            return {"message": "Application approved"}, 200
        elif application.status == "Delete":
            return {"message": "Application deleted"}, 204
