from backend.models.common import db


class InventoryItem(db.Model):
    __tablename__ = "inventory_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    beneficiary_id = db.Column(
        db.Integer, db.ForeignKey("beneficiaries.id"), nullable=False
    )
    charity_id = db.Column(db.Integer, db.ForeignKey("charities.id"), nullable=False)
    charity = db.relationship("Charity", back_populates="inventory_items")
    # Relationships
    beneficiary = db.relationship("Beneficiary", backref="inventory_items")
