# Ollama is a Python package that allows you to interface with Ollama models
from ollama import chat

messages = []

# Define Function
# Explicitly stating the type of the parameters and return value
def add(a: int, b: int) -> int:
    # A description for the Ollama Python program to understand the purpose of the function (a docstring)
    """Add two numbers together."""
    return a + b

# The chat functions enables a conversation with an llm
response = chat(
    model="qwen3:1.7b",
        # Models do not have memory, rather we send in a list of messages to provide context
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        # The user represents the person asking a question
        {"role": "user", "content": "What is 10 + 2?"}
    ],
    tools=[add],

)

# Assess whether the model has requested tool usage
if response.message.tool_calls:
    # Running a loop in the event the models calls our single tool more than once
    for call in response.message.tool_calls:
        # Check if the tool name matches the function we defined
        if call.function.name == "add":
            # Extract the arguments from the tool call
            args = call.function.arguments
            print(args)
            a = args['a']
            b = args['b']
            # Call the function with the provided arguments
            result = add(a, b)
            # Print the result of the function call
            # print(f"Result of add({args[0]}, {args[1]}): {result}")
            print(f"Result of add: {result}")

messages.append({"role": "assistant", "content": f"Result of add({a}, {b}): {result}"})



print(response.message.content)