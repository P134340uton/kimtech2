# src/config.py

import os
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("FLASK_DEBUG", "False").lower() in ["true", "1"]
    ENV = os.getenv("FLASK_ENV", "production")
