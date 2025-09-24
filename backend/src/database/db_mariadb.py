# src/database/db_mariadb.py

import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()  # Carga las variables de entorno del archivo .env

db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    db.init_app(app)
    migrate.init_app(app, db)
