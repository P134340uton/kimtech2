from src.database.db_mariadb import db

class Vehicle(db.Model):
    __tablename__ = "vehicles"
    vehicle_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    plate = db.Column(db.String(20), unique=True, nullable=False)
    current_state_id = db.Column(db.Integer, db.ForeignKey("vehicle_state.state_id"))

    person = db.relationship("Person", backref="vehicles")
    state = db.relationship("VehicleState", backref="vehicles")
