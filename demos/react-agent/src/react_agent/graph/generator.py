from agency import get_llm, get_local_datetime
from react_agent.graph.state import State


def generator_node_factory():
    """Factory function to create a generator node for the state graph.

    Generator LLM is given tool access. These tools are all local to the server.
    """

    def generator_node(state: State):
        llm_with_tools = get_llm(reasoning=True).bind_tools([get_local_datetime])
        response = llm_with_tools.invoke(state["messages"])

        return {"messages": [response]}

    return generator_node
