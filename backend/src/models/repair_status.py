from src.database.db_mariadb import db

class RepairStatus(db.Model):
    __tablename__ = "repair_status"
    status_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_name = db.Column(db.String(50), nullable=False)
