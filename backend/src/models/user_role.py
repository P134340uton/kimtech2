from src.database.db_mariadb import db

class UserRole(db.Model):
    __tablename__ = "user_roles"
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), primary_key=True)
