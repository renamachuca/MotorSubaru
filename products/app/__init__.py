from flask import Flask
from .extensions import db 
from .routes import products_bp  

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:penguin@localhost/products'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    app.register_blueprint(products_bp, url_prefix='/products')  

    @app.route('/')
    def home():
        return "Conexión exitosa a la app"
    
    return app
