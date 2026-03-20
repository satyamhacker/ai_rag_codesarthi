
---

```markdown
# 🧠 CodeSarthi – AI Codebase Assistant

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/langchain-0.3.0+-green.svg)](https://python.langchain.com/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.35+-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/ollama-0.1.30+-orange.svg)](https://ollama.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**A private, local, and intelligent assistant for your codebase.**  
Ask natural language questions about your code, documentation, and PDFs – and get accurate, context‑aware answers with conversation memory.

---

## ✨ What is CodeSarthi?

CodeSarthi is an AI‑powered tool that ingests your entire code repository – including source files, READMEs, markdown docs, and PDFs – and lets you query it in plain English.  
It uses a local Large Language Model (Llama 3.2 via Ollama) for complete privacy, **no cloud API costs**, and runs entirely on your machine.

Whether you’re a new developer trying to understand a large project, or a senior dev who needs quick answers without digging through files, CodeSarthi is your instant code companion.

---

## 🚀 Key Features

- 🔐 **Multi‑user login** – Isolated conversations per user (SQLite authentication)
- 📚 **Full codebase ingestion** – Supports `.py`, `.md`, `.pdf`, and more (extensible)
- 🧠 **Semantic search** – Uses embeddings and a vector database (Chroma) to find the most relevant code/documentation chunks
- 💬 **Conversational memory** – Remembers the context of your conversation across multiple turns
- ⚡ **Streaming responses** – Real‑time word‑by‑word output, just like ChatGPT
- 🔍 **Observability** – Optional integration with LangSmith to trace every step
- 🛡️ **100% local** – Your code never leaves your machine; no internet required after setup

---

## 🧱 How It Works

```mermaid
graph TD
    A[User] -->|Ask question| B(Streamlit UI)
    B --> C{Login / Session}
    C --> D[RetrievalQA Chain]
    D --> E[(Chroma Vector DB)]
    E -->|Top‑k chunks| D
    D --> F[Ollama Llama 3.2]
    F -->|Stream answer| B
    D --> G[(SQLite History)]
    G -->|Inject previous turns| D
```

1. **Ingestion (one‑time):** All files in `repo/` and `data/` are split into chunks, embedded with Ollama, and stored in a local Chroma database.
2. **Query:** Your question is embedded and used to find the most relevant chunks via similarity search.
3. **Augmentation:** Those chunks are injected into a prompt together with the conversation history.
4. **Generation:** The LLM (Llama 3.2) streams the answer back to the UI.
5. **Memory:** Every exchange is saved to SQLite and reused in future interactions.

---

## 🛠️ Tech Stack

- **LangChain** – Orchestration, RAG, memory, and chains
- **Ollama** – Local LLM (Llama 3.2) and embeddings
- **ChromaDB** – Vector database for similarity search
- **Streamlit** – Interactive web UI
- **SQLite** – User accounts and chat history persistence
- **PyPDF / Unstructured** – Document parsing
- **LangSmith** – Optional observability

---

## 📋 Prerequisites

Before you begin, make sure you have:

- Python 3.10 or higher
- [Ollama](https://ollama.com/) installed and running in the background
- Git (optional, for cloning)

---

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/codesarthi.git
cd codesarthi
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Pull the local LLM
Make sure Ollama is running (`ollama serve` in another terminal). Then:
```bash
ollama pull llama3.2
```

### 5. (Optional) Set up LangSmith tracing
Create a `.env` file from the example:
```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=ls__your_key_here
LANGCHAIN_PROJECT=codesarthi
```
You can skip this – the app will still work without it.

### 6. Prepare your codebase
Place your source files, READMEs, and PDFs in the `repo/` folder.  
The sample project already contains a few files for testing.

### 7. Ingest the data
This step creates the vector database (takes a few minutes on first run):
```bash
python ingest.py
```
You should see messages like `Loaded X pages`, `Created Y chunks`, `Vector store created`.

### 8. Run the assistant
```bash
streamlit run app.py
```
Open your browser at http://localhost:8501.

---

## 🧪 Sample Queries

Once the app is running, you can ask questions like:

- “How does the authentication flow work?”
- “What is the purpose of `user_service.py`?”
- “Explain the password hashing function.”
- “List the coding standards from the PDF.”
- “What does the function `hash_password` do?”

The assistant will answer using the content from your repository.

---

## 📁 Project Structure

```
codesarthi/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── auth_db.py
├── ingest.py
├── app.py
├── repo/
│   ├── README.md
│   ├── auth.py
│   └── user_service.py
├── data/
│   └── sample.pdf
├── chroma_code/
└── users.db
```

### 🗂️ File & Folder Breakdown

**`.env`**  
Yahan tumhare secret keys aur environment variables store hote hain – jaise LangSmith API key, tracing endpoint, aur project name. Ye file kabhi bhi GitHub pe push nahi karni chahiye. Agar LangSmith use nahi karna, toh ye file optional hai – app bina iske bhi chalega.

**`.gitignore`**  
Ye file Git ko batati hai ki kaunse folders aur files ko ignore karna hai jab tum code push karo. Isme `venv/`, `chroma_code/`, `.env`, aur `users.db` listed hote hain – kyunki ye sab ya toh sensitive hain ya locally generate hote hain, inhe repo mein nahi rakhna chahiye.

**`requirements.txt`**  
Is file mein saare Python packages listed hain jo is project ko chalane ke liye chahiye – jaise `langchain`, `chromadb`, `streamlit`, `pypdf`, etc. Koi bhi naya developer sirf `pip install -r requirements.txt` run karke poora environment set up kar sakta hai.

**`README.md`**  
Ye wahi file hai jo tum abhi padh rahe ho. Isme project ka overview, setup steps, sample queries, aur project structure explain kiya gaya hai. Ye kisi bhi naye developer ke liye pehla stop hona chahiye.

**`auth_db.py`**  
Is file mein user authentication ka poora logic hai. Ye SQLite database use karke users ke accounts manage karta hai – signup, login, aur password hashing sab yahan hota hai. Har user ka ek alag session hota hai taaki conversations mix na hon.

**`ingest.py`**  
Ye sabse pehle run karne wali file hai – ek baar setup ke time. Ye `repo/` aur `data/` folders ke saare files ko load karta hai, unhe chhote-chhote chunks mein todta hai, har chunk ka embedding banata hai (Ollama se), aur sab kuch Chroma vector database mein save kar deta hai. Jab tak ye nahi chalega, assistant ke paas koi knowledge nahi hogi.

**`app.py`**  
Ye main Streamlit application file hai jo browser mein UI render karti hai. Isme login form, chat interface, streaming responses, aur "New Thread" reset button sab kuch hai. Ye `auth_db.py` se user verify karta hai aur Chroma DB se answers retrieve karta hai.

---

**`repo/` folder**  
Yahan tumhara actual codebase jaata hai – jo bhi files tum assistant ko samjhana chahte ho. By default kuch sample files hain:

- **`repo/README.md`** – Sample project ka overview document. Assistant isse padh ke project ke baare mein high-level questions answer kar sakta hai.
- **`repo/auth.py`** – Ek sample authentication module jisme login, logout, aur token validation ka code hai. Assistant isse padh ke "How does login work?" jaisi queries handle karta hai.
- **`repo/user_service.py`** – Ek sample service file jisme user creation, fetching, aur password hashing ka logic hai. Assistant isse use karke user-related questions answer karta hai.

> 💡 Tum apni khud ki files yahan rakh sakte ho – `.py`, `.md`, ya koi bhi text-based file. `ingest.py` dobara run karo aur assistant tumhari nayi files bhi samjhega.

---

**`data/` folder**  
Yahan additional PDF documents rakh sakte ho – jaise coding standards, architecture docs, onboarding guides, ya koi bhi internal documentation.

- **`data/sample.pdf`** – Ek example PDF file jo demonstrate karta hai ki assistant PDF content se bhi answers de sakta hai.

> 💡 Koi bhi PDF yahan daalo, `ingest.py` run karo – assistant usse bhi padh lega.

---

**`chroma_code/` folder** *(auto-generated, gitignored)*  
Ye folder `ingest.py` run karne ke baad automatically banta hai. Isme saare document chunks ke vector embeddings stored hote hain. Ye tumhara local vector database hai – isko manually edit ya delete mat karo. Agar dobara ingest karna ho toh pehle is folder ko delete karo, phir `ingest.py` run karo.

**`users.db`** *(auto-generated, gitignored)*  
Ye SQLite database file app pehli baar run hone par automatically banti hai. Isme registered users ke credentials aur unki chat history store hoti hai. Har user ka conversation alag-alag save hota hai taaki ek user doosre ki history na dekh sake.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- Built with [LangChain](https://python.langchain.com/)
- Powered by [Ollama](https://ollama.com/) and [Llama 3.2](https://ollama.com/library/llama3.2)
- UI by [Streamlit](https://streamlit.io/)
- Vector database by [Chroma](https://www.trychroma.com/)

---

**Happy coding!** 🚀
```