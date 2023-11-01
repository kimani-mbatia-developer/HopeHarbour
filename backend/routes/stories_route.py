from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from backend.models.charity import Charity
from backend.models.story import Story
from backend.models.common import db
from flask_restx import Resource, Namespace, fields

from backend.models.user import User

stories_ns = Namespace("stories", description="Story operations")
stories_bp = Blueprint("stories", __name__, url_prefix="/charity")

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


@stories_ns.route("/stories")
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

    @stories_ns.doc("Create a story")
    @stories_ns.expect(story_model)
    @stories_ns.marshal_with(
        stories_response_model, code=201, description="Story created successfully"
    )
    @jwt_required
    def post(self):
        # First check the role of the user
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        data = request.get_json()
        title = data.get("title")
        content = data.get("content")
        charity_id = data.get("charity_id")

        # Check if the charity exists
        charity = Charity.query.get(charity_id)
        if user.role == "charity" and user.id == charity_id:
            return {"message": "Charity not found"}, 404

        # Create a new story
        story = Story(title=title, content=content, charity_id=charity_id)

        db.session.add(story)
        db.session.commit()

        return {"message": "Story created successfully", "data": None}, 201


@stories_ns.route("/stories/charity/<int:charity_id>")
class StoryListByCharity(Resource):
    @stories_ns.doc("Get stories by charity ID")
    @stories_ns.marshal_with(
        stories_response_model, code=200, description="Success", as_list=True
    )
    def get(self, charity_id):
        stories = Story.query.filter_by(charity_id=charity_id).all()
        story_data = [
            {"id": story.id, "title": story.title, "content": story.content}
            for story in stories
        ]
        return {"message": "Success", "data": story_data}, 200
