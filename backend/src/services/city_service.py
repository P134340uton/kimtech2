from src.database.db_mariadb import db
from src.models.city import City

def get_all_cities():
    return City.query.all()

def get_city_by_id(city_id):
    return City.query.get_or_404(city_id)

def create_city(data):
    new_city = City(city_name=data["city_name"])
    db.session.add(new_city)
    db.session.commit()
    return new_city

def update_city(city_id, data):
    city = City.query.get_or_404(city_id)
    city.city_name = data["city_name"]
    db.session.commit()
    return city

def delete_city(city_id):
    city = City.query.get_or_404(city_id)
    db.session.delete(city)
    db.session.commit()
    return {"message": "Ciudad eliminada"}
