llm course section --9, 10, 11...practical..
---

### 🗺️ PHASE 1: THE ROADMAP (Agentic Mastery)

**Module 1: Tooling Foundations (LLM ko Haath-Pair dena)**
* Concept of Tooling & Knowledge Cutoffs
* Tool Binding Mechanics (Ollama & Qwen/Llama)
* Search Tools Integration (DuckDuckGo & Brave)

**Module 2: Shastra Nirman (Building Custom Tools)**
* LangChain Tooling Guidelines & Decorators
* Deterministic Math Tools (Handling Hallucinations)
* Tool Metadata & Schema Inspection

**Module 3: The Manual Agent Loop (Dimaag ke Peeche ka Logic)**
* Transitioning from RAG to Agents
* The Three-Message Prompt Structure (Human, AI, Tool)
* Manual Tool Execution & Context Appending

**Module 4: Agentic Frameworks (Automation ka Jaadu)**
* Implementing `AgentExecutor` & `Structured Chat`
* Handling Multi-variable Tool Inputs
* Token Consumption Analysis with LangSmith

**Module 5: Browser ki Duniya (Playwright Automation)**
* Playwright Toolkit Setup in Jupyter
* Async Browser Operations & CSS Selectors
* Dynamic Web Extraction (Links, Tables, & JSON)

**Module 6: The Ultimate Project (Enterprise Agentic RAG)**
* Combining Playwright with Persistent Chroma DB
* Building a Bias Detection Agent
* Final Evaluation & Observability (LangSmith Mastery)

---

==================================================================================



### 🧩 Module 1: Tooling Foundations -> Level 1: Knowledge Cutoff Check

**1. The Concept**
Base LLMs ek "frozen box" mein hote hain. Unhe cutoff date ke baad ki duniya ka kuch nahi pata hota.

**2. Why? (Production Impact)**
* Agar LLM outdated info dega, toh user ka trust zero ho jayega.
* Stock market, medical news, ya elections jaise sensitive tasks fail ho jayenge.

**3. Practical Tasks (The Mission)**
* **Task 1:** Apne local machine pe **Ollama** start kar aur `qwen2.5` ya `llama3.1` model run kar terminal se.
* **Task 2:** Model se ek aisi cheez pooch jo 2024 ke end mein ya 2025 mein hui ho (e.g., "Who won the 2024 US Election?" ya latest space mission).
* **The Logic:** Dhyan se dekh response ko. Model ya toh hallucinate karega (jhoot bolega) ya gracefully mana karega. Note kar ki wo kaunsi cutoff date mention kar raha hai.
* **🔥 THE COMBO TASK:** Model se current date pooch, aur phir pichle 2 ghante ki news. Jab wo mana kare, toh samajh le ki bina "haath-pair" (tools) ke ye model ek band kamre mein qaid hai.

**4. Definition of Done**
* Terminal output mein model ka "Knowledge Cutoff" message ya factual denial dikhna chahiye.
* Tune identify kar liya hai ki model internet se live nahi hai.

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **Parametric Memory** ki limitation dekhi. Model ke weights mein data fix ho chuka hai. Keywords dhyan rakh: **Knowledge Cutoff**, **Parametric Memory**, aur **Hallucination**. Jab model pass accurate data nahi hota, wo pattern guess karta hai. Is problem ko solve karne ke liye humein **Tooling** chahiye.

---

### 🧩 Module 1: Tooling Foundations -> Level 2: Tool Binding Mechanics

**1. The Concept**
Binding ka matlab hai LLM ko bata dena ki "Bhai, tere paas ye specific tools available hain, unhe use kar."

**2. Why? (Production Impact)**
* Bina binding ke LLM ko pata hi nahi chalega ki uske paas Wikipedia ya Search ki power hai.
* Tool bind karne se LLM text ki jagah structured **JSON instruction** dena seekh jata hai.

**3. Practical Tasks (The Mission)**
* **Task 1:** Jupyter notebook mein `ChatOllama` initialize kar `langchain_community` se.
* **Task 2:** Ek fake tool list bana (List of objects) jisme ek `WikipediaQueryRun` tool ho.
* **Task 3:** Model par ek specific method use kar (`bind_tools` flag wala) aur usme apni tool list pass kar.
* **The Logic:** Ab model ko invoke kar same cutoff wale question se. Output mein `.content` check kar aur `.tool_calls` check kar. 
* **🔥 THE COMBO TASK:** Ek aisa prompt likh jo model ko force kare tool use karne pe. Output mein ek `JSON` structure dhoondh jisme `name` aur `args` likha ho. Agar ye JSON dikh gaya, toh tune model ka dimaag "Tool-Aware" bana diya hai.

**4. Definition of Done**
* `response.content` empty string honi chahiye.
* `response.tool_calls` mein tool ka naam aur search query arguments hone chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **Function Calling** ki neev rakhi hai. Method dhyan rakh: `bind_tools()`. Ye method model ke system prompt mein invisible instructions inject karta hai. Internal logic ye hai ki LLM ab seedha jawab dene ke bajaye ek **Payload** taiyar karta hai jo humare Python code ke liye hota hai.

---

### 🧩 Module 1: Tooling Foundations -> Level 3: Live Search Integration

**1. The Concept**
Web Search tools (DuckDuckGo/Brave) LLM ko internet ki "ankhein" dete hain taaki wo snippets padh sake.

**2. Why? (Production Impact)**
* Wikipedia static hai, par news har second badalti hai.
* Web search ke bina live pricing ya real-time event tracking impossible hai.

**3. Practical Tasks (The Mission)**
* **Task 1:** `langchain_community.tools` se `DuckDuckGoSearchRun` install aur import kar.
* **Task 2:** Is tool ko manually `.invoke()` karke dekh ek trending topic ke liye (e.g., "Current Gold Price").
* **The Logic:** Output format ko analyze kar. Kya wo poora HTML hai ya sirf ek summary snippet? Dhyan de ki `count` ya `region` jaise parameters se result kaise change hota hai.
* **🔥 THE COMBO TASK:** Brave Search ki API key setup kar (optional) ya DuckDuckGo ko hi bind kar apne Agent se. Prompt de: "Search for today's weather in Patna". Verify kar ki model ne tool call generate ki hai ya nahi.

**4. Definition of Done**
* Tool invocation se real-world updated data terminal pe print hona chahiye.
* Model ne tool call mein sahi search keywords generate kiye hon.

**5. Practical Takeaway (Asli Siksha)**
Bhai, tune seekha ki **API Wrappers** kaise kaam karte hain. Keywords: `DuckDuckGoSearchRun`, `BraveSearch`, `langchain-community`. Ye tools raw HTML ko filter karke LLM ko sirf kaam ki baat (**Snippets**) dete hain taaki **Context Window** na bhare.

---

🏁 **MODULE 1 RECAP (Tera Status Report)**
* **Siksha Summary:** Tune seekha cutoff kya hota hai, LLM ko tools ke baare mein kaise bataya jata hai (`bind_tools`), aur search tools se live data kaise khincha jata hai.
* **Guru-ji's Warning:** "Check kar le bhai! Kya tujhe `tool_calls` aur `.content` ke beech ka farq samajh aa gaya hai? Bina script run kiye bata sakta hai ki `bind_tools` method naya object return karta hai ya purane ko modify karta hai? Agar confuse hai, toh wapas ja aur logic dekh!"

⚡ **GURUDAKSHINA (The Checkpoint):** Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type **'CONTINUE'** for the next set of missions.

Chal bhai, haath pair jod, terminal khol! Aaj real knowledge ki aag lagate hain. Theory ho gayi, ab practically haath gande karne ka time hai!

---

### 🧩 Module 2: Shastra Nirman -> Level 1: The Decorator Power (@tool)

**1. The Concept**
Normal Python function ko LLM ke layak "Shastra" banane ke liye hum LangChain ka decorator use karte hain jo metadata (Resume) generate karta hai.

**2. Why? (Production Impact)**
* LLM code nahi padh sakta, wo sirf **Descriptions** aur **Schemas** padhta hai. 
* Agar description vague hui toh LLM "Tool Confusion" mein chala jayega aur galat function call kar dega.

**3. Practical Tasks (The Mission)**
* **Task 1:** `langchain_core.tools` se `@tool` decorator import kar.
* **Task 2:** Ek simple function bana jo kisi string ko uppercase mein convert kare.
* **Task 3:** Function ke upar `@tool` lagakar ek solid **Docstring** (triple quotes) likh. Is docstring mein explicitly bata ki ye tool kab use karna hai.
* **The Logic:** Python ke internal `inspect` module ka use karke LangChain tere function ka naam aur docstring nikaal lega.
* **🔥 THE COMBO TASK:** Function define karne ke baad, us tool object ki `.name` aur `.description` property print kar. Check kar ki kya wahi description aa rahi hai jo tune triple quotes mein likhi thi?

**4. Definition of Done**
* Terminal pe print karne par tool ka type `StructuredTool` dikhna chahiye.
* Tool ki description wahi honi chahiye jo tune docstring mein di hai.

**5. Practical Takeaway (Asli Siksha)**
Bhai, dhyan se sun: **Docstring is the Instruction**. LLM ke liye tera Python logic andhera hai, par tera docstring roshni hai. Keywords: `@tool`, **Docstring-as-Prompt**, **Metadata Extraction**.

---

### 🧩 Module 2: Shastra Nirman -> Level 2: Deterministic Math (Hallucination Killer)

**1. The Concept**
LLMs numbers predict karte hain, calculate nahi. Accuracy ke liye math operations ko Python CPU ko offload karna padta hai.

**2. Why? (Production Impact)**
* Production mein agar AI ne `345.67 * 12.3` galat bata diya, toh poora business logic fail ho sakta hai.
* Tooling se hum **Probabilistic** (guiding) ko **Deterministic** (exact) mein badalte hain.

**3. Practical Tasks (The Mission)**
* **Task 1:** Do alag functions bana: `add_numbers` aur `multiply_numbers`.
* **Task 2:** In functions mein **Type Hints** use kar (e.g., `a: int, b: int`). Ye LangChain ko batayega ki LLM se sirf integers mangne hain.
* **Task 3:** Dono functions ko `@tool` se decorate kar aur descriptive docstrings daal.
* **The Logic:** Tool ko manually test kar `.invoke()` use karke. Parameter mein dictionary pass kar: `{"a": 5, "b": 10}`.
* **🔥 THE COMBO TASK:** Ek list bana `tools = [add_numbers, multiply_numbers]`. Ab ek manual check kar ki kya LLM "multiply" sunne par sahi tool nikaal raha hai? (Filhal sirf object metadata inspect kar).

**4. Definition of Done**
* Tool `.invoke()` karne par exact integer output aana chahiye, koi text nahi.
* Dictionary input pass karne par valid response milna chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, tune seekha **Strict Typing**. Keywords: **Type Hints**, **args_schema**, **Pydantic Validation**. LangChain background mein Pydantic use karke check karta hai ki LLM ne kachra data toh nahi bhej diya tool ke liye.

---

### 🧩 Module 2: Shastra Nirman -> Level 3: Schema Inspection (The X-Ray)

**1. The Concept**
LLM ko tool bhejne se pehle, LangChain ek JSON schema banata hai. Ye schema dekhna aana chahiye taaki debugging asaan ho.

**2. Why? (Production Impact)**
* Agar schema mein data type `Any` aa raha hai, toh LLM string ki jagah list bhej sakta hai aur tera server crash kar sakta hai.
* Production integration ke waqt external APIs ko yahi schema chahiye hota hai.

**3. Practical Tasks (The Mission)**
* **Task 1:** Level 2 wale `add_numbers` tool ko utha.
* **Task 2:** Tool object ki `.args_schema.schema()` property ko print kar. 
* **The Logic:** Output mein JSON dhoondh. Kya wahan `properties` ke andar `a` aur `b` ka type `integer` likha hai?
* **🔥 THE COMBO TASK:** Ek function bana jisme type hints mat daal. Uska schema print kar. Phir wahi function type hints ke saath bana aur schema compare kar. Fark dekh aur bheja fry hone se bacha!

**4. Definition of Done**
* Terminal pe tool ka internal JSON schema print hona chahiye.
* Schema mein parameters, types aur descriptions clear dikhni chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **Auto-Generated Schemas** ka power dekha. Keywords: **JSON Schema**, **Pydantic Model**, **Structured Input**. Tera tool ek mini-API ban chuka hai jiske paas apna "Swagger" documentation hai.

---

🏁 **MODULE 2 RECAP (Tera Status Report)**
* **Siksha Summary:** Tune custom tools banaye, docstrings se AI ko instruct kiya, math logic offload kiya, aur tools ka "X-ray" (schema) nikala.
* **Guru-ji's Warning:** "Check kar le bhai! Kya tujhe yeh sab bina chat sheet ke karna aa gaya hai? Agar docstring miss kar di toh tool andha hai. Agar type hints miss kiye toh schema kachra hai. Agar inme se ek bhi cheez mein doubt hai, toh chup chaap peeche ja aur wapas execute kar!"

⚡ **GURUDAKSHINA (The Checkpoint):** Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type **'CONTINUE'** for the next set of missions.

Chal bhai, haath pair jod, terminal khol! Aaj real knowledge ki aag lagate hain. Theory ho gayi, ab practically haath gande karne ka time hai!

---

### 🧩 Module 3: The Manual Agent Loop -> Level 1: The Three-Message Scratchpad

**1. The Concept (Ultra-Short)**
LLMs "Ghajini" hote hain (stateless). Har step ko ek message array mein save karna padta hai taaki context maintain rahe.



**2. Why? (Production Impact)**
* Agar messages ka order bigda ya `id` miss hui, toh API 400 error degi.
* Bina history ke LLM ko pata hi nahi chalega ki usne kaunsa tool manga tha.

**3. Practical Tasks (The Mission)**
* **Task 1:** `langchain_core.messages` se `HumanMessage`, `AIMessage`, aur `ToolMessage` import kar.
* **Task 2:** Ek khali list bana `messages = []`. User ka ek tough query (e.g., math + news) is list mein `HumanMessage` banakar append kar.
* **Task 3:** `llm_with_tools` ko invoke kar aur jo response aaye, usko list mein `AIMessage` ki tarah append kar.
* **The Logic:** Dhyan de, `response.tool_calls` check karna zaroori hai. Agar LLM ne tool manga hai, toh hi aage badhna hai.
* **🔥 THE COMBO TASK:** Pura conversation state verify kar. List ki length exactly 2 honi chahiye aur second message mein `tool_calls` ka JSON metadata hona chahiye.

**4. Definition of Done (Verification)**
* `len(messages)` is 2.
* `messages[1]` ke andar valid tool instructions (name aur args) maujood hain.

**5. Practical Takeaway (Asli Siksha)**
Bhai, tune **Conversation State** manage karna seekha. Keywords: **Stateful Memory**, **Message Roles**, **Metadata Persistence**. LLM ko lagta hai wo soch raha hai, par asliyat mein tu usko har baar pichli poori kahani bhej raha hai!

---

### 🧩 Module 3: The Manual Agent Loop -> Level 2: Manual Trigger (The Executioner)

**1. The Concept (Ultra-Short)**
LLM sirf "Order Ticket" deta hai, khana Python banata hai. Hum `tool_calls` ko padh kar actual function run karenge.

**2. Why? (Production Impact)**
* LLM khud math nahi kar sakta, wo sirf command bhejta hai.
* Agar execution logic mein error handling nahi hai, toh pura agent crash ho jayega.

**3. Practical Tasks (The Mission)**
* **Task 1:** `AIMessage` ke andar `tool_calls` par loop chala.
* **Task 2:** Tool ka naam extract kar aur use `.lower()` kar (defensive coding!).
* **Task 3:** Apne `list_of_tools` dictionary se tool object nikal aur use `.invoke()` kar LLM ke diye gaye arguments ke saath.
* **The Logic:** Execution ke baad ek `ToolMessage` object bana. Isme do cheezein CRITICAL hain: `content` (result) aur `tool_call_id` (jo AI message se match karni chahiye).
* **🔥 THE COMBO TASK:** Is `ToolMessage` ko apni `messages` list mein append kar. Ab teri list ki length 3 honi chahiye.

**4. Definition of Done (Verification)**
* `ToolMessage` successfully create hua aur list mein add hua.
* `tool_call_id` wahi hai jo AI ne maangi thi.

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **Action-Observation Bridge** banaya. Keywords: **Dynamic Mapping**, **Lowercasing Sanitization**, **ID Matching**. Agar ID galat hui, toh LLM "Disconnected tool response" ka error dega.

---

### 🧩 Module 3: The Manual Agent Loop -> Level 3: The Final Synthesis (Closing the Loop)

**1. The Concept (Ultra-Short)**
Ab LLM ke paas Sawal hai, uski Soch hai, aur Tool ka Jawab (Data) hai. Ab wo final human-readable answer banayega.

**2. Why? (Production Impact)**
* Raw tool output (JSON/HTML) user ko dikhana bekar UX hai.
* LLM raw data ko summarize karke "Grounding" (sachai) verify karta hai.

**3. Practical Tasks (The Mission)**
* **Task 1:** Apni 3-messages wali list utha aur use wapas `llm_with_tools.invoke()` mein pass kar.
* **Task 2:** Output ka `.content` print kar.
* **The Logic:** Dhyan se dekh, is baar LLM `tool_calls` nahi dega, balki seedha Text Answer dega kyunki uski "Observation" poori ho chuki hai.
* **🔥 THE COMBO TASK:** Check kar ki kya final answer mein Wikipedia ya Math tool ka data use hua hai? LLM ko prompt de ki source zaroor bataye.

**4. Definition of Done (Verification)**
* Terminal pe ek clean natural language answer print hona chahiye.
* Answer factually sahi hona chahiye (e.g., accurate math sum ya correct election info).

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **End-to-End Agent Lifecycle** poori ki. Keywords: **Data Synthesis**, **Response Grounding**, **Loop Closure**. Tune bina kisi high-level library ke ek Agent ka dimaag (logic loop) khud code se build kar liya hai!

---

🏁 **MODULE 3 RECAP (Tera Status Report)**
* **Siksha Summary:** Tune seekha RAG se Agent pe kaise switch karte hain, 3-message structure (`Human`, `AI`, `Tool`) manage karna, aur manually tool calls ko execute karke context append karna.
* **Guru-ji's Warning:** "Check kar le bhai! Kya tujhe samajh aaya ki `ToolMessage` mein `tool_call_id` kyu zaroori hai? Agar list mein messages ka order badal gaya toh kya hoga? Agar inme se ek bhi cheez mein doubt hai, toh wapas ja aur manual loop firse chala. Aage Frameworks tabhi samajh aayenge jab ye manual logic crystal clear ho!"

⚡ **GURUDAKSHINA (The Checkpoint):** Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type **'CONTINUE'** for the next set of missions.

Chal bhai, haath pair jod, terminal khol! Aaj real knowledge ki aag lagate hain. Theory ho gayi, ab practically haath gande karne ka time hai!

---

### 🧩 Module 4: Agentic Frameworks -> Level 1: Replacing Manual Loops (`AgentExecutor`)

**1. The Concept (Ultra-Short)**
Jo pichle module mein tune manual `if-else` aur `for loop` se tool execute kiya tha, ab wo kaam LangChain ki factory-made motor (**AgentExecutor**) karegi.

**2. Why? (Production Impact)**
* Manual loops 5-10 tools ke baad "Maintenance Nightmare" ban jate hain.
* Frameworks mein built-in error handling aur retry logic hota hai jo tere custom script mein nahi tha.

**3. Practical Tasks (The Mission)**
* **Task 1:** `langchain.agents` se `initialize_agent` aur `AgentType` import kar.
* **Task 2:** Apne LLM aur Tools ki list ko ek single function call mein "bind" kar.
* **Task 3:** Ek specific flag enable kar (`verbose`) taaki terminal pe LLM ka "Thought" process dikhe.
* **The Logic:** Agent ko bata ki tu usey as a reasoning engine use kar raha hai. Check kar ki kya wo `Thought`, `Action`, `Observation` ka loop khud hi chala raha hai?
* **🔥 THE COMBO TASK:** Ek query bhej: "What is 10 plus 20 and tell me a joke". Verify kar ki wo pehle math tool use karta hai ya joke sunata hai?

**4. Definition of Done (Verification)**
* Terminal pe Green/Blue text mein `Thought:` aur `Action:` ke logs dikhne chahiye.
* Bina koi manual `loop` likhe final answer milna chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, tune seekha **Orchestration Abstraction**. Keywords: `AgentExecutor`, `verbose=True`, `ReAct Framework`. Ab LLM ek manager ban gaya hai jo khud Python code ko orders deta hai.

---

### 🧩 Module 4: Agentic Frameworks -> Level 2: Structured Chat (Multi-Variable Handling)

**1. The Concept (Ultra-Short)**
Standard Agents aksar single string bhejte hain. **Structured Chat** agent complex JSON schemas handle karta hai (jaise `a=10, b=20`).

**2. Why? (Production Impact)**
* Math tools ya complex APIs tab fail ho jati hain jab LLM sirf ek string bhej deta hai (e.g., `"10, 20"`).
* Production grade systems mein strictly typed JSON parameters zaroori hain crash rokne ke liye.

**3. Practical Tasks (The Mission)**
* **Task 1:** `AgentType` enum mein se `STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION` choose kar.
* **Task 2:** Is naye type ke saath agent initialize kar.
* **Task 3:** Query de: "Multiply 456 by 123".
* **The Logic:** Terminal logs mein dhyan se dekh `Action Input:` ko. Kya wo ab ek proper JSON dictionary `{ "a": 456, "b": 123 }` hai?
* **🔥 THE COMBO TASK:** Ek aisa tool bind kar jisme 3 arguments hon (e.g., `calculate_roi`). Check kar ki kya agent teeno parameters ko sahi JSON keys mein map kar pa raha hai?

**4. Definition of Done (Verification)**
* Terminal log mein `Action Input` ek valid JSON object hona chahiye.
* Multi-input math functions bina kisi manual parsing ke execute hone chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **JSON Schema Enforcement** seekha. Keywords: `StructuredChat`, `Pydantic-based Tools`, `Multi-variable routing`. Isse LLM ki "hallucination in formatting" khatam ho jati hai.

---

### 🧩 Module 4: Agentic Frameworks -> Level 3: Token Burn & Observability (LangSmith)

**1. The Concept (Ultra-Short)**
Agent smart hai par "Kharchila" hai. LangSmith se hum check karenge ki ek chote answer ke liye agent ne kitne tokens phoonk diye.

**2. Why? (Production Impact)**
* Agents iterative hote hain (repeat loops). Ek query mein 3,000+ tokens udh sakte hain, jo bill asmaan pe le jayega.
* LangSmith ke bina tu andheron mein teer chala raha hai; tujhe pata hi nahi chalega kab tool fail hua.

**3. Practical Tasks (The Mission)**
* **Task 1:** `os.environ` mein `LANGCHAIN_TRACING_V2` ko `"true"` set kar.
* **Task 2:** Apni LangSmith API key configure kar terminal mein.
* **Task 3:** Ek multi-step query bhej (e.g., math + search).
* **The Logic:** Safari/Chrome mein LangSmith dashboard khol. Trace graph dekh. Check kar ki kya LLM ne tool use karne se pehle "Thought" generate kiya tha?
* **🔥 THE COMBO TASK:** LangSmith mein total token count dekh. Manual tool call (Module 1) aur Agent call ka kharcha compare kar.

**4. Definition of Done (Verification)**
* LangSmith dashboard pe ek naya "Project" aur uske andar "Trace" dikhna chahiye.
* Trace mein `AgentExecutor` -> `LLMChain` -> `Tool` ka visual tree hona chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, tune **AI Observability** ka chashma pehan liya hai. Keywords: **Tracing**, **Latency Tracking**, **Token Consumption Analysis**. 1,300 tokens vs 3,800 tokens ka fark dekh kar tujhe samajh aayega ki "Agency" ki keemat kya hai!

---

🏁 **MODULE 4 RECAP (Tera Status Report)**
* **Siksha Summary:** Tune manual loops ko framework (`AgentExecutor`) se replace kiya, multi-variable tools ke liye `Structured Chat` setup kiya, aur LangSmith se token ki "craziness" monitor ki.
* **Guru-ji's Warning:** "Check kar le bhai! Kya tujhe pata hai ki `Structured Chat` kyu use kiya standard ki jagah? Kya tu LangSmith mein tool ka input/output dekh pa raha hai? Agar tokens ka bill nahi bachana seekha, toh koi company tujhe hire nahi karegi. Bheja fry limit reached! Level 3 tak cover kar liya hai. Type 'CONTINUE' for the rest of the levels/modules."

⚡ **GURUDAKSHINA (The Checkpoint):** Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type **'CONTINUE'** for the next set of missions.

Chal bhai, haath pair jod, terminal khol! Aaj real knowledge ki aag lagate hain. Theory ho gayi, ab practically haath gande karne ka time hai!

---

### 🧩 Module 5: Browser ki Duniya -> Level 1: Playwright Setup & Loop Patching

**1. The Concept (Ultra-Short)**
Playwright ek actual browser (Chromium) chalata hai. Jupyter Notebooks mein async code chalane ke liye humein event loop ko "patch" karna padta hai.



**2. Why? (Production Impact)**
* Bina `nest_asyncio` ke, Jupyter mein Playwright start hote hi `RuntimeError` dega.
* Modern web apps (React/Angular) bina browser render kiye blank page deti hain; normal scrapers wahan fail ho jate hain.

**3. Practical Tasks (The Mission)**
* **Task 1:** Terminal mein `playwright` aur `nest_asyncio` install kar. Browser binaries download karne wala specific command zaroor run karna (Warna engine missing bolega).
* **Task 2:** Notebook ke top par `nest_asyncio` ko apply kar. 
* **The Logic:** Dhyan rakh, Playwright asynchronous hota hai. Iska matlab humein `await` keyword ka use karna padega har line pe jo browser se baat karti hai.
* **🔥 THE COMBO TASK:** Ek async browser instance create kar `create_async_playwright_browser` utility se. Check kar ki kya bina error ke memory mein ek browser session start ho raha hai?

**4. Definition of Done (Verification)**
* `nest_asyncio.apply()` run karne par koi error nahi aana chahiye.
* Playwright binaries (Chromium) correctly install ho chuki hon.

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **Asynchronous Event Loop Conflict** solve kiya. Keywords: `nest_asyncio`, `Headless Browser`, `Async Event Loop`. Jupyter pehle se ek loop chala raha hota hai, isliye humein "Nested Loop" allow karna padta hai.

---

### 🧩 Module 5: Browser ki Duniya -> Level 2: Toolkit Initialization & Filter

**1. The Concept (Ultra-Short)**
`PlaywrightWebBrowserToolkit` ek bundle hai. Isme 7-8 specialized tools (click, navigate, extract) ek saath aate hain.

**2. Why? (Production Impact)**
* Saare tools ek saath Agent ko dena "Token Suicide" hai. Agent confuse ho jayega.
* Production mein hum sirf wahi tools nikalte hain jinse humein "DOM manipulation" karni hai.

**3. Practical Tasks (The Mission)**
* **Task 1:** Apne async browser ko `PlaywrightWebBrowserToolkit.from_browser()` mein pass karke ek `toolkit` object bana.
* **Task 2:** `toolkit.get_tools()` method use karke saare tools ki list nikaal.
* **Task 3:** Ek loop chala kar sirf do specific tools isolate kar: `Maps_browser` (ya `Maps_browser`) aur `get_elements`.
* **The Logic:** Tool objects ko unke `.name` property se match kar. Inhe alag variables mein save kar taaki hum inko Agent ke bina manually test kar sakein.
* **🔥 THE COMBO TASK:** In isolated tools ka description print kar. Check kar ki kya `get_elements` tool CSS selectors accept karta hai?

**4. Definition of Done (Verification)**
* Teri list mein sirf wahi tools hone chahiye jo navigation aur element extraction ke liye zaroori hain.
* Tools ka count verify kar, bundle mein total 7-8 tools hone chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, tune **Granular Tool Filtering** seekha. Keywords: `from_browser`, `get_tools`, `Isolated Toolkit`. Agent ko poora toolbox dene ke bajaye sirf "Screwdriver" aur "Hammer" dena seekh liya tune.

---

### 🧩 Module 5: Browser ki Duniya -> Level 3: Manual Extraction (The Unit Test)

**1. The Concept (Ultra-Short)**
Agent ko kaam pe lagane se pehle, hum khud "Driver" ban kar browser chalayenge aur data kheenchiye (`arun` method se).

**2. Why? (Production Impact)**
* Agar manually data nahi aa raha, toh Agent bhi kuch nahi kar payega. 
* CSS selectors (like `td`, `tr`) verify karna zaroori hai warna "Empty List" return hogi.

**3. Practical Tasks (The Mission)**
* **Task 1:** Navigating tool ka `.arun()` method use kar aur ek intranet URL (e.g., `http://eapp.swami.com/employee`) par jao. 
* **Task 2:** `get_elements` tool ko trigger kar. Selector mein `td` tag ka use kar.
* **Task 3:** Attributes parameter mein `innerText` pass kar taaki sirf readable text mile.
* **The Logic:** Kyunki ye async hai, har tool call ke aage `await` lagana mat bhoolna. Check kar ki kya Karthik ka data (Salary: 4000) output array mein dikh raha hai?
* **🔥 THE COMBO TASK:** Ek aisi query likh jo poore table ka raw text extract kare aur use terminal pe format karke dikhaye.

**4. Definition of Done (Verification)**
* Terminal pe employee table ka raw text data dikhna chahiye.
* Navigation success status `True` aana chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, tune **Browser Unit Testing** seekha. Keywords: `.arun()`, `CSS Selectors`, `innerText Extraction`. Tune ye prove kar diya ki browser site tak pahunch sakta hai aur data "scrap" kar sakta hai.

---

### 🧩 Module 5: Browser ki Duniya -> Level 4: The Web Extraction Agent (Final Boss)

**1. The Concept (Ultra-Short)**
Ab Agent khud browser handle karega, table padhega, average calculate karega aur JSON format mein jawab dega.

**2. Why? (Production Impact)**
* Humans ko table scan karne mein time lagta hai, Agent seconds mein multi-step logic (Go -> Extract -> Calculate) poora kar deta hai.
* "JSON Decode Error" handle karna seekhna zaroori hai kyunki unstructured web data aksar messy hota hai.

**3. Practical Tasks (The Mission)**
* **Task 1:** `STRUCTURED_CHAT` agent initialize kar apne filtered tools ke saath.
* **Task 2:** Ek complex prompt likh: "URL pe jao, table extract karo, aur saare employees ki salary ka average batao. Output strictly JSON hona chahiye."
* **Task 3:** `await agent.arun()` call kar.
* **The Logic:** Agent pehle navigation tool chalayega, phir data extract karega. Agar LLM "Karthik: 4000" aur baki data padh leta hai, toh wo math logic use karke `2022.22` average calculate karega.
* **🔥 THE COMBO TASK:** Check kar ki kya agent "JSON formatting" instructions follow kar raha hai? Agar output mein raw text aa raha hai, toh prompt mein "Expert persona" add kar.

**4. Definition of Done (Verification)**
* Final output ek valid JSON hona chahiye.
* Salary average `2022.22` (approx) terminal pe dikhna chahiye.
* Trace mein `Maps_browser` -> `extract_text` ka sequence dikhna chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **Multi-Step Agentic Workflow** master kar liya. Keywords: `Structured Chat Agent`, `JSON Schema Extraction`, `Reasoning + Math`. Tune ek local LLM (Ollama) ko itna smart bana diya ki wo live web data process karke analytical report de raha hai.

---

🏁 **MODULE 5 RECAP (Tera Status Report)**
* **Siksha Summary:** Tune Playwright toolkit setup kiya, async browser operations handle kiye, CSS selectors se manual scraping ki, aur ek analytics agent banaya jo web data process karta hai.
* **Guru-ji's Warning:** "Check kar le bhai! Kya tujhe `arun` aur `run` ka fark pata hai? Kya tune `nest_asyncio` lagaya? Agar agent 'JSON decode error' de raha hai, toh ghabra mat, wo web data ki complexity hai. Local LLM (Llama 3.2/3.3) upgrade kar agar performance slow hai. Level 4 tak sab done hai toh aage badh!"

⚡ **GURUDAKSHINA (The Checkpoint):** Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type **'CONTINUE'** for the next grand project module.

Chal bhai, haath pair jod, terminal khol! Aaj real knowledge ki aag lagate hain. Theory ho gayi, ab practically haath gande karne ka time hai! 

Bhai, ye finale hai! Ab tak tune jo seekha hai—Tools, Agents, RAG, aur Playwright—un sabko mila kar ek **Enterprise Grade Bias Detection Agent** banana hai. 

---

### 🧩 Module 6: Enterprise Agentic RAG -> Level 1: Persistence & Warm-up

**1. The Concept (Ultra-Short)**
Bar-bar PDF split aur embed karke paise aur time barbaad nahi karte. Hum purane persisted **Chroma DB** ko direct connect karenge.

**2. Why? (Production Impact)**
* Real world mein TBs of data hota hai. Har baar ingestion pipeline chalana impossible hai.
* Persisted DB se connection restore karna system ka startup time 90% kam kar deta hai.

**3. Practical Tasks (The Mission)**
* **Task 1:** VS Code mein naya notebook bana aur `.env` file load kar. Purane sections se Playwright initialization ka code le aao.
* **Task 2:** `Chroma` class use karke existing database directory (`../../section5_rag_document/chroma_db`) ka path point kar.
* **Task 3:** Embedding model hamesha wahi rakhna jo DB banate waqt tha (e.g., `llama3.2`).
* **The Logic:** Dhyan se dekh, yahan hum "Bypassing extraction/splitting" kar rahe hain. DB load hone ke baad, Agent ke bina ek simple similarity search maar: "what is bias testing".
* **🔥 THE COMBO TASK:** Check kar ki kya bina PDF upload kiye tera Vector Store text return kar raha hai? Agar documents aa rahe hain, toh tera persistence connection successful hai.

**4. Definition of Done (Verification)**
* Manual query run karne par DB se relevant text chunks terminal pe print hone chahiye.
* `persist_directory` galat hone par empty result aayega, ensure kar path sahi ho.

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **Vector Store Persistence** seekha. Keywords: `persist_directory`, `Chroma.from_directory`, `Relative Pathing`. Dhyan rakh: `..` matlab ek level upar. Agar path galat toh empty DB ka dukh milega!

---

### 🧩 Module 6: Enterprise Agentic RAG -> Level 2: Custom RAG Tool Nirman

**1. The Concept (Ultra-Short)**
LLM ko "Internal Knowledge" dene ke liye hum Retriever ko ek `@tool` mein pack karenge.

**2. Why? (Production Impact)**
* LLM ko agar saaf-saaf nahi bataya ki "Knowledge base yahan hai", toh wo general training se jawab dega jo shayad outdated ho.
* Tooling se Agent ko pata chalta hai ki proprietary documents kab dhoondhne hain.

**3. Practical Tasks (The Mission)**
* **Task 1:** Ek naya function bana `bias_detection_tool`. Iske upar `@tool("bias_detection")` decorator lagao.
* **Task 2:** Function ka **Docstring** (Tool Prompt) ekdum crystal clear rakh: *"You must use this tool for bias related testing in LLM"*.
* **Task 3:** Function ke andar `retriever.invoke(query)` chalao aur saare retrieved documents ka text ek single string mein join karke return karo.
* **The Logic:** Agent ko jab "bias" ke baare mein kuch milega, wo is tool ko trigger karega. 
* **🔥 THE COMBO TASK:** Purane Playwright tools ki list mein is naye `bias_detection` tool ko append kar. Verify kar ki teri final `tools` list mein ab Playwright aur RAG dono powers hain.

**4. Definition of Done (Verification)**
* Tool list print karne par `bias_detection` naya hathiyar dikhna chahiye.
* Docstring wahi honi chahiye jo humne specify ki thi.

**5. Practical Takeaway (Asli Siksha)**
Bhai, tune **Knowledge-as-a-Tool** concept master kiya. Keywords: `Retriever-to-Tool mapping`, `String Aggregation`, `Tool Encapsulation`. Agent ab internet aur private documents dono ka baap ban chuka hai.

---

### 🧩 Module 6: Enterprise Agentic RAG -> Level 3: The Audit Mission (Troubleshooting)

**1. The Concept (Ultra-Short)**
Ab Agent ko real world Times.com article audit karne bhejna hai internal PDF rules (Page 127) ke basis par.

**2. Why? (Production Impact)**
* Automated compliance aur legal auditing mein aise hi complex workflows use hote hain.
* Production mein state management (duplicate tools) system ko crash kar deti hai.

**3. Practical Tasks (The Mission)**
* **Task 1:** Ek heavy prompt likh: "Times.com article [URL] ka content nikal, aur `testing_and_evaluation_llm.pdf` ke page 127 ke rules ke hisaab se social bias check kar."
* **Task 2:** Agent run karne se pehle `tools.clear()` run kar aur firse exactly ek baar tools add kar (State cleanup).
* **Task 3:** GitHub Copilot ya AI suggestions ko blindly trust mat kar; `.page_content` attribute galti se use karne se bacho. Use `.invoke()` logic.
* **The Logic:** Agent pehle Playwright se news padhega, fir RAG se rules layega, aur end mein "Judge" bankar summary dega.
* **🔥 THE COMBO TASK:** Agent execute kar. Summary mein "Source Credibility", "Content Analysis", aur "Positive Bias Direction" check kar.

**4. Definition of Done (Verification)**
* Agent final response mein bataye ki article biased hai ya nahi based on the specific PDF.
* Terminal mein ReAct loop (Thought -> Action -> Observation) complete hona chahiye.

**5. Practical Takeaway (Asli Siksha)**
Bhai, tune **Contextual Grounding** seekha. Keywords: `tools.clear()`, `State Idempotency`, `Cross-Domain Reasoning`. Tune prove kar diya ki AI external world ko internal standards ke against measure kar sakta hai.

---

### 🧩 Module 6: Enterprise Agentic RAG -> Level 4: LangSmith Forensic (The Ultimate Proof)

**1. The Concept (Ultra-Short)**
LLM ke dimaag ka X-ray LangSmith se karenge. Dekhenge ki kya usne asliyat mein PDF ka Page 127 hi padha tha?

**2. Why? (Production Impact)**
* Client ko proof chahiye hota hai ki AI ne hawa mein teer nahi mara.
* "Evaluation" observability se upar ki cheez hai; ye AI ki accuracy verify karti hai.

**3. Practical Tasks (The Mission)**
* **Task 1:** Safari/Chrome mein LangSmith dashboard khol aur apna latest run select kar.
* **Task 2:** Trace mein check kar: `AgentExecutor` -> `LLMChain` -> `bias_detection`.
* **Task 3:** Tool call ke "Metadata" ya "Observation" block mein jaakar dekho.
* **The Logic:** Wahan check kar ki kya `source` metadata mein `testing_and_evaluation_llm.pdf` aur `page label 127` likha hai?
* **🔥 THE COMBO TASK:** Trace ka screenshot nikal aur verify kar ki `extract_text` ne poore page ka DOM sahi fetch kiya tha.

**4. Definition of Done (Verification)**
* LangSmith trace mein confirm ho jaye ki data Page 127 se hi aaya hai.
* Token count aur latency logs check ho jayein.

**5. Practical Takeaway (Asli Siksha)**
Bhai, yahan tune **LLM Evaluation & Grounding Verification** seekha. Keywords: `LangSmith Trace Analysis`, `Metadata Auditing`, `Observation Verification`. Notebook ka verbose bekar hai, asli "Magic" LangSmith mein dikhta hai!

---

🏁 **MODULE 6 RECAP (Tera Status Report)**
* **Siksha Summary:** Tune persistent DB connect kiya, RAG ko tool banaya, complex multi-tool audit mission chalaya, aur LangSmith se AI ki sachai pakdi.
* **Guru-ji's Warning:** "Check kar le bhai! Kya tujhe ab confidence hai ki tu kisi bhi company ka data use karke smart agent bana sakta hai? Bina LangSmith ke agent deploy mat karna, warna andhere mein teer chalate rahoge. Tune asali Agentic RAG seekh liya hai!"

⚡ **GURUDAKSHINA (The Checkpoint):** Bhai, tune poora path phod diya hai! 🎉 
Sare levels aur modules done hain. Screenshots ready hain toh dikha! 
Ab bata, kya naya "Vimaan" (Project) banana hai ya isi system ko production-ready scale karna hai? 

**"Mission Accomplished, Shishya! Terminal band mat kar, agli aag jaldi lagayenge!"**

==================================================================================
