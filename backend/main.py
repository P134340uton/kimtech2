# main.py

from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from src.database.db_mariadb import init_db, db
from src.config import Config
from src.models import *  # Esto importa todos los modelos
from src.controllers import namespaces  # Importa los namespaces

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)
    migrate.init_app(app, db)

     # Configura Swagger con Flask-RESTX
    api = Api(
        app,
        version="1.0",
        title="API KIMTECH",
        description="Documentación generada con Flask-RESTX (tipo Swagger)",
    )

      # Registra todos los namespaces desde __init__.py
    for ns, path in namespaces:
        api.add_namespace(ns, path=path)
   
   
    return app

# Para CLI (flask db ...)
app = create_app()
