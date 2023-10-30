from datetime import datetime
from backend.models.common import db


class Donation(db.Model):
    __tablename__ = "donations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    donor_id = db.Column(db.Integer, db.ForeignKey("donors.id"))
    amount = db.Column(db.Float, nullable=False)
    charity_id = db.Column(db.Integer, db.ForeignKey("charities.id"), nullable=True)
    anonymous = db.Column(db.Boolean, default=False)

    # Relationship to User
    user = db.relationship(
        "User", back_populates="donations", foreign_keys="[Donation.user_id]"
    )
    donor = db.relationship(
        "Donor", back_populates="donations", foreign_keys="[Donation.donor_id]"
    )  # Define the donor relationship
    charity = db.relationship("Charity", back_populates="donations")

    def __init__(self, amount, anonymous, user, charity, donor):
        self.amount = amount
        self.anonymous = anonymous
        self.user = user
        self.charity = charity
        self.donor = donor
