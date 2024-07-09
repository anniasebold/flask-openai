from flask import Flask
from src.config import Config
from src.routes.ecommerce_route import ecommerce_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(ecommerce_bp, url_prefix='/api/ecommerce/v1')

    return app
