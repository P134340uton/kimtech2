from src.database.db_mariadb import db

class Permission(db.Model):
    __tablename__ = "permissions"
    permission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    permission_name = db.Column(db.String(100), nullable=False)
