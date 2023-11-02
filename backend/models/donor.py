from backend.models.common import db


class Donor(db.Model):
    __tablename__ = "donors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255))
    email = db.Column(db.String(120), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    frequency = db.Column(
        db.String(10)
    )  # Options: 'one-time', 'daily', 'weekly', 'monthly', 'quarterly'
    charity_id = db.Column(db.Integer, db.ForeignKey("charities.id"), nullable=True)

    # Relationships
    selected_charities = db.relationship("SelectedCharity", back_populates="donor")
    recurring = db.Column(db.Boolean, default=False)
    initial_donation_date = db.Column(db.DateTime)
    next_donation_date = db.Column(db.DateTime)
    anonymous = db.Column(db.Boolean, nullable=False, default=False)
    donations = db.relationship(
        "Donation", back_populates="donor", foreign_keys="[Donation.donor_id]"
    )
    user = db.relationship("User", back_populates="donor")
    chosen_charity = db.relationship("Charity", back_populates="donors", uselist=False)
    payment_methods = db.relationship("PaymentMethod", backref="donor")
