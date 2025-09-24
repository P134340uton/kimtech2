from src.database.db_mariadb import db

class MaintenanceChecklistItem(db.Model):
    __tablename__ = "maintenance_checklist_item"
    checklist_item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    maintenance_id = db.Column(db.Integer, db.ForeignKey("maintenance.maintenance_id"), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum("Pendiente", "Completado", "Requiere ajuste"), default="Pendiente")

    maintenance = db.relationship("Maintenance", backref="checklist_items")
