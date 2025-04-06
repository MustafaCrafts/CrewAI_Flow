import os
from crewai import Agent, Crew, Task, Process

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Import necessary tools
from crewai_tools import (
    ScrapeWebsiteTool,
    FileWriterTool,
    TXTSearchTool,
    JSONSearchTool,
    SerperDevTool
)

# Import custom tools
from .tools.custom_tool import (
    api_fetcher,
    data_analyzer,
    chart_generator,
    market_data_fetcher,
    investment_simulator,
    report_formatter,
    markdown_converter
)

class FaInvestmentAdvisor:
    def __init__(self, topic="Financial Markets", year=2025):
        """
        Initialize the crew with configurable topic and year.

        Args:
            topic (str): The financial topic or sector to investigate.
            year (int): The current year for contextual research.
        """
        self.topic = topic
        self.year = year

    def researcher(self) -> Agent:
        """Create Data Collector Agent."""
        return Agent(
            role="Financial Market Research Specialist",
            goal="Efficiently gather and synthesize current financial market trends and insights",
            backstory=(
                "You are a meticulous and proactive financial researcher with expertise in collecting "
                "and summarizing complex market information. Your ability to rapidly scan multiple "
                "sources and distill key insights makes you an invaluable asset in understanding "
                "emerging financial trends and opportunities."
            ),
            verbose=True,
            tools=[ScrapeWebsiteTool(), SerperDevTool(), api_fetcher]
        )

    def reporting_analyst(self) -> Agent:
        """Create Financial Analyst Agent."""
        return Agent(
            role="Financial Data Interpretation and Analysis Expert",
            goal="Transform raw financial data into meaningful, actionable insights",
            backstory=(
                "As a detail-oriented financial analyst, you excel at breaking down complex numerical "
                "information into clear, understandable narratives. Your analytical skills bridge "
                "the gap between raw data and strategic decision-making, providing comprehensive "
                "and nuanced financial interpretations."
            ),
            verbose=True,
            tools=[JSONSearchTool(), FileWriterTool(), data_analyzer, chart_generator]
        )

    def investment_advisor(self) -> Agent:
        """Create Investment Advisor Agent."""
        return Agent(
            role="Strategic Investment Strategy Consultant",
            goal="Develop personalized and data-driven investment recommendations",
            backstory=(
                "You are a seasoned investment strategist with a deep understanding of market "
                "dynamics, risk management, and portfolio optimization. Your recommendations are "
                "grounded in thorough research, current market conditions, and a forward-looking "
                "perspective that balances potential returns with calculated risks."
            ),
            verbose=True,
            tools=[market_data_fetcher, investment_simulator]
        )

    def report_generator(self) -> Agent:
        """Create Report Generator Agent."""
        return Agent(
            role="Professional Financial Report Architect",
            goal="Create comprehensive, clear, and professionally formatted financial reports",
            backstory=(
                "A master communicator who transforms complex financial research and analysis into "
                "elegant, accessible reports. You have a unique talent for presenting technical "
                "information in a narrative that is both engaging and intellectually rigorous, "
                "ensuring that key insights are immediately understood by diverse audiences."
            ),
            verbose=True,
            tools=[TXTSearchTool(), FileWriterTool(), report_formatter, markdown_converter]
        )

    def research_task(self) -> Task:
        """Create Research Task."""
        description = (
            f"Conduct a comprehensive investigation of {self.topic} for the year {self.year}. "
            "Focus on emerging trends, potential investment sectors, and global economic indicators. "
            "Utilize multiple sources and cross-reference information to ensure accuracy and depth."
        )
        expected_output = (
            "A structured list of 10 key insights covering market trends, "
            "economic indicators, emerging sectors, and potential investment opportunities."
        )
        return Task(
            description=description,
            expected_output=expected_output,
            agent=self.researcher()
        )

    def analyze_financial_data(self) -> Task:
        """Create Financial Data Analysis Task."""
        description = (
            "Perform an in-depth analysis of the collected research data. "
            "Develop comprehensive insights by examining financial metrics, "
            "historical performance, market sentiment, and potential future trajectories. "
            "Provide a detailed, nuanced interpretation of the research findings."
        )
        expected_output = (
            "A thoroughly researched markdown report with multiple sections, "
            "including market overview, sector-specific analysis, trend interpretations, "
            "and preliminary investment recommendations."
        )
        return Task(
            description=description,
            expected_output=expected_output,
            agent=self.reporting_analyst(),
            output_file='financial_analysis.md'
        )

    def generate_investment_recommendations(self) -> Task:
        """Create Investment Recommendations Task."""
        description = (
            f"Based on the comprehensive {self.topic} analysis for {self.year}, "
            "develop strategic investment recommendations. Consider risk profiles, "
            "market volatility, potential returns, and current economic conditions. "
            "Provide clear, actionable, and diversified investment strategies."
        )
        expected_output = (
            "A concise list of 3-5 targeted investment recommendations, "
            "each including rationale, potential returns, risk assessment, "
            "and strategic positioning."
        )
        return Task(
            description=description,
            expected_output=expected_output,
            agent=self.investment_advisor()
        )

    def compile_and_format_report(self) -> Task:
        """Create Final Report Compilation Task."""
        description = (
            "Synthesize all previous research, analysis, and recommendations "
            "into a cohesive, professional financial report. Ensure logical flow, "
            "clarity, and comprehensive coverage of all key findings."
        )
        expected_output = (
            "A polished, professionally formatted markdown report that integrates "
            "research insights, detailed analysis, and strategic investment "
            "recommendations into a single, compelling document."
        )
        return Task(
            description=description,
            expected_output=expected_output,
            agent=self.report_generator(),
            output_file='investment_report.md'
        )

    def crew(self) -> Crew:
        """Create and Configure the Crew."""
        return Crew(
            agents=[
                self.researcher(),
                self.reporting_analyst(),
                self.investment_advisor(),
                self.report_generator()
            ],
            tasks=[
                self.research_task(),
                self.analyze_financial_data(),
                self.generate_investment_recommendations(),
                self.compile_and_format_report()
            ],
            process=Process.sequential,
            verbose=True,
            memory=True,
            # planning=True,
            # planning_llm="google/gemini-2.0-flash"
        )
