from flask import Blueprint, jsonify
from .models import Product
from . import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET']) 
def get_products():
    products = Product.query.all() 
    products_list = [
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": p.price,
            "stock": p.stock
        } 
        for p in products
    ]  
    return jsonify(products_list)