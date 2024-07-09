from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.question_answer_view import QuestionAnswerView
from src.errors.error_handler import handle_errors

question_answer_bp = Blueprint('question_answer', __name__)

@question_answer_bp.route('', methods=["POST"])
def question_and_answer():
    response = None
    try:
        question_answer_view = QuestionAnswerView()
        http_request = HttpRequest(body=request.json)
        response = question_answer_view.question_answer(http_request)
    except Exception as exception:
        response = handle_errors(exception)

    return jsonify(response.body), response.status_code
