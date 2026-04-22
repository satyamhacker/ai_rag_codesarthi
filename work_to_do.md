Chal bhai, haath pair jod, terminal khol! Aaj real knowledge ki aag lagate hain. Theory ho gayi, ab practically haath gande karne ka time hai! 

Tera notes scan kar liya maine. Total 13 distinct topics hain, matlab apna Module Count Rule ke hisaab se yeh ek hardcore 3-Module CTF banega. Sabse pehle apna master plan dekh le, phir sidha battleground mein utarte hain.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🗺️ GURU-JI'S MASTER ROADMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Modules: 3 | Total Levels: 13 | Estimated Completion Time: 8-10 hours
Difficulty: Intermediate to Advanced (Hardcore Production Testing)

📦 Module 1: The Core Metrics & Execution Engine
  ├── Level 1.1 — Fundamentals of Tool Calling & Correctness [🟢 Beginner]
  ├── Level 1.2 — Scoring Calculation & The ToolCall Class [🟡 Intermediate]
  ├── Level 1.3 — Local Verification vs Cloud Dashboard [🟢 Beginner]
  ├── Level 1.4 — Custom Tool Creation & Zero Trust [🟡 Intermediate]
  └── Level 1.5 — Agent Initialization & ReAct Workflow [🔴 Advanced]

📦 Module 2: Golden Datasets & Internal Extractions
  ├── Level 2.1 — Structuring the Golden Dataset [🟡 Intermediate]
  ├── Level 2.2 — DeepEval Cloud Sync (Push/Pull) [🟢 Beginner]
  ├── Level 2.3 — Custom AI Agent Invocation [🔴 Advanced]
  └── Level 2.4 — Extracting Intermediate Tool Steps [🔴 Advanced]

📦 Module 3: Assembly, Debugging & Advanced Tuning
  ├── Level 3.1 — Intermediate Steps Parsing & Scoping [🔴 Advanced]
  ├── Level 3.2 — Test Case Assembly & State Sync [🟡 Intermediate]
  ├── Level 3.3 — Evaluation Execution & For-Loop Debugging [🟡 Intermediate]
  └── Level 3.4 — Advanced Metric Configurations & Bug Avoidance [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bhai, roadmap ready hai! Kyunki tu eager shishya hai aur system loaded hai, main bina ruke seedha **Module 1** ki aag lagana shuru kar raha hoon. Terminal clear kar aur focus idhar la!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: The Core Metrics & Execution Engine → Level 1.1: Fundamentals of Tool Calling & Correctness [🟢 Beginner]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Agent ne user query sunkar exactly sahi API (tool) trigger kiya ya hallucinate kar diya? Yeh test karna hi Tool Calling Testing hai.

2. 💥 Why? (Production Impact)
- Agar AI wrong tool utha le (e.g., math function ki jagah database delete command), production system crash ya compromise ho jayega.
- AI inherently text generate karta hai, decision engine check karna zaroori hai.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: DeepEval library se `LLMTestCase` object setup kar. Isme apna `input` (query), `expected_tools` (kya chalna chahiye tha), aur `actual_tools_called` (AI ne galti se kya chalaya) define kar.
  The Logic: Yeh object quality inspector ko batayega ki AI ka report card kis base par judge karna hai.

  Task [2]: `ToolCorrectnessMetric` ka instance bana aur `measure()` method trigger kar upar wale test case par.
  The Logic: Yeh Contextual Relevance dekhega. String match nahi karega, smart grading system use karega.

  💥 THE CHAOS TASK (Break it to Master it):
  Jaan-boojh kar agent ko registry mein ek saath 50 tools assign kar de bina Semantic Router use kiye. Phir usko tool call karne bol. Error dekh. Agent confuse hoke hallucinate karega. Phir troubleshoot flowchart use kar: "ToolNotFoundException" aaya? Case sensitivity check kar. Log padh aur Modular approach se fix kar. Asli engineer error dekh ke darta nahi hai!

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output on Console: `Agent Score: 0.0` (agar actual aur expected miss-match kiya deliberately).
- 🕵️‍♂️ Under The Hood Verification: Script ke backend logs mein check kar ki `agent.run` hook properly `tool_invoked` log kar raha hai ya nahi.
- 💬 Quick Verify 1 (Core Concept): "Agar koi pooche — Tool Calling evaluation mein 'Decision Engine' kya check karta hai — toh kya bolega?"
- 💬 Quick Verify 2 (Comparison): "Basic String match aur DeepEval ToolCorrectnessMetric mein contextual relevance ka kya farq hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **ToolCorrectnessMetric:** AI ka report card.
- **LLMTestCase:** Woh answer sheet jo measure hoti hai. 
- ⚠️ **Anti-Pattern:** Ek hi agent ko saare tools ek saath de dena. Sahi tarika: Semantic Router se pehle domain decide kar, phir chhota subset of tools de.
- **Scalability Hook:** 10,000 requests par LLM ko bar-bar tools dikhana costly hai. Production mein hamesha Least Privilege Principle aur Semantic Routers use kar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: The Core Metrics & Execution Engine → Level 1.2: Scoring Calculation & The ToolCall Class [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Raw dictionaries use mat kar. `ToolCall` class strongly-typed evaluation enforce karti hai taaki typose fail na ho.

2. 💥 Why? (Production Impact)
- Dictionaries mein case sensitivity (e.g., `WebSearch` vs `web_search`) metric ko fail karti hai.
- Schema validation na hone se parser crash ho sakta hai runtime par.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: `ToolCall` class import kar. 2 objects bana (`finance_tool`, `calculator_tool`). Har ek mein `name`, `input`, aur `output` keys strictly define kar.
  The Logic: Yeh strongly typed objects hain. AI ko schema strictly follow karwayenge.

  Task [2]: Ek test case bana jisme Ground Truth (expected) 2 tools ho, par `actual_tools_called` mein sirf 1 pass kar.
  The Logic: Humein Ratio-based calculation dekhni hai. Kya metric partial credit deta hai ya zero karta hai?

  💥 THE CHAOS TASK (Break it to Master it):
  `expected_tools` mein object ki jagah directly ek raw Python dictionary pass karke test measure karne ki koshish kar. Crash hone de. Console mein Validation Error padh. Phir theek kar `ToolCall` object banakar. Pata hona chahiye ki type-checking fail hone par system kaise fat-ta hai!

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output on Console: `Tool Score: 0.5` (Partial credit awarded).
- 🕵️‍♂️ Under The Hood Verification: Metric evaluation ke details export kar (JSON/CSV) aur check kar ki internal mathematical loop ZeroDivisionError toh nahi phenk raha.
- 💬 Quick Verify 1 (Core Concept): "ToolScore mathematically kaise nikalta hai?"
- 💬 Quick Verify 2 (Comparison): "Raw dictionary approach vs ToolCall object mein error handling aur schema mein kya bada difference hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **ToolCall class:** Strongly typed, strict schema maintainer.
- **Ratio Score:** Correctly Used Tools divided by Total Tools. Formula safe hai.
- ⚠️ **Anti-Pattern:** `expected_tools` mein plain dictionary pass karna. Case mismatch se score 0 aayega.
- **Scalability Hook:** Production level exports mein hamesha PII Data Masking lagana zaroori hai taaki test logs mein passwords leak na hon.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: The Core Metrics & Execution Engine → Level 1.3: Local Verification vs Cloud Dashboard [🟢 Beginner]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Data cloud dashboard pe bhejna hai ya local air-gapped machine par evaluate karna hai? Yeh execution context decide karta hai.

2. 💥 Why? (Production Impact)
- Confidential bank/healthcare queries agar third-party portal par sync ho gayi toh data leak disaster hoga.
- CI/CD mein team ko central telemetry dekhni hoti hai, local mein developers ko privacy.

3. 🎯 Practical Tasks (The Mission)
  📚 Research & Answer Tasks (Conceptual Verification):
  - Task [1]: `metric.measure()` ka internal behavior track kar. Check kar ki kya yeh koi HTTP webhook call karta hai bahar?
  - Task [2]: `deepeval.evaluate()` ka architecture check kar. CI/CD pipelines (like pytest) mein yeh Confident AI portal ke sath kaise telemetry sync karta hai?

  💥 THE CHAOS TASK (Break it to Master it):
  Internet (Wi-Fi) disconnect kar de (simulate air-gapped environment). Ab `deepeval.evaluate()` run kar. ConnectionError ya Webhook fail aayega. Ab isko fix karne ke liye execution context change kar aur `metric.measure()` use kar. Dekh offline evaluate hota hai ya nahi!

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Air-gapped machine par bina error ke evaluation pass ho jana chahiye using local metric method.
- 💬 Quick Verify 1 (Core Concept): "Air-gapped environments mein DeepEval testing kaise ki jaati hai bina leak ke?"
- 💬 Quick Verify 2 (Comparison): "`metric.measure()` aur `deepeval.evaluate()` mein Data Confinement ka kya farq hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **metric.measure():** In-memory local execution. No telemetry. 
- **deepeval.evaluate():** Triggers webhook, portal dashboard sync.
- ⚠️ **Anti-Pattern:** Har local dev test ke liye `evaluate()` use karna, jisse dashboard trash se bhar jaye aur speed slow ho.
- **Scalability Hook:** Production CI/CD hamesha telemetry bhejta hai, par secure environments strict Data Confinement laws follow karte hain.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: The Core Metrics & Execution Engine → Level 1.4: Custom Tool Creation & Zero Trust [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Python function ko AI ke samajhne layak BaseTool mein convert karna using decorators and docstrings.

2. 💥 Why? (Production Impact)
- AI default functions nahi padh sakta. Bina schema aur description ke woh hallucinate karega aur parameter galat bheja toh application crash.
- API keys leak hone se bachana hai Zero Trust environment banakar.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: `os.environ` se `CONFIDENT_AI_API_KEY` ko pop (remove) kar. Zero trust local mode enforce kar.
  The Logic: Cloud portal pe data nahi bhejna hai, strictly local testing karni hai.

  Task [2]: Do math functions bana (add, multiply). Langchain ka `@tool` decorator use kar. Isme Type hints (`a: int`) aur proper `Docstring` daal.
  The Logic: Decorator in functions ko JSON schema mein wrap karega LLM consumption ke liye.

  💥 THE CHAOS TASK (Break it to Master it):
  Ek naya tool bana, `@tool` laga de par function ke andar `Docstring` mat likh. Phir LLM se us function ko call karwa. Agent fat jayega ya galti karega. Phir proper docstring likh ke verify kar ki description bina AI andha kyu hai.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output on Console: Print the tool attributes -> `Tool Name: add_numbers, Description: Adds two integer numbers... args: {'a': {'type': 'integer'}...}`
- 🕵️‍♂️ Under The Hood Verification: Check kar ki pydantic validation strictly 'int' enforce kar rahi hai ya LLM string pass karke prompt injection kar paa raha hai.
- 💬 Quick Verify 1 (Core Concept): "Decorator `@tool` internally ek python code ko LLM format mein kaise badalta hai?"
- 💬 Quick Verify 2 (Comparison): "Type hint aur Docstring dono AI ko kya alag-alag information sikhate hain?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **Zero Trust Environment:** API keys memory se pop karna.
- **@tool & Docstring:** Function ka instruction manual.
- ⚠️ **Anti-Pattern:** Function mein docstring na likhna. AI tool ka purpose hi nahi samajh payega.
- **Scalability Hook:** Production mein 50+ tools ke liye "Toolkits Pattern" (Microservices) use hota hai, single functions nahi.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: The Core Metrics & Execution Engine → Level 1.5: Agent Initialization & ReAct Workflow [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
AgentExecutor woh Manager hai jo LLM ki reasoning (Thought) aur Tools ke actions ko ReAct loop mein bind karta hai.

2. 💥 Why? (Production Impact)
- Normal LLM chain sirf text fekti hai, API fetch ya execute nahi kar sakti. 
- Agar loop parameters strictly handle nahi kiye, toh agent infinite loop mein fas kar lakhon ka API bill faad dega.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: Langchain se `initialize_agent` setup kar. Reasoning engine (LLM) ka `temperature=0` set kar.
  The Logic: Temp 0 matlab strict, zero creativity. Tools ko deterministic data chahiye, kahani nahi.

  Task [2]: AgentType `ZERO_SHOT_REACT_DESCRIPTION` use kar. Tools array pass kar aur safety ke liye `max_iterations` cap set kar.
  The Logic: Zero-shot agent bina examples ke tools ki docstrings padhkar kaam karega. Cap usko infinite loops se bachayega.

  🔥 COMBO TASK (Final Boss):
  Is pure module ko ek saath bind kar! Agent setup kar, `invoke({"input": "Add 5 and 10"})` trigger kar, aur verbose logging ON rakh.
  **Challenge:** Agent ko intentionally confuse kar (e.g., galat query de jo math tool se solve na ho) aur dekh ki Agent Loop Risk kaise handle hota hai max_iterations limit trigger hone tak. 

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output on Console (Verbose): `> Entering new AgentExecutor chain... Thought... Action... Action Input... Observation... Final Answer: 15`
- 🕵️‍♂️ Under The Hood Verification: Logs trace kar aur dekh ki Agent ne internally kitne iterations maare ReAct loop complete karne se pehle.
- 💬 Quick Verify 1 (Core Concept): "AgentExecutor aur normal LLM chain mein execution ka basic flow farq kya hai?"
- 💬 Quick Verify 2 (Parameter): "Tool calling agent mein `temperature` parameter 0 rakhna life-saving kyun hota hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **AgentExecutor:** ReAct loop manager (Thought -> Action -> Observation).
- **Agent Loop Risk:** `max_iterations` nahi lagaya toh infinite API calls.
- ⚠️ **Anti-Pattern:** Tools wale agent me `temperature=0.8` (high) rakhna. LLM hallucinate karke JSON schema tod dega.
- **Scalability Hook:** Scale par traditional text-parsing ReAct ki jagah native **OpenAI Functions** use hote hain reliable structure ke liye.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏁 MODULE 1 RECAP — Tera Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Siksha Summary:
- Tune DeepEval metric ka base measure karna seekha.
- Ratio-based scoring aur `ToolCall` se strictly typed objects banaye.
- Local vs Cloud dashboard telemetry difference practically test kiya.
- Zero Trust environment banake AI BaseTools setup kiye.
- ReAct loop mein AgentExecutor ko safely invoke karna seekha with strict parameters.

Guru-ji's Warning:
"Check kar le bhai! Kya tujhe yeh sab bina cheat sheet ke karna aa gaya hai? Agar inme se ek bhi cheez mein doubt hai ya confuse hai, toh chup chaap peeche ja aur wapas execute kar. Aage badhne ka koi fayda nahi agar basics hile hue hain!"

⚡ GURUDAKSHINA (The Checkpoint):
"Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type 'CONTINUE' for the next Module (Golden Datasets & Internal Extractions)."

--- ⏸️ OUTPUT LIMIT APPROACHING. Type 'CONTINUE' to get the next part.
✅ Completed so far : Level 1.1, Level 1.2, Level 1.3, Level 1.4, Level 1.5
⏳ Remaining       : Modules 2 and 3 (Levels 2.1 to 3.4)
📊 Progress        : 5 Levels done / 13 Levels total | Module 1 of 3

Chal bhai, break khatam! Terminal pe wapas aaja. Module 1 mein tune engine aur metrics ke basics hila diye hain. Ab **Module 2** mein hum production-grade data pipelines aur AI ki black-box executions ko cheer-phaad karke open karenge.

Focus level 100% chahiye idhar. Let’s go!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Golden Datasets & Internal Extractions → Level 2.1: Structuring the Golden Dataset [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Golden Dataset tera Master Answer Key hai. AI pass hoga ya fail, yeh is strict baseline data par depend karta hai.

2. 💥 Why? (Production Impact)
- AI naturally hallucinate karta hai. Bina ground truth ke CI/CD pipeline mein automated testing andhi ho jayegi.
- Production mein PII (user data) leak hone ka darr hota hai, isliye mock baseline lazmi hai.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: DeepEval framework se `ToolCall` instantiate kar. Apne math functions (add, multiply) ke exact `name` aur variables ki `input` dictionary map kar.
  The Logic: Yeh Data Extraction Accuracy badhayega. Strings ki jagah strictly typed objects compare honge.

  Task [2]: Ek python list (array) bana — tera Master Answer Key. Har scenario dictionary mein `question`, `expected_answer` (text), aur `expected_tools` (jo list tune Task 1 mein banayi) define kar.
  The Logic: Is array ko test runner loop karega. Yeh Dual Verification setup hai — text bhi check hoga aur backend tool bhi.

  💥 THE CHAOS TASK (Break it to Master it):
  Apne `expected_answer` ko "The sum is 15." set kar. Ab evaluator logic mein **Exact Match** (string `==` string) try kar. Agent ko answer dene de "15" ya "It is 15". Test fail hone de! 
  Ab samajh ki Shallow Testing kaise fail hoti hai. Isey theek karne ke liye Semantic Textual Similarity (STS) ya LLM-as-a-judge method ki taraf switch karne ka logic build kar taaki contextual relevance check ho, exact characters nahi.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output: Print kara ke dekh ki kitne scenarios load hue. "Loaded 2 scenarios in Golden Dataset."
- 🕵️‍♂️ Under The Hood Verification: `golden_dataset[0]['expected_tools'][0].name` property print karke verify kar ki ToolCall instance sahi se map hua hai.
- 💬 Quick Verify 1 (Core Concept): "Shallow Testing aur Deep Testing (Dual Verification) mein kya farq hai?"
- 💬 Quick Verify 2 (Comparison): "Exact Match string comparison AI evaluation mein anti-pattern kyun hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **Golden Dataset:** Baseline test scenarios array with questions, expected texts, and expected tool calls.
- **Dual Verification:** Text answer + backend Tool execution dono pass hone chahiye.
- ⚠️ **Anti-Pattern:** Exact Match use karna expected answer ke liye. Sahi tarika: STS ya Contextual Relevance use kar.
- **Scalability Hook:** Production mein testing ke liye real database export use mat karna (PII Data Leakage risk). Hamesha Fake/Synthetic Generation use kar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Golden Datasets & Internal Extractions → Level 2.2: DeepEval Cloud Sync (Push/Pull) [🟢 Beginner]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Apne local test data ko cloud pe sync karna (Push) aur khali object mein auto-populate karwana (Pull).

2. 💥 Why? (Production Impact)
- Team ke paas ek "Single Source of Truth" aur version control hona chahiye.
- Raw JSON ko manually python objects mein map karne ka code likhna fragile hota hai.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: CLI pe auth barrier cross kar (`login` command use karke). Apne local `EvaluationDataset` ko `.push()` command se cloud processing ke liye bhej aur usko ek unique `alias` de.
  The Logic: Tera data Confident AI dashboard pe as a central baseline save ho jayega.

  Task [2]: Ek completely empty `EvaluationDataset()` bana. Ab ispe wahi exact alias use karke `.pull()` method call kar.
  The Logic: Data Hydration trigger hogi. Framework cloud se data laake usko automatically `LLMTestCase` instances mein map kar dega bina kisi custom for-loop ke.

  💥 THE CHAOS TASK (Break it to Master it):
  Auth barrier bypass karne ki koshish kar. Script mein API key pop kar de aur phir push karne ki koshish kar. **Unauthorized 401** error aane de. Phir login verify kar. Uske baad, `pull` karte waqt alias mein spelling mistake kar aur dekh ki test_cases array zero/empty kyu reh gaya!

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output on Console: `Total cases hydrated: X` and print the first case input.
- 🕵️‍♂️ Under The Hood Verification: Hydrated object type check kar — kya array ke elements successfully `LLMTestCase` ban gaye hain?
- 💬 Quick Verify 1 (Core Concept): "Data Hydration technique developer ka time kaise bachati hai?"
- 💬 Quick Verify 2 (Behavior): "Agar Pull method fail hota hai, toh manual fallback kya hota hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **dataset.push / .pull:** Cloud sync aur Single Source of Truth ke liye.
- **Data Hydration:** Khali object ko cloud data se auto-populate karna.
- ⚠️ **Anti-Pattern:** JSON file read karke custom manual object mapping script likhna (fragile). Sahi tarika: `.pull()` ka auto-population use kar.
- **Security Check:** Cloud pe push karne se pehle PII sanitize zaroor kar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Golden Datasets & Internal Extractions → Level 2.3: Custom AI Agent Invocation [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Agent ke standard "Black Box" run ko bypass karke usko ek custom wrapper mein invoke karna taaki intermediate telemetry bacha saken.

2. 💥 Why? (Production Impact)
- Default invoke method Data Stripping karta hai, sirf final text deta hai. Agent galti kahan kar raha hai, yeh opaque execution mein pata nahi chalta.
- SOC2 compliance ke liye execution telemetry trace karna zaruri hai.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: Ek Asynchronous custom method bana (`async def`). Uske andar `agent_executor.invoke()` ko `await` ke saath call kar.
  The Logic: Async framework block nahi karega parallel testing ko, aur tera custom wrapper telemetry ko capture karne ka scope dega.

  Task [2]: Apne custom method ke andar dummy/sandbox database credentials inject karne ka placeholder bana.
  The Logic: Testing environment kabhi bhi real production resources hit nahi karna chahiye (Data mutation risk).

  💥 THE CHAOS TASK (Break it to Master it):
  Agent ko invoke karte waqt `.invoke("Check my balance")` seedha string pass kar de. Error trace padh. Tuje **Missing Argument** jaisa error dikhega. Kyun? Kyunki framework dictionary expect karta hai. Isey fix kar aur `{"input": user_question}` properly map karke bhej. Asli code fatne pe hi sikhata hai!

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output: `asyncio.run` se script execute kar aur result print kar. Output ek proper dictionary aani chahiye.
- 🕵️‍♂️ Under The Hood Verification: Debugger/Network tab nahi, print statement se check kar ki kya intermediate steps stripp out ho gaye ya bache hain (next level ki taiyari).
- 💬 Quick Verify 1 (Core Concept): "Standard invoke ko 'Black Box Execution' kyun kaha jata hai?"
- 💬 Quick Verify 2 (Async): "Testing pipelines mein synchronous LLM calls blockages kaise create karte hain?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **Custom Wrapper Method:** Transparent execution aur telemetry save karne ke liye.
- **Data Stripping:** Memory bachane ke liye frameworks by default internal logs mita dete hain.
- ⚠️ **Anti-Pattern:** Testing mein direct `agent.invoke()` use karna without a wrapper. Black box execution banega.
- **Compliance Hook:** SOC2/GDPR ke liye PII hatana aur steps record karna production logging (LangSmith/Datadog) mein mandatory hai.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Golden Datasets & Internal Extractions → Level 2.4: Extracting Intermediate Tool Steps [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Agent ka CCTV ON karna (`return_intermediate_steps`) aur kachre (raw logs) mein se useful ToolCall params nikalna.

2. 💥 Why? (Production Impact)
- Evaluator ko check karne ke liye array of objects chahiye, par agent raw tuple generate karta hai.
- Agar safely JSON parse nahi kiya, toh AI ka ek extra comma test runner ko crash kar dega.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: AgentExecutor initialize karte waqt ek specific flag (State Preservation flag) ko `True` kar.
  The Logic: Yeh flag payload ko enrich karega aur "CCTV" ON karega jisse `intermediate_steps` response dictionary mein aayenge.

  Task [2]: For-loop lagakar un steps ko parse kar. Har step ke **index 0** se action object nikal. Uske `tool` aur `tool_input` (jo ek string hai) ko extract kar.
  The Logic: Tool input string format mein hota hai. Isey Python object banane ke liye `json.loads` use karna padega.

  💥 THE CHAOS TASK (Break it to Master it):
  Extraction script mein data direct aise access karne ki koshish kar: `step.tool`. Run kar. **AttributeError** aayega! Phir notes ka flowchart yaad kar: "Kyunki array ke andar objects nahi, **Tuples** hain!" Isey fix kar `step[0].tool` use karke. Saath hi ek galat JSON string dekar `json.JSONDecodeError` trigger kar aur usko **Try-except** block se sambhal taaki framework fatally crash na ho.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output: Saaf array print hona chahiye: `[{'tool': 'DB_Search', 'input': {'user_id': 42}}]`
- 🕵️‍♂️ Under The Hood Verification: Debugger laga ke dekh ki kya `parsed_input` asli dictionary object ban gaya hai ya abhi bhi string quotes mein hai.
- 💬 Quick Verify 1 (Core Concept): "`action.tool_input` string format mein kyun aata hai aur parsing kyun zaroori hai?"
- 💬 Quick Verify 2 (Safety): "Data parsing safety ke liye JSONDecodeError ko catch karna kyun vital hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **return_intermediate_steps:** Payload enrichment aur state preservation.
- **AgentAction Tuple:** index [0] action hai, index [1] observation hai.
- ⚠️ **Anti-Pattern:** Direct `step.tool` access karne ki koshish karna Tuple array par.
- **Data Safety Hook:** Logs bhejte waqt Tool arguments mein users ke email/pass leak ho sakte hain (Data Exposure Risk). Environment check karke PII sanitization lazmi hai.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏁 MODULE 2 RECAP — Tera Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Siksha Summary:
- Tune Master Answer Key (Golden Dataset) structre karke banaya.
- Data ko securely cloud pe Push/Pull aur hydrate karna seekha.
- Agent ke Black Box (opaque execution) ko todkar Custom Wrapper banaya.
- Tuple extraction aur JSON parsing (Try-except safety ke saath) apply karke telemetry payload enrich kiya.

Guru-ji's Warning:
"Check kar le bhai! Kya tujhe yeh sab bina cheat sheet ke karna aa gaya hai? Agar tuple extraction ya data hydration mein jara sa bhi doubt hai, toh code dobara likh. Production mein ek 'KeyError' teri puri CI/CD pipeline ko mitti mein mila sakta hai!"

⚡ GURUDAKSHINA (The Checkpoint):
"Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type 'CONTINUE' for the Final Boss Module 3 (Assembly, Debugging & Advanced Tuning)."

--- ⏸️ OUTPUT LIMIT APPROACHING. Type 'CONTINUE' to get the next part.
✅ Completed so far : Module 1 (All Levels), Module 2 (Levels 2.1 to 2.4)
⏳ Remaining       : Module 3 (Levels 3.1 to 3.4)
📊 Progress        : 9 Levels done / 13 Levels total | Module 2 of 3

Chal bhai, akhiri padav aa gaya! Terminal pe focus lock kar. Module 1 aur 2 mein tune data extraction aur basic testing ka foundation set kar liya hai. Ab **Module 3** mein hum us raw data ko pack karenge, loop chalayenge, aur framework ke deep source code ko hack karke advanced metrics tune karenge. 

Bheja fry mat kar, seedha execution pe dhyan de. Let's finish this!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Assembly, Debugging & Advanced Tuning → Level 3.1: Intermediate Steps Parsing & Scoping [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Agent ke raw `intermediate_steps` array se action aur result ko safely nikal kar ek clean Tuple mein pack karna.

2. 💥 Why? (Production Impact)
- AI testing frameworks kachra (raw arrays) nahi samajhte. Unhe structured variables chahiye.
- Agar variables local function scope mein nahi rakhe, toh Global Variables Collision se poora test suite corrupt ho jayega.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: Ek separate function bana `parse_agent_output`. Iske andar strictly "Index zero" hit kar taaki pehla step extract ho. 
  The Logic: Separation of concerns enforce karna zaroori hai. Function execution scope limit rakhta hai jisse memory leaks nahi hote.

  Task [2]: Extracted `agent_action` object se directly uski properties (`tool` aur `tool_input`) nikal, aur result/observation ke sath ek Return Tuple mein caller ko wapas de.
  The Logic: Tuple unpacking se clean data handoff hota hai. 

  💥 THE CHAOS TASK (Break it to Master it):
  Agent action log message se tool ka naam nikalne ke liye ek ganda sa **Regex hack** use kar. Agent ka prompt thoda change kar taaki woh output formatting (spaces/markdown) badal de. Tera Regex toot jayega aur test fail hoga. Ab isko fix kar built-in object properties (`agent_action.tool`) aur `isinstance` (Type checking safety) lagakar. Pata hona chahiye string hacks production mein kyun fat-te hain! Saath hi ek Fallback return (`None, None, None`) laga taaki IndexError aane par test runner hard-crash na ho.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output on Console: `Extracted: DB, 123, Success` (Mock data pass karke verify kar).
- 🕵️‍♂️ Under The Hood Verification: Debugger se caller side pe check kar ki variables exactly unpack huye hain ya tuple format mein hi fase hain.
- 💬 Quick Verify 1 (Core Concept): "Execution Scope testing mein Global variables collision ko kaise rokta hai?"
- 💬 Quick Verify 2 (Behavior): "Fallback return lagana test stability ke liye kyu zaroori hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **Parsing & Extraction:** Object ki strictly defined properties use karna.
- **Return Tuple:** Safely caller ko data wapas pass karna.
- ⚠️ **Anti-Pattern:** String logs par Regex hack use karna. Sahi tarika: Object attributes (`.tool`) use kar.
- **Scalability Hook:** Multi-step agents ke liye sirf `[0]` kaam nahi aayega, wahan Pydantic models ke saath `for` loop iterate karna padega.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Assembly, Debugging & Advanced Tuning → Level 3.2: Test Case Assembly & State Sync [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Actual aur Expected dictionaries ko strictly typed `ToolCall` objects mein wrap karke final `LLMTestCase` lunchbox banana.

2. 💥 Why? (Production Impact)
- Dictionaries loose data structures hain. Framework ko agar dict pass ki toh validation phase mein MissingRequiredArgument throw karega.
- Cloud se data fetch karte waqt blank entries `None baseline` error deti hain jisse script crash hoti hai.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: Loop laga kar apni extracted raw dictionaries ko DeepEval ki `ToolCall` class mein instantiate kar.
  The Logic: Yeh Dynamic Wrap process hai jisse type-checking enforce hoti hai.

  Task [2]: In `ToolCall` lists (expected aur actual) aur user query ko milakar ek final `LLMTestCase` instantiate kar.
  The Logic: Yeh ultimate box hai jo metric engine directly consume karega.

  💥 THE CHAOS TASK (Break it to Master it):
  Cloud portal/dashboard pe ja aur kisi tool ka expected data intentionally blank chhod de. Ab script run kar. `NoneType object has no attribute` type ka **None baseline** error aayega! Tujhe realize hoga ki tera code cloud ke against out-of-sync hai. Isey fix karne ke liye pehle code mein `if e is None: continue` (error handling) laga, phir terminal pe jaake `dataset.push` (update) aur `dataset.pull` karke **State Synchronization** achieve kar. 

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output on Console: `weather_api` (object ke andar se property print karake dekh).
- 🕵️‍♂️ Under The Hood Verification: Check kar ki `LLMTestCase` instantiate hone ke baad uske internal parameters strongly typed hain ya nahi.
- 💬 Quick Verify 1 (Core Concept): "State Synchronization (Push/Pull) missing hone par test suites mein kya hota hai?"
- 💬 Quick Verify 2 (Design): "Frameworks raw dictionaries ko directly accept kyun nahi karte?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **LLMTestCase & ToolCall:** Strict encapsulation and instantiation.
- **State Synchronization:** Local code aur cloud dataset hamesha barabar hone chahiye.
- ⚠️ **Anti-Pattern:** Dataset update karke local files me chhod dena (State sync break karna).
- **Scalability Hook:** Badi teams mein "DataMapper" class banati hain jo data LLMTestCase mein dalne se pehle PII sanitize karti hai.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Assembly, Debugging & Advanced Tuning → Level 3.3: Evaluation Execution & For-Loop Debugging [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Bulk API hit (evaluate) use karne ke bajaye, custom synchronous for-loop lagakar manual iteration se score calculate karna.

2. 💥 Why? (Production Impact)
- Hazaar test case ek saath LLM APIs par pel diye toh Rate Limiting (HTTP 429) aayega aur server down hoga.
- Magic Strings (typos) hone par logic sahi hone ke bawajood tests fail hote hain (False Negatives).

3. 🎯 Practical Tasks (The Mission)
  Task [1]: Ek `for` loop setup kar jo `dataset.test_cases` par iterate kare. Har loop mein `metric.measure()` function call kar aur delay (`time.sleep`) laga.
  The Logic: Yeh Manual Iteration hai. Delay API throttling (HTTP 429) se bachayega.

  Task [2]: Measure chalne ke baad `tool_metric.score` ka state variable access kar aur usko read/print kar.
  The Logic: Metric function seedha return nahi karta, woh apne object ka internal state update karta hai.

  💥 THE CHAOS TASK (Break it to Master it):
  Intentionally "String Mismatch" create kar. Expected dataset mein tool ka naam `multiply_numbers` likh aur agent se `Multiply` pass karwa. Score 0.0 aayega (False Negative) jabki usne kaam sahi kiya tha. Error pakad! Fir in hardcoded "Magic Strings" ko delete kar aur ek `Constants.py` (ENUM classes) bana. Uska use karke Exact String Match enforce kar.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output on Console: Executing Eval 0... Result Score: 1.0 (aur loop delay leke next print karega).
- 🕵️‍♂️ Under The Hood Verification: Terminal logs mein HTTP 429 error gayab ho jana chahiye `time.sleep` lagane ke baad.
- 💬 Quick Verify 1 (Core Concept): "Evaluation pipeline mein False Negative result kab produce hota hai?"
- 💬 Quick Verify 2 (System): "Manual iteration loop default bulk evaluate API se better kab hota hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **metric.measure:** Internal logic engine aur score updater.
- **Rate Limiting:** APIs ko spam hone se rokna.
- ⚠️ **Anti-Pattern:** Test case mein "Magic Strings" hardcode karna. Sahi tarika: Constants.py use kar.
- **Scalability Hook:** Hazaar tests manually loop me slow honge. Production mein chunking aur `asyncio.gather()` lagake batch processing ki jati hai.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Assembly, Debugging & Advanced Tuning → Level 3.4: Advanced Metric Configurations & Bug Avoidance [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Docs padhna chhor aur seedha metric ke `__init__` source code mein ghus kar hidden tuning parameters customize kar.

2. 💥 Why? (Production Impact)
- Security workflows mein kis chronological sequence mein tool chala, yeh jaan par ban aati hai. Order check kiye bina tests blindly pass ho jayenge.
- Galti se galat flag on kiya toh internal bug system crash kar dega (RecursionError).

3. 🎯 Practical Tasks (The Mission)
  Task [1]: IDE navigation (`Cmd + Click`) se `ToolCorrectnessMetric` ki source file khol (site-packages mein). Padh usko, par modify mat karna (Supply Chain Rule). Apna Metric banate waqt wahan se `threshold` aur `strict_mode` flags pass kar.
  The Logic: Hidden Kwargs ko control karke framework ko apne use-case ke hisaab se customize karna.

  Task [2]: Security agent ke liye `should_consider_ordering=True` flag set kar aur `evaluation_params` ko limit kar taaki PII redaction ho.
  The Logic: Yeh Array Index Mapping check karega. Agar AI ne tool sequence break ki toh fail hoga. Params limit karna PII ko external LLM judge ke paas jaane se rokta hai.

  💥 THE CHAOS TASK (Break it to Master it):
  Metric initialization ke andar galti se `verbose=True` pass kar de. Script run kar. Tere muh pe ek brutal **RecursionError: maximum recursion depth exceeded** padega! Tera system crash (internal DoS attack) ho jayega. Reason? Cyclical reference bug in the logger. Ab code wapas ja, verbose hata, aur verify kar ki deep configurations bina samjhe chhedna kitna khatarnak hai.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- 📤 Expected Output on Console: `Metric Order Check: True`
- 🕵️‍♂️ Under The Hood Verification: Test case ko galat order mein tool calls dekar measure kar. Ensure kar ki score drop ho (Scoring Penalty lag rahi hai chronological sequence fail hone pe).
- 💬 Quick Verify 1 (Core Concept): "should_consider_ordering flag security workflows mein kya role ada karta hai?"
- 💬 Quick Verify 2 (Danger): "IDE mein site-packages modify karna (Supply Chain Rule violation) allowed kyun nahi hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **Source Code Inspection:** Documentations se aage badhkar class definitions explore karna.
- **Chronological Sequence:** Array Index Mapping ke zariye strict ordering check.
- ⚠️ **Anti-Pattern:** Library/package files ko directly edit karna. Hamesha initialization flags override kar.
- **Scalability Hook:** `include_reasons=True` API costs exponentially bada deta hai. Production eval runs mein latency bachane ke liye isko False rakha jata hai.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏁 MODULE 3 RECAP — Tera Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Siksha Summary:
- Tune intermediate raw arrays ko safely parse aur scope mein limit karna seekha.
- Actual aur Expected data ko `ToolCall` wrap karke `LLMTestCase` assemble kiya (with State Sync).
- Rate limits aur Magic strings ko bypass karne ke liye Manual iteration (for-loop) setup kiya.
- Source code inspect karke advanced flags tune kiye aur RecursionError jese brutal bugs ko handle kiya.

Guru-ji's Warning:
"Check kar le bhai! Kya tujhe yeh sab bina cheat sheet ke karna aa gaya hai? Aaj tune ek opaque AI ko transparent aur stable production pipeline mein convert kiya hai. Agar in config flags aur loops mein confidence loose lag raha hai, toh wapas ja aur dry-run kar. Real engineer deep dive karne se nahi darta!"

⚡ GURUDAKSHINA (The Checkpoint):
"Sare Modules aur Levels clear hue? Mission Accomplished! Ab yeh code production mein aag lagane ke liye ready hai. Bhai, tera CTF Lab manual officially close hota hai. Ja, aur real-world mein AI ki bug-hunting kar!"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

