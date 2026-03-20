
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

### **What We're Building in Module 3:**
RAG (Retrieval-Augmented Generation) works in 3 phases:
1. **Ingestion** (this module) – Load all files, split into chunks, convert to vectors, store in DB
2. **Retrieval** (Module 4) – When user asks a question, find similar chunks from the DB
3. **Generation** (Module 4) – Feed those chunks to LLM to generate answer

Without ingestion, the assistant has ZERO knowledge. This module is the foundation.

---

**Level 3.1: Files Load Karo – Why Different Loaders?**

**What we're achieving:**
Load all knowledge sources (code files, markdown docs, PDFs) into memory as "documents" that LangChain can process.

**Why different loaders?**
- `.py` and `.md` files are plain text → use `DirectoryLoader` (reads file system)
- `.pdf` files are binary with special formatting → use `PyPDFLoader` (extracts text from PDF structure)
- If we used wrong loader, we'd get garbage or errors

**How it works:**
- `DirectoryLoader` recursively scans a folder, finds files matching a pattern (glob), reads them
- `PyPDFLoader` opens PDF, extracts text from each page
- Each file becomes a "Document" object with `page_content` (text) and `metadata` (source file name)

**Your task:**
1. Create `ingest.ipynb` notebook
2. Cell 1: Import the loaders
3. Cell 2-4: Load files from `repo/` (markdown + Python) and `pdf_file/` (PDF)
4. Cell 5: Combine all into one list, print total count

**Research & Learn:**
- How does `DirectoryLoader` work? What does `glob` pattern do?
- What's the difference between `glob="**/*.md"` and `glob="*.md"`? (Hint: `**` means recursive)
- What does `PyPDFLoader` return? How many documents from 1 PDF?
- What's inside a LangChain `Document` object? (Hint: `.page_content` and `.metadata`)

**Definition of Done:**
Print shows: "Loaded X documents" where X = 3 (from repo) + number of pages in PDF. Each document has source file name in metadata.

**Level 3.2: Chunks Banao – Why Split Documents?**

**What we're achieving:**
Convert large documents into smaller, overlapping pieces (chunks) so that:
- Each chunk fits in LLM's context window
- Similarity search returns focused, relevant pieces (not entire 100-page file)
- Context is preserved between chunks (via overlap)

**Why chunking matters:**
- If we feed entire 100-page PDF to LLM, it's slow and wastes tokens
- If chunks are too small (e.g., 100 chars), we lose context
- If chunks don't overlap, we might split a sentence in half
- `chunk_size=1500` means ~300-400 words per chunk (good for code)
- `chunk_overlap=200` means last 200 chars of chunk N = first 200 chars of chunk N+1

**How it works:**
- `RecursiveCharacterTextSplitter` splits on sentence boundaries first, then paragraphs, then words (smart splitting)
- It tries to keep chunks close to `chunk_size` but respects sentence boundaries
- Overlap ensures context continuity

**Your task:**
1. Cell 6: Create `RecursiveCharacterTextSplitter` with `chunk_size=1500`, `chunk_overlap=200`
2. Cell 7: Split all documents from Cell 5 using `.split_documents()`
3. Cell 8: Print chunk count

**Research & Learn:**
- Why use `RecursiveCharacterTextSplitter` instead of simple string slicing?
- What happens if `chunk_overlap=0`? What if `chunk_overlap=chunk_size`?
- How many chunks do you expect from 3 code files + 1 PDF? (Estimate based on file sizes)
- What's the difference between `.split_documents()` and `.split_text()`?

**Definition of Done:**
Print shows: "Created Y chunks" where Y > X (more chunks than original documents). Each chunk has metadata showing source file.

**Level 3.3: Embeddings Banao – Converting Text to Vectors**

**What we're achieving:**
Convert each chunk of text into a numerical vector (embedding) so that:
- Similar text chunks have similar vectors (mathematically close)
- We can use vector math to find relevant chunks (similarity search)
- The LLM can understand semantic meaning, not just keyword matching

**Why embeddings?**
- Text is strings (unstructured) → vectors are numbers (structured, mathematical)
- Vector similarity = semantic similarity ("password hashing" and "hash password" are similar)
- Keyword search would miss this; embeddings capture meaning
- Ollama's `mistral:7b` model can generate embeddings (it's not just for chat)

**How it works:**
- `OllamaEmbeddings` calls Ollama's embedding API
- Each chunk becomes a vector of ~3072 dimensions (for mistral:7b)
- Similar chunks have vectors pointing in similar directions (high cosine similarity)

**Your task:**
1. Cell 9: Create `OllamaEmbeddings(model="mistral:7b")`
2. Cell 10: Take one sample chunk, call `.embed_query(chunk_text)` to get its vector
3. Cell 11: Print vector length and first 10 values

**Research & Learn:**
- What's a vector embedding? Why 3072 dimensions?
- What's cosine similarity? How does it measure text similarity?
- Why use Ollama embeddings instead of OpenAI? (Hint: privacy, cost)
- What happens if you embed "password hashing" and "hash password"? Are vectors similar?

**Definition of Done:**
Print shows: "Vector length: 3072" and first 10 values are floats. No errors from Ollama.

**Level 3.4: Chroma DB Mein Save Karo – Building the Vector Store**

**What we're achieving:**
Store all chunks + their embeddings in a persistent vector database so we can:
- Quickly search for relevant chunks later (without re-embedding)
- Persist knowledge across app restarts
- Scale to thousands of documents

**Why Chroma?**
- It's a vector database (optimized for similarity search)
- It's local (no cloud dependency, privacy)
- It persists to disk (`chroma_code/` folder)
- It's fast (uses approximate nearest neighbor search)

**How it works:**
- `Chroma.from_documents()` takes chunks + embeddings
- It stores vectors in a special format optimized for similarity search
- `persist_directory="./chroma_code"` saves to disk
- Later, you can load it back without re-embedding

**Your task:**
1. Cell 12: Call `Chroma.from_documents(documents=chunks, embedding=embeddings_model, persist_directory="./chroma_code", collection_name="code_knowledge")`
2. Cell 13: Print "Vector store created successfully"

**Research & Learn:**
- What's a vector database? How is it different from SQL databases?
- What's inside `chroma_code/` folder? (Hint: binary files with vectors)
- Why `persist_directory`? What happens if you don't persist?
- What's a collection? Can you have multiple collections in one Chroma DB?

**Definition of Done:**
`chroma_code/` folder appears with files inside. Print confirms success. No errors.

**🔥 COMBO TASK (Level 3.5): Verify Ingestion Works – Similarity Search Test**

**What we're achieving:**
Test that the entire ingestion pipeline works end-to-end:
- Load DB from disk
- Search for relevant chunks using natural language queries
- Verify that code questions return code chunks, PDF questions return PDF chunks

**Why this test?**
- Proves ingestion worked (vectors are stored correctly)
- Proves retrieval works (similarity search finds relevant chunks)
- Proves both code and PDF sources are searchable
- If this fails, everything downstream fails

**How it works:**
- Load Chroma DB from disk (same `persist_directory`)
- Create a retriever with `search_kwargs={"k": 3}` (return top 3 similar chunks)
- Call `.similarity_search(query)` with natural language questions
- Check that returned chunks are relevant and from correct source files

**Your task:**
1. Cell 14: Load Chroma DB: `db = Chroma(persist_directory="./chroma_code", embedding_function=embeddings_model, collection_name="code_knowledge")`
2. Cell 15: Create retriever: `retriever = db.as_retriever(search_kwargs={"k": 3})`
3. Cell 16: Search for code question: `results = retriever.invoke("how does authentication work?")`
4. Cell 17: Print results with source file names
5. Cell 18: Search for PDF question: `results = retriever.invoke("how to use JOIN in MySQL?")`
6. Cell 19: Print results with source file names

**Research & Learn:**
- What does `.as_retriever()` do? Why not use `.similarity_search()` directly?
- What's `search_kwargs={"k": 3}`? What if you set `k=10`?
- How do you extract source file name from retrieved chunks? (Hint: `.metadata`)
- Why should code question return code chunks and PDF question return PDF chunks?

**Definition of Done:**
Both searches return relevant chunks. Source files clearly show which file each chunk came from. Code question returns chunks from `repo/`, PDF question returns chunks from `mysql_cheatsheet.pdf`.

**Practical Takeaway for Module 3:**
- **Keywords:** `DirectoryLoader`, `PyPDFLoader`, `RecursiveCharacterTextSplitter`, `OllamaEmbeddings`, `Chroma.from_documents`, `as_retriever`, `similarity_search`, `jupyter notebook`.
- **Why:** Without ingestion, assistant has no knowledge. This is the foundation of RAG. You're converting unstructured text into searchable vectors.
- **Key Insight:** Ingestion is a one-time cost (takes a few minutes). Retrieval is fast (milliseconds). This is why RAG is efficient.
- **Next Step:** Once ingestion works, you can build the RAG chain (Module 4) that uses this retriever to answer questions.

---

## 🧩 **Module 4: RAG Chain – Assistant Ka Brain**  
*(Retrieval-Augmented Generation Setup)*

### **What We're Building in Module 4:**
Now that we have a vector database (Module 3), we build the RAG chain that:
1. Takes user's question
2. Retrieves relevant chunks from the DB
3. Feeds chunks + question to LLM
4. LLM generates answer based on retrieved context

This is where the "magic" happens – the assistant becomes intelligent.

---

**Level 4.1: Vector DB Load Karo – Connecting to Knowledge**

**What we're achieving:**
Load the vector database we created in Module 3 so we can query it.

**Why separate from ingestion?**
- Ingestion happens once (slow, takes minutes)
- Querying happens many times (fast, milliseconds)
- We load the DB once, then reuse it for thousands of queries
- This is why RAG is efficient

**How it works:**
- `Chroma(persist_directory="./chroma_code")` loads the DB from disk
- It doesn't re-embed anything (vectors already stored)
- It's ready for similarity search immediately

**Your task:**
1. Create `rag_chain_test.ipynb` notebook
2. Cell 1: Import `Chroma`, `OllamaEmbeddings`, `ChatOllama`, `RetrievalQA`
3. Cell 2: Load Chroma DB with same `persist_directory` and embedding model
4. Cell 3: Print DB info (e.g., collection count)

**Research & Learn:**
- Why do we need to pass the same `embedding_function` when loading?
- What happens if you load with a different embedding model?
- How fast is loading compared to ingestion?

**Definition of Done:**
DB loads without error. Print shows collection info.

**Level 4.2: Retriever Banao – The Bridge Between Query and DB**

**What we're achieving:**
Create a retriever object that:
- Takes a user's question
- Converts it to a vector (using same embedding model)
- Finds similar chunks in the DB
- Returns top-k most relevant chunks

**Why a retriever?**
- It's a wrapper around the DB that handles the query-to-vector conversion
- It standardizes the interface (`.invoke(query)` returns documents)
- It's reusable across different chain types

**How it works:**
- `.as_retriever(search_kwargs={"k": 3})` creates a retriever
- `k=3` means return top 3 most similar chunks
- When you call `.invoke(query)`, it:
  1. Embeds the query
  2. Finds 3 nearest neighbors in vector space
  3. Returns those 3 chunks

**Your task:**
1. Cell 4: Create retriever: `retriever = db.as_retriever(search_kwargs={"k": 3})`
2. Cell 5: Test it: `results = retriever.invoke("what is authentication?")`
3. Cell 6: Print results (should be 3 chunks)

**Research & Learn:**
- What's the difference between `k=1` and `k=10`?
- What's a "nearest neighbor" in vector space?
- Why use cosine similarity instead of Euclidean distance?
- What if you set `k=100` but only 50 chunks exist?

**Definition of Done:**
Retriever returns 3 chunks. Each chunk has `.page_content` and `.metadata`.

**Level 4.3: LLM Connect Karo – The Answer Generator**

**What we're achieving:**
Instantiate the local LLM (Mistral 7B via Ollama) that will:
- Read the retrieved chunks
- Read the user's question
- Generate a natural language answer

**Why Ollama?**
- It's local (no API calls, no latency, no cost)
- It's private (your data never leaves your machine)
- It's fast enough for interactive use
- Mistral 7B is small but capable

**How it works:**
- `ChatOllama(model="mistral:7b")` connects to Ollama service
- `.invoke(prompt)` sends a prompt and gets a response
- It streams tokens (word by word) for real-time feel

**Your task:**
1. Cell 7: Create LLM: `llm = ChatOllama(model="mistral:7b")`
2. Cell 8: Test it: `response = llm.invoke("What is a Python decorator?")`
3. Cell 9: Print response

**Research & Learn:**
- What's the difference between `ChatOllama` and `Ollama`?
- Why Mistral 7B instead of larger models?
- What's token streaming? Why is it better UX?
- How long does a response take? (Measure it)

**Definition of Done:**
LLM responds without error. Response is coherent and relevant.

**Level 4.4: RetrievalQA Chain Banao – Connecting Retriever + LLM**

**What we're achieving:**
Create a chain that orchestrates:
1. Retriever (finds relevant chunks)
2. LLM (generates answer)
3. Prompt template (formats the question + chunks into a prompt)

**Why a chain?**
- It automates the workflow (no manual orchestration)
- It handles prompt formatting ("Here are relevant docs: ... Now answer: ...")
- It returns both answer AND source documents
- It's reusable and composable

**How it works:**
- `RetrievalQA.from_chain_type()` creates a chain
- `chain_type="stuff"` means "stuff all retrieved docs into the prompt" (simple, works for small contexts)
- `return_source_documents=True` means return which chunks were used
- When you call `.invoke({"query": "..."})`:
  1. Retriever finds top-k chunks
  2. Prompt template formats: "Context: [chunks]\n\nQuestion: [query]"
  3. LLM generates answer
  4. Chain returns {"result": answer, "source_documents": chunks}

**Your task:**
1. Cell 10: Create chain: `qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)`
2. Cell 11: Print chain object

**Research & Learn:**
- What's `chain_type="stuff"`? What are other chain types? (Hint: map_reduce, refine)
- Why `return_source_documents=True`? What if False?
- What's a prompt template? How does it format the input?
- What happens if retrieved chunks are contradictory?

**Definition of Done:**
Chain object created. Print shows chain configuration.

**🔥 COMBO TASK (Level 4.5): End-to-End RAG Test – From Question to Answer**

**What we're achieving:**
Test the complete RAG pipeline:
- Ask a code question → retriever finds code chunks → LLM answers
- Ask a PDF question → retriever finds PDF chunks → LLM answers
- Verify source documents are correct

**Why this test?**
- Proves the entire chain works
- Proves retrieval is accurate (right chunks for right questions)
- Proves LLM can use context to answer
- This is the core of the assistant

**How it works:**
- `.invoke({"query": "..."})`  returns `{"result": answer, "source_documents": chunks}`
- You extract the answer and source documents
- You verify they're relevant

**Your task:**
1. Cell 12: Query 1: `response = qa_chain.invoke({"query": "What does auth.py do?"})`
2. Cell 13: Print `response["result"]` and `response["source_documents"]`
3. Cell 14: Query 2: `response = qa_chain.invoke({"query": "What is the syntax for SELECT in MySQL?"})`
4. Cell 15: Print `response["result"]` and `response["source_documents"]`

**Research & Learn:**
- Why does the first query return code chunks and second returns PDF chunks?
- What if you ask a question not in the knowledge base? (Try it)
- How does the LLM know to use the retrieved chunks?
- What's the prompt template that formats the question + chunks?

**Definition of Done:**
Both queries return relevant answers. Source documents clearly show which file each chunk came from. Code question uses code files, PDF question uses mysql_cheatsheet.pdf.

**Practical Takeaway for Module 4:**
- **Keywords:** `Chroma`, `as_retriever`, `RetrievalQA.from_chain_type`, `return_source_documents`, `ChatOllama`, `chain_type="stuff"`, `jupyter notebook`.
- **Why:** RAG is the core of the assistant. It combines retrieval (finding relevant context) + generation (creating answers). Without RAG, the LLM would hallucinate.
- **Key Insight:** The quality of answers depends on:
  1. Quality of ingestion (Module 3) – are chunks relevant?
  2. Quality of retrieval (k value, similarity threshold) – are top-k chunks correct?
  3. Quality of LLM (model size, temperature) – can it reason over context?
- **Next Step:** Now that RAG works, build the Streamlit UI (Module 5) to make it interactive.

---

## 🧩 **Module 5: Chat UI – Jadoo Ki Jhappi**  
*(Streamlit Interface & User Interaction)*

### **What We're Building in Module 5:**
A web UI that:
1. Handles user signup/login (authentication)
2. Shows a chat interface (conversation history)
3. Integrates RAG chain (answers questions)
4. Displays source documents (transparency)

This is where the assistant becomes a product.

---

**Level 5.1: Login + Signup Form – User Authentication**

**What we're achieving:**
Create a login/signup interface so:
- New users can register
- Existing users can login
- Each user has isolated conversations

**Why authentication?**
- Multi-user support (different users, different histories)
- Privacy (user A can't see user B's conversations)
- Persistence (user can logout and login later, history is saved)

**How it works:**
- Streamlit `st.tabs()` creates two tabs: Login and Sign Up
- Login tab: email + password → call `auth_db.verify_user()` → if match, set `st.session_state.user_email`
- Sign Up tab: email + password → call `auth_db.register_user()` → if success, show "Account created"
- `st.session_state` persists data across reruns (Streamlit's way of storing state)

**Your task:**
1. Create `app.py` file
2. Add Streamlit imports and page config
3. Check if `st.session_state.user_email` exists (user logged in?)
4. If not logged in, show two tabs:
   - **Login tab:** email input, password input, "Login" button → call `verify_user()` → if success, set `st.session_state.user_email` and `st.rerun()`
   - **Sign Up tab:** email input, password input, "Sign Up" button → call `register_user()` → if success, show success message

**Research & Learn:**
- What's `st.session_state`? How is it different from Python variables?
- What's `st.rerun()`? Why do we need it after login?
- What's `st.tabs()`? How do you switch between tabs?
- What's `st.text_input()` vs `st.text_area()`?

**Definition of Done:**
New user can signup. Existing user can login. After login, `st.session_state.user_email` is set.

**Level 5.2: Chat Interface – Conversation History**

**What we're achieving:**
Create a chat interface that:
- Shows previous messages (conversation history)
- Accepts new user input
- Displays messages in a chat-like format

**Why a chat interface?**
- Users expect ChatGPT-like experience
- Visual history helps users understand context
- Chat format is intuitive

**How it works:**
- `st.session_state.messages` is a list of message dicts: `{"role": "user", "content": "..."}` or `{"role": "assistant", "content": "..."}`
- Loop through `st.session_state.messages` and display each with `st.chat_message(role)`
- `st.chat_input()` gets new user input
- When user sends a message, append to `st.session_state.messages` and rerun

**Your task:**
1. After login, initialize `st.session_state.messages = []` if not exists
2. Loop through messages and display each: `for msg in st.session_state.messages: st.chat_message(msg["role"]).write(msg["content"])`
3. Add chat input: `user_input = st.chat_input("Ask me anything...")`
4. If user_input, append to messages: `st.session_state.messages.append({"role": "user", "content": user_input})`

**Research & Learn:**
- What's `st.chat_message()`? What roles does it support?
- What's the difference between `st.write()` and `st.text()`?
- How does `st.chat_input()` work? Does it block?
- Why do we need to append to `st.session_state.messages` manually?

**Definition of Done:**
Type a message, it appears in the chat. Previous messages are visible. Chat looks like ChatGPT.

**Level 5.3: RAG Integration – Connecting Chat to Assistant Brain**

**What we're achieving:**
When user sends a message, call the RAG chain to generate an answer.

**Why integrate RAG?**
- Without RAG, chat is just echo (no intelligence)
- With RAG, chat becomes an assistant (answers based on knowledge base)

**How it works:**
- User sends message → append to `st.session_state.messages`
- Call `qa_chain.invoke({"query": user_input})`
- Extract answer and source documents
- Append assistant response to `st.session_state.messages`
- Display in chat

**Your task:**
1. After user appends their message, check if `user_input` is not empty
2. Call RAG chain: `response = qa_chain.invoke({"query": user_input})`
3. Extract answer: `answer = response["result"]`
4. Append to messages: `st.session_state.messages.append({"role": "assistant", "content": answer})`
5. Display in chat: `st.chat_message("assistant").write(answer)`

**Research & Learn:**
- What's the structure of `qa_chain.invoke()` response?
- What if the query is empty or very short?
- What if RAG chain fails? How do you handle errors?
- How long does a response take? (Measure it)

**Definition of Done:**
Ask a question, assistant answers based on knowledge base. Answer appears in chat.

**Level 5.4: Source Documents Display – Transparency**

**What we're achieving:**
Show which files/chunks were used to generate the answer.

**Why show sources?**
- Users trust answers more when they see sources
- Users can verify if sources are correct
- Users can click through to original documents
- It's standard in modern AI apps (ChatGPT, Perplexity, etc.)

**How it works:**
- `response["source_documents"]` contains the chunks used
- Each chunk has `.page_content` (text) and `.metadata` (source file)
- Use `st.expander()` to create a collapsible section
- Display file names and chunk previews

**Your task:**
1. After displaying assistant answer, extract source documents: `sources = response["source_documents"]`
2. Create expander: `with st.expander("📚 Sources Used"):`
3. Loop through sources and display:
   ```python
   for i, doc in enumerate(sources):
       st.write(f"**Source {i+1}:** {doc.metadata.get('source', 'Unknown')}")
       st.write(f"Preview: {doc.page_content[:200]}...")
   ```

**Research & Learn:**
- What's `st.expander()`? Why use it instead of always showing sources?
- What's in `doc.metadata`? What keys are available?
- How do you truncate text to first 200 chars?
- What if there are no source documents?

**Definition of Done:**
After each answer, an expandable "Sources Used" section appears. Clicking it shows file names and chunk previews.

**🔥 COMBO TASK (Level 5.5): Complete Chat UI – End-to-End Test**

**What we're achieving:**
Test the complete UI:
- Signup as new user
- Login
- Ask a code question → get answer with sources
- Ask a PDF question → get answer with sources
- Verify chat history is visible

**Why this test?**
- Proves UI works end-to-end
- Proves authentication works
- Proves RAG integration works
- Proves sources are displayed correctly

**Your task:**
1. Run `streamlit run app.py`
2. Signup with email `test@example.com`, password `password123`
3. Login with same credentials
4. Ask: "What does auth.py do?"
5. Verify answer appears and sources show `auth.py`
6. Ask: "How do I use GROUP BY in MySQL?"
7. Verify answer appears and sources show `mysql_cheatsheet.pdf`
8. Verify both messages are visible in chat history

**Research & Learn:**
- What happens if you refresh the page? Is chat history still there?
- What happens if you logout and login again? Is history still there?
- What if you ask a question not in the knowledge base?
- How long does it take to get an answer?

**Definition of Done:**
UI works end-to-end. Signup, login, chat, sources all work. No errors.

**Practical Takeaway for Module 5:**
- **Keywords:** `st.session_state`, `st.chat_input`, `st.chat_message`, `st.tabs`, `st.expander`, `st.rerun`, `streamlit`.
- **Why:** UI makes the assistant usable. Without UI, it's just a Python script. With UI, it's a product.
- **Key Insight:** Streamlit reruns the entire script on every interaction. `st.session_state` persists data across reruns.
- **Next Step:** Now that UI works, add memory (Module 6) so the assistant remembers previous conversations.

---

## 🧩 **Module 6: Memory – Ghajini Se Genie Tak**  
*(Conversation History & Context Persistence)*

### **What We're Building in Module 6:**
Right now, the assistant answers each question independently. We add memory so:
- Assistant remembers previous questions
- Assistant can reference earlier context
- Conversations feel natural (like ChatGPT)

Example:
- User: "What is authentication?"
- Assistant: "Authentication is the process of verifying user identity..."
- User: "How does it work in auth.py?"
- Assistant: "In auth.py, authentication works by [uses context from previous question]"

---

**Level 6.1: SQLite History Setup – Persistent Memory**

**What we're achieving:**
Create a function that retrieves conversation history from SQLite so:
- Messages persist across app restarts
- Each user has isolated history
- History is searchable and queryable

**Why SQLite?**
- It's local (no cloud dependency)
- It's persistent (survives app restarts)
- It's queryable (can search history)
- It's simple (no setup needed)

**How it works:**
- `SQLChatMessageHistory` is a LangChain class that stores messages in SQLite
- `get_session_history(session_id)` returns a history object for that session
- Each session_id is unique per user (e.g., user email)
- Messages are stored as JSON in the DB

**Your task:**
1. Create a function `get_session_history(session_id)` that returns `SQLChatMessageHistory(session_id=session_id, connection_string="sqlite:///code_history.db")`
2. Test it: call the function with a session_id, add a message, verify it's stored

**Research & Learn:**
- What's `SQLChatMessageHistory`? How is it different from regular SQLite?
- What's a `session_id`? Why is it important?
- What's the schema of the SQLite table? (Hint: session_id, message, type)
- How do you query the history? (Hint: `.messages` property)

**Definition of Done:**
`code_history.db` file is created. Function returns a history object. Messages can be added and retrieved.

**Level 6.2: History Wrapper Lagao – Injecting Memory into RAG**

**What we're achieving:**
Wrap the RAG chain with `RunnableWithMessageHistory` so:
- Previous messages are automatically injected into the prompt
- LLM can reference earlier context
- No manual prompt engineering needed

**Why a wrapper?**
- It automates memory injection
- It handles message formatting
- It's reusable across different chains
- It's the LangChain way of adding memory

**How it works:**
- `RunnableWithMessageHistory` wraps your chain
- When you call `.invoke({"query": "...", "session_id": "..."})`:
  1. It retrieves history for that session_id
  2. It formats: "Previous messages: [history]\n\nNew question: [query]"
  3. It passes to RAG chain
  4. RAG chain generates answer using both history and retrieved chunks
- `input_messages_key="query"` tells it which key is the user's question
- `history_messages_key="history"` tells it where to inject history

**Your task:**
1. Wrap the chain: `qa_chain_with_memory = RunnableWithMessageHistory(runnable=qa_chain, get_session_history=get_session_history, input_messages_key="query", history_messages_key="history")`
2. Test it: call `.invoke({"query": "...", "session_id": "..."})`

**Research & Learn:**
- What's `RunnableWithMessageHistory`? How is it different from `RetrievalQA`?
- What's `input_messages_key` and `history_messages_key`? Why do we need both?
- What happens if you don't pass `session_id`?
- How does the wrapper format the prompt?

**Definition of Done:**
Chain with memory is created. Test with multi-turn conversation (ask 2 questions, verify second uses context from first).

**Level 6.3: Session ID Management – User Isolation**

**What we're achieving:**
Generate unique session IDs for each user so:
- Each user's history is isolated
- User A can't see User B's conversations
- Multiple users can use the app simultaneously

**Why session IDs?**
- SQLite stores all messages in one table
- Session ID is the key that separates users
- Without it, all users would share history

**How it works:**
- Session ID can be simple: just the user's email
- Or complex: `f"{user_email}_{timestamp}"` for multiple sessions per user
- Store in `st.session_state.session_id` so it persists across reruns
- Pass to chain: `.invoke({"query": "...", "session_id": session_id})`

**Your task:**
1. After user logs in, generate session_id: `st.session_state.session_id = user_email` (simple approach)
2. When calling chain, pass session_id: `qa_chain_with_memory.invoke({"query": user_input, "session_id": st.session_state.session_id})`

**Research & Learn:**
- Why use email as session_id instead of user ID?
- What if a user wants multiple separate conversations?
- How do you query all sessions for a user?
- What if session_id is not unique?

**Definition of Done:**
Different users have different session_ids. Each user's history is isolated.

**Level 6.4: Multi-Turn Test – Verify Memory Works**

**What we're achieving:**
Test that the assistant remembers context across multiple turns.

**Why this test?**
- Proves memory injection works
- Proves LLM can use history
- Proves context is preserved

**How it works:**
- Ask question 1: "What is a MySQL JOIN?"
- Ask question 2: "Can you show me an example of LEFT JOIN?"
- In question 2, the assistant should reference "LEFT JOIN" specifically (not just generic JOIN)
- This proves it remembered the context from question 1

**Your task:**
1. Create `memory_test.ipynb` notebook
2. Cell 1: Setup (imports, load chain with memory)
3. Cell 2: Ask question 1: `response1 = qa_chain_with_memory.invoke({"query": "What is a MySQL JOIN?", "session_id": "test_user"})`
4. Cell 3: Print response1
5. Cell 4: Ask question 2: `response2 = qa_chain_with_memory.invoke({"query": "Can you show me an example of LEFT JOIN?", "session_id": "test_user"})`
6. Cell 5: Print response2
7. Cell 6: Verify that response2 mentions "LEFT JOIN" specifically (not just generic JOIN)

**Research & Learn:**
- What's the difference between stateless and stateful chains?
- How does the wrapper inject history into the prompt?
- What if you use different session_ids for the same user?
- What if you ask 100 questions? Does memory get too long?

**Definition of Done:**
Response 2 mentions "LEFT JOIN" specifically, proving it remembered context from response 1.

**🔥 COMBO TASK (Level 6.5): Persistence Across Restarts – Full Memory Test**

**What we're achieving:**
Test that memory persists across app restarts.

**Why this test?**
- Proves SQLite persistence works
- Proves history survives app restart
- Proves user can logout and login later, history is still there

**How it works:**
1. Have a conversation (3 turns)
2. Stop the app
3. Restart the app
4. Login as same user
5. Ask a follow-up question
6. Verify assistant remembers previous conversation
7. Check SQLite DB to see stored messages

**Your task:**
1. Run `streamlit run app.py`
2. Signup/login as `test@example.com`
3. Ask: "What is authentication?"
4. Ask: "How does it work in auth.py?"
5. Ask: "What's the password hashing function?"
6. Stop the app (Ctrl+C)
7. Restart: `streamlit run app.py`
8. Login as `test@example.com`
9. Ask: "Can you summarize what we discussed?"
10. Verify assistant mentions all 3 previous questions
11. Check `code_history.db` with SQLite browser to see stored messages

**Research & Learn:**
- What's inside `code_history.db`? (Hint: use `sqlite3 code_history.db` to query)
- How many messages are stored? (Hint: `SELECT COUNT(*) FROM message_store`)
- What's the schema of the message table?
- How do you clear history for a user?

**Definition of Done:**
Memory persists across restarts. Assistant remembers previous conversation. SQLite DB contains all messages.

**Practical Takeaway for Module 6:**
- **Keywords:** `RunnableWithMessageHistory`, `SQLChatMessageHistory`, `session_id`, `get_session_history`, `input_messages_key`, `history_messages_key`, `jupyter notebook`.
- **Why:** Memory is essential for natural conversations. Without it, each question is independent (like talking to a stateless API). With it, conversations feel human-like.
- **Key Insight:** Memory is injected into the prompt. The LLM doesn't have special memory logic; it just sees a longer prompt with history included.
- **Next Step:** Now that memory works, add streaming and reset buttons (Module 7) for better UX.

---

## 🧩 **Module 7: Streaming + Reset – Pro Level UX**  
*(Real-time Response & Session Management)*

### **What We're Building in Module 7:**
Polish the UX:
1. **Streaming** – Show answer word-by-word (like ChatGPT) instead of all at once
2. **Reset** – Clear conversation history and start fresh
3. **Logout** – End user session

These are standard features in modern chatbots.

---

**Level 7.1: Streaming Responses – Real-Time Typing Effect**

**What we're achieving:**
Instead of waiting for full answer, show it word-by-word as it's generated.

**Why streaming?**
- Better UX (user sees progress)
- Feels faster (even if total time is same)
- Standard in ChatGPT, Claude, etc.
- Reduces perceived latency

**How it works:**
- RAG chain has a `.stream()` method that yields tokens as they're generated
- `st.write_stream()` displays tokens in real-time
- Instead of: `response = chain.invoke()` then `st.write(response)`
- Do: `st.write_stream(chain.stream({"query": "...", "session_id": "..."}))`

**Your task:**
1. In `app.py`, after user sends message, replace static display with streaming
2. Instead of: `st.chat_message("assistant").write(answer)`
3. Do: `with st.chat_message("assistant"): st.write_stream(qa_chain_with_memory.stream({"query": user_input, "session_id": session_id}))`

**Research & Learn:**
- What's `.stream()` vs `.invoke()`?
- What's `st.write_stream()`? How does it work?
- What's a token? How many tokens per word?
- Why does streaming feel faster even if total time is same?

**Definition of Done:**
Answer appears word-by-word, not all at once. Streaming is smooth and real-time.

**Level 7.2: Reset Button – Naya Thread**

**What we're achieving:**
Add a button that clears conversation history so user can start fresh.

**Why reset?**
- User might want to start a new topic
- User might want to clear sensitive information
- Standard feature in ChatGPT ("New Chat")

**How it works:**
- `st.sidebar` creates a sidebar
- Button in sidebar: `if st.sidebar.button("🔄 New Thread"):`
- On click:
  1. Clear UI history: `st.session_state.messages = []`
  2. Clear SQLite history: `get_session_history(session_id).clear()`
  3. Show success message
  4. Rerun app

**Your task:**
1. In sidebar, add button: `if st.sidebar.button("🔄 New Thread"):`
2. Inside button handler:
   ```python
   st.session_state.messages = []
   get_session_history(st.session_state.session_id).clear()
   st.success("Thread cleared! Start fresh.")
   st.rerun()
   ```

**Research & Learn:**
- What's `st.sidebar`? How is it different from main area?
- What's `.clear()` on history object? Does it delete from SQLite?
- What's `st.success()` vs `st.info()` vs `st.warning()`?
- What happens if you click reset twice?

**Definition of Done:**
After clicking reset, chat history is gone. New conversation starts fresh. SQLite history is cleared.

**Level 7.3: Logout Button – End Session**

**What we're achieving:**
Add a logout button so user can end their session.

**Why logout?**
- User might want to switch accounts
- User might want to end session for security
- Standard feature in all apps

**How it works:**
- Button in sidebar: `if st.sidebar.button("🚪 Logout"):`
- On click:
  1. Clear session state: `st.session_state.user_email = None` and `st.session_state.session_id = None`
  2. Clear messages: `st.session_state.messages = []`
  3. Rerun app (Streamlit shows login form)

**Your task:**
1. In sidebar, add button: `if st.sidebar.button("🚪 Logout"):`
2. Inside button handler:
   ```python
   st.session_state.user_email = None
   st.session_state.session_id = None
   st.session_state.messages = []
   st.success("Logged out successfully!")
   st.rerun()
   ```

**Research & Learn:**
- What's the difference between clearing `st.session_state` and deleting from SQLite?
- Should logout delete SQLite history? (Hint: No, user might login again later)
- What if user closes browser without clicking logout?
- How do you implement "Remember me" functionality?

**Definition of Done:**
After clicking logout, login form appears. User can login as different user.

**🔥 COMBO TASK (Level 7.4): Full UX Polish – Streaming + Reset + Logout**

**What we're achieving:**
Test all UX features together:
- Streaming works smoothly
- Reset clears history
- Logout ends session
- User isolation is maintained

**Why this test?**
- Proves all UX features work together
- Proves no bugs in interaction
- Proves user isolation is maintained

**Your task:**
1. Run `streamlit run app.py`
2. Signup/login as `user1@example.com`
3. Ask a question, verify streaming (answer appears word-by-word)
4. Click "🔄 New Thread", verify chat clears
5. Ask a new question, verify it's a fresh conversation
6. Click "🚪 Logout"
7. Signup/login as `user2@example.com`
8. Verify user2 doesn't see user1's history
9. Ask a question as user2
10. Logout and login as user1 again
11. Verify user1's history is still there (from step 5)

**Research & Learn:**
- Why does streaming feel faster than non-streaming?
- What happens if you click reset while streaming?
- What if two users login simultaneously?
- How do you handle session conflicts?

**Definition of Done:**
Streaming smooth, reset works, logout works, user isolation verified. No errors.

**Practical Takeaway for Module 7:**
- **Keywords:** `st.write_stream`, `.stream()`, `.clear()`, `st.session_state`, `st.sidebar`, `st.rerun`, `streamlit`.
- **Why:** Streaming and reset are standard in modern chatbots. They make the app feel polished and professional.
- **Key Insight:** Streaming doesn't make the response faster; it just makes it feel faster (better UX). Reset and logout are essential for multi-user apps.
- **Next Step:** Now that all features work, do end-to-end testing (Module 8) to validate the entire system.

---

## 🧩 **Module 8: Final Integration – CodeSarthi Zinda Hai**  
*(End-to-End Testing & Validation)*

### **What We're Building in Module 8:**
Final validation that everything works together:
1. **Multi-user isolation** – Different users have separate histories
2. **Memory + RAG** – Assistant uses both context and knowledge base
3. **PDF queries** – MySQL questions are answered from PDF
4. **Code queries** – Code questions are answered from repo
5. **Project structure** – Everything is organized correctly

This is the final checkpoint before deployment.

---

**Level 8.1: Multi-User Isolation Test**

**What we're achieving:**
Verify that different users have completely separate conversations.

**Why this test?**
- Proves session_id isolation works
- Proves SQLite history is per-user
- Proves no data leakage between users
- Critical for privacy

**How it works:**
- User A signs up and has a conversation
- User B signs up and has a different conversation
- User A logs back in and sees only their history
- User B logs back in and sees only their history
- They never see each other's messages

**Your task:**
1. Run `streamlit run app.py`
2. Signup as `alice@example.com`, password `alice123`
3. Ask: "What is authentication?"
4. Logout
5. Signup as `bob@example.com`, password `bob123`
6. Verify chat is empty (no alice's message)
7. Ask: "What is MySQL?"
8. Logout
9. Login as `alice@example.com`
10. Verify only alice's message is visible
11. Login as `bob@example.com`
12. Verify only bob's message is visible

**Research & Learn:**
- How does session_id prevent data leakage?
- What if two users have the same email?
- What if session_id is not unique?
- How do you audit which user accessed what?

**Definition of Done:**
Users don't see each other's history. Each user's chat is completely private.

**Level 8.2: Memory + RAG Combined Test**

**What we're achieving:**
Verify that the assistant uses BOTH memory (previous context) AND RAG (knowledge base) together.

**Why this test?**
- Proves memory injection works
- Proves RAG retrieval works
- Proves LLM can combine both
- This is the core of the assistant

**How it works:**
- Ask question 1 about a specific file (e.g., "What does auth.py do?")
- Ask question 2 that references question 1 (e.g., "How does it handle password hashing?")
- In question 2, assistant should:
  1. Remember question 1 (memory)
  2. Retrieve relevant chunks from auth.py (RAG)
  3. Combine both to answer

**Your task:**
1. Run `streamlit run app.py`
2. Signup/login
3. Ask: "What does auth.py do?"
4. Verify answer mentions authentication functions
5. Ask: "How does it handle password hashing?"
6. Verify answer:
   - References auth.py from question 1 (memory)
   - Mentions specific hashing function from code (RAG)
   - Combines both contexts

**Research & Learn:**
- What's the difference between memory-only and RAG-only?
- Why is combining both better than either alone?
- What if memory and RAG contradict each other?
- How does the LLM decide which to trust?

**Definition of Done:**
Second answer uses context from first question AND retrieves relevant code chunks. Both memory and RAG are working together.

**Level 8.3: PDF Query Test – MySQL Cheatsheet**

**What we're achieving:**
Verify that PDF documents are properly ingested and retrievable.

**Why this test?**
- Proves PDF ingestion works (Module 3)
- Proves PDF retrieval works (Module 4)
- Proves LLM can answer PDF-based questions
- Proves source documents show PDF file

**How it works:**
- Ask MySQL-related questions
- Retriever finds chunks from `mysql_cheatsheet.pdf`
- LLM generates answer based on PDF content
- Source documents show `mysql_cheatsheet.pdf`

**Your task:**
1. Run `streamlit run app.py`
2. Signup/login
3. Ask: "What is the syntax for a SELECT statement in MySQL?"
4. Verify:
   - Answer mentions SELECT syntax
   - Source documents show `mysql_cheatsheet.pdf`
5. Ask: "How do I use JOIN in MySQL?"
6. Verify:
   - Answer mentions JOIN types
   - Source documents show `mysql_cheatsheet.pdf`
7. Ask: "What are the different MySQL data types?"
8. Verify:
   - Answer lists data types
   - Source documents show `mysql_cheatsheet.pdf`

**Research & Learn:**
- Why is PDF retrieval important?
- What if PDF is poorly formatted?
- How do you handle multi-page PDFs?
- What if PDF has images/tables?

**Definition of Done:**
All 3 MySQL questions are answered correctly. Source documents clearly show `mysql_cheatsheet.pdf`.

**Level 8.4: Code Query Test – Repository**

**What we're achieving:**
Verify that code files are properly ingested and retrievable.

**Why this test?**
- Proves code ingestion works (Module 3)
- Proves code retrieval works (Module 4)
- Proves LLM can answer code-based questions
- Proves source documents show code files

**How it works:**
- Ask code-related questions
- Retriever finds chunks from `repo/` files
- LLM generates answer based on code content
- Source documents show code file names

**Your task:**
1. Run `streamlit run app.py`
2. Signup/login
3. Ask: "What does auth.py do?"
4. Verify:
   - Answer mentions authentication functions
   - Source documents show `auth.py`
5. Ask: "What is the purpose of user_service.py?"
6. Verify:
   - Answer mentions user management
   - Source documents show `user_service.py`
7. Ask: "Explain the password hashing function."
8. Verify:
   - Answer mentions hashing algorithm
   - Source documents show relevant code file

**Research & Learn:**
- Why is code retrieval important?
- What if code has complex logic?
- How do you handle multi-file dependencies?
- What if code has comments vs no comments?

**Definition of Done:**
All 3 code questions are answered correctly. Source documents clearly show correct code files.

**Level 8.5: Project Structure Verification**

**What we're achieving:**
Verify that the entire project is organized correctly and all files are in place.

**Why this test?**
- Proves project is production-ready
- Proves nothing is missing
- Proves `.gitignore` is correct
- Proves documentation is complete

**How it works:**
- Check that all required files exist
- Check that all generated files are gitignored
- Check that project structure matches README
- Check that all notebooks run without errors

**Your task:**
1. Verify these files exist:
   - `.env` (optional, for LangSmith)
   - `.gitignore`
   - `requirements.txt`
   - `README.md`
   - `app.py`
   - `auth_db.py`
   - `ingest.ipynb`
   - `test_env.ipynb`
   - `rag_chain_test.ipynb`
   - `auth_test.ipynb`
   - `memory_test.ipynb`

2. Verify these folders exist:
   - `repo/` with `README.md`, `auth.py`, `user_service.py`
   - `pdf_file/` with `mysql_cheatsheet.pdf`

3. Verify these auto-generated files/folders exist:
   - `chroma_code/` (created by ingest.ipynb)
   - `users.db` (created by auth_db.py)
   - `code_history.db` (created by app.py)

4. Verify `.gitignore` contains:
   - `venv/`
   - `.env`
   - `chroma_code/`
   - `users.db`
   - `code_history.db`
   - `__pycache__/`
   - `*.pyc`
   - `.ipynb_checkpoints/`

5. Run `git status` and verify auto-generated files are ignored

**Research & Learn:**
- Why is project structure important?
- What happens if files are in wrong locations?
- How do you document project structure?
- What's the difference between `.gitignore` and `.gitkeep`?

**Definition of Done:**
All files present, auto-generated files are gitignored, project structure matches README.

**🔥 COMBO TASK (Level 8.6): Full System Validation – Everything Together**

**What we're achieving:**
Run the ENTIRE system end-to-end to validate everything works.

**Why this test?**
- Proves all modules work together
- Proves no integration bugs
- Proves system is production-ready
- Final checkpoint before deployment

**How it works:**
- Run all notebooks in sequence
- Test all UI features
- Test multi-user scenarios
- Verify all data persists

**Your task (Full Validation Checklist):**

1. **Notebooks (Sequential):**
   - [ ] Run `test_env.ipynb` → Ollama + LangChain work
   - [ ] Run `auth_test.ipynb` → User auth works
   - [ ] Run `ingest.ipynb` → Vector DB created
   - [ ] Run `rag_chain_test.ipynb` → RAG chain works
   - [ ] Run `memory_test.ipynb` → Memory works

2. **UI Testing (Sequential):**
   - [ ] Run `streamlit run app.py`
   - [ ] Signup as `alice@example.com`
   - [ ] Login as alice
   - [ ] Ask code question: "What does auth.py do?"
   - [ ] Verify answer + sources
   - [ ] Ask PDF question: "What is SELECT in MySQL?"
   - [ ] Verify answer + sources
   - [ ] Ask follow-up: "Can you explain more?"
   - [ ] Verify memory works (references previous context)
   - [ ] Click "🔄 New Thread"
   - [ ] Verify chat clears
   - [ ] Ask new question
   - [ ] Click "🚪 Logout"

3. **Multi-User Testing:**
   - [ ] Signup as `bob@example.com`
   - [ ] Login as bob
   - [ ] Verify bob doesn't see alice's history
   - [ ] Ask a question as bob
   - [ ] Logout
   - [ ] Login as alice
   - [ ] Verify alice sees only her history

4. **Data Persistence:**
   - [ ] Stop app (Ctrl+C)
   - [ ] Restart app
   - [ ] Login as alice
   - [ ] Verify alice's history is still there
   - [ ] Login as bob
   - [ ] Verify bob's history is still there

5. **LangSmith (Optional):**
   - [ ] If `.env` is configured, check LangSmith dashboard
   - [ ] Verify traces for all LLM calls
   - [ ] Verify traces show retrieval + generation

**Research & Learn:**
- What's the difference between unit tests and integration tests?
- Why is end-to-end testing important?
- How do you automate these tests?
- What's a regression test?

**Definition of Done:**
All notebooks run without errors. All UI features work. Multi-user isolation verified. Data persists across restarts. LangSmith traces visible (if configured).

**Practical Takeaway for Module 8:**
- **Keywords:** Full architecture validation, multi-user testing, data persistence, integration testing, end-to-end testing.
- **Why:** Module 8 is the final checkpoint. If everything passes here, the system is production-ready.
- **Key Insight:** Testing is not optional. A system that works in isolation might fail when all components interact. End-to-end testing catches these bugs.
- **Next Step:** After Module 8, you have a complete, production-ready codebase assistant. You can:
  1. Deploy it (Streamlit Cloud, Docker, etc.)
  2. Add new features (file upload, export, etc.)
  3. Optimize performance (caching, indexing, etc.)
  4. Scale to larger codebases (distributed ingestion, etc.)

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
