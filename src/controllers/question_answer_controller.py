import json
from typing import Dict
from src.drivers.openai_handler import OpenAIHandler

class QuestionAnswerController:
    '''
        Responsibility for implementing business rules
    '''

    def question_answer(self, question: str) -> Dict:
        response = self.__question_answer(question)
        formatted_response = self.__format_response(response)
        return formatted_response

    def __question_answer(self, question: str) -> str:
        openai_handler = OpenAIHandler()
        return openai_handler.get_answer(question)

    def __format_response(self, answer: str) -> Dict:
        parsed_response = json.loads(answer)
        response_content = parsed_response["resposta"]
        return {
            "response": response_content
        }
