from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, unset_jwt_cookies
from flask import make_response

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_jwt_access_token(identity):
    # Creating an access token
    access_token = create_access_token(identity=identity)
    return access_token


def create_response_with_jwt_token(identity):
    # Creating an access token
    access_token = create_jwt_access_token(identity)
    response = make_response("User logged in successfully")
    unset_jwt_cookies(response)
    return response, access_token
