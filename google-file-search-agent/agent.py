from google.adk.agents import Agent
from .file_tools import upload_file, ask_file

root_agent = Agent(
    name="google_file_search_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant that can search through files.",
    tools=[upload_file, ask_file]
)
