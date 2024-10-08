from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:penguin@localhost/orders_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    @app.route('/')
    def home():
        return "Conexión exitosa a la app"
    
   
    from .routes import orders_bp
    app.register_blueprint(orders_bp, url_prefix='/orders')
    
    return app
