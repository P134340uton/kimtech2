from flask_restx import Namespace, Resource, fields
from src.services.maintenance_service import MaintenanceService

api = Namespace("maintenances", description="Maintenance operations")

maintenance_model = api.model("Maintenance", {
    "maintenance_id": fields.Integer(readonly=True, description="Maintenance ID"),
    "vehicle_id": fields.Integer(required=True, description="Associated vehicle ID"),
    "scheduled_date": fields.String(required=True, description="Scheduled date (YYYY-MM-DD)"),
    "type": fields.String(
        required=True,
        description="Maintenance type",
        enum=["Preventivo", "Correctivo"]
    ),
    "priority": fields.Integer(description="Priority level"),
    "status_id": fields.Integer(description="Status ID from maintenance_status"),
})


@api.route("/")
class MaintenanceList(Resource):
    @api.marshal_list_with(maintenance_model)
    def get(self):
        """Get all maintenances"""
        return MaintenanceService.get_all()

    @api.expect(maintenance_model)
    @api.marshal_with(maintenance_model, code=201)
    def post(self):
        """Create a new maintenance"""
        data = api.payload
        return MaintenanceService.create(data), 201


@api.route("/<int:maintenance_id>")
@api.response(404, "Maintenance not found")
class MaintenanceResource(Resource):
    @api.marshal_with(maintenance_model)
    def get(self, maintenance_id):
        """Get a maintenance by ID"""
        maintenance = MaintenanceService.get_by_id(maintenance_id)
        if not maintenance:
            api.abort(404, "Maintenance not found")
        return maintenance

    @api.expect(maintenance_model)
    @api.marshal_with(maintenance_model)
    def put(self, maintenance_id):
        """Update a maintenance"""
        data = api.payload
        maintenance = MaintenanceService.update(maintenance_id, data)
        if not maintenance:
            api.abort(404, "Maintenance not found")
        return maintenance

    @api.response(204, "Maintenance deleted")
    def delete(self, maintenance_id):
        """Delete a maintenance"""
        maintenance = MaintenanceService.delete(maintenance_id)
        if not maintenance:
            api.abort(404, "Maintenance not found")
        return "", 204
