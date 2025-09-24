from src.models.repair_status import RepairStatus
from src.database.db_mariadb import db

class RepairStatusService:

    @staticmethod
    def get_all():
        return RepairStatus.query.all()

    @staticmethod
    def get_by_id(status_id):
        return RepairStatus.query.get(status_id)

    @staticmethod
    def create(data):
        status = RepairStatus(**data)
        db.session.add(status)
        db.session.commit()
        return status

    @staticmethod
    def update(status_id, data):
        status = RepairStatus.query.get(status_id)
        if not status:
            return None
        for key, value in data.items():
            setattr(status, key, value)
        db.session.commit()
        return status

    @staticmethod
    def delete(status_id):
        status = RepairStatus.query.get(status_id)
        if not status:
            return None
        db.session.delete(status)
        db.session.commit()
        return status
