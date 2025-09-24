from src.models.vehicle_state import VehicleState
from src.database.db_mariadb import db

class VehicleStateService:

    @staticmethod
    def get_all():
        return VehicleState.query.all()

    @staticmethod
    def get_by_id(state_id):
        return VehicleState.query.get(state_id)

    @staticmethod
    def create(data):
        state = VehicleState(**data)
        db.session.add(state)
        db.session.commit()
        return state

    @staticmethod
    def update(state_id, data):
        state = VehicleState.query.get(state_id)
        if not state:
            return None
        for key, value in data.items():
            setattr(state, key, value)
        db.session.commit()
        return state

    @staticmethod
    def delete(state_id):
        state = VehicleState.query.get(state_id)
        if not state:
            return None
        db.session.delete(state)
        db.session.commit()
        return state
