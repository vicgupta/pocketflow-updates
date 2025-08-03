from ollama import chat

def call_llm(messages, model="llama3.2"):
    """
    Calls the Ollama API with a list of messages and returns the response content.
    
    Args:
        messages (list): List of message dictionaries with 'role' and 'content' keys
        model (str): Name of the Ollama model to use (default: "llama3.2")
    
    Returns:
        str: The content of the assistant's response message
    """
    try:
        response = chat(
            model=model,
            messages=messages  # Pass the messages list directly
        )
        return response['message']['content']
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return f"Error: {str(e)}"
