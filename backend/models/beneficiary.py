from backend.models.common import db


class Beneficiary(db.Model):
    __tablename__ = "beneficiaries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    charity_id = db.Column(db.Integer, db.ForeignKey("charities.id"))

    # Relationships
    charity = db.relationship("Charity", back_populates="beneficiaries")
