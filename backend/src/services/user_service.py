from src.models.user import User
from src.database.db_mariadb import db

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_user(data):
    new_user = User(
        person_id=data["person_id"],
        password=data["password"]
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return None

    user.person_id = data.get("person_id", user.person_id)
    user.password = data.get("password", user.password)

    db.session.commit()
    return user

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return None

    db.session.delete(user)
    db.session.commit()
    return user
