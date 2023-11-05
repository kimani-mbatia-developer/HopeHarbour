from backend.models.common import db


class PaymentMethod(db.Model):
    __tablename__ = "payment_methods"
    id = db.Column(db.Integer, primary_key=True)
    payment_type = db.Column(db.String(50), nullable=False)
    card_number = db.Column(db.String(20))
    expiration_date = db.Column(db.String(10))
    security_code = db.Column(db.String(4))
    is_default = db.Column(db.Boolean, default=False)
    donor_id = db.Column(db.Integer, db.ForeignKey("donors.id"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    charity_id = db.Column(db.Integer, db.ForeignKey("charities.id"))
    charity = db.relationship("Charity", back_populates="payment_methods")

    def __init__(
        self,
        payment_type,
        card_number,
        expiration_date,
        security_code,
        is_default,
        donor_id,
    ):
        self.payment_type = payment_type
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.is_default = is_default
        self.donor = donor_id
