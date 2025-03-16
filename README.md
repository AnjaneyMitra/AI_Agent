AI Research Assistant
This project is an AI-powered research assistant that retrieves and summarizes information using Google Gemini API, Wikipedia, and DuckDuckGo Search. It can also save responses to a file for later reference.

Features
✅ Web Search – Uses DuckDuckGo for real-time web searches.
✅ Wikipedia Search – Fetches summarized data from Wikipedia.
✅ Response Saving – Saves research results to a text file.
✅ AI-Powered Summaries – Uses Google Gemini API for generating structured research responses.

Installation
Clone the repository:
bash
Copy
Edit
git clone https://github.com/your-username/research-assistant.git  
cd research-assistant
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables:
Create a .env file and add your Google Gemini API key:
ini
Copy
Edit
GOOGLE_API_KEY=your_api_key_here
Run the script:
bash
Copy
Edit
python main.py
Usage
Enter a query when prompted.
The assistant will search the web and Wikipedia.
It will generate a structured research summary.
The response will be saved in response_output.txt.
File Structure
bash
Copy
Edit
📂 research-assistant  
 ├── tools.py          # Defines web search, Wikipedia search, and file-saving tools  
 ├── main.py           # Main script that runs the AI assistant  
 ├── requirements.txt  # List of dependencies  
 ├── .env              # Environment variables (not included in repo)  
 ├── response_output.txt # Saved research responses  
 └── README.md         # Project documentation  
