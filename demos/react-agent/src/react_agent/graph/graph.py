from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt.tool_node import ToolNode

from agency.tools import get_local_datetime
from react_agent.graph.generator import generator_node_factory
from react_agent.graph.state import State


def should_continue(state: State) -> str:
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tool"
    return END


def build_graph() -> CompiledStateGraph:
    tool_node = ToolNode(tools=[get_local_datetime])
    graph = StateGraph(state_schema=State)

    graph.add_node("generator", generator_node_factory())
    graph.add_node("tool", tool_node)

    graph.add_edge(START, "generator")
    graph.add_conditional_edges("generator", should_continue)
    graph.add_edge("tool", "generator")
    graph.add_edge("generator", END)

    return graph.compile()
