from src.models.person import Person
from src.database.db_mariadb import db

def get_all_persons():
    return Person.query.all()

def get_person_by_id(person_id):
    return Person.query.get(person_id)

def create_person(data):
    new_person = Person(
        name=data["name"],
        email=data["email"],
        phone=data.get("phone"),
        city_id=data.get("city_id")
    )
    db.session.add(new_person)
    db.session.commit()
    return new_person

def update_person(person_id, data):
    person = Person.query.get(person_id)
    if not person:
        return None
    person.name = data.get("name", person.name)
    person.email = data.get("email", person.email)
    person.phone = data.get("phone", person.phone)
    person.city_id = data.get("city_id", person.city_id)
    db.session.commit()
    return person

def delete_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return None
    db.session.delete(person)
    db.session.commit()
    return person
