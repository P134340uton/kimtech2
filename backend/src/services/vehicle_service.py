from src.models.vehicle import Vehicle
from src.database.db_mariadb import db

class VehicleService:

    @staticmethod
    def get_all():
        return Vehicle.query.all()

    @staticmethod
    def get_by_id(vehicle_id):
        return Vehicle.query.get(vehicle_id)

    @staticmethod
    def create(data):
        vehicle = Vehicle(**data)
        db.session.add(vehicle)
        db.session.commit()
        return vehicle

    @staticmethod
    def update(vehicle_id, data):
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return None
        for key, value in data.items():
            setattr(vehicle, key, value)
        db.session.commit()
        return vehicle

    @staticmethod
    def delete(vehicle_id):
        vehicle = Vehicle.query.get(vehicle_id)
        if not vehicle:
            return None
        db.session.delete(vehicle)
        db.session.commit()
        return vehicle
