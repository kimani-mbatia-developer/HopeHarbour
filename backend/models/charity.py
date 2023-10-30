from backend.models.common import db
from backend.models.donation import Donation
from backend.models.user import User
from sqlalchemy.ext.hybrid import hybrid_property


class Charity(db.Model):
    __tablename__ = "charities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    total_donation_amount = db.Column(db.Float, server_default="0.0")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Relationships
    user = db.relationship("User", back_populates="charity", uselist=False)
    donations = db.relationship("Donation", back_populates="charity")
    applications = db.relationship("Application", back_populates="charity")
    beneficiaries = db.relationship("Beneficiary", back_populates="charity")
    stories = db.relationship("Story", back_populates="charity")
    inventory_items = db.relationship("InventoryItem", back_populates="charity")
    selected_charities = db.relationship("SelectedCharity", back_populates="charity")
    donors = db.relationship("Donor", back_populates="chosen_charity")

    # def __init__(self, name, description, user_id):
    #     self.name = name
    #     self.description = description
    #     self.user_id = user_id

    @hybrid_property
    def total_donation_amount(self):
        return sum(donation.amount for donation in self.donations)

    @total_donation_amount.expression
    def total_donation_amount(cls):
        return (
            db.select([db.func.sum(Donation.amount)])
            .where(Donation.charity_id == cls.id)
            .label("total_donation_amount")
        )

    @property
    def anonymous_donation_amount(self):
        return sum(donation.amount for donation in self.donations if donation.anonymous)
