from src.models.maintenance import Maintenance
from src.database.db_mariadb import db

class MaintenanceService:

    @staticmethod
    def get_all():
        return Maintenance.query.all()

    @staticmethod
    def get_by_id(maintenance_id):
        return Maintenance.query.get(maintenance_id)

    @staticmethod
    def create(data):
        maintenance = Maintenance(**data)
        db.session.add(maintenance)
        db.session.commit()
        return maintenance

    @staticmethod
    def update(maintenance_id, data):
        maintenance = Maintenance.query.get(maintenance_id)
        if not maintenance:
            return None
        for key, value in data.items():
            setattr(maintenance, key, value)
        db.session.commit()
        return maintenance

    @staticmethod
    def delete(maintenance_id):
        maintenance = Maintenance.query.get(maintenance_id)
        if not maintenance:
            return None
        db.session.delete(maintenance)
        db.session.commit()
        return maintenance
