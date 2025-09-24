from src.database.db_mariadb import db

class Notification(db.Model):
    __tablename__ = "notification"
    notification_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.vehicle_id"), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    read_status = db.Column(db.Boolean, default=False)

    user = db.relationship("User", backref="notifications")
    vehicle = db.relationship("Vehicle", backref="notifications")
