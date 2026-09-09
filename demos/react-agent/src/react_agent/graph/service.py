from typing import Any

from langgraph.graph.state import CompiledStateGraph

from react_agent.graph.state import State


def stream_agent_chat(graph: CompiledStateGraph, messages: list) -> Any | None:
    """Executes the state graph with the given messages and streams the output.

    Final graph execution state is returned after the graph execution is complete. If
    the graph fails to finish, None is returned.
    """
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

        return final_state
