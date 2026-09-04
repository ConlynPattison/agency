from langchain_ollama import ChatOllama


def get_llm(
    model="gemma4", base_url="http://localhost:11434", reasoning=False
) -> ChatOllama:
    return ChatOllama(model=model, base_url=base_url, verbose=True, reasoning=reasoning)
