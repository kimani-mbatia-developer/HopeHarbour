from backend.models.common import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(
        db.String(20), nullable=False
    )  # 'donor', 'charity', 'administrator'

    # Define relationships and back references
    donor = db.relationship("Donor", back_populates="user", uselist=False)
    charity = db.relationship("Charity", back_populates="user", uselist=False)
    # Add the 'donations' relationship with foreign key
    donations = db.relationship(
        "Donation", back_populates="user", foreign_keys="[Donation.user_id]"
    )
