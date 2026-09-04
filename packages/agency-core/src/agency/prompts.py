from langchain_core.messages import SystemMessage


def sys_prompt() -> SystemMessage:
    return SystemMessage(
        content="""You are a helpful assistant that can reason and answer questions. 
    If you don't know the answer, you should say "I don't know"."""
    )


def init_messages() -> list:
    return [sys_prompt()]
