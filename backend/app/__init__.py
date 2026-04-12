from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, cors

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inisialisasi extensions dengan app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app) # Penting agar frontend Vue.js tidak kena error CORS

    # Registrasi Blueprints
    from app.routes.users import users_bp
    app.register_blueprint(users_bp)

    return app