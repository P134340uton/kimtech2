from src.database.db_mariadb import db

class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    city_id = db.Column(db.Integer, db.ForeignKey("city.city_id"))

    city = db.relationship("City", backref="persons")
