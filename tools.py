import math


# --------------------------------
# Calculator
# --------------------------------

def calculator(expression):
    """
    Performs a mathematical calculation.
    """

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {
                "sqrt": math.sqrt,
                "pow": pow
            }
        )

        return str(result)

    except Exception:
        return "Sorry, I could not calculate that."


# --------------------------------
# Task list
# --------------------------------

tasks = []


def add_task(task):
    """
    Adds a task to our task list.
    """

    tasks.append(task)

    return f"Added task: {task}"


def get_tasks():
    """
    Returns all tasks.
    """

    if not tasks:
        return "You currently have no tasks."

    result = "Your tasks:\n"

    for number, task in enumerate(tasks, start=1):
        result += f"{number}. {task}\n"

    return result


def remove_task(task_number):
    """
    Removes a task from the list.
    """

    try:

        index = int(task_number) - 1

        removed_task = tasks.pop(index)

        return f"Removed task: {removed_task}"

    except (ValueError, IndexError):

        return "I could not find that task."