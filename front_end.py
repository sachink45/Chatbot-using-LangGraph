import streamlit as st
from backend import chatbot, chat, retrieve_all_threads
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
import uuid



# generate new thread id    -- utility functions
def generate_therad():
    thread_id = uuid.uuid4()
    return thread_id

# reset the chat
def reset_chat():
    thread_id = generate_therad()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

# adding new thread
def add_thread(thread_id):
    if thread_id not in st.session_state['chat_thread']:
        st.session_state['chat_thread'].append(thread_id)

# load convo 
def load_convo(thread_id):
    snapshot = chat.get_state(config={'configurable': {'thread_id': thread_id}})
    return snapshot.values.get("messages", [])

# ---------------------------------------------------------------------------------------------------------------------------------------
# session begin

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_therad()

if 'chat_thread' not in st.session_state:
    st.session_state['chat_thread'] = retrieve_all_threads()
add_thread(st.session_state['thread_id'])


# ------------------------------------------------------------------------------------------------------------------------------------------
# ui


st.sidebar.title('LangGraph ChatBot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')

# --------------------------------------------------------------------------------------------------------------------------------------------
for i in st.session_state['chat_thread'][::-1]:
    if st.sidebar.button(str(i)):
        st.session_state['thread_id'] = i
        messages = load_convo(i)

        temp_msg = []
        for j in messages:
            if isinstance(j, HumanMessage):
                role = 'user' 
            else:
                role = 'assistant'
            temp_msg.append({'role' : role, 'content' : j.content})

        st.session_state['message_history'] = temp_msg


for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])



user_input = st.chat_input('Type Here ......')



if user_input:
    st.session_state['message_history'].append({'role' : 'user', 'content' : user_input})
    with st.chat_message('user'):
        st.text(user_input)
    
    # config = {'configurable' : {'thread_id' : st.session_state['thread_id']}}
    config = {'configurable' : {'thread_id' : st.session_state['thread_id']},
              "metadata" : {
                "thread_id" : st.session_state['thread_id']
              },
              "run_name" : "chat_turn"}

    with st.chat_message('assistant'):

        ai_message = st.write_stream(message_chunk.content for message_chunk, metadata in chat.stream({
            'messages' : [HumanMessage(content=user_input)]
            }, config=config, stream_mode='messages'))
        
    
    st.session_state['message_history'].append({'role' : 'assistant', 'content' : ai_message})