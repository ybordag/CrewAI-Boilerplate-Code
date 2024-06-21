from crewai import Agent
from langchain_community.llms import Ollama
from textwrap import dedent

# Import Tools
# from tools.example_tools import ExampleTools
# TODO: Add tools


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class ExampleAgents:
    def __init__(self):
        self.ollama_llama_3 = Ollama(model="crewai-llama3") #TODO: add crewai-llama3 to ollama
        # self.example_tool = ExampleTools.example_tool

    def example_agent(self):
        return Agent(
            role="Example Agent",
            goal = dedent(f"""
                        Add a short description for the Agent's functionality which aligns with their 
                        role. Be as precise and concise as possible.
                        """),
            backstory = dedent(f"""
                            Add a more detailed description for the Agent's backstory which adds more 
                            information and context around the agent's behavior, motivations, tone, 
                            style, interests, etc.
                            """),
            tools=[], #[self.example_tool],
            allow_delegation = True,
            verbose = True,
            llm = self.ollama_llama_3,
        )
