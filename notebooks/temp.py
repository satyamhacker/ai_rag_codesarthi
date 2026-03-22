import asyncio
from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit

async def main():
    # Step 1: Start Playwright
    playwright = await async_playwright().start()

    # Step 2: Launch browser
    browser = await playwright.chromium.launch(headless=True)

    # Step 3: Create toolkit
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)

    # Step 4: Get all tools
    all_tools = toolkit.get_tools()
    print(f"Total tools in bundle: {len(all_tools)}")

    # Step 5: Filter tools
    target_tool_names = ["navigate_browser", "get_elements"]
    filtered_tools = [tool for tool in all_tools if tool.name in target_tool_names]

    # Step 6: Print descriptions
    for tool in filtered_tools:
        print(f"🛠️ Tool: {tool.name}")
        print(f"📝 Description: {tool.description}\n")

    # Cleanup
    await browser.close()
    await playwright.stop()

# Run async function
asyncio.run(main())