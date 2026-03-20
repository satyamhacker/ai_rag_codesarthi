
---

## 🧩 **Module 1: Base Camp Setup – Apna Kitchen Taiyar Kar**  
*(Installation & Prerequisites)*

**Level 1.1: Virtual Environment – Alag Kitchen**

1. **Task:** Folder `codesarthi/` banao. Usme virtual environment `venv` create karo aur activate karo.  
2. **Logic:** Python projects ke liye isolation zaroori hai – dependencies clash na karein.  
3. **Definition of Done:** Terminal prompt me `(venv)` dikhe.

**Level 1.2: Dependencies – LangChain, Streamlit, Jupyter, aur Saathi**

1. **Task:** `requirements.txt` file banao aur usme saari libraries likho: `langchain`, `langchain-community`, `langchain-chroma`, `langchain-ollama`, `python-dotenv`, `streamlit`, `pypdf`, `unstructured`, `chromadb`, `jupyter`. Phir `pip install -r requirements.txt` chalao.  
2. **Logic:** Modular installs keep environment light. `langchain-ollama` specifically Ollama integration ke liye chahiye. `jupyter` interactive development ke liye.  
3. **Definition of Done:** `pip list` mein saari packages dikhein.

**Level 1.3: Ollama – Local LLM Ka Engine**

1. **Task:** Ollama install karo (https://ollama.com/), background service start karo (`ollama serve` ek alag terminal mein). `ollama pull mistral:7b` chalao. Terminal mein `ollama run mistral:7b` se test karo: "What is a Python decorator?".  
2. **Logic:** Ollama runs the LLM locally – no cloud dependency. Ye hamesha background mein chalna chahiye.  
3. **Definition of Done:** Model answer de aur Ollama service running rahe.

**Level 1.4: .gitignore – Sensitive Files Ko Chhupao**

1. **Task:** `.gitignore` file banao aur inhe add karo: `venv/`, `.env`, `chroma_code/`, `users.db`, `code_history.db`, `__pycache__/`, `*.pyc`, `.ipynb_checkpoints/`.  
2. **Logic:** Ye files ya toh sensitive hain (`.env`, `users.db`) ya locally generate hoti hain – inhe repo mein nahi rakhna chahiye. `.ipynb_checkpoints/` Jupyter ke temporary files hain.  
3. **Definition of Done:** `git status` mein ye files ignored dikhein.

**Level 1.5: LangSmith – CCTV Lagao (Optional)**

1. **Task:** `.env` file banao. Usme `LANGCHAIN_TRACING_V2=true`, `LANGCHAIN_ENDPOINT=https://api.smith.langchain.com`, `LANGCHAIN_API_KEY=ls__your_key_here`, `LANGCHAIN_PROJECT=codesarthi` daalo.  
2. **Logic:** Har LLM call trace hoti hai – debugging aasan. Ye optional hai – app bina iske bhi chalega.  
3. **Definition of Done:** Baad mein Jupyter notebooks run karne par LangSmith dashboard pe traces dikhe (agar setup kiya).

**🔥 COMBO TASK (Level 1.6):**  
1. **Task:** Ek Jupyter Notebook `test_env.ipynb` banao. Isme cells likho:
   - Cell 1: `from langchain_community.llms import ChatOllama` import karo
   - Cell 2: `llm = ChatOllama(model="mistral:7b")` instantiate karo
   - Cell 3: `response = llm.invoke("What is a unit test?")` invoke karo
   - Cell 4: `print(response)` print karo
   Notebook run karo aur output dekho.  
2. **Logic:** Sab components ek saath kaam kar rahe hain ya nahi verify karo – Ollama, LangChain, Python environment, Jupyter.  
3. **Definition of Done:** Notebook mein answer aaye; LangSmith trace dikhe (agar setup kiya).

**Practical Takeaway:**  
- Keywords: `virtual environment`, `pip install`, `ollama serve`, `ollama pull`, `.gitignore`, `.env`, `jupyter notebook`, `LANGCHAIN_TRACING_V2`.  
- Why: Ye foundation hai – bina iske kuch bhi nahi chalega.

---

## 🧩 **Module 2: User Authentication – Har User Ka Apna Kamra**  
*(User Management & Database Setup)*

**Level 2.1: Sample Data Taiyar Kar**

1. **Task:** `repo/` folder banao. Usme teen files daalo:  
   - `README.md` – kuch bhi 1-2 paragraph (project overview)  
   - `auth.py` – Python file jisme login/logout functions ke comments aur docstrings hon  
   - `user_service.py` – user create, fetch, password hash ke functions  
   - `pdf_file/` folder banao aur usme `mysql_cheatsheet.pdf` daalo (MySQL commands ka reference guide)  
2. **Logic:** Yehi files assistant ki "knowledge" banegi – code files se code questions, PDF se MySQL questions.  
3. **Definition of Done:** `repo/` mein 3 files aur `pdf_file/` mein `mysql_cheatsheet.pdf`.

**Level 2.2: Auth DB – SQLite Mein Users**

1. **Task:** `auth_db.py` file banao. Isme teen functions implement karo:  
   - `init_db()` – Database initialize karo – `users` table banao with columns: `id`, `email`, `password` (hashed)  
   - `register_user(email, password)` – password ko `hashlib.sha256` se hash karo, insert karo  
   - `verify_user(email, password)` – email aur password check karo, match pe user ID return karo, mismatch pe None  
2. **Logic:** SQLite local hai, passwords store mat karo plain mein. Hashing ensures security.  
3. **Definition of Done:** Script run karo, ek test user register karo, login verify karo – `users.db` file ban jaaye.

**🔥 COMBO TASK (Level 2.3):**  
1. **Task:** Ek Jupyter Notebook `auth_test.ipynb` banao. Isme cells likho:
   - Cell 1: `from auth_db import init_db, register_user, verify_user` import karo
   - Cell 2: `init_db()` call karo
   - Cell 3: `register_user("test@example.com", "password123")` call karo
   - Cell 4: `result = verify_user("test@example.com", "password123")` call karo aur print karo
   - Cell 5: `result = verify_user("test@example.com", "wrongpassword")` call karo aur print karo
   Notebook run karo aur verify karo.  
2. **Logic:** Verify that hashing and DB operations work correctly.  
3. **Definition of Done:** Correct password pe user ID return ho, wrong pe None return ho.

**Practical Takeaway:**  
- Keywords: `sqlite3`, `hashlib.sha256`, `INSERT`, `SELECT`, `CREATE TABLE`, `jupyter notebook`.  
- Why: Multi‑user support ke liye user isolation zaroori hai.

---

## 🧩 **Module 3: Data Ingestion – Codebase Ko Samajhna**  
*(Vector Database Creation & Embedding)*

**Level 3.1: Files Load Karo**

1. **Task:** Ek Jupyter Notebook `ingest.ipynb` banao. Isme cells likho:
   - Cell 1: Imports – `DirectoryLoader`, `PyPDFLoader`, `RecursiveCharacterTextSplitter`, `OllamaEmbeddings`, `Chroma`
   - Cell 2: Load markdown files from `repo/` using `DirectoryLoader` with `glob="**/*.md"`
   - Cell 3: Load Python files from `repo/` using `DirectoryLoader` with `glob="**/*.py"`
   - Cell 4: Load PDF from `pdf_file/mysql_cheatsheet.pdf` using `PyPDFLoader`
   - Cell 5: Combine all documents in a list aur print total count
   Notebook run karo.  
2. **Logic:** Different loaders for different file types. This is the first step of RAG.  
3. **Definition of Done:** Print total documents loaded – count should match files (3 from repo + 1 PDF).

**Level 3.2: Chunks Banao**

1. **Task:** `ingest.ipynb` mein naya cell likho:
   - Cell 6: `RecursiveCharacterTextSplitter` use karo with `chunk_size=1500`, `chunk_overlap=200`
   - Cell 7: Saari documents ko split karo aur chunks list banao
   - Cell 8: Print chunk count
   Notebook run karo.  
2. **Logic:** Overlap ensures context continuity between chunks. Smaller chunks = better retrieval accuracy.  
3. **Definition of Done:** Number of chunks > original document count. Print chunk count.

**Level 3.3: Embeddings Banao**

1. **Task:** `ingest.ipynb` mein naya cell likho:
   - Cell 9: `OllamaEmbeddings` with `model="mistral:7b"` instantiate karo
   - Cell 10: Ek sample chunk ka vector generate karo
   - Cell 11: Vector length print karo
   Notebook run karo.  
2. **Logic:** Embeddings capture code semantics – similar code chunks will have similar vectors.  
3. **Definition of Done:** Vector length constant (e.g., 3072). Verify embedding works without errors.

**Level 3.4: Chroma DB Mein Save Karo**

1. **Task:** `ingest.ipynb` mein naya cell likho:
   - Cell 12: `Chroma.from_documents` use karo – pass chunks, embeddings, `persist_directory="./chroma_code"`, collection name `"code_knowledge"`
   - Cell 13: Print success message
   Notebook run karo.  
2. **Logic:** Vector store disk par persist hota hai – isse baad mein quickly load kar sakte ho.  
3. **Definition of Done:** `chroma_code/` folder ban jaaye with vector data inside.

**🔥 COMBO TASK (Level 3.5):**  
1. **Task:** `ingest.ipynb` mein naya cell likho:
   - Cell 14: Load the persisted DB back using `Chroma` constructor with same `persist_directory`
   - Cell 15: Create retriever with `search_kwargs={"k": 3}`
   - Cell 16: Perform similarity search – `"how does authentication work?"`
   - Cell 17: Print top 3 chunks with source file names
   - Cell 18: Perform similarity search – `"how to use JOIN in MySQL?"`
   - Cell 19: Print top 3 chunks with source file names
   Notebook run karo.  
2. **Logic:** Verify that both code and PDF retrieval works correctly.  
3. **Definition of Done:** Retrieved chunks contain relevant content from respective sources. Source documents clearly show which file they came from.

**Practical Takeaway:**  
- Keywords: `DirectoryLoader`, `PyPDFLoader`, `RecursiveCharacterTextSplitter`, `OllamaEmbeddings`, `Chroma.from_documents`, `similarity_search`, `jupyter notebook`.  
- Why: Without ingestion, assistant has no knowledge. This is the foundation of RAG.

---

## 🧩 **Module 4: RAG Chain – Assistant Ka Brain**  
*(Retrieval-Augmented Generation Setup)*

**Level 4.1: Vector DB Load Karo**

1. **Task:** Ek Jupyter Notebook `rag_chain_test.ipynb` banao. Isme cells likho:
   - Cell 1: Imports – `Chroma`, `OllamaEmbeddings`, `ChatOllama`, `RetrievalQA`
   - Cell 2: Load Chroma DB using `persist_directory="./chroma_code"` and same embedding model
   - Cell 3: Print collection count to verify
   Notebook run karo.  
2. **Logic:** DB already built from ingest.ipynb, just connect to it.  
3. **Definition of Done:** DB object loads without error. Verify by checking collection count.

**Level 4.2: Retriever Banao**

1. **Task:** `rag_chain_test.ipynb` mein naya cell likho:
   - Cell 4: `.as_retriever(search_kwargs={"k": 3})` use karo
   - Cell 5: Test retriever with a sample query
   Notebook run karo.  
2. **Logic:** Retriever is the bridge between user query and vector DB.  
3. **Definition of Done:** Retriever object ban jaaye. Test with a sample query.

**Level 4.3: LLM Connect Karo**

1. **Task:** `rag_chain_test.ipynb` mein naya cell likho:
   - Cell 6: `ChatOllama` with model `"mistral:7b"` instantiate karo
   - Cell 7: `llm.invoke("test")` call karo aur output print karo
   Notebook run karo.  
2. **Logic:** Local LLM engine – ye actual answers generate karega.  
3. **Definition of Done:** `llm.invoke("test")` works without error.

**Level 4.4: RetrievalQA Chain Banao**

1. **Task:** `rag_chain_test.ipynb` mein naya cell likho:
   - Cell 8: `RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)` use karo
   - Cell 9: Print chain object
   Notebook run karo.  
2. **Logic:** This chain automatically retrieves context and generates answer. `return_source_documents=True` ensures we know which files were used.  
3. **Definition of Done:** Chain object ready. Test with hardcoded query.

**🔥 COMBO TASK (Level 4.5):**  
1. **Task:** `rag_chain_test.ipynb` mein naya cell likho:
   - Cell 10: `qa_chain.invoke({"query": "What does auth.py do?"})` call karo
   - Cell 11: Print answer aur source documents
   - Cell 12: `qa_chain.invoke({"query": "What is the syntax for SELECT in MySQL?"})` call karo
   - Cell 13: Print answer aur source documents
   Notebook run karo.  
2. **Logic:** Verify RAG works for both code and PDF sources.  
3. **Definition of Done:** Answers based on correct source files. Source documents clearly show which file was used.

**Practical Takeaway:**  
- Keywords: `Chroma`, `as_retriever`, `RetrievalQA.from_chain_type`, `return_source_documents`, `ChatOllama`, `jupyter notebook`.  
- Why: RAG is the core of the assistant – it combines retrieval + generation.

---

## 🧩 **Module 5: Chat UI – Jadoo Ki Jhappi**  
*(Streamlit Interface & User Interaction)*

**Level 5.1: Login + Signup Form**

1. **Task:** `app.py` mein Streamlit app start karo. Agar user logged in nahi hai, do tabs dikhao – **Login** aur **Sign Up**:  
   - Login tab: email + password input fields → `auth_db.py` ke `verify_user()` function se check karo → success/failure message  
   - Sign Up tab: email + password input fields → `auth_db.py` ke `register_user()` function se naya user banao → success/failure message  
2. **Logic:** Session state tracks login. Naye users bina manual DB entry ke register ho sakein.  
3. **Definition of Done:** Naya user signup kar sake, existing user login kar sake, "Welcome [email]" message aaye.

**Level 5.2: Chat Interface**

1. **Task:** Login ke baad `st.chat_input("Ask me anything...")` use karo. User messages ko `st.session_state.messages` list mein store karo with structure: `{"role": "user", "content": text}`. Loop through list aur each message ko `st.chat_message(role)` se display karo.  
2. **Logic:** Builds the visual conversation history.  
3. **Definition of Done:** Type karo, message appear ho. Previous messages visible rahen.

**Level 5.3: RAG Integration**

1. **Task:** Jab user message bheje, call the RetrievalQA chain with the user's query. Display the answer using `st.chat_message("assistant")`. Store assistant response in `st.session_state.messages` too.  
2. **Logic:** Assistant answers using codebase and PDF.  
3. **Definition of Done:** "How do I use GROUP BY in MySQL?" puchho – answer from PDF aaye. Source documents visible.

**Level 5.4: Source Documents Display**

1. **Task:** RetrievalQA chain se `source_documents` extract karo. Ek expandable section mein show karo – "📚 Sources Used" – jisme file names aur relevant chunks dikhein.  
2. **Logic:** Transparency – user ko pata chale ki answer kahan se aaya.  
3. **Definition of Done:** Sources section visible with file names and chunk previews.

**🔥 COMBO TASK (Level 5.5):**  
1. **Task:** Chat UI complete karo – signup/login, chat input, RAG answer display, source documents. Test with both a code question and a MySQL question.  
2. **Logic:** Basic working chatbot.  
3. **Definition of Done:** Answer appears, sources visible, no errors.

**Practical Takeaway:**  
- Keywords: `st.session_state`, `st.chat_input`, `st.chat_message`, `st.tabs`, `st.expander`, `streamlit`.  
- Why: UI makes the assistant usable and transparent.

---

## 🧩 **Module 6: Memory – Ghajini Se Genie Tak**  
*(Conversation History & Context Persistence)*

**Level 6.1: SQLite History Setup**

1. **Task:** `get_session_history(session_id)` function banao jo `SQLChatMessageHistory` return kare with connection string `sqlite:///code_history.db`. Ye function session_id ke basis par history retrieve karega.  
2. **Logic:** Messages will persist across app restarts.  
3. **Definition of Done:** File `code_history.db` create ho. Function callable ho.

**Level 6.2: History Wrapper Lagao**

1. **Task:** Apni RAG chain ko `RunnableWithMessageHistory` mein wrap karo. Pass:  
   - `get_session_history` function  
   - `input_messages_key="query"`  
   - `history_messages_key="history"`  
2. **Logic:** Wrapper automatically injects past messages into the prompt.  
3. **Definition of Done:** Chain object now stateful. Test with multi-turn conversation.

**Level 6.3: Session ID Management**

1. **Task:** Har logged-in user ke liye unique `session_id` generate karo (e.g., `f"{user_email}_{timestamp}"` or just `user_email`). Ye session_id `st.session_state` mein store karo.  
2. **Logic:** Each user's history isolated.  
3. **Definition of Done:** Different users have different session IDs.

**Level 6.4: Multi‑Turn Test**

1. **Task:** Ek Jupyter Notebook `memory_test.ipynb` banao. Isme cells likho:
   - Cell 1: Imports aur setup
   - Cell 2: User se do questions puchho jo pehle wale par depend karte hain (e.g., "What is a MySQL JOIN?" then "Can you show me an example of LEFT JOIN?")
   - Cell 3: Verify ki second answer mentions "LEFT JOIN" specifically
   Notebook run karo.  
2. **Logic:** Second answer should reference first question's context.  
3. **Definition of Done:** Context preserved. Second answer mentions "LEFT JOIN" specifically.

**🔥 COMBO TASK (Level 6.5):**  
1. **Task:** Simulate a full conversation (3 turns) in Jupyter, stop app, restart, login again – ask a follow‑up question. Bot should remember previous conversation. Check SQLite DB to see stored messages.  
2. **Logic:** Persistence works across restarts.  
3. **Definition of Done:** Memory works across restarts. `code_history.db` contains all messages.

**Practical Takeaway:**  
- Keywords: `RunnableWithMessageHistory`, `SQLChatMessageHistory`, `session_id`, `get_session_history`, `jupyter notebook`.  
- Why: Memory is essential for natural conversations.

---

## 🧩 **Module 7: Streaming + Reset – Pro Level UX**  
*(Real-time Response & Session Management)*

**Level 7.1: Streaming Responses**

1. **Task:** Replace static answer with streaming. Use `st.write_stream()` inside the assistant's chat message. Iterate over `chain.stream({"query": user_query, "session_id": session_id})` and yield chunks.  
2. **Logic:** Real‑time typing effect – user sees answer appearing word by word.  
3. **Definition of Done:** Answer appears word by word, not all at once.

**Level 7.2: Reset Button – Naya Thread**

1. **Task:** Sidebar mein "🔄 New Thread" button daalo. On click:  
   - Clear `st.session_state.messages` (UI history)  
   - Call `get_session_history(session_id).clear()` to wipe SQLite history for that user  
   - Show "Thread cleared! Start fresh." message  
2. **Logic:** UI and backend both cleared.  
3. **Definition of Done:** After click, chat history gone, bot forgets. New conversation starts fresh.

**Level 7.3: Logout Button**

1. **Task:** Sidebar mein "🚪 Logout" button daalo. On click:  
   - Clear `st.session_state.user_email` aur `st.session_state.session_id`  
   - Rerun app (Streamlit automatically shows login form)  
2. **Logic:** User session ends.  
3. **Definition of Done:** After logout, login form appears again.

**🔥 COMBO TASK (Level 7.4):**  
1. **Task:** Test streaming + reset together. Start a conversation, use reset, ask a new question – bot should behave as if fresh. Then logout and login as different user – verify isolation.  
2. **Logic:** Full UX polish.  
3. **Definition of Done:** Streaming smooth, reset works, logout works, user isolation verified.

**Practical Takeaway:**  
- Keywords: `st.write_stream`, `.stream()`, `.clear()`, `st.session_state`, `st.sidebar`, `streamlit`.  
- Why: Streaming and reset are standard in modern chatbots.

---

## 🧩 **Module 8: Final Integration – CodeSarthi Zinda Hai**  
*(End-to-End Testing & Validation)*

**Level 8.1: End‑to‑End Test – Multi‑User**

1. **Task:** Two different users signup and login (different emails). Each asks separate questions. Verify conversations are isolated.  
2. **Logic:** Each user's session_id different → different history in SQLite.  
3. **Definition of Done:** Users don't see each other's history. Each user's chat is private.

**Level 8.2: Memory & RAG Combined**

1. **Task:** Single user, ask a question that requires both memory and codebase knowledge (e.g., first ask "What does auth.py do?" then ask "How does it handle password hashing?").  
2. **Logic:** RAG provides code facts, memory provides context from first question.  
3. **Definition of Done:** Second answer uses first context and codebase. Answer mentions "auth.py" from first question.

**Level 8.3: PDF Query Test – MySQL Cheatsheet**

1. **Task:** Ask MySQL-related questions from `pdf_file/mysql_cheatsheet.pdf`:  
   - "What is the syntax for a SELECT statement in MySQL?"  
   - "How do I use JOIN in MySQL?"  
   - "What are the different MySQL data types?"  
2. **Logic:** PDF should be ingested and retrievable.  
3. **Definition of Done:** Answers come from `mysql_cheatsheet.pdf` content, source document shows the PDF file.

**Level 8.4: Code Query Test – Repository**

1. **Task:** Ask code-related questions from `repo/`:  
   - "What does auth.py do?"  
   - "What is the purpose of user_service.py?"  
   - "Explain the password hashing function."  
2. **Logic:** Code files should be ingested and retrievable.  
3. **Definition of Done:** Answers come from code files, source documents show correct file names.

**Level 8.5: Project Structure Verify Karo**

1. **Task:** Final project structure check karo – ensure ye sab files/folders exist hain:  
   ```
   codesarthi/
   ├── .env                  ← LangSmith keys (optional, gitignored)
   ├── .gitignore
   ├── requirements.txt
   ├── README.md
   ├── app.py                ← Main Streamlit app
   ├── auth_db.py            ← User signup, login, password hashing
   ├── ingest.ipynb          ← Data ingestion notebook
   ├── test_env.ipynb        ← Environment testing notebook
   ├── rag_chain_test.ipynb  ← RAG chain testing notebook
   ├── auth_test.ipynb       ← Authentication testing notebook
   ├── memory_test.ipynb     ← Memory testing notebook
   ├── repo/                 ← Your codebase goes here
   │   ├── README.md
   │   ├── auth.py
   │   └── user_service.py
   ├── pdf_file/             ← PDF documents go here
   │   └── mysql_cheatsheet.pdf
   ├── chroma_code/          ← auto-generated, gitignored
   ├── users.db              ← auto-generated, gitignored
   └── code_history.db       ← auto-generated, gitignored
   ```
2. **Logic:** README mein defined structure se match karna zaroori hai.  
3. **Definition of Done:** Sab files present, `chroma_code/`, `users.db`, `code_history.db`, `.ipynb_checkpoints/` gitignored.

**🔥 COMBO TASK (Level 8.6):**  
1. **Task:** Run all features together in sequence:  
   - Run `ingest.ipynb` → Run `test_env.ipynb` → Run `auth_test.ipynb` → Run `rag_chain_test.ipynb` → Run `memory_test.ipynb` → Signup → Login → multi‑turn RAG conversation (code + PDF) → MySQL PDF query → reset → new conversation → streaming test → logout → login as different user → verify isolation → check LangSmith traces (if setup).  
2. **Logic:** Full system validation.  
3. **Definition of Done:** All features work, no errors, traces visible, user isolation verified.

**Practical Takeaway:**  
- Keywords: Full architecture – RAG + Memory + UI + Observability + Multi-user + Jupyter Notebooks.  
- Why: This is exactly how enterprise assistants are built.

---

## 🏁 **MODULE 8 RECAP (Tera Status Report)**  

**Siksha Summary:**  
You built a complete production‑ready **codebase assistant** that:  
- ✅ Uses local LLM (Ollama + mistral:7b) for privacy  
- ✅ Ingests code files (`repo/`) and PDF documents (`pdf_file/mysql_cheatsheet.pdf`)  
- ✅ Chunks, embeds, stores in Chroma vector database  
- ✅ Retrieves semantically relevant context from both code and PDF  
- ✅ Maintains conversation memory per user (SQLite)  
- ✅ Provides a chat UI with streaming and reset  
- ✅ Includes multi‑user signup/login and isolated sessions  
- ✅ Uses LangSmith for full observability (optional)  
- ✅ Proper `.gitignore` for sensitive files  
- ✅ Shows source documents for transparency  
- ✅ Uses Jupyter Notebooks for interactive development and testing  

**Guru-ji's Warning:**  
*"Check kar le bhai! Kya tujhe yeh sab bina chat sheet ke karna aa gaya hai?  
- Virtual environment bana sakta hai?  
- Ollama background service ki tarah chalana?  
- `.gitignore` properly set karna?  
- Sample files structure set karna (`repo/` aur `pdf_file/`)?  
- auth_db.py mein hashed passwords store karna aur signup implement karna?  
- `ingest.ipynb` se files load, chunk, embed, DB store karna (code + PDF dono)?  
- `test_env.ipynb` se environment verify karna?  
- `auth_test.ipynb` se authentication test karna?  
- `rag_chain_test.ipynb` se RAG chain test karna?  
- `memory_test.ipynb` se memory test karna?  
- Streamlit signup/login aur chat UI banana?  
- Source documents display karna?  
- RunnableWithMessageHistory se memory add karna?  
- Streaming aur reset implement karna?  
- Logout button add karna?  
- Multi‑user isolation test karna?  
- MySQL PDF se questions answer ho rahe hain?  
- Code files se questions answer ho rahe hain?  
- Final project structure README se match karna?  

Agar inme se ek bhi cheez mein doubt hai ya confuse hai, toh chup chaap peeche ja aur wapas execute kar. Aage badhne ka koi fayda nahi agar basics hile hue hain!"*

---

⚡ **GURUDAKSHINA (The Checkpoint):**  
**Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type 'CONTINUE' for the next set of missions – yani tujhe kuch aur nahi, tu ab apne man se koi bhi code repository le ke ye app bana sakta hai. Aage kya karna hai? Feedback de, ya naye features add kar.**
