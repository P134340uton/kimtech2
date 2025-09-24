from src.database.db_mariadb import db

class VehicleState(db.Model):
    __tablename__ = "vehicle_state"
    state_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_name = db.Column(db.String(50), nullable=False)
