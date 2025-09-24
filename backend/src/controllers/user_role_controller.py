from flask_restx import Namespace, Resource, fields
from src.services.user_role_service import UserRoleService

api = Namespace("user_roles", description="User-Role relationship operations")

user_role_model = api.model("UserRole", {
    "user_id": fields.Integer(required=True, description="User ID"),
    "role_id": fields.Integer(required=True, description="Role ID")
})


@api.route("/")
class UserRoleList(Resource):
    @api.marshal_list_with(user_role_model)
    def get(self):
        """Get all user-role relationships"""
        return UserRoleService.get_all_user_roles()

    @api.expect(user_role_model)
    @api.marshal_with(user_role_model, code=201)
    def post(self):
        """Assign a role to a user"""
        data = api.payload
        return UserRoleService.add_role_to_user(data["user_id"], data["role_id"]), 201


@api.route("/<int:user_id>")
class UserRolesByUser(Resource):
    @api.marshal_list_with(user_role_model)
    def get(self, user_id):
        """Get all roles assigned to a user"""
        return UserRoleService.get_roles_by_user(user_id)


@api.route("/<int:user_id>/<int:role_id>")
@api.response(404, "UserRole not found")
class UserRoleResource(Resource):
    @api.response(204, "UserRole deleted")
    def delete(self, user_id, role_id):
        """Remove a role from a user"""
        user_role = UserRoleService.remove_role_from_user(user_id, role_id)
        if not user_role:
            api.abort(404, "UserRole not found")
        return "", 204
