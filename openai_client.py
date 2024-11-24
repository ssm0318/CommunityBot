import os
import openai
from dotenv import load_dotenv

load_dotenv()  # load all the variables from the env file


class OpenAIClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(OpenAIClient, cls).__new__(cls)
            cls._instance._init(*args, **kwargs)
        return cls._instance

    def _init(self, api_key=None):
        if not hasattr(self, 'client'):  # Initialize only once
            self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
            if not self.api_key:
                raise ValueError("API key is required")

            # Instantiate the OpenAI client
            self.client = openai.OpenAI(api_key=self.api_key)


# use a singleton instance of the OpenAI client
open_ai_client = OpenAIClient()
