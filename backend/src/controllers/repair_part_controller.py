from flask_restx import Namespace, Resource, fields
from src.services.repair_part_service import RepairPartService

api = Namespace("repair_parts", description="Repair Parts operations")

repair_part_model = api.model("RepairPart", {
    "repair_part_id": fields.Integer(readonly=True, description="Repair Part ID"),
    "repair_id": fields.Integer(required=True, description="Associated repair ID"),
    "description": fields.String(required=True, description="Part description"),
    "quantity": fields.Integer(required=True, description="Quantity of parts"),
    "source": fields.String(required=True, description="Source (Cliente or Proveedor)"),
})


@api.route("/")
class RepairPartList(Resource):
    @api.marshal_list_with(repair_part_model)
    def get(self):
        """Get all repair parts"""
        return RepairPartService.get_all()

    @api.expect(repair_part_model)
    @api.marshal_with(repair_part_model, code=201)
    def post(self):
        """Create a new repair part"""
        data = api.payload
        return RepairPartService.create(data), 201


@api.route("/<int:repair_part_id>")
@api.response(404, "Repair part not found")
class RepairPartResource(Resource):
    @api.marshal_with(repair_part_model)
    def get(self, repair_part_id):
        """Get a repair part by ID"""
        part = RepairPartService.get_by_id(repair_part_id)
        if not part:
            api.abort(404, "Repair part not found")
        return part

    @api.expect(repair_part_model)
    @api.marshal_with(repair_part_model)
    def put(self, repair_part_id):
        """Update a repair part"""
        data = api.payload
        part = RepairPartService.update(repair_part_id, data)
        if not part:
            api.abort(404, "Repair part not found")
        return part

    @api.response(204, "Repair part deleted")
    def delete(self, repair_part_id):
        """Delete a repair part"""
        part = RepairPartService.delete(repair_part_id)
        if not part:
            api.abort(404, "Repair part not found")
        return "", 204
