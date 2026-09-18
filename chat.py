# Ollama is a Python package that allows you to interface with Ollama models
from ollama import chat

# The chat functions enables a conversation with an llm
response = chat(
    model="qwen3:1.7b",
        # Models do not have memory, rather we send in a list of messages to provide context
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        # The user represents the person asking a question
        {"role": "user", "content": "What is the capital of France?"}
    ],
)

print(response.message.content)