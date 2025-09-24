from src.models.role import Role
from src.database.db_mariadb import db

class RoleService:

    @staticmethod
    def get_all_roles():
        return Role.query.all()

    @staticmethod
    def get_role_by_id(role_id):
        return Role.query.get(role_id)

    @staticmethod
    def create_role(data):
        new_role = Role(**data)
        db.session.add(new_role)
        db.session.commit()
        return new_role

    @staticmethod
    def update_role(role_id, data):
        role = Role.query.get(role_id)
        if role:
            for key, value in data.items():
                setattr(role, key, value)
            db.session.commit()
        return role

    @staticmethod
    def delete_role(role_id):
        role = Role.query.get(role_id)
        if role:
            db.session.delete(role)
            db.session.commit()
        return role
