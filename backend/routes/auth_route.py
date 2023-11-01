from flask import Blueprint, make_response, request, jsonify
from flask_jwt_extended import jwt_required, unset_jwt_cookies
from backend.models.user import User
from backend.models.common import create_response_with_jwt_token, db, bcrypt
from flask_restx import Resource, Namespace, fields


auth_ns = Namespace("auth", description="Authentication operations")
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Common response model
auth_response_model = auth_ns.model(
    "ResponseModel",
    {
        "message": fields.String(description="A message describing the response"),
        "data": fields.Raw(description="Response data, if applicable"),
    },
)


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


def identity(payload):
    user_id = payload["identity"]
    return User.query.get(user_id)


# Route to register a new user
@auth_ns.route("/register", methods=["POST"])
class RegisterUser(Resource):
    @auth_ns.doc("Register a new user")
    @auth_ns.expect(
        auth_ns.model(
            "RegisterModel",
            {
                "username": fields.String(required=True, description="Username"),
                "email": fields.String(required=True, description="Email"),
                "password": fields.String(required=True, description="Password"),
                "role": fields.String(description="User role"),
            },
        )
    )
    @auth_ns.marshal_with(
        auth_response_model, code=201, description="User registered successfully"
    )
    def post(self):
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        role = data.get("role")

        # Creating a new user
        user = User(username=username, email=email, password=hashed_password, role=role)

        db.session.add(user)
        db.session.commit()

        return {"message": "User registered successfully", "data": None}, 201


# Route to log in a user
@auth_ns.route("/login")
class LoginUser(Resource):
    @auth_ns.doc("Login a user")
    @auth_ns.expect(
        auth_ns.model(
            "LoginModel",
            {
                "email": fields.String(required=True, description="Email"),
                "password": fields.String(required=True, description="Password"),
            },
        )
    )
    @auth_ns.marshal_with(auth_response_model, code=200, description="Login successful")
    @auth_ns.marshal_with(auth_response_model, code=401, description="Login failed")
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            response, token = create_response_with_jwt_token(identity=user.id)
            return response, 200, token
        else:
            return {"message": "Login failed", "data": None}, 401


@auth_ns.route("/logout")
class LogoutUser(Resource):
    @auth_ns.doc("Logout a user")
    @jwt_required
    @auth_ns.marshal_with(
        auth_response_model, code=200, description="User logged out successfully"
    )
    def post(self):
        response = make_response("User logged out successfully")
        unset_jwt_cookies(response)
        return {"message": "User logged out successfully", "data": None}, 200
