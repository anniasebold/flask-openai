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
        formatted_question = (
            "Responda em formato JSON: { 'resposta': 'texto da resposta' }. "
            f"Pergunta: {question}"
        )
        return openai_handler.get_answer(formatted_question)

    def __format_response(self, answer: str) -> Dict:
        parsed_response = json.loads(answer)
        response_content = parsed_response.get("resposta", answer)
        return {
            "response": response_content
        }
