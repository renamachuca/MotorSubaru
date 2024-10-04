from flask import Blueprint, jsonify, request
from .models import Order, Product
from . import db

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    orders_list = [{"id": o.id, "product_id": o.product_id, "product_name": o.product.name, "quantity": o.quantity, "total_price": o.total_price} for o in orders]
    return jsonify(orders_list)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    
    # Buscar el producto por su nombre
    product_name = data.get('product_name')
    product = Product.query.filter_by(name=product_name).first()
    
    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404

    new_order = Order(
        product_id=product.id,
        quantity=data['quantity'],
        total_price=product.price * data['quantity']  # Calcular el precio total basado en la cantidad
    )
    
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({"message": "Order created successfully"}), 201
