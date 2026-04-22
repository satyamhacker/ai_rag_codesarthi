Bhai, yeh kaam bahut lamba hai — 13 concepts, har ek mein PART A (8 questions) + PART B (har parameter ke 4 questions). Total 100+ questions easily banega.

Chunking mein dunga taaki kuch miss na ho.

---

# STEP 1 — DEPENDENCY MAP

```
LLMTestCase → no dependencies (start here)
ToolCall → no dependencies (start here)
ToolCorrectnessMetric → needs LLMTestCase + ToolCall
metric.measure() → needs ToolCorrectnessMetric
deepeval.evaluate() → needs metric.measure()
Zero Trust Environment → no dependencies
@tool Decorator + Docstring → needs Zero Trust
AgentExecutor + ReAct → needs @tool Decorator
Golden Dataset → needs LLMTestCase + ToolCall
EvaluationDataset Push/Pull → needs Golden Dataset
Custom Async Wrapper → needs AgentExecutor
return_intermediate_steps → needs Custom Async Wrapper
parse_agent_output → needs return_intermediate_steps
State Synchronization → needs EvaluationDataset Push/Pull
Manual For-Loop Evaluation → needs metric.measure() + Golden Dataset
Advanced Metric Flags → needs ToolCorrectnessMetric + AgentExecutor
```

---

# RECOMMENDED STUDY ORDER

```
1. LLMTestCase
2. ToolCall
3. ToolCorrectnessMetric
4. metric.measure()
5. deepeval.evaluate()
6. Zero Trust Environment
7. @tool Decorator + Docstring
8. AgentExecutor + ReAct Loop
9. Golden Dataset
10. EvaluationDataset Push/Pull
11. Custom Async Wrapper
12. return_intermediate_steps
13. parse_agent_output
14. State Synchronization
15. Manual For-Loop Evaluation
16. Advanced Metric Flags
```

---

# CONCEPT 1 — LLMTestCase [Beginner]
📌 Prerequisites: None (start here)

## PART A — CONCEPT LEVEL

**[WHAT] 🟢**
What is `LLMTestCase`? Define it in simple words — what role does it play in AI evaluation?

**[STRUCTURE] 🟢**
What are the mandatory fields of `LLMTestCase`? What goes inside each field? Show the minimal working code skeleton.

**[WHEN] 🟡**
When should you use `LLMTestCase`? Give 3 real-world situations. When should you NOT use it?

**[COMPARE] 🟡**
Compare `LLMTestCase` vs raw Python dictionary vs JSON object. Make a side-by-side table covering: type safety, error detection, framework compatibility, ease of use.

**[PURPOSE] 🟡**
If `LLMTestCase` didn't exist, what exact problem would you face when evaluating AI agents?

**[ANTI-PATTERN] 🔴**
What is the most common wrong way to use `LLMTestCase`? What mistake do beginners make? What is the correct approach?

**[REAL EXAMPLE] 🟡**
Give a real-world scenario — e.g., a banking chatbot — where `LLMTestCase` is used. Show exactly how it fits.

**[BREAK IT] 🔴**
What can go wrong with `LLMTestCase`? What exact error will you see and why?

## PART B — PARAMETER DEEP DIVE

**→ Parameter: `input`**

[PARAM-WHAT] 🟢 What is the `input` parameter? What does it represent? What happens if you don't pass it?

[PARAM-VALUES] 🟡 What data type does `input` accept? Can it be a list or only string? Show examples of valid and invalid values.

[PARAM-MISTAKE] 🔴 What is the most common mistake with `input`? What silent bug or error appears?

[PARAM-REALCODE] 🟡 Show exactly how `input` is used in a real working code snippet. Why is that specific value chosen?

**→ Parameter: `expected_tools`**

[PARAM-WHAT] 🟢 What is `expected_tools`? What does it hold? What happens if you skip it?

[PARAM-VALUES] 🟡 What data type does it accept — list of strings, list of ToolCall objects, or both? What is default value if not passed?

[PARAM-MISTAKE] 🔴 What happens if you pass raw dictionaries instead of ToolCall objects here? What exact error or silent failure occurs?

[PARAM-REALCODE] 🟡 Show a real code snippet where `expected_tools` is correctly populated with ToolCall objects.

**→ Parameter: `actual_tools_called`**

[PARAM-WHAT] 🟢 What is `actual_tools_called`? Where does this data come from in real production testing?

[PARAM-VALUES] 🟡 What type does it accept? Can it be empty list? What happens if it is empty?

[PARAM-MISTAKE] 🔴 What is the most common mistake — manually hardcoding it vs extracting from agent? What goes wrong?

[PARAM-REALCODE] 🟡 Show how `actual_tools_called` is populated from a real agent's `intermediate_steps` output.

---

# CONCEPT 2 — ToolCall [Beginner]
📌 Prerequisites: None (start here)

## PART A — CONCEPT LEVEL

**[WHAT] 🟢**
What is `ToolCall`? What does it represent in the evaluation pipeline?

**[STRUCTURE] 🟢**
What are the 3 mandatory fields of `ToolCall`? What goes inside each? Show minimal code skeleton.

**[WHEN] 🟡**
When should you use `ToolCall`? Give 3 real situations. When should you NOT use it?

**[COMPARE] 🟡**
Compare `ToolCall` vs raw Python dictionary vs JSON Schema. Table covering: type safety, validation, DeepEval compatibility, error detection time.

**[PURPOSE] 🟡**
If `ToolCall` didn't exist and you used raw dictionaries, what exact production failures would happen?

**[ANTI-PATTERN] 🔴**
What is the wrong way to use `ToolCall`? What do beginners skip? What is the correct approach?

**[REAL EXAMPLE] 🟡**
Give a real-world Swiggy/Zomato scenario where `ToolCall` objects are used in evaluation. Show how they fit.

**[BREAK IT] 🔴**
What breaks if you pass `ToolCall` with wrong case in `name` field? What exact error or score failure occurs?

## PART B — PARAMETER DEEP DIVE

**→ Parameter: `name`**

[PARAM-WHAT] 🟢 What is the `name` field in ToolCall? What does it store? What happens if it doesn't match exactly?

[PARAM-VALUES] 🟡 What data type? Case sensitive or not? What happens with `WebSearch` vs `web_search`?

[PARAM-MISTAKE] 🔴 What is the most common case-sensitivity mistake? What score will you get and why?

[PARAM-REALCODE] 🟡 Show a real code example where `name` is correctly set matching the actual tool name.

**→ Parameter: `input`**

[PARAM-WHAT] 🟢 What is the `input` field in ToolCall? What data does it hold? What if you skip it?

[PARAM-VALUES] 🟡 What type does it accept — string or dictionary? Show examples of both.

[PARAM-MISTAKE] 🔴 What happens if you pass a string instead of a dictionary here? Silent bug or crash?

[PARAM-REALCODE] 🟡 Show real code with `input` correctly filled from an agent's tool call data.

**→ Parameter: `output`**

[PARAM-WHAT] 🟢 What is the `output` field? What does it store? What happens if left empty?

[PARAM-VALUES] 🟡 What type does it accept? Can it be None? What is the default?

[PARAM-MISTAKE] 🔴 What is the most common mistake with `output`? What evaluation failure results?

[PARAM-REALCODE] 🟡 Show real code with `output` correctly capturing an API's return value.

---

# CONCEPT 3 — ToolCorrectnessMetric [Intermediate]
📌 Prerequisites: Concept 1 (LLMTestCase), Concept 2 (ToolCall)

## PART A — CONCEPT LEVEL

**[WHAT] 🟢**
What is `ToolCorrectnessMetric`? Does it use an LLM internally or is it purely programmatic?

**[STRUCTURE] 🟢**
How do you instantiate `ToolCorrectnessMetric`? What parameters can you pass at initialization? Show minimal code skeleton.

**[WHEN] 🟡**
When should you use `ToolCorrectnessMetric`? Give 3 real situations. When should you NOT use it?

**[COMPARE] 🟡**
Compare `ToolCorrectnessMetric` vs LLM-as-a-Judge metric vs exact string match. Table covering: speed, cost, accuracy, use case.

**[PURPOSE] 🟡**
If this metric didn't exist and you used simple string comparison, what exact failures would happen in production?

**[ANTI-PATTERN] 🔴**
What is the wrong way to use this metric? What do beginners misunderstand about how it scores?

**[REAL EXAMPLE] 🟡**
Give a real-world scenario — e.g., a customer support bot — where this metric catches a critical failure.

**[BREAK IT] 🔴**
What can cause this metric to return unexpected scores? What exact scenario produces a false negative?

## PART B — PARAMETER DEEP DIVE

**→ Parameter: `threshold`**

[PARAM-WHAT] 🟢 What is `threshold` in ToolCorrectnessMetric? What does it control? What is default?

[PARAM-VALUES] 🟡 What range of values does it accept? What happens at 0.0 vs 0.5 vs 1.0?

[PARAM-MISTAKE] 🔴 What is the most common mistake with threshold? What false pass/fail results?

[PARAM-REALCODE] 🟡 Show real code setting threshold for a strict security evaluation use case.

**→ Parameter: `strict_mode`**

[PARAM-WHAT] 🟢 What is `strict_mode`? What changes in scoring behavior when enabled?

[PARAM-VALUES] 🟡 What values does it accept — True/False? What is default? Show both scenarios.

[PARAM-MISTAKE] 🔴 What happens if you enable strict_mode without understanding partial credit? What score surprise occurs?

[PARAM-REALCODE] 🟡 Show real code with strict_mode enabled for a zero-tolerance evaluation pipeline.

**→ Parameter: `should_consider_ordering`**

[PARAM-WHAT] 🟢 What is `should_consider_ordering`? What does it check that default mode doesn't?

[PARAM-VALUES] 🟡 True/False — what does each value do? When does ordering matter vs not matter?

[PARAM-MISTAKE] 🔴 What happens in a security workflow if you forget to set this to True? What passes that should fail?

[PARAM-REALCODE] 🟡 Show real code using `should_consider_ordering=True` for a login-then-verify tool sequence.

**→ Parameter: `evaluation_params`**

[PARAM-WHAT] 🟢 What is `evaluation_params`? What does limiting it do? What if not set?

[PARAM-VALUES] 🟡 What values can it accept? How do you limit params to prevent PII exposure?

[PARAM-MISTAKE] 🔴 What happens if evaluation_params is not limited and sensitive data is in tool inputs?

[PARAM-REALCODE] 🟡 Show real code with `evaluation_params` limited for a GDPR-compliant pipeline.

**→ Parameter: `include_reasons`**

[PARAM-WHAT] 🟢 What is `include_reasons`? What extra data does it expose when True?

[PARAM-VALUES] 🟡 True/False — what does each produce? What is the default?

[PARAM-MISTAKE] 🔴 Why is `include_reasons=True` dangerous in production at scale? What cost/latency impact?

[PARAM-REALCODE] 🟡 Show when and how to use `include_reasons=True` safely for debugging only.

---

**⏸️ CONTINUE karke next batch maang — CONCEPT 4 se aage!**

```
✅ Done : Concept 1, 2, 3
⏳ Remaining : Concept 4 to 16
📊 Progress : 3/16 concepts
```

# CONCEPT 4 — metric.measure() [Intermediate]
📌 Prerequisites: Concept 3 (ToolCorrectnessMetric)

## PART A — CONCEPT LEVEL

**[WHAT] 🟢**
What is `metric.measure()`? Does it return a value or update internal state? What exactly happens when you call it?

**[STRUCTURE] 🟢**
What is the exact syntax to call `measure()`? What must you pass inside it? Show minimal working code skeleton including how to read the result after calling it.

**[WHEN] 🟡**
When should you use `metric.measure()`? Give 3 real situations. When should you NOT use it and use `deepeval.evaluate()` instead?

**[COMPARE] 🟡**
Compare `metric.measure()` vs `deepeval.evaluate()`. Side-by-side table covering: execution location, cloud sync, speed, cost, bulk support, use case.

**[PURPOSE] 🟡**
If `metric.measure()` didn't exist and only `deepeval.evaluate()` was available, what exact problems would a solo developer face?

**[ANTI-PATTERN] 🔴**
What is the wrong way to use `metric.measure()`? What do beginners assume about its return value that is wrong?

**[REAL EXAMPLE] 🟡**
Give a real scenario — developer testing a healthcare chatbot locally with sensitive data. Show how `metric.measure()` fits vs why `evaluate()` would be dangerous here.

**[BREAK IT] 🔴**
What happens if you call `metric.measure()` without a properly formed `LLMTestCase`? What exact error appears?

## PART B — PARAMETER DEEP DIVE

**→ Parameter: test_case (the argument passed inside measure())**

[PARAM-WHAT] 🟢 What type of object must be passed into `measure()`? What happens if you pass a raw dictionary instead?

[PARAM-VALUES] 🟡 Can you pass multiple test cases in one `measure()` call? What is the accepted input format?

[PARAM-MISTAKE] 🔴 What is the most common mistake — what exact error or silent failure happens if wrong type is passed?

[PARAM-REALCODE] 🟡 Show exact real code: create LLMTestCase → pass to measure() → read score. Full flow in one snippet.

**→ Reading result: `metric.score`**

[PARAM-WHAT] 🟢 What is `metric.score`? When is it populated — before or after `measure()` is called?

[PARAM-VALUES] 🟡 What range of values can `metric.score` return? What does 0.0, 0.5, 1.0 each mean?

[PARAM-MISTAKE] 🔴 What happens if you read `metric.score` before calling `measure()`? What value do you get?

[PARAM-REALCODE] 🟡 Show real code reading `metric.score` and `metric.reason` together after measure() call.

**→ Reading result: `metric.reason`**

[PARAM-WHAT] 🟢 What is `metric.reason`? What information does it contain after measure() runs?

[PARAM-VALUES] 🟡 Is `metric.reason` always populated? When is it None or empty?

[PARAM-MISTAKE] 🔴 What cost/performance mistake happens if you always log `metric.reason` in production?

[PARAM-REALCODE] 🟡 Show real code using `metric.reason` only during debug mode with an if-condition guard.

---

# CONCEPT 5 — deepeval.evaluate() [Intermediate]
📌 Prerequisites: Concept 4 (metric.measure())

## PART A — CONCEPT LEVEL

**[WHAT] 🟢**
What is `deepeval.evaluate()`? What does it do differently from `metric.measure()`? Where does the result go?

**[STRUCTURE] 🟢**
What are the mandatory arguments of `deepeval.evaluate()`? What goes inside each? Show minimal working code skeleton.

**[WHEN] 🟡**
When should you use `deepeval.evaluate()`? Give 3 real situations. When should you strictly NOT use it?

**[COMPARE] 🟡**
Compare `deepeval.evaluate()` vs `metric.measure()` vs pytest integration. Table covering: cloud sync, bulk handling, telemetry, privacy, speed.

**[PURPOSE] 🟡**
If `deepeval.evaluate()` didn't exist, how would a team of 10 engineers share and track evaluation results across CI/CD?

**[ANTI-PATTERN] 🔴**
What is the biggest mistake when using `deepeval.evaluate()` in a local dev environment? What problems does it create?

**[REAL EXAMPLE] 🟡**
Give a real CI/CD pipeline scenario — GitHub Actions triggered on PR — where `deepeval.evaluate()` automatically validates the AI agent before merge.

**[BREAK IT] 🔴**
What happens if you run `deepeval.evaluate()` without internet connection? What exact error appears and how do you fix it?

## PART B — PARAMETER DEEP DIVE

**→ Parameter: `test_cases`**

[PARAM-WHAT] 🟢 What is the `test_cases` parameter? What type does it accept — single object or list?

[PARAM-VALUES] 🟡 Can it be an empty list? What happens if you pass a single LLMTestCase instead of a list?

[PARAM-MISTAKE] 🔴 What is the most common mistake with `test_cases` parameter that causes silent failures?

[PARAM-REALCODE] 🟡 Show real code building a list of 3 LLMTestCase objects and passing to evaluate().

**→ Parameter: `metrics`**

[PARAM-WHAT] 🟢 What is the `metrics` parameter? What goes inside — single metric or list?

[PARAM-VALUES] 🟡 Can you pass multiple different metrics at once? What happens if metrics list is empty?

[PARAM-MISTAKE] 🔴 What happens if you pass an uninstantiated metric class instead of an instance object?

[PARAM-REALCODE] 🟡 Show real code passing multiple metrics — ToolCorrectnessMetric + another metric — together.

**→ Webhook/Telemetry behavior**

[PARAM-WHAT] 🟢 What HTTP call does `deepeval.evaluate()` make internally? Where does data go?

[PARAM-VALUES] 🟡 Can you disable the cloud sync? What configuration controls telemetry on/off?

[PARAM-MISTAKE] 🔴 What data leak risk exists if you pass real user queries to `deepeval.evaluate()` without sanitization?

[PARAM-REALCODE] 🟡 Show real code with PII sanitization applied before passing test cases to evaluate().

---

# CONCEPT 6 — Zero Trust Environment [Beginner]
📌 Prerequisites: None (start here)

## PART A — CONCEPT LEVEL

**[WHAT] 🟢**
What is a Zero Trust Environment in the context of DeepEval testing? What does "zero trust" mean here practically?

**[STRUCTURE] 🟢**
How do you enforce Zero Trust in code? What is the exact one-line command? Show minimal code skeleton.

**[WHEN] 🟡**
When must you enforce Zero Trust? Give 3 real situations. When is it NOT needed?

**[COMPARE] 🟡**
Compare Zero Trust mode vs normal mode in DeepEval. Table covering: data privacy, cloud calls, speed, use case.

**[PURPOSE] 🟡**
If you didn't enforce Zero Trust and ran tests with real API keys active, what exact security disaster could happen?

**[ANTI-PATTERN] 🔴**
What is the most common mistake developers make with API keys during local testing? What is the correct approach?

**[REAL EXAMPLE] 🟡**
Give a real scenario — a bank's AI agent being tested locally by a junior developer. Show why Zero Trust is critical here.

**[BREAK IT] 🔴**
What happens if you forget to pop the API key but run evaluate() with sensitive healthcare queries? What is the risk?

## PART B — PARAMETER DEEP DIVE

**→ `os.environ.pop()` method**

[PARAM-WHAT] 🟢 What does `os.environ.pop()` do? How is it different from just not setting the key?

[PARAM-VALUES] 🟡 What arguments does `pop()` take? What is the second argument (default) and why is it important?

[PARAM-MISTAKE] 🔴 What happens if you use `os.environ.pop('KEY')` without a default and the key doesn't exist? What error?

[PARAM-REALCODE] 🟡 Show exact real code safely popping `CONFIDENT_AI_API_KEY` with a fallback default.

**→ `CONFIDENT_AI_API_KEY` environment variable**

[PARAM-WHAT] 🟢 What is `CONFIDENT_AI_API_KEY`? What does DeepEval use it for internally?

[PARAM-VALUES] 🟡 Where is this key set — `.env` file, system environment, or code? What are all valid ways?

[PARAM-MISTAKE] 🔴 What is the most dangerous mistake — hardcoding this key directly in Python script? What risk?

[PARAM-REALCODE] 🟡 Show real code loading key safely from `.env` using `python-dotenv` then popping for local test.

---

# CONCEPT 7 — @tool Decorator + Docstring [Intermediate]
📌 Prerequisites: Concept 6 (Zero Trust Environment)

## PART A — CONCEPT LEVEL

**[WHAT] 🟢**
What does the `@tool` decorator do? What does it convert a plain Python function into?

**[STRUCTURE] 🟢**
What is the exact syntax to create a tool using `@tool`? What 3 things must every tool function have? Show minimal working skeleton.

**[WHEN] 🟡**
When should you use `@tool`? Give 3 real situations. When should you NOT use it?

**[COMPARE] 🟡**
Compare `@tool` decorated function vs plain Python function vs BaseTool class. Table covering: AI readability, schema generation, LLM compatibility, complexity.

**[PURPOSE] 🟡**
If `@tool` decorator didn't exist, how would you make a Python function usable by an LLM agent? What manual work would be needed?

**[ANTI-PATTERN] 🔴**
What is the most dangerous anti-pattern with `@tool`? What happens when Docstring is missing? What exact AI behavior results?

**[REAL EXAMPLE] 🟡**
Give a real scenario — a stock trading agent — where `@tool` is used for `get_stock_price` and `execute_trade` functions. Show how they fit.

**[BREAK IT] 🔴**
What happens if you put `@tool` on a function but use wrong Type hints — e.g., no type hint at all? What breaks in the agent?

## PART B — PARAMETER DEEP DIVE

**→ Docstring content**

[PARAM-WHAT] 🟢 What is the Docstring in a `@tool` function? What does the AI use it for? What if it's missing?

[PARAM-VALUES] 🟡 What information must a good Docstring contain — just description or also param explanation? Show good vs bad example.

[PARAM-MISTAKE] 🔴 What exact AI behavior occurs when Docstring is vague or missing? Hallucination or wrong tool selection?

[PARAM-REALCODE] 🟡 Show real code with a complete well-written Docstring vs empty Docstring and explain the difference.

**→ Type Hints (e.g., `a: int`)**

[PARAM-WHAT] 🟢 What do Type Hints do in a `@tool` function? What does the AI use them for?

[PARAM-VALUES] 🟡 What types are supported — int, str, float, dict, list? What happens with unsupported types?

[PARAM-MISTAKE] 🔴 What happens if LLM passes a string where int is expected? Does Pydantic catch it or does it silently fail?

[PARAM-REALCODE] 🟡 Show real code with strict type hints and what happens when wrong type is passed by LLM.

**→ Return type annotation**

[PARAM-WHAT] 🟢 What is the return type annotation in `@tool` function? What does it tell the agent?

[PARAM-VALUES] 🟡 What return types are valid? What if you don't annotate the return type?

[PARAM-MISTAKE] 🔴 What agent behavior breaks if return type is missing or wrong?

[PARAM-REALCODE] 🟡 Show real tool function with correct return type annotation and why it matters.

---

# CONCEPT 8 — AgentExecutor + ReAct Loop [Advanced]
📌 Prerequisites: Concept 7 (@tool Decorator)

## PART A — CONCEPT LEVEL

**[WHAT] 🟢**
What is `AgentExecutor`? What is the ReAct loop? How do they work together?

**[STRUCTURE] 🟢**
What are the mandatory parameters of `initialize_agent()`? What goes inside each? Show minimal working skeleton with all required params.

**[WHEN] 🟡**
When should you use `AgentExecutor`? Give 3 real situations. When is a simple LLM chain enough instead?

**[COMPARE] 🟡**
Compare `AgentExecutor` vs normal LLM chain vs OpenAI Functions agent. Table covering: tool execution, loop control, reliability, cost, complexity.

**[PURPOSE] 🟡**
If `AgentExecutor` didn't exist, how would you make an LLM execute real APIs? What manual work would be needed?

**[ANTI-PATTERN] 🔴**
What are the 2 most dangerous anti-patterns with AgentExecutor? What catastrophic production failure results from each?

**[REAL EXAMPLE] 🟡**
Give a real scenario — a travel booking agent — where AgentExecutor manages flight search + hotel booking + payment tools in ReAct loop.

**[BREAK IT] 🔴**
What happens if `max_iterations` is not set and agent gets a query it can't solve? What exact consequence in production?

## PART B — PARAMETER DEEP DIVE

**→ Parameter: `tools` (in initialize_agent)**

[PARAM-WHAT] 🟢 What is the `tools` parameter? What type does it accept — list of what exactly?

[PARAM-VALUES] 🟡 Can tools list be empty? What happens if you pass 50 tools without a Semantic Router?

[PARAM-MISTAKE] 🔴 What hallucination behavior occurs when too many tools are given at once to the agent?

[PARAM-REALCODE] 🟡 Show real code passing a small focused subset of tools using Semantic Router pattern.

**→ Parameter: `llm`**

[PARAM-WHAT] 🟢 What is the `llm` parameter? What does it provide to the AgentExecutor?

[PARAM-VALUES] 🟡 What LLM objects can be passed here — ChatOpenAI, Anthropic, local model? Any restrictions?

[PARAM-MISTAKE] 🔴 What breaks if you pass an LLM with `temperature=0.8` to a tool-calling agent? Exact failure?

[PARAM-REALCODE] 🟡 Show real code initializing ChatOpenAI with `temperature=0` and passing it as llm.

**→ Parameter: `agent` (AgentType)**

[PARAM-WHAT] 🟢 What is the `agent` parameter? What is `ZERO_SHOT_REACT_DESCRIPTION` and what does it mean?

[PARAM-VALUES] 🟡 What other AgentType values exist? When would you use each one? 🔍 Verify from docs

[PARAM-MISTAKE] 🔴 What happens if you pick wrong AgentType for your use case? What behavior breaks?

[PARAM-REALCODE] 🟡 Show real code using `ZERO_SHOT_REACT_DESCRIPTION` and explain why zero-shot is chosen here.

**→ Parameter: `max_iterations`**

[PARAM-WHAT] 🟢 What is `max_iterations`? What does it cap? What is the default value if not set?

[PARAM-VALUES] 🟡 What is a safe value for production? What happens at value 1 vs 5 vs unlimited?

[PARAM-MISTAKE] 🔴 What exact production disaster happens when `max_iterations` is not set? API cost impact?

[PARAM-REALCODE] 🟡 Show real code setting `max_iterations=5` and what log output you see when limit is hit.

**→ Parameter: `verbose`**

[PARAM-WHAT] 🟢 What does `verbose=True` do in AgentExecutor? What extra output appears?

[PARAM-VALUES] 🟡 True/False — what does each produce in logs? What is default?

[PARAM-MISTAKE] 🔴 Why is `verbose=True` dangerous in production? What data exposure risk exists?

[PARAM-REALCODE] 🟡 Show real code with verbose enabled for debugging and how to disable for production.

**→ Method: `.invoke()`**

[PARAM-WHAT] 🟢 What is the `.invoke()` method on AgentExecutor? What does it trigger?

[PARAM-VALUES] 🟡 What format must the argument be — string or dictionary? What key is required inside the dict?

[PARAM-MISTAKE] 🔴 What exact error appears if you pass a plain string instead of `{"input": "..."}` to invoke()?

[PARAM-REALCODE] 🟡 Show real code calling `.invoke({"input": "Add 5 and 10"})` with verbose output explained.

---

**⏸️ CONTINUE karke next batch maang!**

```
✅ Done    : Concept 1-8
⏳ Remaining: Concept 9-16
📊 Progress : 8/16 concepts | Module 1 complete!
```

