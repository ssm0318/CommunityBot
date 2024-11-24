from openai_client import open_ai_client


class HistorianAgent:
    def __init__(self, messages=None, channel_history=None):
        self.system_prompt = HistorianAgent._load_system_prompt()
        self.messages = messages or [{'role': 'system', 'content': self.system_prompt}]
        self.channel_history = channel_history

    def summarize(self) -> str:
        self.messages[0]['content'] = (
            f'{self.system_prompt}\nChannel History:\n {self.channel_history}'
        )
        if self.channel_history:
            response = open_ai_client.client.chat.completions.create(
                model='gpt-4o',
                messages=self.messages,
                stream=False
            )
            if response and hasattr(response, 'choices') and response.choices:
                return response.choices[0].message.content.strip()
            return "No valid response from OpenAI"
        return "No channel history provided"

    @staticmethod
    def _load_system_prompt():
        try:
            with open('./prompts/historian.txt', 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "error loading system prompt"
