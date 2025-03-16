from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_file(data: str, filename: str = "response_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    formatted_text = f"Response generated at {timestamp}\n\n{data}"

    with open(filename, "a",encoding="utf-8") as file:
        file.write(formatted_text)

    return f"Response saved to {filename}"

save_tool = Tool(
    name="SaveToFile",
    func=save_to_file,
    description="Save the response to a text file",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Search the web for information",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=3, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)


