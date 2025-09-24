from flask_restx import Namespace, Resource, fields
from src.services.role_service import RoleService

api = Namespace("roles", description="Role operations")

role_model = api.model("Role", {
    "role_id": fields.Integer(readonly=True),
    "role_name": fields.String(required=True, description="Role name")
})


@api.route("/")
class RoleList(Resource):
    @api.marshal_list_with(role_model)
    def get(self):
        """Get all roles"""
        return RoleService.get_all_roles()

    @api.expect(role_model)
    @api.marshal_with(role_model, code=201)
    def post(self):
        """Create a new role"""
        data = api.payload
        return RoleService.create_role(data), 201


@api.route("/<int:role_id>")
@api.response(404, "Role not found")
class RoleResource(Resource):
    @api.marshal_with(role_model)
    def get(self, role_id):
        """Get a role by ID"""
        role = RoleService.get_role_by_id(role_id)
        if not role:
            api.abort(404, "Role not found")
        return role

    @api.expect(role_model)
    @api.marshal_with(role_model)
    def put(self, role_id):
        """Update a role"""
        data = api.payload
        role = RoleService.update_role(role_id, data)
        if not role:
            api.abort(404, "Role not found")
        return role

    @api.response(204, "Role deleted")
    def delete(self, role_id):
        """Delete a role"""
        role = RoleService.delete_role(role_id)
        if not role:
            api.abort(404, "Role not found")
        return "", 204
