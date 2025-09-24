from src.database.db_mariadb import db

class RepairPart(db.Model):
    __tablename__ = "repair_parts"
    repair_part_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    repair_id = db.Column(db.Integer, db.ForeignKey("repair.repair_id"), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    source = db.Column(db.Enum("Cliente", "Proveedor"), nullable=False)

    repair = db.relationship("Repair", backref="parts")

