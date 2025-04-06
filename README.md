# CrewAI Framework

CrewAI is a lightweight and fast Python framework designed to help developers create autonomous AI agents that work together to perform complex tasks. Unlike other frameworks, CrewAI is built from scratch and doesn't rely on external libraries like LangChain, making it efficient and flexible.

## Key Features of CrewAI

* **Agents:** These are autonomous units in CrewAI that perform specific tasks, make decisions based on their roles and goals, use tools to achieve objectives, and can collaborate with other agents. For example, a 'Researcher' agent might focus on gathering information, while a 'Writer' agent could be responsible for creating content.

* **Tasks:** Tasks are specific assignments given to agents. They include details like descriptions, the responsible agent, required tools, and more. Tasks can be executed sequentially or hierarchically, depending on the defined workflow.

* **Crews:** A crew is a group of agents working together to accomplish a set of tasks. The crew defines the strategy for task execution, agent collaboration, and the overall workflow.

## Getting Started with CrewAI

To begin using CrewAI, follow these steps:

1. **Installation:** Install CrewAI using pip:
   ```bash
   pip install crewai
   ```

   For additional tools, use:
   ```bash
   pip install 'crewai[tools]'
   ```

2. **Creating a New Project:** Initialize a new CrewAI project by running:
   ```bash
   crewai create crew project_name
   ```
   This command sets up a new directory with the basic structure for your project.

3. **Defining Agents and Tasks:** Customize the `agents.yaml` and `tasks.yaml` files to define the roles, goals, and tasks for your agents. Variables like `{topic}` can be used and will be replaced by values defined in your main script.

4. **Running the Crew:** Execute your project by running the main script:
   ```bash
   python main.py
   ```
   This will initiate the agents and tasks as configured.

## Example File Structure

Here's a typical structure for a CrewAI project:
```
my_crewai_project/
├── .env
├── agents.py
├── tools.py
├── tasks.py
├── requirements.txt
└── main.py
```

In this setup:
* `.env` stores environment variables.
* `agents.py` defines the agents.
* `tools.py` includes any tools the agents might use.
* `tasks.py` outlines the tasks assigned to agents.
* `requirements.txt` lists the dependencies.
* `main.py` is the entry point that ties everything together.

## Learning Resources

For a comprehensive beginner's guide, consider exploring the official documentation at [docs.crewai.com](https://docs.crewai.com).

By following these steps and utilizing the provided resources, you can set up CrewAI and begin developing collaborative AI agents tailored to your specific needs.
