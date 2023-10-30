from backend.models.common import db


class Story(db.Model):
    __tablename__ = "stories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    charity_id = db.Column(db.Integer, db.ForeignKey("charities.id"), nullable=False)

    # Relationships
    charity = db.relationship("Charity", back_populates="stories")
