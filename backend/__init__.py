from dotenv import load_dotenv

load_dotenv()

import os
from flask import Flask
from flask_cors import CORS
from backend.models.common import bcrypt, db, jwt
from flask_migrate import Migrate
from backend.routes.auth_route import authenticate, identity
from flask_restx import Api

migrate = Migrate()


app = Flask(__name__, instance_relative_config=False)

secret_key = os.urandom(32).hex()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["SECRET_KEY"] = secret_key
jwt.init_app(app)
db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)

# Initialize CORS for cross-origin requests
cors = CORS(app)

# Instance of the API
api = Api(
    app,
    version="1.0",
    title="HopeHarbour API",
    description="API for HopeHarbour application",
)


app_swagger = Flask(__name__)
CORS(app_swagger)

api_swagger = Api(
    app_swagger,
    version="1.0",
    title="Swagger Documentation",
    description="Documentation for HopeHarbour API",
)


@app_swagger.route("/swagger")
def show_swagger():
    return api_swagger.documentation


# # Import the database models here
from backend.models.user import User
from backend.models.charity import Charity
from backend.models.donation import Donation
from backend.models.donor import Donor
from backend.models.beneficiary import Beneficiary
from backend.models.application import Application
from backend.models.story import Story
from backend.models.selected_charity import SelectedCharity
from backend.models.inventory_item import InventoryItem
from backend.models.payment_method import PaymentMethod
from backend.models.donation_reminder import Reminder


# Define your routes here
from backend.routes.auth_route import auth_bp, auth_ns
from backend.routes.admin_route import admin_bp, admin_ns
from backend.routes.stories_route import stories_bp, stories_ns
from backend.routes.charities_route import charities_bp, charities_ns
from backend.routes.donors_route import donors_bp, donors_ns
from backend.routes.donations_route import donations_bp, donations_ns
from backend.routes.applications_route import applications_bp, applications_ns
from backend.routes.beneficiary_route import beneficiaries_bp, beneficiaries_ns
from backend.routes.email_route import email

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(email)
app.register_blueprint(charities_bp)
app.register_blueprint(donors_bp)
app.register_blueprint(donations_bp)
app.register_blueprint(applications_bp)
app.register_blueprint(beneficiaries_bp)
app.register_blueprint(stories_bp)


# Add the namespaces to the Swagger API
api.add_namespace(auth_ns)
api.add_namespace(admin_ns)
api.add_namespace(charities_ns)
api.add_namespace(donors_ns)
api.add_namespace(donations_ns)
api.add_namespace(stories_ns)
api.add_namespace(applications_ns)
api.add_namespace(beneficiaries_ns)


@app.route("/")
def home():
    return "<h1>Welcome to the HopeHarbour API</h1>"
