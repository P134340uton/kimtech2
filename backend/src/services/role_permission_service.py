from src.models.role_permission import RolePermission
from src.database.db_mariadb import db

class RolePermissionService:

    @staticmethod
    def get_all():
        return RolePermission.query.all()

    @staticmethod
    def get_by_ids(role_id, permission_id):
        return RolePermission.query.get((role_id, permission_id))

    @staticmethod
    def create(data):
        role_permission = RolePermission(**data)
        db.session.add(role_permission)
        db.session.commit()
        return role_permission

    @staticmethod
    def delete(role_id, permission_id):
        role_permission = RolePermission.query.get((role_id, permission_id))
        if not role_permission:
            return None
        db.session.delete(role_permission)
        db.session.commit()
        return role_permission
