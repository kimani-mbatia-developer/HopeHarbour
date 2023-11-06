from flask import Blueprint, make_response, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
)
from backend.models.user import User
from backend.models.common import create_response_with_jwt_token, db, bcrypt
from flask_restx import Resource, Namespace, fields


users_bp = Blueprint("users", __name__, url_prefix="/users")
users_ns = Namespace("users", description="User operations")


# Response model for the data
user_model = users_ns.model(
    "UserModel",
    {
        "id": fields.Integer(description="User ID"),
        "username": fields.String(description="Username"),
        "email": fields.String(description="Email"),
        "password": fields.String(description="Password"),
        "role": fields.String(description="Role"),
    },
)


# Get all users
@users_ns.route("/all")
class AllUsersList(Resource):
    @users_ns.doc("Get all users")
    @users_ns.marshal_list_with(user_model, skip_none=True)
    def get(self):
        users = User.query.all()
        user_data = [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "role": user.role,
            }
            for user in users
        ]
        return user_data, 200


# Update user details
@users_ns.route("/update/<int:user_id>")
class UpdateUser(Resource):
    @users_ns.doc("Update user details")
    @users_ns.expect(user_model)
    def put(self, user_id):
        data = request.json
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        user.username = data["username"]
        user.email = data["email"]
        user.password = data["password"]
        user.role = data["role"]
        db.session.add(user)
        db.session.commit()
        return {"message": "User details updated successfully"}, 200


# Delete a user
@users_ns.route("/delete/<int:user_id>")
class DeleteUser(Resource):
    @users_ns.doc("Delete a user")
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}, 200
