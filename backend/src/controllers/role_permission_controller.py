from flask_restx import Namespace, Resource, fields
from src.services.role_permission_service import RolePermissionService

api = Namespace("role_permissions", description="Assign permissions to roles")

role_permission_model = api.model("RolePermission", {
    "role_id": fields.Integer(required=True, description="Role ID"),
    "permission_id": fields.Integer(required=True, description="Permission ID"),
})


@api.route("/")
class RolePermissionList(Resource):
    @api.marshal_list_with(role_permission_model)
    def get(self):
        """Get all role-permission associations"""
        return RolePermissionService.get_all()

    @api.expect(role_permission_model)
    @api.marshal_with(role_permission_model, code=201)
    def post(self):
        """Assign a permission to a role"""
        data = api.payload
        return RolePermissionService.create(data), 201


@api.route("/<int:role_id>/<int:permission_id>")
@api.response(404, "RolePermission not found")
class RolePermissionResource(Resource):
    @api.marshal_with(role_permission_model)
    def get(self, role_id, permission_id):
        """Get a role-permission by IDs"""
        rp = RolePermissionService.get_by_ids(role_id, permission_id)
        if not rp:
            api.abort(404, "RolePermission not found")
        return rp

    @api.response(204, "RolePermission deleted")
    def delete(self, role_id, permission_id):
        """Remove a permission from a role"""
        rp = RolePermissionService.delete(role_id, permission_id)
        if not rp:
            api.abort(404, "RolePermission not found")
        return "", 204
