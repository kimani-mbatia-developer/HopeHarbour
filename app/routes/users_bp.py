from ..extensions import db, Blueprint, request, Resource, Api
from ..models.users import User

users_bp = Blueprint("users_bp", __name__)
api = Api(users_bp)
