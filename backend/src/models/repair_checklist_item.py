from src.database.db_mariadb import db

class RepairChecklistItem(db.Model):
    __tablename__ = "repair_checklist_item"
    checklist_item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    repair_id = db.Column(db.Integer, db.ForeignKey("repair.repair_id"), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum("Pendiente", "Completado", "Requiere ajuste"), default="Pendiente")

    repair = db.relationship("Repair", backref="checklist_items")
