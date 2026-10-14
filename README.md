Personal AI Task Agent

A Python-based AI agent that interprets natural-language requests and selects tools to perform tasks on behalf of a user.

This project explores how Large Language Models (LLMs) can go beyond generating text by selecting and calling tools to complete practical tasks. It is a small personal project inspired by my interest in AI agents and Human-AI Interaction.

Features
Natural Language Understanding: Accepts requests written in everyday language.
Tool Calling: Uses OpenAI's API to select appropriate tools based on the user's request.
Calculator: Evaluates mathematical expressions through a Python tool.
Task Management: Add, view, and remove tasks using natural-language commands.
Tool Execution: Executes the selected Python function and returns its result to the AI model.
Interactive CLI: Allows users to interact with the agent through a terminal.
How It Works

The agent follows a simple tool-calling workflow:

The user submits a request in natural language.
The LLM interprets the request and determines whether a tool is needed.
The Python application executes the selected tool.
The tool result is returned to the LLM.
The agent generates a response for the user.

For example:

User: "Add finish my thesis proposal to my tasks."

Agent workflow:

Identifies the task-management tool.
Calls the add_task function.
Stores the task in the application's task list.
Returns a confirmation to the user.
Technologies Used
Python
OpenAI API
OpenAI Responses API and function calling
JSON
python-dotenv
Project Structure
ai-task-agent/
├── agent.py           # Agent logic and tool-calling workflow
├── tools.py           # Calculator and task-management functions
├── requirements.txt   # Python dependencies
├── .env               # Local API key configuration
├── .gitignore         # Excludes secrets and local files
└── README.md          # Project documentation
Getting Started
Prerequisites
Python 3.10 or newer
An OpenAI API key
An OpenAI API account with available credits
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/ai-task-agent.git
cd ai-task-agent


2. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure the API key

Create a .env file in the project directory:

OPENAI_API_KEY=your_api_key_here

Replace the placeholder with your own API key.

Security: Never commit your API key or .env file to GitHub. The repository's .gitignore should exclude .env and venv/.

5. Run the agent
python agent.py

Enter a request in the terminal. Type exit to close the application.

Example Requests
What is 25% of 240?
Add finish my thesis proposal to my tasks.
What tasks do I have?
Remove task 1.
Current Limitations
An active OpenAI API account with available credits is required for LLM-powered interactions.
Tasks are stored in memory and are cleared when the application restarts.
The current version runs in a terminal and does not include a graphical interface.
The agent has a limited set of tools and does not connect to external services such as email or calendars.
Tool execution and model outputs should be validated carefully before using an agent for important tasks.
Future Improvements
Add persistent task storage using SQLite.
Build a web interface using Streamlit.
Introduce user-defined permissions and confirmation before executing actions.
Explore agent identity, memory, and personalization.
Investigate how users perceive and trust AI agents acting on their behalf.
Learning Objectives

This project explores practical concepts in:

LLM integration
Function calling and tool orchestration
Natural-language interfaces
Python application design
Human-AI interaction and task delegation