from backend.models.common import db


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default="Pending", nullable=False)
    charity_id = db.Column(db.Integer, db.ForeignKey("charities.id"))
    charity = db.relationship("Charity", back_populates="applications", lazy=True)

    def __init__(self, charity_name):
        self.charity_name = charity_name
