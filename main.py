# import frameworks and llms
from crewai import Crew, Process
from langchain_community.llms import Ollama

#from textwrap import dedent #useful for inputs

# import agents and tasks
from agents import ExampleAgents
from tasks import ExampleTasks


# Define Article Writing Crew
class Crew:
    def __init__(self):
        self.ollama_llama_3 = Ollama(model="crewai-llama3")

    def run(self):
        # Define your agents and tasks in agents.py and tasks.py and import here
        agents = ExampleAgents()
        tasks = ExampleTasks()

        # set up agents
        # example_agent = agents.example_agent()
        #TODO: Add Agents

        # set up tasks
        # example_task = tasks.example_task(example_agent) 
        #TODO: Add tasks

        # define crew with all agents and tasks
        crew = Crew(
            agents = [], #TODO: Add agents
            tasks = [], #TODO: Add tasks
            process = Process.hierarchical,
            manager_llm = self.ollama_llama_3, #Change manager?
            verbose=True,
        )

        # run crew
        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Let's kick off our crew")

    crew = Crew()
    result = crew.run()
    print("\n\n########################")
    print("## Recommendation generation result:")
    print("########################\n")
    print(result)