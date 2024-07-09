from flask import Blueprint
from src.routes.question_answer_route import question_answer_bp

ecommerce_bp = Blueprint('ecommerce', __name__)

ecommerce_bp.register_blueprint(question_answer_bp, url_prefix='/question-and-answer')
