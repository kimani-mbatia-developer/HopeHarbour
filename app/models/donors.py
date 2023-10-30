from ..extensions import db, migrate


class Donor(db.Model):
    __tablename__ = "donors"
    donor_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    donations = db.Column(db.Integer, default=0)
    address = db.Column(db.String(255))
    total_donation_amount = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    # Relationship
    user = db.relationship("User", backref="donor")
