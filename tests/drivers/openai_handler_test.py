import unittest
from unittest.mock import patch, MagicMock
from openai import APIError
from src.drivers.openai_handler import OpenAIHandler
from src.errors.openai_error import OpenAIError

class TestOpenAiHandler(unittest.TestCase):

    @patch('src.drivers.openai_handler.OpenAI')
    def test_get_answer_success(self, mock_open_ai):
        test_response = "This is a test response for question"
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = test_response

        mock_open_ai.return_value.chat.completions.create.return_value = mock_response

        handler = OpenAIHandler()
        response = handler.get_answer("This is a test question?")

        self.assertEqual(response, test_response)

    @patch('src.drivers.openai_handler.OpenAI')
    def test_get_answer_api_error(self, mock_open_ai):
        error_message = "API error message test"
        api_error = APIError(message=error_message, request=None, body=None)
        api_error.code = 500
        api_error.type = "server_error"
        mock_open_ai.return_value.chat.completions.create.side_effect = api_error
        handler = OpenAIHandler()

        with self.assertRaises(OpenAIError) as context:
            handler.get_answer("This is a test question?")

        self.assertEqual(context.exception.message, error_message)
        self.assertEqual(context.exception.code, 500)
        self.assertEqual(context.exception.error_type, "server_error")

    @patch('src.drivers.openai_handler.OpenAI')
    def test_get_answer_generic_exception(self, mock_open_ai):
        generic_error_message = "Generic error response"
        generic_error = Exception(generic_error_message)
        mock_open_ai.return_value.chat.completions.create.side_effect = generic_error

        handler = OpenAIHandler()

        with self.assertRaises(OpenAIError) as context:
            handler.get_answer("This is a test question?")

        self.assertEqual(str(context.exception), generic_error_message)
