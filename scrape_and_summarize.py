from dotenv import load_dotenv # type: ignore
import os
import openai # type: ignore
from langchain_openai import ChatOpenAI # type: ignore
from langchain_community.tools.tavily_search import TavilySearchResults # type: ignore
import streamlit as st # type: ignore

# Load environment variables from .env file
load_dotenv(dotenv_path="C:/Users/KIIT/insurance-news-insights/.env.txt")  # Specify full path to your .env file

# Get API keys from environment variables
openai_apikey = os.getenv("OPENAI_API_KEY")  # Correct key name
tavily_key = os.getenv("TAVILY_API_KEY")

# Check if the OpenAI API key is loaded correctly
if not openai_apikey:
    raise ValueError("OpenAI API key is not set. Please check your .env file.")

# Set the OpenAI API key
openai.api_key = openai_apikey

# Initialize the ChatOpenAI model from LangChain
model = ChatOpenAI(api_key=openai_apikey)

# Initialize TavilySearch tool
tool = TavilySearchResults(
    max_results=50,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True,
    api_key=tavily_key
)

# Function to summarize text using OpenAI API
def summarize_text(content):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# Function to structure the response from Tavily API
def structure_the_response(response):
    articles = []
    for item in response:  # No `.get()` here, just iterate directly
        articles.append({
            "title": item.get("title"),
            "source": item.get("source", {}).get("name", "Unknown"),
            "date": item.get("published"),
            "summary": item.get("summary") or item.get("content", "")[:300],
            "tags": ["climate change", "insurance"]
        })
    return articles

    

# Function to search for related research papers
def find_research_references_correlating_with_each_news_snnipets(structured_response):
    research_papers = [
        {
            "title": "Managing Basis Risks in Weather Parametric Insurance",
            "authors": "Hang Gao, Shuohua Yang",
            "date": "2024-09-25",
            "abstract": "Monte Carlo simulations reduce basis risk in weather parametric insurance.",
            "tags": ["basis risk", "parametric insurance"]
        },
        {
            "title": "Data-driven Parametric Insurance Framework Using Bayesian Neural Networks",
            "authors": "Subeen Pang, Chanyeol Choi",
            "date": "2022-09-22",
            "abstract": "Bayesian neural networks for improved risk predictions.",
            "tags": ["Bayesian neural networks", "parametric insurance"]
        }
    ]
    enriched_responses = []
    references_dict = {}
    for news in structured_response:
        related_papers = [paper for paper in research_papers if any(tag in paper["tags"] for tag in news["tags"])]
        enriched_responses.append(news)
        references_dict[news["title"]] = related_papers
    return enriched_responses, references_dict

# Function to define UI and visual elements in Streamlit
def define_ui_and_visual_elements(enriched_responses, references_dict):
    def filter_by_tag(data, selected_tag):
        return [item for item in data if selected_tag in item["tags"]]

    def get_all_tags(datasets):
        tags = set()
        for data in datasets:
            for item in data:
                tags.update(item["tags"])
        return sorted(tags)

    st.title("Climate Risk Insurance Dashboard")

    all_tags = get_all_tags([enriched_responses])
    selected_tag = st.selectbox("Select Tag", all_tags)

    filtered_responses = filter_by_tag(enriched_responses, selected_tag)
    
    st.write("### Filtered Results")
    for response in filtered_responses:
        st.subheader(response["title"])
        st.write(f"Source: {response['source']} | Date: {response['date']}")
        st.write(f"Summary: {response['summary']}")
        st.write("#### Related Research Papers:")
        for paper in references_dict.get(response["title"], []):
            st.write(f"Title: {paper['title']}, Authors: {paper['authors']}")
        st.markdown("---")

# Main function to run the app
def main():
    # Search for news articles related to Climate Risk Insurance
    query = "Climate Risk Insurance 2025"
    response = tool.invoke({"query": query})

    # Structure the response into articles
    structured_response = structure_the_response(response)

    # Find related research papers
    enriched_responses, references_dict = find_research_references_correlating_with_each_news_snnipets(structured_response)

    # Display the UI and results
    define_ui_and_visual_elements(enriched_responses, references_dict)

if __name__ == "__main__":
    main()