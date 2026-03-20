
---

## 🧩 **Module 1: Base Camp Setup – Apna Kitchen Taiyar Kar**  
*(Steps 1–3 from roadmap)*

**Level 1.1: Virtual Environment – Alag Kitchen**

1. **Task:** Folder `codesarthi/` banao. Usme virtual environment `venv` create karo aur activate karo.  
2. **Logic:** Python projects ke liye isolation zaroori hai – dependencies clash na karein.  
3. **Definition of Done:** Terminal prompt me `(venv)` dikhe.

**Level 1.2: Dependencies – LangChain, Streamlit, aur Saathi**

1. **Task:** `requirements.txt` file banao aur usme saari libraries likho: `langchain`, `langchain-community`, `langchain-chroma`, `langchain-ollama`, `python-dotenv`, `streamlit`, `pypdf`, `unstructured`, `chromadb`. Phir `pip install -r requirements.txt` chalao.  
2. **Logic:** Modular installs keep environment light. `langchain-ollama` specifically Ollama integration ke liye chahiye.  
3. **Definition of Done:** `pip list` mein saari packages dikhein.

**Level 1.3: Ollama – Local LLM Ka Engine**

1. **Task:** Ollama install karo, background service start karo (`ollama serve`). `ollama pull mistral:7b` chalao. Terminal mein `ollama run mistral:7b` se test karo: "What is a Python decorator?".  
2. **Logic:** Ollama runs the LLM locally – no cloud dependency.  
3. **Definition of Done:** Model answer de.

**Level 1.4: .gitignore – Sensitive Files Ko Chhupao**

1. **Task:** `.gitignore` file banao aur inhe add karo: `venv/`, `.env`, `chroma_code/`, `users.db`, `code_history.db`, `__pycache__/`, `*.pyc`.  
2. **Logic:** Ye files ya toh sensitive hain (`.env`, `users.db`) ya locally generate hoti hain – inhe repo mein nahi rakhna chahiye.  
3. **Definition of Done:** `git status` mein ye files ignored dikhein.

**Level 1.5: LangSmith – CCTV Lagao (Optional)**

1. **Task:** `.env` file banao. Usme `LANGCHAIN_TRACING_V2=true`, `LANGCHAIN_ENDPOINT`, `LANGCHAIN_API_KEY`, `LANGCHAIN_PROJECT=codesarthi` daalo.  
2. **Logic:** Har LLM call trace hoti hai – debugging aasan.  
3. **Definition of Done:** Baad mein `app.py` run karne par LangSmith dashboard pe traces dikhe.

**🔥 COMBO TASK (Level 1.6):**  
1. **Task:** Ek chhota Python script (e.g., `test_env.py`) banao jo `ChatOllama` import kare, `mistral:7b` se invoke kare "What is a unit test?", aur response print kare. Script run karo.  
2. **Logic:** Sab components ek saath kaam kar rahe hain ya nahi verify karo.  
3. **Definition of Done:** Terminal pe answer aaye; LangSmith trace dikhe (agar setup kiya).

**Practical Takeaway:**  
- Keywords: `virtual environment`, `pip install`, `ollama serve`, `ollama pull`, `.gitignore`, `.env`, `LANGCHAIN_TRACING_V2`.  
- Why: Ye foundation hai – bina iske kuch bhi nahi chalega.

---

## 🧩 **Module 2: User Authentication – Har User Ka Apna Kamra**  
*(Steps 4–5 from roadmap)*

**Level 2.1: Sample Data Taiyar Kar**

1. **Task:** `repo/` folder banao. Usme teen files daalo:  
   - `README.md` – kuch bhi 1-2 paragraph (project overview)  
   - `auth.py` – Python file jisme login/logout functions ke comments aur docstrings hon  
   - `user_service.py` – user create, fetch, password hash ke functions  
   - `pdf_file/` folder banao aur usme `mysql_cheatsheet.pdf` daalo (MySQL commands ka reference guide)  
2. **Logic:** Yehi files assistant ki "knowledge" banegi – code files se code questions, PDF se MySQL questions.  
3. **Definition of Done:** `repo/` mein 3 files aur `pdf_file/` mein `mysql_cheatsheet.pdf`.

**Level 2.2: Auth DB – SQLite Mein Users**

1. **Task:** `auth_db.py` file banao. Isme teen cheezein implement karo:  
   - Database initialize karo – `users` table banao with `email`, `password` (hashed)  
   - User register karo – password ko hash karo, insert karo  
   - User verify karo – email aur password check karo, match pe user ID return karo  
2. **Logic:** SQLite local hai, passwords store mat karo plain mein.  
3. **Definition of Done:** Script run karo, ek test user register karo, login verify karo – `users.db` file ban jaaye.

**🔥 COMBO TASK (Level 2.3):**  
1. **Task:** `auth_db.py` ke functions ko use karke ek quick test script likho. Register a user, then try to login with correct and wrong password. Print messages for each.  
2. **Logic:** Verify that hashing and DB operations work.  
3. **Definition of Done:** Correct password pe success message, wrong pe failure.

**Practical Takeaway:**  
- Keywords: `sqlite3`, `hashlib.sha256`, `INSERT`, `SELECT`.  
- Why: Multi‑user support ke liye user isolation zaroori hai.

---

## 🧩 **Module 3: Data Ingestion – Codebase Ko Samajhna**  
*(Step 6 from roadmap)*

**Level 3.1: Files Load Karo**

1. **Task:** `ingest.py` banao. Pehle `repo/` aur `pdf_file/` se sab files load karo:  
   - Markdown files ke liye `DirectoryLoader` with `glob="**/*.md"`  
   - Python files ke liye `DirectoryLoader` with `glob="**/*.py"`  
   - PDF files ke liye `PyPDFLoader` – path: `pdf_file/mysql_cheatsheet.pdf`  
   - Saari files ek list mein collect karo.  
2. **Logic:** Different loaders for different file types.  
3. **Definition of Done:** Print total documents loaded – count should match files.

**Level 3.2: Chunks Banao**

1. **Task:** `RecursiveCharacterTextSplitter` use karo with `chunk_size=1500`, `chunk_overlap=200`. Saari documents ko split karo.  
2. **Logic:** Overlap ensures context continuity.  
3. **Definition of Done:** Number of chunks > original document count.

**Level 3.3: Embeddings Banao**

1. **Task:** `OllamaEmbeddings` with `mistral:7b` instantiate karo. Ek sample chunk ka vector generate karo aur length print karo.  
2. **Logic:** Embeddings capture code semantics.  
3. **Definition of Done:** Vector length constant (e.g., 3072).  

**Level 3.4: Chroma DB Mein Save Karo**

1. **Task:** `Chroma.from_documents` use karo – chunks, embeddings, `persist_directory="./chroma_code"`, collection name `"code_knowledge"`.  
2. **Logic:** Vector store disk par persist hota hai.  
3. **Definition of Done:** `chroma_code/` folder ban jaaye.

**🔥 COMBO TASK (Level 3.5):**  
1. **Task:** Load the persisted DB back (using `Chroma` constructor), perform two similarity searches:  
   - `"how does authentication work?"` – should return chunks from `auth.py`  
   - `"how to use JOIN in MySQL?"` – should return chunks from `mysql_cheatsheet.pdf`  
   Print top 3 chunks for each.  
2. **Logic:** Verify that both code and PDF retrieval works.  
3. **Definition of Done:** Retrieved chunks contain relevant content from respective sources.

**Practical Takeaway:**  
- Keywords: `DirectoryLoader`, `PyPDFLoader`, `RecursiveCharacterTextSplitter`, `OllamaEmbeddings`, `Chroma.from_documents`, `similarity_search`.  
- Why: Without ingestion, assistant has no knowledge.

---

## 🧩 **Module 4: RAG Chain – Assistant Ka Brain**  
*(Steps 8 from roadmap)*

**Level 4.1: Vector DB Load Karo**

1. **Task:** `app.py` mein (after login) Chroma DB load karo using `persist_directory="./chroma_code"` and same embedding model.  
2. **Logic:** DB already built, just connect.  
3. **Definition of Done:** DB object prints without error.

**Level 4.2: Retriever Banao**

1. **Task:** `.as_retriever(search_kwargs={"k": 3})` use karo.  
2. **Logic:** Retriever top 3 most relevant chunks lega.  
3. **Definition of Done:** Retriever object ban jaaye.

**Level 4.3: LLM Connect Karo**

1. **Task:** `Ollama` with model `mistral:7b` instantiate karo.  
2. **Logic:** Local LLM engine.  
3. **Definition of Done:** `llm.invoke("test")` works (optional test).

**Level 4.4: RetrievalQA Chain Banao**

1. **Task:** `RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)` use karo.  
2. **Logic:** This chain automatically retrieves context and generates answer.  
3. **Definition of Done:** Chain object ready.

**🔥 COMBO TASK (Level 4.5):**  
1. **Task:** Do hardcoded queries test karo:  
   - `qa_chain.invoke({"query": "What does auth.py do?"})` – answer from `repo/auth.py`  
   - `qa_chain.invoke({"query": "What is the syntax for SELECT in MySQL?"})` – answer from `pdf_file/mysql_cheatsheet.pdf`  
   Print answer and source documents for both.  
2. **Logic:** Verify RAG works for both code and PDF sources.  
3. **Definition of Done:** Answers based on correct source files.

**Practical Takeaway:**  
- Keywords: `Chroma`, `as_retriever`, `RetrievalQA.from_chain_type`, `return_source_documents`.  
- Why: RAG is the core of the assistant.

---

## 🧩 **Module 5: Chat UI – Jadoo Ki Jhappi**  
*(Steps 7, 9 from roadmap)*

**Level 5.1: Login + Signup Form**

1. **Task:** `app.py` mein Streamlit app start karo. Agar user logged in nahi hai, do tabs dikhao – **Login** aur **Sign Up**:  
   - Login tab: email + password → `auth_db.py` ke verify function se check karo  
   - Sign Up tab: email + password → `auth_db.py` ke register function se naya user banao  
2. **Logic:** Session state tracks login. Naye users bina manual DB entry ke register ho sakein.  
3. **Definition of Done:** Naya user signup kar sake, existing user login kar sake, "Welcome" message aaye.

**Level 5.2: Chat Interface**

1. **Task:** Login ke baad `st.chat_input` use karo. User messages ko `st.session_state.messages` list mein store karo (role: user, content: text). Loop through list aur each message ko `st.chat_message` se display karo.  
2. **Logic:** Builds the visual conversation.  
3. **Definition of Done:** Type karo, message appear ho.

**Level 5.3: RAG Integration**

1. **Task:** Jab user message bheje, call the RetrievalQA chain with the user's query. Display the answer using `st.chat_message` (assistant role).  
2. **Logic:** Assistant answers using codebase and PDF.  
3. **Definition of Done:** "How do I use GROUP BY in MySQL?" puchho – answer from PDF aaye.

**🔥 COMBO TASK (Level 5.4):**  
1. **Task:** Chat UI complete karo – signup/login, chat input, RAG answer display. Test with both a code question and a MySQL question.  
2. **Logic:** Basic working chatbot.  
3. **Definition of Done:** Answer appears, no errors.

**Practical Takeaway:**  
- Keywords: `st.session_state`, `st.chat_input`, `st.chat_message`, `st.form`, `st.tabs`.  
- Why: UI makes the assistant usable.

---

## 🧩 **Module 6: Memory – Ghajini Se Genie Tak**  
*(Step 10 from roadmap)*

**Level 6.1: SQLite History Setup**

1. **Task:** `get_session_history` function banao jo `SQLChatMessageHistory` return kare with connection string `sqlite:///code_history.db`.  
2. **Logic:** Messages will persist.  
3. **Definition of Done:** File `code_history.db` create ho.

**Level 6.2: History Wrapper Lagao**

1. **Task:** Apni RAG chain ko `RunnableWithMessageHistory` mein wrap karo. Pass `get_session_history`, `input_messages_key="query"`, `history_messages_key="history"`.  
2. **Logic:** Wrapper automatically injects past messages.  
3. **Definition of Done:** Chain object now stateful.

**Level 6.3: Multi‑Turn Test**

1. **Task:** User se do questions puchho jo pehle wale par depend karte hain (e.g., "What is a MySQL JOIN?" then "Can you show me an example of LEFT JOIN?").  
2. **Logic:** Second answer should reference first.  
3. **Definition of Done:** Context preserved.

**🔥 COMBO TASK (Level 6.4):**  
1. **Task:** Simulate a full conversation (3 turns), stop app, restart, login again – ask a follow‑up question. Bot should remember. Check SQLite DB to see stored messages.  
2. **Logic:** Persistence works.  
3. **Definition of Done:** Memory works across restarts.

**Practical Takeaway:**  
- Keywords: `RunnableWithMessageHistory`, `SQLChatMessageHistory`, `session_id`.  
- Why: Memory is essential for natural conversations.

---

## 🧩 **Module 7: Streaming + Reset – Pro Level UX**  
*(Step 11 from roadmap)*

**Level 7.1: Streaming Responses**

1. **Task:** Replace static answer with streaming. Use `st.write_stream` inside the assistant's chat message. Iterate over `chain.stream()` and yield chunks.  
2. **Logic:** Real‑time typing effect.  
3. **Definition of Done:** Answer appears word by word.

**Level 7.2: Reset Button – Naya Thread**

1. **Task:** Sidebar mein "New Thread" button daalo. On click:  
   - Clear `st.session_state.messages`  
   - Call `get_session_history(session_id).clear()` to wipe SQLite history for that user.  
2. **Logic:** UI and backend both cleared.  
3. **Definition of Done:** After click, chat history gone, bot forgets.

**🔥 COMBO TASK (Level 7.3):**  
1. **Task:** Test streaming + reset together. Start a conversation, use reset, ask a new question – bot should behave as if fresh.  
2. **Logic:** Full UX polish.  
3. **Definition of Done:** Streaming smooth, reset works.

**Practical Takeaway:**  
- Keywords: `st.write_stream`, `.stream()`, `.clear()`.  
- Why: Streaming and reset are standard in modern chatbots.

---

## 🧩 **Module 8: Final Integration – CodeSarthi Zinda Hai**  
*(Step 12 from roadmap)*

**Level 8.1: End‑to‑End Test – Multi‑User**

1. **Task:** Two different users signup and login (different emails). Each asks separate questions. Verify conversations are isolated.  
2. **Logic:** Each user's session_id different.  
3. **Definition of Done:** Users don't see each other's history.

**Level 8.2: Memory & RAG Combined**

1. **Task:** Single user, ask a question that requires both memory and codebase knowledge (e.g., first ask "What does auth.py do?" then ask "How does it handle password hashing?").  
2. **Logic:** RAG provides code facts, memory provides context.  
3. **Definition of Done:** Second answer uses first context and codebase.

**Level 8.3: PDF Query Test – MySQL Cheatsheet**

1. **Task:** Ask MySQL-related questions from `pdf_file/mysql_cheatsheet.pdf`:  
   - "What is the syntax for a SELECT statement in MySQL?"  
   - "How do I use JOIN in MySQL?"  
   - "What are the different MySQL data types?"  
2. **Logic:** PDF should be ingested and retrievable.  
3. **Definition of Done:** Answers come from `mysql_cheatsheet.pdf` content, source document shows the PDF file.

**Level 8.4: Project Structure Verify Karo**

1. **Task:** Final project structure check karo – ensure ye sab files/folders exist hain:  
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
   ├── pdf_file/
   │   └── mysql_cheatsheet.pdf
   ├── chroma_code/      ← auto-generated, gitignored
   ├── users.db          ← auto-generated, gitignored
   └── code_history.db   ← auto-generated, gitignored
   ```
2. **Logic:** README mein defined structure se match karna zaroori hai.  
3. **Definition of Done:** Sab files present, `chroma_code/`, `users.db`, `code_history.db` gitignored.

**🔥 COMBO TASK (Level 8.5):**  
1. **Task:** Run all features together: Signup → Login → multi‑turn RAG conversation → MySQL PDF query → reset → new conversation → streaming. Check LangSmith traces (if setup).  
2. **Logic:** Full system validation.  
3. **Definition of Done:** All features work, no errors, traces visible.

**Practical Takeaway:**  
- Keywords: Full architecture – RAG + Memory + UI + Observability.  
- Why: This is exactly how enterprise assistants are built.

---

## 🏁 **MODULE 8 RECAP (Tera Status Report)**  
**Siksha Summary:**  
- You built a complete production‑ready **codebase assistant** that:  
  - Uses local LLM (Ollama + mistral:7b) for privacy  
  - Ingests code files (`repo/`) and PDF documents (`pdf_file/mysql_cheatsheet.pdf`)  
  - Chunks, embeds, stores in Chroma  
  - Retrieves semantically relevant context from both code and PDF  
  - Maintains conversation memory per user (SQLite)  
  - Provides a chat UI with streaming and reset  
  - Includes multi‑user signup/login and isolated sessions  
  - Uses LangSmith for full observability  
  - Proper `.gitignore` for sensitive files  

**Guru-ji's Warning:**  
*"Check kar le bhai! Kya tujhe yeh sab bina chat sheet ke karna aa gaya hai?  
- Virtual environment bana sakta hai?  
- Ollama background service ki tarah chalana?  
- `.gitignore` properly set karna?  
- Sample files structure set karna (`repo/` aur `pdf_file/`)?  
- auth_db.py mein hashed passwords store karna aur signup implement karna?  
- ingest.py se files load, chunk, embed, DB store karna (code + PDF dono)?  
- Vector DB load karke RetrievalQA chain banana?  
- Streamlit signup/login aur chat UI banana?  
- RunnableWithMessageHistory se memory add karna?  
- Streaming aur reset implement karna?  
- Multi‑user isolation test karna?  
- MySQL PDF se questions answer ho rahe hain?  
- Final project structure README se match karna?  

Agar inme se ek bhi cheez mein doubt hai ya confuse hai, toh chup chaap peeche ja aur wapas execute kar. Aage badhne ka koi fayda nahi agar basics hile hue hain!"*

---

⚡ **GURUDAKSHINA (The Checkpoint):**  
**Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type 'CONTINUE' for the next set of missions – yani tujhe kuch aur nahi, tu ab apne man se koi bhi code repository le ke ye app bana sakta hai. Aage kya karna hai? Feedback de, ya naye features add kar.**
