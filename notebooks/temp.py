import asyncio
from playwright.async_api import async_playwright

from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# ✅ Use this instead:
from langchain_classic.agents import AgentExecutor, create_structured_chat_agent

async def main():
    # 🔹 Start Playwright
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)

    # 🔹 Toolkit
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    tools = toolkit.get_tools()

    # 🔹 Filter only required tools
    target_tool_names = ["navigate_browser", "get_elements"]
    tools = [t for t in tools if t.name in target_tool_names]

    # 🔹 LLM (Ollama)
    # Updated to use the dedicated langchain_ollama package
    llm = ChatOllama(
        model="llama3.1",   # make sure this exists locally
        temperature=0
    )

    # 🔹 Structured chat prompt (local, no hub required)
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Respond to the human as helpfully and accurately as possible. You have access to the following tools:\n\n{tools}\n\nUse a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input).\n\nValid \"action\" values: \"Final Answer\" or {tool_names}\n\nProvide only ONE action per $JSON_BLOB, as shown:\n\n```\n{{\n  \"action\": $TOOL_NAME,\n  \"action_input\": $INPUT\n}}\n```\n\nFollow this format:\n\nQuestion: input question to answer\nThought: consider previous and subsequent steps\nAction:\n```\n$JSON_BLOB\n```\nObservation: action result\n... (repeat Thought/Action/Observation N times)\nThought: I know what to respond\nAction:\n```\n{{\n  \"action\": \"Final Answer\",\n  \"action_input\": \"Final response to human\"\n}}\n```\n\nBegin! Reminder to ALWAYS respond with a valid json blob of a single action. Use tools if necessary. Respond directly if appropriate."""),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}\n\n{agent_scratchpad}\n(reminder to respond in a json blob no matter what)"),
    ])

    # 🔹 Create the Agent and Executor (The Modern Way)
    agent = create_structured_chat_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )
    
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True,
        handle_parsing_errors=True # Highly recommended for local models like Llama 3
    )

    # =========================
    # 🧠 FINAL BOSS PROMPT
    # =========================
    query = """
    You are a precise data extraction and analysis agent.

    Step-by-step:
    1. Open the URL: https://www.w3schools.com/html/html_tables.asp
    2. Extract all table cell text using the get_elements tool with selector "td"
    3. Identify the salary column (assume numeric values if present)
    4. Compute the average of all numeric values found
    5. If no salary column exists, return average as 0

    Output MUST be strictly valid JSON:
    {
      "average_salary": number,
      "status": "success"
    }

    Do NOT return anything except JSON.
    """

    # =========================
    # 🚀 Run Agent
    # =========================
    print("🤖 Running Agent...\n")

    # 🔹 Updated from .arun() to .ainvoke()
    result = await agent_executor.ainvoke({"input": query})

    print("\n📦 Final Output:\n")
    # .ainvoke() returns a dictionary, so we print the 'output' key
    print(result.get("output"))

    # 🔹 Cleanup
    await browser.close()
    await playwright.stop()


# ▶️ Run
if __name__ == "__main__":
    asyncio.run(main())