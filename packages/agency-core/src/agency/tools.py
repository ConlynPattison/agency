from datetime import datetime

from langchain_core.tools import tool


@tool(description="Get the current server-local date and time")
def get_local_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
