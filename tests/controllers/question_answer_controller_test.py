import json
import unittest
from unittest.mock import patch
from src.controllers.question_answer_controller import QuestionAnswerController
from src.drivers.openai_handler import OpenAIHandler

class TestQuestionAnswerController(unittest.TestCase):

    @patch.object(OpenAIHandler, 'get_answer')
    def test_answer_question(self, mock_get_answer):
        mock_response = json.dumps({"resposta": "Response test"})
        mock_get_answer.return_value = mock_response

        controller = QuestionAnswerController()
        question = "Question test?"
        result = controller.question_answer(question)

        self.assertIsInstance(result, dict)
        self.assertIn("response", result)
        self.assertEqual(result["response"], "Response test")
