English | [简体中文](README_CN.md)  
# LangGraph Checkpoint OceanBase

Implementation of LangGraph CheckpointSaver that uses OceanBase MySQL mode.

This project is forked from [langgraph-checkpoint-mysql](https://github.com/tjni/langgraph-checkpoint-mysql).
The main changes were made to this file `langgraph/checkpoint/mysql/base.py`, resolved compatibility issues during table creation.


The following dependencies should be installed before use:
- pymysql
- langgraph
- langchain[openai]
- aiomysql
- asyncmy

Since LangGraph Checkpointer uses the JSON data type for storage, it requires an OceanBase version that supports JSON.

langgraph-checkpoint-oceanbase has been uploaded to PyPI. You can install it using  
`pip install langgraph-checkpoint-oceanbase`
## Usage
In LangGraph's definition, Checkpointer refers to short-term memory (i.e. memory within a single conversation), while Store refers to long-term memory (i.e. memory across conversations). Therefore, usage is divided as a Checkpointer and as a Store.
### As Checkpointer
```python
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.checkpoint.mysql.pymysql import PyMySQLSaver
from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import HumanMessage
model = init_chat_model(model="qwen-max-latest", api_key="xxx",
                        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", model_provider="openai",temperature=0)
DB_URI = "mysql://username:password@ip:port/database"
with PyMySQLSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup()

    def call_model(state: MessagesState):
        response = model.invoke(state["messages"])
        return {"messages": response}
    builder = StateGraph(MessagesState)
    builder.add_node(call_model)
    builder.add_edge(START, "call_model")
    graph = builder.compile(checkpointer=checkpointer)
    config: RunnableConfig = {
        "configurable": {
            "thread_id": "1"
        }
    }
    for chunk in graph.stream(
        {"messages": [HumanMessage(content="hi! I'm bob")]},
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
    for chunk in graph.stream(
        {"messages":[HumanMessage(content="what's my name?")]},
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
```
### As Store
```python
from langchain_core.runnables import RunnableConfig
from langgraph.config import get_store
from langgraph.prebuilt import create_react_agent
from langgraph.store.mysql import PyMySQLStore
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from typing_extensions import TypedDict
DB_URI = "mysql://username:password@ip:port/database"
model = init_chat_model(model="qwen-max-latest", api_key="xxx",
                        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", model_provider="openai",temperature=0)


class UserInfo(TypedDict):
    name: str


def save_user_info(user_info: UserInfo, config: RunnableConfig) -> str:
    """Save user info"""
    store = get_store()
    user_id = config.get("configurable", {}).get("user_id")
    if user_id is None:
        raise ValueError("user_id must be provided in config['configurable']")
    store.put(("users",), user_id, dict(user_info))
    return "Successfully saved user info."


with PyMySQLStore.from_conn_string(DB_URI) as store:
    store.setup()
    agent=create_react_agent(
        model=model,
        tools=[save_user_info],
        store=store
    )
    # Run the agent
    agent.invoke(
        {"messages":[HumanMessage(content="My name is Tom and save my information")]},
        config={"configurable":{"user_id":"user_1"}}
    )
    # You can access the store directly to get the value
    result = store.get(("users",), "user_1")
    if result is not None:
        print(result.value)
    else:
        print("No value found for user_1")
```
For detailed usage instructions, please refer to [README document](https://github.com/tjni/langgraph-checkpoint-mysql/blob/main/README.md) of the original repository.