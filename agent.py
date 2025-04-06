from crewai import  Agent , LLM
from dotenv import load_dotenv

load_dotenv()

model = LLM(model="gemini/gemini-2.0-flash-exp")

class MyBookWriterAgents:


    def Outline_Writer(self):
        return Agent(
            role = "Outline_Writer",
            goal = "Develop a detailed outline for the book",
            backstory = "i am a season expert in writing book outlines i have 10+ years of experience in writing book outlines",
            verbose = True,
            llm = model,
        )
    

    def Book_writer(self):
        return Agent(
            role = "Book_writer",
            goal = "Write the book based on the outline",
            backstory = "i am a season expert in writing books i have 15+ years of experience in writing books",
            verbose = True,
            llm = model,
        )