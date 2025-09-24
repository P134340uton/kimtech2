from flask_restx import Namespace, Resource, fields
from src.services import user_service

api = Namespace("users", description="Operaciones relacionadas con usuarios")

user_model = api.model("User", {
    "user_id": fields.Integer(readOnly=True, description="El ID del usuario"),
    "person_id": fields.Integer(required=True, description="El ID de la persona"),
    "password": fields.String(required=True, description="La contraseña"),
})

# GET /users/
@api.route("/")
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """Lista todos los usuarios"""
        return user_service.get_all_users()

    @api.expect(user_model, validate=True)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Crea un nuevo usuario"""
        data = api.payload
        return user_service.create_user(data), 201


# GET, PUT, DELETE /users/{id}
@api.route("/<int:user_id>")
@api.response(404, "Usuario no encontrado")
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Obtiene un usuario por ID"""
        user = user_service.get_user_by_id(user_id)
        if not user:
            api.abort(404, "Usuario no encontrado")
        return user

    @api.expect(user_model, validate=True)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Actualiza un usuario existente"""
        data = api.payload
        user = user_service.update_user(user_id, data)
        if not user:
            api.abort(404, "Usuario no encontrado")
        return user

    @api.response(204, "Usuario eliminado")
    def delete(self, user_id):
        """Elimina un usuario por ID"""
        user = user_service.delete_user(user_id)
        if not user:
            api.abort(404, "Usuario no encontrado")
        return "", 204
