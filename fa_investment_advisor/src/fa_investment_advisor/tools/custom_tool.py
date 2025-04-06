from crewai.tools import BaseTool
from typing import Type, Optional
from pydantic import BaseModel, Field
from crewai.tools import tool
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables
load_dotenv(find_dotenv())


github_token = os.getenv("GITHUB_TOKEN", "GITHUB_TOKEN")
import os
from dotenv import load_dotenv, find_dotenv
# from crewai_tools import GithubSearchTool

# Load environment variables
load_dotenv(find_dotenv())

# # Retrieve GitHub token from environment
# github_token = os.getenv("GITHUB_TOKEN")

# # Check if GitHub token exists
# if not github_token:
#     raise ValueError("GitHub token is missing. Please set GITHUB_TOKEN in your .env file.")

# # Initialize GitHub Search Tool with explicit configuration
# github_search_tool = GithubSearchTool(
#     gh_token=github_token,  # Required: GitHub Personal Access Token
#     content_types=["repositories", "issues"]  # Required: Specify content types
# )


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

@tool("Api Fetcher Tool")
def api_fetcher(url: str, params: Optional[dict] = None) -> dict:
    """
    Fetches data from a financial API using HTTP GET requests.
    Example: Use this tool with an API endpoint and parameters.
    """
    if params is None:
        params = {}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

@tool("Data Analyzer Tool")
def data_analyzer(data: list) -> dict:
    """
    Processes and analyzes numerical or financial data.
    This tool uses pandas to generate descriptive statistics.
    """
    df = pd.DataFrame(data)
    analysis = df.describe().to_dict()
    return analysis

@tool("Chart Generator Tool")
def chart_generator(data: list, chart_type: str = "line") -> bytes:
    """
    Creates visualizations or charts from data using matplotlib.
    Returns the chart as image bytes.
    """
    df = pd.DataFrame(data)
    plt.figure(figsize=(8, 4))
    if chart_type == "line":
        for column in df.columns:
            plt.plot(df.index, df[column], label=column)
    elif chart_type == "bar":
        df.plot(kind="bar")
    else:
        raise ValueError("Unsupported chart type. Use 'line' or 'bar'.")
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return buf.read()

@tool("Market Data Fetcher Tool")
def market_data_fetcher(symbol: str, api_key: Optional[str] = None) -> dict:
    """
    Retrieves market-specific data for a given symbol from a financial API.
    If api_key is not provided, automatically read it from the environment variable.
    """
    import os
    if api_key is None:
        api_key = os.environ.get("MARKET_DATA_API_KEY")
        if not api_key:
            raise ValueError("MARKET_DATA_API_KEY is not provided in parameters or environment variables.")
    
    url = "https://www.alphavantage.co/query"
    params = {
         "function": "TIME_SERIES_DAILY",
         "symbol": symbol,
         "apikey": api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

@tool("Investment Simulator Tool")
def investment_simulator(initial_investment: float, annual_return_rate: float = 0.05, years: int = 10) -> dict:
    """
    Simulates investment scenarios using a compound interest formula.
    Returns the final investment value along with simulation details.
    """
    final_value = initial_investment * ((1 + annual_return_rate) ** years)
    return {
        "initial_investment": initial_investment,
        "annual_return_rate": annual_return_rate,
        "years": years,
        "final_value": final_value
    }

@tool("Report Formatter Tool")
def report_formatter(data: dict) -> str:
    """
    Formats raw analysis data into a structured report string.
    """
    report = "=== Financial Analysis Report ===\n\n"
    for key, value in data.items():
        report += f"{key}:\n{value}\n\n"
    return report

@tool("Markdown Converter Tool")
def markdown_converter(text: str) -> str:
    """
    Converts plain text into Markdown format.
    Uses the markdown library to transform the text.
    """
    import markdown
    return markdown.markdown(text)