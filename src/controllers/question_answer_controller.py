import json
from typing import Dict
from src.drivers.openai_handler import OpenAiHandler

class QuestionAnswerController:
    '''
        Responsibility for implementing business rules
    '''
    def answer_question(self, question: str) -> Dict:
        response = self.__answer_question(question)
        formatted_response = self.__format_response(response)
        return formatted_response

    def __answer_question(self, question: str) -> str:
        openai_handler = OpenAiHandler()
        return openai_handler.get_answer(question)

    def __format_response(self, answer: str) -> Dict:
        parsed_response = json.loads(answer)
        response_content = parsed_response["resposta"]
        return {
            "response": response_content
        }
