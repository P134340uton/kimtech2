from flask_restx import Namespace, Resource, fields
from src.services.maintenance_status_service import MaintenanceStatusService

api = Namespace("maintenance_statuses", description="Maintenance Status operations")

status_model = api.model("MaintenanceStatus", {
    "status_id": fields.Integer(readonly=True, description="Status ID"),
    "status_name": fields.String(required=True, description="Name of the maintenance status"),
})


@api.route("/")
class MaintenanceStatusList(Resource):
    @api.marshal_list_with(status_model)
    def get(self):
        """Get all maintenance statuses"""
        return MaintenanceStatusService.get_all()

    @api.expect(status_model)
    @api.marshal_with(status_model, code=201)
    def post(self):
        """Create a new maintenance status"""
        data = api.payload
        return MaintenanceStatusService.create(data), 201


@api.route("/<int:status_id>")
@api.response(404, "Maintenance status not found")
class MaintenanceStatusResource(Resource):
    @api.marshal_with(status_model)
    def get(self, status_id):
        """Get a maintenance status by ID"""
        status = MaintenanceStatusService.get_by_id(status_id)
        if not status:
            api.abort(404, "Maintenance status not found")
        return status

    @api.expect(status_model)
    @api.marshal_with(status_model)
    def put(self, status_id):
        """Update a maintenance status"""
        data = api.payload
        status = MaintenanceStatusService.update(status_id, data)
        if not status:
            api.abort(404, "Maintenance status not found")
        return status

    @api.response(204, "Maintenance status deleted")
    def delete(self, status_id):
        """Delete a maintenance status"""
        status = MaintenanceStatusService.delete(status_id)
        if not status:
            api.abort(404, "Maintenance status not found")
        return "", 204
