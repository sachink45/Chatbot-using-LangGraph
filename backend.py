# Importing Lib.
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import ToolNode, tools_condition


# calling API
load_dotenv()

# model
model = ChatOpenAI(model = "gpt-3.5-turbo")

# state
class chatbot(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]


# node logic
def chat_node(state : chatbot):
    query = state['messages']
    response = model.invoke(query)
    return {'messages' : [response]}


conn = sqlite3.connect(database = 'chatbot.db', check_same_thread=False)

# define checkpointer for persistence
checkpointer = SqliteSaver(conn = conn)


# creating a graph
graph = StateGraph(chatbot)

# adding node 
graph.add_node('chat_node', chat_node)

# adding edges
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

# compiling the graph
chat = graph.compile(checkpointer)

# extract the no. of threads

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)
    


