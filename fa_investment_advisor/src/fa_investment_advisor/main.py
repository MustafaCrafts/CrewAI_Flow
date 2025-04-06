#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from fa_investment_advisor.crew import FaInvestmentAdvisor

# Ignore specific warnings that might clutter output
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with predefined inputs.
    This method allows flexible topic and year specification.
    """
    inputs = {
        'topic': 'Pakistan Ecnomical Research and Development',
        'current_year': str(datetime.now().year)
    }
    
    try:
        FaInvestmentAdvisor().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a specified number of iterations.
    Requires two command-line arguments: number of iterations and filename.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        FaInvestmentAdvisor().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    Requires task ID as a command-line argument.
    """
    try:
        FaInvestmentAdvisor().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution for a specified number of iterations.
    Requires two command-line arguments: number of iterations and OpenAI model name.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        FaInvestmentAdvisor().crew().test(
            n_iterations=int(sys.argv[1]), 
            openai_model_name=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

# Optional: Add a main block for direct script execution
if __name__ == "__main__":
    run()  # Default to running the crew