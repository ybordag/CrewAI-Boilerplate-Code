#import json
#import os
#import requestsl
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime

from langchain.tools import tool

# example input
class ExampleInput(BaseModel):
    """Inputs to a list of relevant articles"""
    #TODO: add example input

# example output
class ExampleOutput(BaseModel):
    """Inputs to a list of relevant articles"""
    #TODO: add example input

class ExampleTools():
    @tool("example tool description", args_schema=ExampleInput)
    def example_tool() -> ExampleOutput:
        """
        A short description for this example tool

        Args:
            example_input: input defined in ExampleInput
        
        Returns:
            put a description here of what this tool returns
        """
        #TODO: Implement example tool
        return ExampleOutput()