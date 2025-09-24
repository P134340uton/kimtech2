from src.database.db_mariadb import db

class Repair(db.Model):
    __tablename__ = "repair"
    repair_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.vehicle_id"), nullable=False)
    reported_issue = db.Column(db.String(255), nullable=False)
    scheduled_date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.Integer)
    status_id = db.Column(db.Integer, db.ForeignKey("repair_status.status_id"))

    vehicle = db.relationship("Vehicle", backref="repairs")
    status = db.relationship("RepairStatus", backref="repairs")
