import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools import calculator, add_task, get_tasks, remove_task


# --------------------------------
# Load API key
# --------------------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# --------------------------------
# Describe our tools to the AI
# --------------------------------

tools = [

    {
        "type": "function",

        "name": "calculator",

        "description": "Calculate a mathematical expression.",

        "parameters": {
            "type": "object",

            "properties": {

                "expression": {
                    "type": "string",
                    "description": "Mathematical expression to calculate."
                }

            },

            "required": ["expression"]
        }
    },

    {
        "type": "function",

        "name": "add_task",

        "description": "Add a new task to the user's task list.",

        "parameters": {
            "type": "object",

            "properties": {

                "task": {
                    "type": "string",
                    "description": "The task to add."
                }

            },

            "required": ["task"]
        }
    },

    {
        "type": "function",

        "name": "get_tasks",

        "description": "Show the user's current task list.",

        "parameters": {
            "type": "object",

            "properties": {},

            "required": []
        }
    },

    {
        "type": "function",

        "name": "remove_task",

        "description": "Remove a task from the task list.",

        "parameters": {
            "type": "object",

            "properties": {

                "task_number": {
                    "type": "string",
                    "description": "The number of the task to remove."
                }

            },

            "required": ["task_number"]
        }
    }
]


# --------------------------------
# Connect AI tool calls to Python
# --------------------------------

def execute_tool(name, arguments):

    if name == "calculator":

        return calculator(
            arguments["expression"]
        )

    elif name == "add_task":

        return add_task(
            arguments["task"]
        )

    elif name == "get_tasks":

        return get_tasks()

    elif name == "remove_task":

        return remove_task(
            arguments["task_number"]
        )

    return "Unknown tool."


# --------------------------------
# Run the AI agent
# --------------------------------

def run_agent(user_request):

    response = client.responses.create(

        model="gpt-5-mini",

        instructions="""
        You are a personal AI task agent.

        Your job is to understand the user's request
        and decide whether you need to use one of
        the available tools.

        Available tools:

        - calculator
        - add_task
        - get_tasks
        - remove_task

        Use tools when they are appropriate.

        Be concise and helpful.
        """,

        tools=tools,

        input=user_request
    )


    # --------------------------------
    # Check whether the AI requested a tool
    # --------------------------------

    while True:

        tool_calls = [

            item for item in response.output

            if item.type == "function_call"
        ]


        # If there are no tools to execute,
        # return the AI's answer.

        if not tool_calls:

            return response.output_text


        # --------------------------------
        # Execute requested tools
        # --------------------------------

        tool_outputs = []

        for tool_call in tool_calls:

            name = tool_call.name

            arguments = json.loads(
                tool_call.arguments
            )

            result = execute_tool(
                name,
                arguments
            )

            tool_outputs.append({

                "type": "function_call_output",

                "call_id": tool_call.call_id,

                "output": result
            })


        # --------------------------------
        # Give the tool results back to AI
        # --------------------------------

        response = client.responses.create(

            model="gpt-5-mini",

            instructions="""
            You are a personal AI task agent.

            Explain the result of the action
            clearly to the user.
            """,

            tools=tools,

            input=tool_outputs
        )


# --------------------------------
# Main program
# --------------------------------

print("=" * 50)

print("PERSONAL AI TASK AGENT")

print("=" * 50)

print("Type 'exit' to stop.")

print()


while True:

    user_request = input("You: ")

    if user_request.lower() == "exit":

        print("Goodbye!")

        break


    answer = run_agent(
        user_request
    )

    print()

    print("Agent:", answer)

    print()