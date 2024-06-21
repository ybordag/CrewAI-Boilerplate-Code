from crewai import Task
from textwrap import dedent
# from datetime import datetime

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py

# Add output pydantics????

class ExampleTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def example_task(self, agent):
        return Task(
            description = dedent(f"""
                            Add a brief task description
                            """),
            agent = agent,
            async_execution = True,
            expected_output = dedent("""
                                Brief des
                                     
                                Example Output:
                                     
                                [
                                    {
                                        'title': 'My Example',
                                        'URL': 'https://example.com/example',
                                        'summary': 'Lorem ipsum dolor sit amet, consectetur adipiscing 
                                                    elit, sed do eiusmod tempor incididunt ut labore et 
                                                    dolore magna aliqua. Ut enim ad minim veniam, quis 
                                                    nostrud exercitation ullamco laboris nisi ut aliquip 
                                                    ex ea commodo consequat. Duis aute irure dolor in 
                                                    reprehenderit in voluptate velit esse cillum dolore 
                                                    eu fugiat nulla pariatur. Excepteur sint occaecat 
                                                    cupidatat non proident, sunt in culpa qui officia 
                                                    deserunt mollit anim id est laborum ...',
                                    },

                                    {{...}}
                                ]
                                """)
        )
