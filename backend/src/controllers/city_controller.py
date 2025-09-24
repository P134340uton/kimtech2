from flask_restx import Namespace, Resource, fields
from src.services import city_service

api = Namespace("cities", description="Operaciones relacionadas con ciudades")

city_model = api.model("City", {
    "city_id": fields.Integer(readOnly=True, description="ID de la ciudad"),
    "city_name": fields.String(required=True, description="Nombre de la ciudad"),
})

@api.route("/")
class CityList(Resource):
    @api.marshal_list_with(city_model)
    def get(self):
        """Lista todas las ciudades"""
        return city_service.get_all_cities()

    @api.expect(city_model)
    @api.marshal_with(city_model, code=201)
    def post(self):
        """Crea una nueva ciudad"""
        return city_service.create_city(api.payload), 201


@api.route("/<int:city_id>")
@api.param("city_id", "El identificador de la ciudad")
class CityResource(Resource):
    @api.marshal_with(city_model)
    def get(self, city_id):
        """Obtiene una ciudad por su ID"""
        return city_service.get_city_by_id(city_id)

    @api.expect(city_model)
    @api.marshal_with(city_model)
    def put(self, city_id):
        """Actualiza una ciudad existente"""
        return city_service.update_city(city_id, api.payload)

    def delete(self, city_id):
        """Elimina una ciudad"""
        return city_service.delete_city(city_id)
