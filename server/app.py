from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db
from controllers.auth_controllers import auth_bp
from controllers.guest_controllers import guest_bp
from controllers.episode_controllers import episode_bp
from server.controllers.appearance_controllers import appearance_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Setup extensions
db.init_app(app)
Migrate(app, db)
JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)

if __name__ == '__main__':
    app.run(debug=True)
