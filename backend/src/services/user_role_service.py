from src.models.user_role import UserRole
from src.database.db_mariadb import db

class UserRoleService:

    @staticmethod
    def get_all_user_roles():
        return UserRole.query.all()

    @staticmethod
    def get_roles_by_user(user_id):
        return UserRole.query.filter_by(user_id=user_id).all()

    @staticmethod
    def add_role_to_user(user_id, role_id):
        user_role = UserRole(user_id=user_id, role_id=role_id)
        db.session.add(user_role)
        db.session.commit()
        return user_role

    @staticmethod
    def remove_role_from_user(user_id, role_id):
        user_role = UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
        if user_role:
            db.session.delete(user_role)
            db.session.commit()
        return user_role
