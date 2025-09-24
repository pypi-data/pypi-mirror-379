[English](README.md) | 简体中文
# LangGraph Checkpoint OceanBase

使用 OceanBase MySQL 模式实现了 LangGraph CheckpointSaver。

这个项目是从 [langgraph-checkpoint-mysql](https://github.com/tjni/langgraph-checkpoint-mysql) fork 的, 主要更改了这个文件 `langgraph/checkpoint/mysql/base.py`，解决了在 OceanBase 中创建表时的一些兼容性问题。


在使用之前需要安装以下的依赖包:
- pymysql
- langgraph
- langchain[openai]
- aiomysql
- asyncmy

因为 LangGraph Checkpointer 在存储数据时使用了 JSON 类型，所以需要使用支持 JSON 的 OceanBase 版本。

langgraph-checkpoint-oceanbase 已经上传到 PyPI。可以使用下面的命令安装:   
`pip install langgraph-checkpoint-oceanbase`

## 使用方式
在 LangGraph 的定义中，Checkpointer 是短期记忆（即一轮对话中的记忆），Store 是长期记忆（即跨对话的记忆），所以使用方式分为 Checkpointer 和 Store。
### 作为 Checkpointer
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
### 作为 Store
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
更详细的使用方法, 可以参考原仓库的 [README 文档](https://github.com/tjni/langgraph-checkpoint-mysql/blob/main/README.md)。