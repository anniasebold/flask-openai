import unittest
from unittest.mock import patch
from src.views.http_types.http_request import HttpRequest
from src.views.question_answer_view import QuestionAnswerView
from src.controllers.question_answer_controller import QuestionAnswerController

class TestQuestionAnswerView(unittest.TestCase):

    @patch.object(QuestionAnswerController, "question_answer")
    def test_question_answer_success(self, mock_question_answer):
        test_answer = "This is a test answer"
        mock_question_answer.return_value = {"response": test_answer}

        http_request = HttpRequest(body={"question": "Question test?"})
        question_answer_view = QuestionAnswerView()
        http_response = question_answer_view.question_answer(http_request)

        self.assertEqual(http_response.status_code, 200)
        self.assertIsInstance(http_response.body, dict)
        self.assertIn("response", http_response.body)
        self.assertEqual(http_response.body["response"], test_answer)

    @patch.object(QuestionAnswerController, "question_answer")
    def test_question_answer_no_question(self, mock_question_answer):
        mock_question_answer.return_value = {"response": ""}

        http_request = HttpRequest(body={})
        question_answer_view = QuestionAnswerView()
        http_response = question_answer_view.question_answer(http_request)


        self.assertEqual(http_response.status_code, 200)
        self.assertIsInstance(http_response.body, dict)
        self.assertIn("response", http_response.body)
        self.assertEqual(http_response.body["response"], "")
