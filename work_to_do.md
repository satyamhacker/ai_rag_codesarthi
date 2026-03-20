---

## 🧩 **PROJECT: CODESARTHI – THE ALL-KNOWING CODEBASE ASSISTANT**

### 🎯 **What is it?**  
Ek AI-powered tool jo tumhare code repository ki documentation, code comments, READMEs, aur internal design notes ko ingest karta hai. Phir developers (ya naye joiners) usse natural language me sawaal puch sakte hain – jaise *“How does the authentication flow work?”* ya *“What is the purpose of the `user_service` module?”* – aur wo context‑aware, accurate jawab deta hai, aur pichli baaton ko yaad rakh sakta hai (conversation memory).

### 🧠 **What problem does it solve?**  
- **Onboarding time kam karna:** Naye developer ko codebase samjhne me hafte lagte hain. CodeSarthi usse minutes me relevant chunks de sakta hai.  
- **Documentation overhead:** Teams documentation likhna bhool jaati hain. CodeSarthi existing comments aur code structure se hi answers nikal leta hai.  
- **Context switching:** Jab ek developer multiple projects handle karta hai, to har baar doosre project ka flow yaad karne me time lagta hai. Assistant yaad rakhta hai.  
- **Knowledge silos:** Kisi ek senior ke dimaag me jo knowledge hai, wo assistant me store ho jata hai – reproducible.

### 💡 **Why it's great?**  
- **Real‑world use:** Har software company ke liye ye tool immediately useful hai.  
- **Covers all LangChain modules:** Document loaders (code files), splitters (chunking code comments), embeddings (code semantics), memory (conversation), streaming UI (ChatGPT‑like), observability.  
- **Extensible:** Aage jaake unit tests generate karna, code review assist, ya even PR descriptions likhna – sab is foundation par bana sakte ho.

---

## 🗺️ **Mission Flow (Index)**
1. **Mission 0: Base Camp Setup**  
   - Virtual Env, LangChain, Ollama  
2. **Mission 1: Local LLM – Pehla Code Sawaal**  
   - Model test, LangSmith tracing  
3. **Mission 2: Prompt & Chain – Technical Sawaal Banana**  
   - Prompt templates, pipe operator, output parser  
4. **Mission 3: Memory – Conversation Thread**  
   - Session ID, RunnableWithMessageHistory, SQLite  
5. **Mission 4: Data Ingest – Code Repository Ko Samajhna**  
   - Loaders (README, Markdown, code comments), chunking, embeddings, Chroma  
6. **Mission 5: Retrieval – Codebase Ki File**  
   - Retriever, similarity search, manual RAG, RetrievalQA  
7. **Mission 6: UI – Developer Dashboard**  
   - Streamlit login (user), session state, chat history, streaming, reset  
8. **Mission 7: Final Integration – CodeSarthi Zinda Hai**  
   - RAG + Memory + UI + Multi‑user + Observability  

---

## 🚀 **Mission 0: Base Camp Setup**  
*(Covers Module 1)*

**Level 0.1: Apna Kitchen Taiyar Kar**  
1. **Task:** Folder `codesarthi/` banao. Uske andar virtual environment `venv` create karo aur activate karo.  
2. **Logic:** Isolate dependencies – codebase ingestion tools won’t clash with system Python.  
3. **Definition of Done:** Terminal prompt shows `(venv)`.  
4. **Practical Takeaway:** Keywords: `python -m venv venv`, `source venv/bin/activate` (or `venv\Scripts\activate`). Virtual env ensures every project has its own clean space.

**Level 0.2: Ollama – Code Samajhne Wala Dimag**  
1. **Task:** Ollama daemon start karo (agar already running nahi hai). `ollama pull llama3.2` run karo. Phir terminal me `ollama run llama3.2` se test karo “What is a Python decorator?”.  
2. **Logic:** Ollama runs the LLM locally – no codebase leaves your machine.  
3. **Definition of Done:** You get a decent explanation from the model in the terminal.  
4. **Practical Takeaway:** Keywords: `ollama serve`, `ollama pull`, `ollama run`. The model must be downloaded and running before LangChain can use it.

**Level 0.3: LangChain + Friends Install**  
1. **Task:** Activate venv. Install: `langchain`, `langchain-community`, `langchain-chroma`, `python-dotenv`, `streamlit`, `pypdf`, `unstructured`.  
2. **Logic:** Modular installs keep dependencies light; `unstructured` helps parse code files.  
3. **Definition of Done:** `pip list` shows all these packages.  
4. **Practical Takeaway:** Keywords: `pip install`. LangChain is modular; install only what you need.

**Level 0.4: LangSmith – Developer Dashboard**  
1. **Task:** `.env` file banao. Add:  
   ```
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   LANGCHAIN_API_KEY=ls__your_key_here
   LANGCHAIN_PROJECT=codesarthi
   ```  
2. **Logic:** These environment variables automatically send traces to LangSmith.  
3. **Definition of Done:** After any chain runs, you’ll see traces in dashboard under project “codesarthi”.  
4. **Practical Takeaway:** Keywords: `LANGCHAIN_TRACING_V2`, `LANGCHAIN_API_KEY`. Tracing is key for debugging LLM apps.

**🔥 COMBO TASK (Level 0.5):**  
1. **Task:** Inside venv, write `test_env.py` that imports `ChatOllama` from `langchain_community.chat_models`, creates `llm = ChatOllama(model="llama3.2")`, invokes `llm.invoke("What is a unit test?")`, prints response. Run the script.  
2. **Logic:** Combines environment setup, Ollama connection, and LangSmith tracing.  
3. **Definition of Done:** Terminal prints answer; LangSmith dashboard shows a trace with the prompt and output.  
4. **Practical Takeaway:** You now have a working local LLM with full observability.

---

## 🚀 **Mission 1: Local LLM – Pehla Code Sawaal**  
*(Covers Module 1 invoke & Module 2 basics)*

**Level 1.1: LangChain Se Pehla Sawaal**  
1. **Task:** Create script `first_code_chat.py`. Use `ChatOllama` with `llama3.2`. Invoke `llm.invoke("What is dependency injection in programming?")`. Print response.  
2. **Logic:** `.invoke()` sends the prompt; the model returns an `AIMessage`.  
3. **Definition of Done:** Terminal prints a technical answer.  
4. **Practical Takeaway:** Keywords: `ChatOllama`, `.invoke()`. First step to talk to LLM programmatically.

**Level 1.2: Metadata Dekh – Token Ka Bill**  
1. **Task:** Store response in variable. Print `response.content` and `response.usage_metadata`.  
2. **Logic:** `AIMessage` holds both text and token counts.  
3. **Definition of Done:** You see input/output token numbers printed.  
4. **Practical Takeaway:** Keywords: `content`, `usage_metadata`. Tracking tokens helps optimise prompts and costs.

**Level 1.3: LangSmith Trace – Code Review Slip**  
1. **Task:** Re‑run the script. Go to LangSmith dashboard, find the trace for this run. Click to see the exact prompt sent and the output.  
2. **Logic:** LangSmith records every LLM call with full input/output.  
3. **Definition of Done:** You can see the exact conversation in the trace.  
4. **Practical Takeaway:** Observability is your best friend when debugging LLM behaviour.

**🔥 COMBO TASK (Level 1.4):**  
1. **Task:** Modify script to ask two technical questions: “What is SOLID?” and “Explain the Single Responsibility Principle”. Print both answers. Run the script and check LangSmith for two separate traces.  
2. **Logic:** Each `invoke` creates a separate trace.  
3. **Definition of Done:** Both answers printed; LangSmith shows two distinct traces.  
4. **Practical Takeaway:** You now understand how to invoke multiple independent queries and trace them.

---

## 🚀 **Mission 2: Prompt & Chain – Technical Sawaal Banana**  
*(Covers Module 2)*

**Level 2.1: Template – Senior Dev Ka Frame**  
1. **Task:** Create a `ChatPromptTemplate` using `from_messages` with a system message: “You are a senior software engineer, explaining code concepts clearly.” and a human message with variable `{query}`. Print the template’s `input_variables`.  
2. **Logic:** Variables allow reuse.  
3. **Definition of Done:** `input_variables` shows `['query']`.  
4. **Practical Takeaway:** Keywords: `ChatPromptTemplate.from_messages`. Prompt templates make queries consistent.

**Level 2.2: Chain – Assembly Line**  
1. **Task:** Chain the template, the LLM, and `StrOutputParser` using `|`. Print the type of the chain.  
2. **Logic:** Pipe operator creates a `RunnableSequence`.  
3. **Definition of Done:** The chain object is a `RunnableSequence`.  
4. **Practical Takeaway:** Keywords: `|` operator, `RunnableSequence`. LCEL enables modular pipelines.

**Level 2.3: Invoke – Concept Explanation**  
1. **Task:** Invoke the chain with `{"query": "Explain the Factory pattern"}`. Print the result.  
2. **Logic:** Parser extracts only the text from the LLM’s output.  
3. **Definition of Done:** Clean text output (no metadata).  
4. **Practical Takeaway:** Keywords: `StrOutputParser`. It’s essential to get plain text from the LLM.

**🔥 COMBO TASK (Level 2.4):**  
1. **Task:** Create another template with two variables: `{concept}` and `{language}`. Build a chain that asks “Explain {concept} in the context of {language}”. Test with different values.  
2. **Logic:** Multiple variables make prompts dynamic.  
3. **Definition of Done:** Chain runs without errors; output changes with language.  
4. **Practical Takeaway:** You now can build reusable, parameterised prompts for different scenarios.

---

## 🚀 **Mission 3: Memory – Conversation Thread**  
*(Covers Module 3)*

**Level 3.1: Session ID – Developer Session**  
1. **Task:** In your script, define `session_id = "dev_123"`.  
2. **Logic:** This ID identifies a conversation thread.  
3. **Definition of Done:** Variable defined.  
4. **Practical Takeaway:** Keywords: session_id. You’ll use this to isolate conversations.

**Level 3.2: History Wrapper – Yaad Rakhega**  
1. **Task:** Write a `get_session_history(session_id: str)` function that returns a `SQLChatMessageHistory` with `connection_string="sqlite:///code_history.db"`. Wrap your chain with `RunnableWithMessageHistory`.  
2. **Logic:** SQLite stores messages permanently.  
3. **Definition of Done:** After running, a file `code_history.db` appears.  
4. **Practical Takeaway:** Keywords: `SQLChatMessageHistory`, `RunnableWithMessageHistory`. Memory survives script restarts.

**Level 3.3: Multi‑Turn – Follow‑up Test**  
1. **Task:** Ask “What is an interface?” then follow with “How is it different from an abstract class?” using the history‑aware chain.  
2. **Logic:** The wrapper injects past messages automatically.  
3. **Definition of Done:** Second answer references the first.  
4. **Practical Takeaway:** The assistant now remembers context across turns.

**Level 3.4: DB Inspection – Knowledge Base**  
1. **Task:** Open `code_history.db` with an SQLite viewer (e.g., DB Browser). Find the `message_store` table. Verify messages for `session_id = dev_123`.  
2. **Logic:** Data is persisted.  
3. **Definition of Done:** You see the full conversation stored.  
4. **Practical Takeaway:** You can inspect the stored conversation history directly.

**🔥 COMBO TASK (Level 3.5):**  
1. **Task:** Start a conversation (2‑3 turns). Stop the script. Run again with the same `session_id`. Ask a new question – the LLM should remember the past. Check DB for new rows.  
2. **Logic:** Persistence works across runs.  
3. **Definition of Done:** Second run recalls earlier context; DB contains all messages.  
4. **Practical Takeaway:** You now have a persistent, stateful chatbot for each developer.

---

## 🚀 **Mission 4: Data Ingest – Code Repository Ko Samajhna**  
*(Covers Module 4, but with code files)*

**Level 4.1: Loader – README, Markdown, Comments**  
1. **Task:** Create a folder `repo/` with a few sample files: a README.md, a Python file with docstrings/comments, and a PDF doc. Use `DirectoryLoader` with `glob="**/*.md"` to load markdowns, `TextLoader` for `.py` files, and `PyPDFLoader` for PDFs. Collect all into a list of Documents.  
2. **Logic:** Different loaders handle different file types.  
3. **Definition of Done:** Print total documents – should count each file/page.  
4. **Practical Takeaway:** Keywords: `DirectoryLoader`, `TextLoader`, `PyPDFLoader`. You can ingest a whole codebase.

**Level 4.2: Chunking – Code Block Ko Logical Unit**  
1. **Task:** Use `RecursiveCharacterTextSplitter` with `chunk_size=1500`, `chunk_overlap=200`. Split all documents. Print number of chunks.  
2. **Logic:** Overlap ensures context isn’t lost at boundaries.  
3. **Definition of Done:** Number of chunks > original file count.  
4. **Practical Takeaway:** Keywords: `RecursiveCharacterTextSplitter`. Chunking is crucial for search quality.

**Level 4.3: Embedding – Code Semantics Ko Number Bana**  
1. **Task:** Instantiate `OllamaEmbeddings` with `llama3.2`. Test on a sample chunk: get its vector, print the length.  
2. **Logic:** Embeddings capture code semantics.  
3. **Definition of Done:** Vector length is constant (e.g., 3072).  
4. **Practical Takeaway:** Keywords: `OllamaEmbeddings`. Local embeddings keep your code private.

**Level 4.4: Vector Store – Chroma Code Library**  
1. **Task:** Create Chroma database from all chunks using `Chroma.from_documents()`. Set `persist_directory="./chroma_code"` and collection name `"code_knowledge"`.  
2. **Logic:** This stores vectors on disk.  
3. **Definition of Done:** Folder `chroma_code` appears with database files.  
4. **Practical Takeaway:** Keywords: `Chroma.from_documents`, `persist_directory`. You now have a searchable index of your codebase.

**🔥 COMBO TASK (Level 4.5):**  
1. **Task:** Load the created vector store back using `Chroma(persist_directory="./chroma_code", embedding_function=embeddings)`. Perform a similarity search with a query like “how to handle user authentication”. Print the top 3 chunks (their page_content).  
2. **Logic:** Retrieval is now possible.  
3. **Definition of Done:** Retrieved chunks contain relevant code snippets or comments.  
4. **Practical Takeaway:** You’ve built a semantic search engine for your codebase.

---

## 🚀 **Mission 5: Retrieval – Codebase Ki File**  
*(Covers Module 5)*

**Level 5.1: Retriever Interface**  
1. **Task:** Convert the Chroma store to a retriever using `.as_retriever(search_type="similarity", search_kwargs={"k": 3})`. Print its config.  
2. **Logic:** Retriever standardizes fetching.  
3. **Definition of Done:** Retriever config shows `k=3`.  
4. **Practical Takeaway:** Keywords: `as_retriever`. The retriever is a reusable component.

**Level 5.2: Manual RAG – Khud Ka Code Explanation**  
1. **Task:** Write a function that takes a query, retrieves documents via retriever, joins their `page_content` with `\n\n`, builds a prompt: `"Use the codebase context to answer:\n{context}\nQuestion: {question}"`, and invokes the LLM chain. Return the answer.  
2. **Logic:** You manually combine retrieval and generation.  
3. **Definition of Done:** The answer is based on the retrieved code/documentation.  
4. **Practical Takeaway:** You now understand the internal steps of RAG.

**Level 5.3: RetrievalQA – Automatic Code Assistant**  
1. **Task:** Use `RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)`. Test it with a query. Print the answer and the source documents.  
2. **Logic:** This chain automates everything.  
3. **Definition of Done:** Output dictionary contains `result` and `source_documents`.  
4. **Practical Takeaway:** Keywords: `RetrievalQA.from_chain_type`, `return_source_documents`. You now have a one‑line RAG pipeline.

**🔥 COMBO TASK (Level 5.4):**  
1. **Task:** Compare manual chain and RetrievalQA chain on a complex query (e.g., “What is the purpose of the `auth` module?”). Print both answers and the source documents from RetrievalQA.  
2. **Logic:** Both should give correct answers; source documents show origin.  
3. **Definition of Done:** Both answers correct; source documents show the exact files/comments used.  
4. **Practical Takeaway:** You now can choose between manual control and automatic speed.

---

## 🚀 **Mission 6: UI – Developer Dashboard**  
*(Covers Module 6)*

**Level 6.1: Login – Developer Profile**  
1. **Task:** Build a Streamlit app (`ui.py`). Create a SQLite table for users (email, hashed password). Add login form with `st.text_input` and `st.form`. On successful login, set `st.session_state.logged_in = True` and `session_id = email + "_code"`.  
2. **Logic:** Different developers have separate conversations.  
3. **Definition of Done:** After login, page shows “Welcome”.  
4. **Practical Takeaway:** Keywords: `st.session_state`, SQLite authentication. User isolation starts here.

**Level 6.2: Chat UI – ChatGPT Jaise**  
1. **Task:** After login, display `st.chat_input`. Store messages in `st.session_state.messages` as list of dicts (`{"role": "user", "content": ...}` and similarly for assistant). Loop through the list and display each with `st.chat_message`.  
2. **Logic:** This builds the visual conversation.  
3. **Definition of Done:** You can type and see messages appear.  
4. **Practical Takeaway:** Keywords: `st.chat_input`, `st.chat_message`. UI mimics ChatGPT.

**Level 6.3: RAG + Memory – Smart Code Assistant**  
1. **Task:** In the chat loop, when a user sends a message, call the **RetrievalQA chain** (from Mission 5) with the user’s query. Wrap it with `RunnableWithMessageHistory` (using the session_id from login) to inject past conversation. Display the assistant’s answer using `st.chat_message`.  
2. **Logic:** Combines codebase knowledge retrieval with memory.  
3. **Definition of Done:** Bot answers from the codebase and remembers earlier questions.  
4. **Practical Takeaway:** You’ve integrated the full RAG+Memory backend into the UI.

**Level 6.4: Streaming – Real‑time Response**  
1. **Task:** Replace the static chain invocation with streaming. Use `chain.stream(...)` and iterate over chunks. Use `st.write_stream` inside the assistant’s chat message to render the stream.  
2. **Logic:** Streaming reduces perceived wait.  
3. **Definition of Done:** Answer appears word by word.  
4. **Practical Takeaway:** Keywords: `st.write_stream`, `.stream()`. Streaming is essential for UX.

**Level 6.5: Reset – Naya Session**  
1. **Task:** Add a sidebar button “New Thread”. On click, clear `st.session_state.messages` and call `get_session_history(session_id).clear()` to wipe SQLite memory for that user.  
2. **Logic:** UI and backend memory both wiped.  
3. **Definition of Done:** After click, history disappears and bot forgets.  
4. **Practical Takeaway:** Keywords: `.clear()`. Reset gives users control.

**🔥 COMBO TASK (Level 6.6):**  
1. **Task:** Build the full Streamlit app with login, chat, streaming, reset, and RAG+memory. Test two users (log in with different emails) – they should have isolated conversations.  
2. **Logic:** Each user’s session is independent.  
3. **Definition of Done:**  
   - Each user sees their own chat.  
   - Answers are grounded in the codebase.  
   - Streaming works, reset works.  
   - LangSmith traces show both retrieval and generation.  
4. **Practical Takeaway:** You now have a multi‑tenant, production‑ready chatbot interface.

---

## 🚀 **Mission 7: Final Integration – CodeSarthi Zinda Hai**  
*(Covers everything together)*

**Level 7.1: Single File – Sab Kuch Ek Saath**  
1. **Task:** Combine all pieces into a single file `codesarthi_app.py`. It should:  
   - Set up LangSmith tracing via `.env`.  
   - Load persistent Chroma store (codebase knowledge).  
   - Create RetrievalQA chain.  
   - Wrap with `RunnableWithMessageHistory` using SQLite.  
   - Implement Streamlit UI with login, chat, streaming, reset.  
2. **Logic:** All components work together in one place.  
3. **Definition of Done:** The script runs without errors and loads the UI.  
4. **Practical Takeaway:** You’ve built a fully integrated application.

**Level 7.2: Run & Test – End‑to‑End**  
1. **Task:** Start the app with `streamlit run codesarthi_app.py`. Log in as two different developers. Ask technical questions that require both memory and codebase knowledge (e.g., first “What is the main function of `auth.py`?”, then “How does it validate tokens?”).  
2. **Logic:** Tests full stack.  
3. **Definition of Done:**  
   - Different users have separate conversations.  
   - Answers are accurate from the codebase.  
   - LangSmith shows traces for every interaction.  
   - Chat history persists after restart (SQLite).  
   - Reset works independently.  
4. **Practical Takeaway:** You’ve verified that the complete assistant works.

**🔥 COMBO TASK (Level 7.3):**  
1. **Task:** Add citations: when the bot answers, display the source file and line number (extracted from `response['source_documents']` metadata). For example, “Source: `auth.py`, line 42”.  
2. **Logic:** Citations increase trust.  
3. **Definition of Done:** Citations appear with every answer.  
4. **Practical Takeaway:** You now have a transparent, auditable AI assistant.

---

## 🏁 **MODULE 8 RECAP (Tera Status Report)**  
**Siksha Summary:**  
- You built a complete production‑ready **codebase assistant** that:  
  - Uses local LLM (Ollama) for privacy (code stays local).  
  - Ingests code repositories, READMEs, comments, and docs.  
  - Chunks, embeds, and stores them in a vector database (Chroma).  
  - Performs semantic retrieval for accurate answers.  
  - Maintains conversation memory per developer (SQLite).  
  - Provides a chat UI (Streamlit) with streaming and reset.  
  - Includes multi‑user login and isolated sessions.  
  - Leverages LangSmith for full auditability.  

**Guru-ji’s Warning:**  
*“Check kar le bhai! Kya tujhe yeh sab bina chat sheet ke karna aa gaya hai?  
- Virtual environment bana sakta hai?  
- Ollama background service ki tarah chalana?  
- Prompt template me technical variables inject karna?  
- Pipe operator se chain banana?  
- RunnableWithMessageHistory lagana aur SQLite file inspect karna?  
- Codebase files load karke chunks banana aur embeddings generate karna?  
- Chroma database me store aur similarity search karna?  
- Retriever interface aur RetrievalQA chain ka istemal?  
- Streamlit me login, session state, chat messages, streaming, reset – sab?  
- In sabko ek saath mila ke final code assistant bana sakta hai?  

Agar inme se ek bhi cheez mein doubt hai ya confuse hai, toh chup chaap peeche ja aur wapas execute kar. Aage badhne ka koi fayda nahi agar basics hile hue hain!”*

---

⚡ **GURUDAKSHINA (The Checkpoint):**  
**Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type ‘CONTINUE’ for the next set of missions – yani tujhe kuch aur nahi, tu ab apne man se koi bhi code repository le ke ye app bana sakta hai. Aage kya karna hai? Feedback de, ya naye developer‑friendly features add kar.**

==================================================================================
