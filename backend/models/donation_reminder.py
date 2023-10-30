from backend.models.common import db


class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    reminder_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), default="active")
