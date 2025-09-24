from flask_restx import Namespace, Resource, fields
from src.services.repair_checklist_item_service import RepairChecklistItemService

api = Namespace("repair_checklist_items", description="Repair Checklist Items operations")

checklist_item_model = api.model("RepairChecklistItem", {
    "checklist_item_id": fields.Integer(readonly=True, description="Checklist item ID"),
    "repair_id": fields.Integer(required=True, description="Associated repair ID"),
    "description": fields.String(required=True, description="Item description"),
    "status": fields.String(
        required=True,
        description="Status (Pendiente, Completado, Requiere ajuste)",
        enum=["Pendiente", "Completado", "Requiere ajuste"]
    ),
})


@api.route("/")
class RepairChecklistItemList(Resource):
    @api.marshal_list_with(checklist_item_model)
    def get(self):
        """Get all repair checklist items"""
        return RepairChecklistItemService.get_all()

    @api.expect(checklist_item_model)
    @api.marshal_with(checklist_item_model, code=201)
    def post(self):
        """Create a new repair checklist item"""
        data = api.payload
        return RepairChecklistItemService.create(data), 201


@api.route("/<int:checklist_item_id>")
@api.response(404, "Checklist item not found")
class RepairChecklistItemResource(Resource):
    @api.marshal_with(checklist_item_model)
    def get(self, checklist_item_id):
        """Get a checklist item by ID"""
        item = RepairChecklistItemService.get_by_id(checklist_item_id)
        if not item:
            api.abort(404, "Checklist item not found")
        return item

    @api.expect(checklist_item_model)
    @api.marshal_with(checklist_item_model)
    def put(self, checklist_item_id):
        """Update a checklist item"""
        data = api.payload
        item = RepairChecklistItemService.update(checklist_item_id, data)
        if not item:
            api.abort(404, "Checklist item not found")
        return item

    @api.response(204, "Checklist item deleted")
    def delete(self, checklist_item_id):
        """Delete a checklist item"""
        item = RepairChecklistItemService.delete(checklist_item_id)
        if not item:
            api.abort(404, "Checklist item not found")
        return "", 204
