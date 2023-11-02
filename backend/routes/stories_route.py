from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from backend.models.charity import Charity
from backend.models.story import Story
from backend.models.common import db
from flask_restx import Resource, Namespace, fields

from backend.models.user import User

stories_ns = Namespace("stories", description="Story operations")
stories_bp = Blueprint("stories", __name__, url_prefix="/stories")

# Common response model
stories_response_model = stories_ns.model(
    "ResponseModel",
    {
        "message": fields.String(description="A message describing the response"),
        "data": fields.Raw(description="Response data, if applicable"),
    },
)

# Story model for request and response
story_model = stories_ns.model(
    "StoryModel",
    {
        "title": fields.String(required=True, description="The title of the story"),
        "content": fields.String(required=True, description="The content of the story"),
        "charity_id": fields.Integer(
            required=True, description="ID of the associated charity"
        ),
    },
)


@stories_ns.route("/")
class StoryList(Resource):
    @stories_ns.doc("Get list of stories")
    @stories_ns.marshal_with(
        stories_response_model, code=200, description="Success", as_list=True
    )
    def get(self):
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)

        stories = Story.query.paginate(page=page, per_page=per_page, error_out=False)
        story_data = [
            {"id": story.id, "title": story.title, "content": story.content}
            for story in stories.items
        ]

        return {"message": "Success", "data": story_data}, 200
