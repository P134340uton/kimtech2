from flask_restx import Namespace, Resource, fields
from src.services.vehicle_state_service import VehicleStateService

api = Namespace("vehicle_states", description="Vehicle state operations")

vehicle_state_model = api.model("VehicleState", {
    "state_id": fields.Integer(readonly=True, description="State ID"),
    "state_name": fields.String(required=True, description="State name"),
})


@api.route("/")
class VehicleStateList(Resource):
    @api.marshal_list_with(vehicle_state_model)
    def get(self):
        """Get all vehicle states"""
        return VehicleStateService.get_all()

    @api.expect(vehicle_state_model)
    @api.marshal_with(vehicle_state_model, code=201)
    def post(self):
        """Create a new vehicle state"""
        data = api.payload
        return VehicleStateService.create(data), 201


@api.route("/<int:state_id>")
@api.response(404, "Vehicle state not found")
class VehicleStateResource(Resource):
    @api.marshal_with(vehicle_state_model)
    def get(self, state_id):
        """Get a vehicle state by ID"""
        state = VehicleStateService.get_by_id(state_id)
        if not state:
            api.abort(404, "Vehicle state not found")
        return state

    @api.expect(vehicle_state_model)
    @api.marshal_with(vehicle_state_model)
    def put(self, state_id):
        """Update a vehicle state"""
        data = api.payload
        state = VehicleStateService.update(state_id, data)
        if not state:
            api.abort(404, "Vehicle state not found")
        return state

    @api.response(204, "Vehicle state deleted")
    def delete(self, state_id):
        """Delete a vehicle state"""
        state = VehicleStateService.delete(state_id)
        if not state:
            api.abort(404, "Vehicle state not found")
        return "", 204
