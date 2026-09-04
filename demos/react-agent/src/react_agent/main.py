from agency.prompts import init_messages
from langchain_core.messages import HumanMessage

from react_agent.graph.graph import build_graph
from react_agent.graph.state import State


def main() -> None:
    graph = build_graph()
    messages = init_messages()

    while True:
        user_message = input("User message: ")
        if user_message:
            messages.append(HumanMessage(content=user_message))

        final_state = None
        for mode, payload in graph.stream(
            State(messages=messages), stream_mode=["messages", "values"]
        ):
            if mode == "values":
                final_state = payload
                continue

            chunk, metadata = payload
            node = metadata.get("langgraph_node")

            # Handle the streamed chunks from the graph node executions
            if node == "generator":
                for tool_call in chunk.tool_call_chunks:
                    if tool_call.get("name"):
                        print(f"\n[calling {tool_call['name']}]", flush=True)
                if chunk.content:
                    print(chunk.content, end="", flush=True)
            elif node == "tool":
                print(f"[{chunk.name} -> {chunk.content}]\n", flush=True)

        if final_state is not None:
            messages = final_state["messages"]

        print("\n\n---\n")


if __name__ == "__main__":
    main()
