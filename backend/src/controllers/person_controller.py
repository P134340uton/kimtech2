from flask_restx import Namespace, Resource, fields
from src.services.person_service import (
    get_all_persons, get_person_by_id, create_person,
    update_person, delete_person
)

api = Namespace("persons", description="Operaciones relacionadas con personas")

person_model = api.model("Person", {
    "person_id": fields.Integer(readOnly=True, description="El ID de la persona"),
    "name": fields.String(required=True, description="Nombre de la persona"),
    "email": fields.String(required=True, description="Email único"),
    "phone": fields.String(description="Número de teléfono"),
    "city_id": fields.Integer(description="ID de la ciudad")
})

@api.route("/")
class PersonList(Resource):
    @api.marshal_list_with(person_model)
    def get(self):
        """Lista todas las personas"""
        return get_all_persons()

    @api.expect(person_model)
    @api.marshal_with(person_model, code=201)
    def post(self):
        """Crea una nueva persona"""
        return create_person(api.payload), 201

@api.route("/<int:person_id>")
@api.response(404, "Persona no encontrada")
class PersonResource(Resource):
    @api.marshal_with(person_model)
    def get(self, person_id):
        """Obtiene una persona por ID"""
        person = get_person_by_id(person_id)
        if not person:
            api.abort(404, "Persona no encontrada")
        return person

    @api.expect(person_model)
    @api.marshal_with(person_model)
    def put(self, person_id):
        """Actualiza una persona por ID"""
        person = update_person(person_id, api.payload)
        if not person:
            api.abort(404, "Persona no encontrada")
        return person

    @api.response(204, "Persona eliminada")
    def delete(self, person_id):
        """Elimina una persona por ID"""
        person = delete_person(person_id)
        if not person:
            api.abort(404, "Persona no encontrada")
        return "", 204
