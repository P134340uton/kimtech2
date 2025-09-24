from src.models.permission import Permission
from src.database.db_mariadb import db

class PermissionService:

    @staticmethod
    def get_all_permissions():
        return Permission.query.all()

    @staticmethod
    def get_permission_by_id(permission_id):
        return Permission.query.get(permission_id)

    @staticmethod
    def create_permission(data):
        permission = Permission(**data)
        db.session.add(permission)
        db.session.commit()
        return permission

    @staticmethod
    def update_permission(permission_id, data):
        permission = Permission.query.get(permission_id)
        if not permission:
            return None
        for key, value in data.items():
            setattr(permission, key, value)
        db.session.commit()
        return permission

    @staticmethod
    def delete_permission(permission_id):
        permission = Permission.query.get(permission_id)
        if not permission:
            return None
        db.session.delete(permission)
        db.session.commit()
        return permission
