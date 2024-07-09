from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.question_answer_controller import QuestionAnswerController

class QuestionAnswerView:
    '''
        Responsibility for interacting with HTTP
    '''

    def answer_question(self, http_request: HttpRequest) -> HttpResponse:
        question_answer_controller = QuestionAnswerController()
        body = http_request.body
        question = body.get("question", "")
        formatted_response = question_answer_controller.answer_question(question)
        return HttpResponse(status_code=200, body=formatted_response)
