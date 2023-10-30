from dotenv import load_dotenv

load_dotenv()

import os
from flask import Flask
from flask_cors import CORS
from backend.models.common import bcrypt, db, jwt
from flask_migrate import Migrate

# from backend.routes.route_auth import authenticate, identity

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


@app.route("/")
def home():
    return "<h1>Welcome to the HopeHarbour API</h1>"
