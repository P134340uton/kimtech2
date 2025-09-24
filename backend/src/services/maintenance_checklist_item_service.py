from src.models.maintenance_checklist_item import MaintenanceChecklistItem
from src.database.db_mariadb import db

class MaintenanceChecklistItemService:

    @staticmethod
    def get_all():
        return MaintenanceChecklistItem.query.all()

    @staticmethod
    def get_by_id(checklist_item_id):
        return MaintenanceChecklistItem.query.get(checklist_item_id)

    @staticmethod
    def create(data):
        item = MaintenanceChecklistItem(**data)
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def update(checklist_item_id, data):
        item = MaintenanceChecklistItem.query.get(checklist_item_id)
        if not item:
            return None
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return item

    @staticmethod
    def delete(checklist_item_id):
        item = MaintenanceChecklistItem.query.get(checklist_item_id)
        if not item:
            return None
        db.session.delete(item)
        db.session.commit()
        return item
