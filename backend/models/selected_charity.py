from backend.models.common import db


class SelectedCharity(db.Model):
    __tablename__ = "selected_charities"

    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey("donors.id"), nullable=False)
    charity_id = db.Column(db.Integer, db.ForeignKey("charities.id"), nullable=False)

    # Define the relationships
    donor = db.relationship("Donor", back_populates="selected_charities")
    charity = db.relationship("Charity", back_populates="selected_charities")

    def __init__(self, donor, charity):
        self.donor = donor
        self.charity = charity
