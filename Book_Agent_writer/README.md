# Book Writer Project

This project is a book writing system built using the CrewAI framework. It creates and executes two main tasks—one for generating a detailed book outline and another for writing the complete book content. The system leverages online search and web scraping to gather the latest data and trends on a given topic.

## Main Features

- **Automated Outline Generation:**  
  Uses the `Outline_Writer` agent to research and develop a detailed outline for a book on a specific topic.
- **Complete Book Writing:**  
  The `Book_writer` agent uses the generated outline to write the full book with detailed chapters and content.
- **Online Data Integration:**  
  Incorporates the `SerperDevTool` for online search and `ScrapeWebsiteTool` for web scraping to ensure data validity and relevance.
- **LLM Powered Agents:**  
  Both agents are powered by the language model `gemini/gemini-2.0-flash-exp`, enabling expert-level content generation.
- **Environment Management:**  
  Utilizes the `dotenv` library to load environment variables securely from a `.env` file.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Required Packages:**
   Make sure you have Python 3.8 or higher installed. Then install the dependencies using pip:
   ```bash
   pip install crewai crewai_tools python-dotenv
   ```

3. **Setup Environment Variables:**
   Create a `.env` file in the root directory and add any required environment variables, for example:
   ```env
   API_KEY=your_api_key_here
   ```

## Usage

Run the Main Script:
Execute the following command to start the process:
```bash
python main.py
```

## How It Works:

The code defines two tasks:
- **Outline_Writer_Task**: Generates a detailed outline for a book based on online data.
- **Book_Writer_Task**: Writes the complete book using the outline.

Two agents, `Outline_Writer` and `Book_writer`, are instantiated with specific roles and goals.
The `Crew` class from CrewAI orchestrates the execution of these tasks and agents.
The final output (the book content) is printed to the console.

## Project Structure

```
.
├── main.py         # Main entry point of the project
├── agents.py       # Contains agent definitions for outline and book writing
├── tasks.py        # Contains task definitions for the book writing process
├── .env            # Environment variables file
└── README.md       # Project documentation
```

## License

Include license information here.

## Contributing

Contributions are welcome! Please follow the contribution guidelines for submitting issues or pull requests.