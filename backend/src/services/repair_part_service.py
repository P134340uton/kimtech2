from src.models.repair_part import RepairPart
from src.database.db_mariadb import db

class RepairPartService:

    @staticmethod
    def get_all():
        return RepairPart.query.all()

    @staticmethod
    def get_by_id(repair_part_id):
        return RepairPart.query.get(repair_part_id)

    @staticmethod
    def create(data):
        repair_part = RepairPart(**data)
        db.session.add(repair_part)
        db.session.commit()
        return repair_part

    @staticmethod
    def update(repair_part_id, data):
        repair_part = RepairPart.query.get(repair_part_id)
        if not repair_part:
            return None
        for key, value in data.items():
            setattr(repair_part, key, value)
        db.session.commit()
        return repair_part

    @staticmethod
    def delete(repair_part_id):
        repair_part = RepairPart.query.get(repair_part_id)
        if not repair_part:
            return None
        db.session.delete(repair_part)
        db.session.commit()
        return repair_part
