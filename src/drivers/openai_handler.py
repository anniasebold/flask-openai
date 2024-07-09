from openai import OpenAI, APIError
from src.config import Config
from src.errors.openai_error import OpenAIError

class OpenAIHandler:
    def __init__(self):
        self.client = OpenAI(
            organization=Config.OPENAI_ORGANIZATION_ID, api_key=Config.OPENAI_API_KEY
        )
    def get_answer(self, question: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                temperature=1,
                max_tokens=4096,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant designed to output JSON."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )
            choices = response.choices
            if choices and isinstance(choices, list) and len(choices) > 0:
                return choices[0].message.content
            raise OpenAIError(message="Invalid response structure from OpenAI")

        except APIError as api_error:
            raise OpenAIError(
                message=api_error.message,
                code=api_error.code,
                error_type=api_error.type,
            ) from api_error

        except Exception as error:
            raise OpenAIError(str(error)) from error
