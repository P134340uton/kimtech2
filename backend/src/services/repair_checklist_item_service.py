from src.models.repair_checklist_item import RepairChecklistItem
from src.database.db_mariadb import db

class RepairChecklistItemService:

    @staticmethod
    def get_all():
        return RepairChecklistItem.query.all()

    @staticmethod
    def get_by_id(checklist_item_id):
        return RepairChecklistItem.query.get(checklist_item_id)

    @staticmethod
    def create(data):
        item = RepairChecklistItem(**data)
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def update(checklist_item_id, data):
        item = RepairChecklistItem.query.get(checklist_item_id)
        if not item:
            return None
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return item

    @staticmethod
    def delete(checklist_item_id):
        item = RepairChecklistItem.query.get(checklist_item_id)
        if not item:
            return None
        db.session.delete(item)
        db.session.commit()
        return item
