from flask_restx import Namespace, Resource, fields
from src.services.permission_service import PermissionService

api = Namespace("permissions", description="Permission operations")

permission_model = api.model("Permission", {
    "permission_id": fields.Integer(readonly=True, description="Permission ID"),
    "permission_name": fields.String(required=True, description="Permission name")
})


@api.route("/")
class PermissionList(Resource):
    @api.marshal_list_with(permission_model)
    def get(self):
        """Get all permissions"""
        return PermissionService.get_all_permissions()

    @api.expect(permission_model)
    @api.marshal_with(permission_model, code=201)
    def post(self):
        """Create a new permission"""
        data = api.payload
        return PermissionService.create_permission(data), 201


@api.route("/<int:permission_id>")
@api.response(404, "Permission not found")
class PermissionResource(Resource):
    @api.marshal_with(permission_model)
    def get(self, permission_id):
        """Get a permission by ID"""
        permission = PermissionService.get_permission_by_id(permission_id)
        if not permission:
            api.abort(404, "Permission not found")
        return permission

    @api.expect(permission_model)
    @api.marshal_with(permission_model)
    def put(self, permission_id):
        """Update a permission"""
        data = api.payload
        permission = PermissionService.update_permission(permission_id, data)
        if not permission:
            api.abort(404, "Permission not found")
        return permission

    @api.response(204, "Permission deleted")
    def delete(self, permission_id):
        """Delete a permission"""
        permission = PermissionService.delete_permission(permission_id)
        if not permission:
            api.abort(404, "Permission not found")
        return "", 204
