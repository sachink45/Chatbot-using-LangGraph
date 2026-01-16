# 🤖 Chatbot using LangGraph and Streamlit

An interactive **stateful chatbot** built using **LangGraph**, **LangChain**, **OpenAI**, and **Streamlit**, with **SQLite-based persistence** for storing and resuming conversations.

---

## 🚀 Features

- 🧠 Stateful conversations using LangGraph
- 🧵 Multiple chat threads with unique thread IDs
- 💾 Persistent chat memory using SQLite
- ⚡ Streaming AI responses in real time
- 🖥️ Interactive chat UI using Streamlit
- 🔁 Resume previous conversations anytime

---

## 🧱 Tech Stack

- **Frontend:** Streamlit
- **Backend / Orchestration:** LangGraph
- **LLM:** OpenAI (GPT-3.5-Turbo)
- **Memory / Persistence:** SQLite
- **Frameworks:** LangChain
- **Environment Management:** python-dotenv

---

## 📂 Project Structure

```text
chatbot_with_db/
│
├── backend.py
├── front_end.py
├── chatbot.db
├── .env
└── README.md
```

---

## 🧠 How the Application Works

### Frontend (Streamlit)

- Accepts user input
- Displays chat messages
- Manages session state
- Streams assistant responses

### Backend (LangGraph)

- Defines chatbot state using `TypedDict`
- Controls message flow with graph nodes
- Calls OpenAI model for responses
- Stores checkpoints in SQLite

### Persistence

- Each chat has a unique `thread_id`
- Messages are saved in SQLite
- Old conversations can be reloaded

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sachink45/Chatbot-using-LangGraph.git
cd Chatbot-using-LangGraph
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate
myenv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit langgraph langchain langchain-openai python-dotenv
```

### 4️⃣ Configure Environment Variables

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5️⃣ Run the Application

```bash
streamlit run front_end.py
```

---

## 🖥️ User Interface Overview

### Sidebar

- ➕ New Chat
- 📜 Conversation List

### Main Area

- 💬 Chat messages
- ⚡ Streaming assistant responses
- 🧠 Context preserved automatically

---

## 🧵 Conversation Threads

- Unique UUID per conversation
- Stored in SQLite
- Reloadable anytime

---

## 🧩 Backend Architecture

```text
START → chat_node → END
```

---

## 💾 SQLite Persistence

- Uses `SqliteSaver`
- Stores messages and checkpoints
- Enables conversation recovery

---

## 🧪 Use Cases

- AI assistant with memory
- Multi-session chatbots
- Portfolio project
