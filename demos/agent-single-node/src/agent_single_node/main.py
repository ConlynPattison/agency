from langchain_core.messages import AIMessage, HumanMessage

from agency import get_llm, init_messages


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
                aggregate_msg = (
                    chunk if aggregate_msg is None else aggregate_msg + chunk
                )

        messages.append(AIMessage(content=aggregate_msg.content))

        print("\n\n---\n")


if __name__ == "__main__":
    main()
