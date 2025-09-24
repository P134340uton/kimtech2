from src.database.db_mariadb import db

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    person = db.relationship("Person", backref="user")

