from src.models.repair import Repair
from src.database.db_mariadb import db

class RepairService:

    @staticmethod
    def get_all():
        return Repair.query.all()

    @staticmethod
    def get_by_id(repair_id):
        return Repair.query.get(repair_id)

    @staticmethod
    def create(data):
        repair = Repair(**data)
        db.session.add(repair)
        db.session.commit()
        return repair

    @staticmethod
    def update(repair_id, data):
        repair = Repair.query.get(repair_id)
        if not repair:
            return None
        for key, value in data.items():
            setattr(repair, key, value)
        db.session.commit()
        return repair

    @staticmethod
    def delete(repair_id):
        repair = Repair.query.get(repair_id)
        if not repair:
            return None
        db.session.delete(repair)
        db.session.commit()
        return repair
