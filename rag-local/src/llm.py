from ollamaClient import OllamaClient
from systemPrompt import get_system_prompt

class LLM:
    def __init__(self, name):
        self.llm=OllamaClient(
            model="llama3.2:3b",
            stream=True,
        )

    def call_llm(self, context, prompt):
        try:
            response = self.llm.chat(
                messages=[
                    {
                        "role": "system",
                        "content": get_system_prompt(),
                    },
                    {
                        "role": "user",
                        "content": f"Context: {context}, Question: {prompt}",
                    },
                ],
            )
            for chunk in response:
                if chunk["done"] is False:
                    yield chunk["message"]["content"]
                else:
                    break
        except Exception as e:
            yield f"An error occurred while calling the LLM: {str(e)}"