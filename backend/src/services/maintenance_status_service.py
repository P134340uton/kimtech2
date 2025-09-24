from src.models.maintenance_status import MaintenanceStatus
from src.database.db_mariadb import db

class MaintenanceStatusService:

    @staticmethod
    def get_all():
        return MaintenanceStatus.query.all()

    @staticmethod
    def get_by_id(status_id):
        return MaintenanceStatus.query.get(status_id)

    @staticmethod
    def create(data):
        status = MaintenanceStatus(**data)
        db.session.add(status)
        db.session.commit()
        return status

    @staticmethod
    def update(status_id, data):
        status = MaintenanceStatus.query.get(status_id)
        if not status:
            return None
        for key, value in data.items():
            setattr(status, key, value)
        db.session.commit()
        return status

    @staticmethod
    def delete(status_id):
        status = MaintenanceStatus.query.get(status_id)
        if not status:
            return None
        db.session.delete(status)
        db.session.commit()
        return status
