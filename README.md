# Climate-Risk-Insurance-Dashboard
Climate Risk Insurance Dashboard is a web app that scrapes real-time news on climate risk and insurance, classifies articles by tags, and matches them with related research papers. Built using LangChain, OpenAI, and Streamlit, it helps users explore insights and trends in climate risk insurance.

⚙️ Features:

🔎 Real-time web scraping of news from legitimate sources

📄 Structured summaries of articles with tag classification

📚 Matches academic papers from open research databases

🎯 Interactive filters to explore topics visually via Streamlit

📊 Evaluation of content coverage, research pairing, and tagging accuracy

Requirements:

Python 3.x

langchain, streamlit, python-dotenv, and other dependencies (see below for setup instructions)

Setup Instructions:

Clone the repository:
Clone the repository to your local machine.

Install dependencies:
Install the required Python packages using the requirements.txt file.

Create a .env.txt file:
Create a .env.txt file in the root directory and add your API keys and other environment variables:

OPENAI_API_KEY=your_openai_api_key_here

TAVILY_API_KEY=your_tavily_api_key_here

Add .env.txt to .gitignore:
Ensure that .env.txt is not tracked by Git by adding it to the .gitignore file.

Load environment variables:
Use the python-dotenv library in your code to load the environment variables from .env.txt.

Run the app:
Launch the app using Streamlit to view the dashboard.

📊 Evaluation Metrics

Metric	Description

✅ Coverage	Fetches an average of 10–15 articles per query via Tavily API.

✅ Tags Accuracy	Manual evaluation shows ~90% accuracy in relevant tag assignment.

✅ Research Matching	~70% of news articles are successfully matched to at least 1 academic paper.

✅ Performance	~6.2 seconds per complete search, tagging, and research match pipeline.
