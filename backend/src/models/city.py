from src.database.db_mariadb import db

class City(db.Model):
    __tablename__ = "city"
    city_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(100), nullable=False)
