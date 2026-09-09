from typing import Annotated, TypedDict

from langgraph.graph import add_messages


class State(TypedDict):
    """Schema for the React Agent's graph state."""

    messages: Annotated[list, add_messages]
