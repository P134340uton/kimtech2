from flask_restx import Namespace, Resource, fields
from src.services.repair_status_service import RepairStatusService

api = Namespace("repair_statuses", description="Repair Status operations")

repair_status_model = api.model("RepairStatus", {
    "status_id": fields.Integer(readonly=True, description="Status ID"),
    "status_name": fields.String(required=True, description="Status name"),
})


@api.route("/")
class RepairStatusList(Resource):
    @api.marshal_list_with(repair_status_model)
    def get(self):
        """Get all repair statuses"""
        return RepairStatusService.get_all()

    @api.expect(repair_status_model)
    @api.marshal_with(repair_status_model, code=201)
    def post(self):
        """Create a new repair status"""
        data = api.payload
        return RepairStatusService.create(data), 201


@api.route("/<int:status_id>")
@api.response(404, "Repair status not found")
class RepairStatusResource(Resource):
    @api.marshal_with(repair_status_model)
    def get(self, status_id):
        """Get a repair status by ID"""
        status = RepairStatusService.get_by_id(status_id)
        if not status:
            api.abort(404, "Repair status not found")
        return status

    @api.expect(repair_status_model)
    @api.marshal_with(repair_status_model)
    def put(self, status_id):
        """Update a repair status"""
        data = api.payload
        status = RepairStatusService.update(status_id, data)
        if not status:
            api.abort(404, "Repair status not found")
        return status

    @api.response(204, "Repair status deleted")
    def delete(self, status_id):
        """Delete a repair status"""
        status = RepairStatusService.delete(status_id)
        if not status:
            api.abort(404, "Repair status not found")
        return "", 204
