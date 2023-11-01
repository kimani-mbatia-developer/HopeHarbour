from backend import app

from backend.models.user import User
from backend.models.charity import Charity
from backend.models.donor import Donor
from backend.models.application import Application
from backend.models.beneficiary import Beneficiary
from backend.models.story import Story
from backend.models.inventory_item import InventoryItem
from backend.models.payment_method import PaymentMethod
from backend.models.selected_charity import SelectedCharity
from backend.models.donation import Donation
from backend.models.common import db, bcrypt
from faker import Faker
import random
import re

fake = Faker()


def clean_amount(amount_str):
    # Removing currency signs and commas from the string and convert to float
    cleaned_amount = float(re.sub(r"[^\d.]", "", amount_str))
    return cleaned_amount


# Roles for users
ROLES = ["donor", "charity", "administrator"]

# Payment methods
PAYMENT_METHODS = [
    "Mastercard",
    "Visa",
    "American Express",
    "UnionPay",
    "JCB",
    "Maestro",
    "PayPal",
    "Amazon Pay",
    "Google Pay",
    "Apple Pay",
    "Yandex",
    "Qiwi",
    "Skrill",
    "Sofort",
    "iDEAL",
    "Direct Debit",
    "Bitcoin",
]

# Descriptions for charities
CHARITY_DESCRIPTIONS = [
    "Connecting communities in need with vital support.",
    "Join us in making the world a better place.",
    "Providing hope and care to those who need it most.",
    "Your support changes lives every day.",
]

# Application status
APPLICATION_STATUSES = ["Pending", "Approved", "Rejected"]

# Donation frequency
DONATION_FREQUENCIES = ["one-time", "daily", "weekly", "monthly", "quarterly"]


def seed_data(num_entries):
    users = []
    charities = []
    beneficiaries = []

    for _ in range(num_entries):
        username = fake.user_name()
        email = fake.email()
        password = "your_password_here"

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        role = random.choice(ROLES)
        user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(user)
        users.append(user)

        charity_name = fake.company()
        description = fake.paragraph(ext_word_list=CHARITY_DESCRIPTIONS)
        charity = Charity(name=charity_name, description=description, user=user)
        db.session.add(charity)
        charities.append(charity)

    db.session.commit()

    for user in users:
        donor_name = fake.name()
        email = fake.email()
        address = fake.address()
        frequency = random.choice(DONATION_FREQUENCIES)
        recurring = frequency != "one-time"
        initial_donation_date = fake.date_between(start_date="-1y", end_date="today")
        next_donation_date = fake.date_between_dates(date_start=initial_donation_date)
        anonymous = random.choice([True, False])
        chosen_charity = random.choice(charities)

        donor = Donor(
            name=donor_name,
            email=email,
            address=address,
            frequency=frequency,
            recurring=recurring,
            initial_donation_date=initial_donation_date,
            next_donation_date=next_donation_date,
            anonymous=anonymous,
            chosen_charity=chosen_charity,
            user=user,
        )
        db.session.add(donor)

        for _ in range(random.randint(0, 5)):
            application = Application(charity_name=fake.company())
            application.charity = random.choice(charities)
            application.status = random.choice(APPLICATION_STATUSES)
            db.session.add(application)

        for _ in range(random.randint(0, 5)):
            beneficiary = Beneficiary(
                name=fake.name(), charity=random.choice(charities)
            )
            db.session.add(beneficiary)
            beneficiaries.append(beneficiary)

        # Seed Story
        for _ in range(random.randint(0, 5)):
            title = fake.catch_phrase()
            beneficiaries_names = [beneficiary.name for beneficiary in beneficiaries]
            story_content = fake.paragraph(ext_word_list=beneficiaries_names)
            story = Story(
                title=title,
                content=story_content,
                charity=random.choice(charities),
            )
            db.session.add(story)

        for _ in range(random.randint(0, 5)):
            inventory_item = InventoryItem(
                name=fake.word(),
                quantity=random.randint(1, 100),
                beneficiary=random.choice(beneficiaries),
                charity=random.choice(charities),
            )
            db.session.add(inventory_item)

        for _ in range(random.randint(0, 5)):
            payment_method = PaymentMethod(
                payment_type=random.choice(PAYMENT_METHODS),
                card_number=fake.credit_card_number(),
                expiration_date=fake.credit_card_expire(),
                security_code=fake.credit_card_security_code(),
                is_default=random.choice([True, False]),
                donor=donor,
            )
            db.session.add(payment_method)

        for _ in range(random.randint(0, 5)):
            selected_charity = SelectedCharity(
                donor=donor, charity=random.choice(charities)
            )
            db.session.add(selected_charity)

    db.session.commit()

    for _ in range(num_entries * 10):
        user = random.choice(users)
        donor = Donor.query.filter_by(user=user).first()
        amount_str = "{:.2f}".format(random.uniform(10, 500))
        amount = clean_amount(amount_str)
        anonymous = random.choice([True, False])
        charity = random.choice(charities)
        # frequency = random.choice(DONATION_FREQUENCIES)
        initial_donation_date = fake.date_between(start_date="-1y", end_date="today")
        next_donation_date = fake.date_between_dates(date_start=initial_donation_date)
        recurring = frequency != "one-time"
        donation = Donation(
            amount=amount,
            anonymous=anonymous,
            user=user,
            charity=charity,
            donor=donor,
        )
        db.session.add(donation)

    db.session.commit()


# Create a Flask application context
with app.app_context():
    # Delete existing records in the tables
    Application.query.delete()
    Story.query.delete()
    Beneficiary.query.delete()
    InventoryItem.query.delete()
    PaymentMethod.query.delete()
    SelectedCharity.query.delete()
    Donation.query.delete()
    Charity.query.delete()
    Donor.query.delete()
    User.query.delete()

    # Number of entries to create
    num_entries = 10

    # Seed the database
    db.create_all()
    seed_data(num_entries)
    db.session.commit()

    print("Fake data generation completed 🍻")
