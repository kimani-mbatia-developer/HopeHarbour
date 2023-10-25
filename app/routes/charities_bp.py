# charities_bp.py
from ..extensions import Blueprint, request, jsonify, Schema, fields, Api, ma, Resource
from app import db
from ..models import Charity

charities_bp = Blueprint("charities_bp", __name__)
api = Api(charities_bp)


class CharitySchema(ma.Schema):
    class Meta:
        model = Charity


# Charity Resource for getting a single charity
class CharityResource(ma.SQLAlchemyAutoSchema):
    def get(self, charity_id):
        charity = Charity.query.get(charity_id)
        if not charity:
            return {"message": "Charity not found"}, 404
        result = CharitySchema().dump(charity)
        return result

    def put(self, charity_id):
        charity = Charity.query.get(charity_id)
        if not charity:
            return {"message": "Charity not found"}, 404

        data = request.get_json()
        charity_schema = CharitySchema()
        updated_charity = charity_schema.load(data, instance=charity)
        db.session.commit()
        return charity_schema.dump(updated_charity)

    def delete(self, charity_id):
        charity = Charity.query.get(charity_id)
        if not charity:
            return {"message": "Charity not found"}, 404
        db.session.delete(charity)
        db.session.commit()
        return {"message": "Charity deleted"}, 204


# CharityList resource for creating new charities
class CharityListResource(Resource):
    def get(self):
        charities = Charity.query.all()
        result = CharitySchema(many=True).dump(charities)
        return result

    def post(self):
        data = request.get_json()
        charity_schema = CharitySchema()
        charity = charity_schema.load(data)
        db.session.add(charity)
        db.session.commit()
        return charity_schema.dump(charity), 201


# Add resources to the API
api.add_resource(CharityListResource, "/charities")
api.add_resource(CharityResource, "/charities/<int:charity_id>")
