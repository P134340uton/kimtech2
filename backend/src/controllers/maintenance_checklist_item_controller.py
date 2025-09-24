from flask_restx import Namespace, Resource, fields
from src.services.maintenance_checklist_item_service import MaintenanceChecklistItemService

api = Namespace("maintenance_checklist_items", description="Maintenance Checklist Item operations")

checklist_item_model = api.model("MaintenanceChecklistItem", {
    "checklist_item_id": fields.Integer(readonly=True, description="Checklist item ID"),
    "maintenance_id": fields.Integer(required=True, description="Related maintenance ID"),
    "description": fields.String(required=True, description="Description of the checklist item"),
    "status": fields.String(enum=["Pendiente", "Completado", "Requiere ajuste"], description="Status of the checklist item"),
})


@api.route("/")
class MaintenanceChecklistItemList(Resource):
    @api.marshal_list_with(checklist_item_model)
    def get(self):
        """Get all checklist items"""
        return MaintenanceChecklistItemService.get_all()

    @api.expect(checklist_item_model)
    @api.marshal_with(checklist_item_model, code=201)
    def post(self):
        """Create a new checklist item"""
        data = api.payload
        return MaintenanceChecklistItemService.create(data), 201


@api.route("/<int:checklist_item_id>")
@api.response(404, "Checklist item not found")
class MaintenanceChecklistItemResource(Resource):
    @api.marshal_with(checklist_item_model)
    def get(self, checklist_item_id):
        """Get a checklist item by ID"""
        item = MaintenanceChecklistItemService.get_by_id(checklist_item_id)
        if not item:
            api.abort(404, "Checklist item not found")
        return item

    @api.expect(checklist_item_model)
    @api.marshal_with(checklist_item_model)
    def put(self, checklist_item_id):
        """Update a checklist item"""
        data = api.payload
        item = MaintenanceChecklistItemService.update(checklist_item_id, data)
        if not item:
            api.abort(404, "Checklist item not found")
        return item

    @api.response(204, "Checklist item deleted")
    def delete(self, checklist_item_id):
        """Delete a checklist item"""
        item = MaintenanceChecklistItemService.delete(checklist_item_id)
        if not item:
            api.abort(404, "Checklist item not found")
        return "", 204
