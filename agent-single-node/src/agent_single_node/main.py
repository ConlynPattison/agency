from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage



def get_llm(
        model="gemma4",
        base_url="http://localhost:11434",
        reasoning=False
    ) -> ChatOllama:
    return ChatOllama(
        model=model,
        base_url=base_url,
        verbose=True,
        reasoning=reasoning
    )


def sys_prompt() -> SystemMessage:
    return SystemMessage(content="""You are a helpful assistant that can reason and answer questions. 
    If you don't know the answer, you should say "I don't know".""")


def init_messages() -> list:
    return [sys_prompt()]


def main() -> None:
    messages = init_messages()
    llm = get_llm(reasoning=True)

    while True:
        user_message = input("User message: ")
        if user_message:
            messages.append(HumanMessage(content=user_message))

        aggregate_msg = None
        for chunk in llm.stream(messages):
            if chunk.content:
                print(chunk.content, end="", flush=True)
                aggregate_msg = chunk if aggregate_msg is None else aggregate_msg + chunk

        messages.append(AIMessage(content=aggregate_msg.content))

        print("\n\n---\n")

if __name__ == "__main__":
    main()