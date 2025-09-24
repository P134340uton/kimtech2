from src.database.db_mariadb import db

class Maintenance(db.Model):
    __tablename__ = "maintenance"
    maintenance_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.vehicle_id"), nullable=False)
    scheduled_date = db.Column(db.Date, nullable=False)
    type = db.Column(db.Enum("Preventivo", "Correctivo"), nullable=False)
    priority = db.Column(db.Integer)
    status_id = db.Column(db.Integer, db.ForeignKey("maintenance_status.status_id"))

    vehicle = db.relationship("Vehicle", backref="maintenances")
    status = db.relationship("MaintenanceStatus", backref="maintenances")
