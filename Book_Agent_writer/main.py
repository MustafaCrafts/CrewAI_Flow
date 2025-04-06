from agent import MyBookWriterAgents
from task import BookWriterTask
from crewai import Crew

Topic = "Artificial Intelligence"


agents = MyBookWriterAgents()
tasks = BookWriterTask()



# Agent class
Outline_Writer = agents.Outline_Writer()
Book_writer = agents.Book_writer()
# Task class
Outline_Writer_Task = tasks.Outline_Writer_Task(
    agent = Outline_Writer,
    topic = Topic
)

Book_Writer_Task = tasks.Book_Writer_Task(
    agent = Book_writer,
    context = Outline_Writer_Task.output
)

crew =  Crew(
    tasks = [Outline_Writer_Task, Book_Writer_Task],
    agents = [Outline_Writer, Book_writer],
    verbose = True,
)

def BookWriter():
    results = crew.kickoff()
    print(results)