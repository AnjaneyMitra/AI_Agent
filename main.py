from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
import json
from tools import search_tool,wiki_tool,save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool,wiki_tool,save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("Enter your query: ")

raw_response = agent_executor.invoke({"query": query})

# Extract the JSON string from the response
raw_json_string = raw_response.get("output")

# Remove Markdown formatting (backticks and "json" tag)
clean_json_string = raw_json_string.strip("```json\n").strip("```")

# Convert string to dictionary

try:
    structured_response = parser.parse(clean_json_string)
    print(structured_response)
except  Exception as e:
    print(f"Failed to parse response: {e}","Response - ",clean_json_string)