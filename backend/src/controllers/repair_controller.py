from flask_restx import Namespace, Resource, fields
from src.services.repair_service import RepairService

api = Namespace("repairs", description="Repair operations")

repair_model = api.model("Repair", {
    "repair_id": fields.Integer(readonly=True, description="Repair ID"),
    "vehicle_id": fields.Integer(required=True, description="Vehicle ID"),
    "reported_issue": fields.String(required=True, description="Reported issue"),
    "scheduled_date": fields.Date(required=True, description="Scheduled repair date"),
    "priority": fields.Integer(description="Priority level"),
    "status_id": fields.Integer(description="Repair status ID"),
})


@api.route("/")
class RepairList(Resource):
    @api.marshal_list_with(repair_model)
    def get(self):
        """Get all repairs"""
        return RepairService.get_all()

    @api.expect(repair_model)
    @api.marshal_with(repair_model, code=201)
    def post(self):
        """Create a new repair"""
        data = api.payload
        return RepairService.create(data), 201


@api.route("/<int:repair_id>")
@api.response(404, "Repair not found")
class RepairResource(Resource):
    @api.marshal_with(repair_model)
    def get(self, repair_id):
        """Get a repair by ID"""
        repair = RepairService.get_by_id(repair_id)
        if not repair:
            api.abort(404, "Repair not found")
        return repair

    @api.expect(repair_model)
    @api.marshal_with(repair_model)
    def put(self, repair_id):
        """Update a repair"""
        data = api.payload
        repair = RepairService.update(repair_id, data)
        if not repair:
            api.abort(404, "Repair not found")
        return repair

    @api.response(204, "Repair deleted")
    def delete(self, repair_id):
        """Delete a repair"""
        repair = RepairService.delete(repair_id)
        if not repair:
            api.abort(404, "Repair not found")
        return "", 204
