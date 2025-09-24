from flask_restx import Namespace, Resource, fields
from src.services.vehicle_service import VehicleService

api = Namespace("vehicles", description="Vehicle operations")

vehicle_model = api.model("Vehicle", {
    "vehicle_id": fields.Integer(readonly=True, description="Vehicle ID"),
    "person_id": fields.Integer(required=True, description="Owner (person_id)"),
    "brand": fields.String(required=True, description="Vehicle brand"),
    "model": fields.String(required=True, description="Vehicle model"),
    "year": fields.Integer(required=True, description="Manufacturing year"),
    "plate": fields.String(required=True, description="License plate"),
    "current_state_id": fields.Integer(description="Current vehicle state ID"),
})


@api.route("/")
class VehicleList(Resource):
    @api.marshal_list_with(vehicle_model)
    def get(self):
        """Get all vehicles"""
        return VehicleService.get_all()

    @api.expect(vehicle_model)
    @api.marshal_with(vehicle_model, code=201)
    def post(self):
        """Create a new vehicle"""
        data = api.payload
        return VehicleService.create(data), 201


@api.route("/<int:vehicle_id>")
@api.response(404, "Vehicle not found")
class VehicleResource(Resource):
    @api.marshal_with(vehicle_model)
    def get(self, vehicle_id):
        """Get a vehicle by ID"""
        vehicle = VehicleService.get_by_id(vehicle_id)
        if not vehicle:
            api.abort(404, "Vehicle not found")
        return vehicle

    @api.expect(vehicle_model)
    @api.marshal_with(vehicle_model)
    def put(self, vehicle_id):
        """Update a vehicle"""
        data = api.payload
        vehicle = VehicleService.update(vehicle_id, data)
        if not vehicle:
            api.abort(404, "Vehicle not found")
        return vehicle

    @api.response(204, "Vehicle deleted")
    def delete(self, vehicle_id):
        """Delete a vehicle"""
        vehicle = VehicleService.delete(vehicle_id)
        if not vehicle:
            api.abort(404, "Vehicle not found")
        return "", 204
