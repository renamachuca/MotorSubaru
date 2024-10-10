from flask import Blueprint, jsonify, request
from .models import Order
from . import db

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['GET'])
@orders_bp.route('/', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        orders_list = [{"id": o.id, "product_id": o.product_id, "quantity": o.quantity, "total_price": o.total_price} for o in orders]
        return jsonify(orders_list)
    except Exception as e:
        
        return jsonify({"error": str(e)}), 500

