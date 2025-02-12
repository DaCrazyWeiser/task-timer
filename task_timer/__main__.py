"""
main.py
Isaac Dawson <isaac.dawson@student.cune.edu>
2025/02/04

This program is a task timer CLI tool. It can track tasks began by
the user, and export the timesheet to a separate file.
"""

import click
import json
import os
import pandas as pd
from datetime import datetime


@click.group()
def main():
    """This is my main cli."""


def load_task_list():
    """Load the list of tasks from the JSON file."""
    if os.path.exists("timesheet.json"):
        with open("timesheet.json", "r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):  # Ensure it's a list
                    return []
                return data
            except json.JSONDecodeError:
                return []
    return []


@click.command()
def start():
    """Start one or more tasks and track their duration."""
    
    tasks = load_task_list()

    if any(task.get("end_time") is None for task in tasks):
        again = click.prompt("Would you like to start another task? y/n")

        if ((again == "n") or (again == "N")):
            return

    task_name = click.prompt("Enter the name of your task")
    time_stamp = datetime.now().isoformat()

    tasks.append({"task": task_name, "start_time": time_stamp, "end_time": None, "total_time": None})

    with open("timesheet.json", "w") as file:
        json.dump(tasks, file, indent=4)

    click.echo(f"Task started: {task_name}")


@click.command()
def stop():
    """End a chosen task and record its duration."""

    tasks = load_task_list()
    time_stamp = datetime.now().isoformat()

    target_task = click.prompt("Enter the name of the task you want to end")
    task = next((t for t in tasks if t["task"] == target_task and t["end_time"] is None), None)
    
    if task is None:
        click.echo("There is no task by that name.")

    elif (task["task"] == target_task):
        
        task["end_time"] = time_stamp
        start_time = datetime.fromisoformat(task["start_time"])
        task["total_time"] = str(datetime.fromisoformat(time_stamp) - start_time)

        with open("timesheet.json", "w") as file:
            json.dump(tasks, file, indent=4)

        click.echo(f"Task stopped: {task['task']}")
        return


@click.command()
def summary():
    """Provide a summary of the current time sheet."""

    tasks = load_task_list()

    if not tasks:
        click.echo("No tasks recorded yet.")
        return

    click.echo(json.dumps(tasks, indent=4))


@click.command()
def peek():
    """Show the current task if there's one running."""
    
    tasks = load_task_list()

    for task in tasks:
        if task["end_time"] is None:
            click.echo(f"Current task: {task['task']} (Started at {task['start_time']})")
            return

    click.echo("No task is currently running.")


@click.command()
def clear_tasks():
    """Clear the content of the JSON file timesheet."""

    with open("timesheet.json", "w") as file:
        file.write("")


@click.command()
def transfer_to_csv():
    """Convert the json data into an exportable csv file."""
    
    try:
        df = pd.read_json("timesheet.json")
        df.to_csv("timesheet.csv", index=False)
        click.echo("json file successfully converted to a csv file.")

    except Exception as e:
        click.echo(f"Gasp! An ERROR has occurred: {e}")

main.add_command(start)
main.add_command(stop)
main.add_command(summary)
main.add_command(peek)
main.add_command(clear_tasks)
main.add_command(transfer_to_csv)


if __name__ == '__main__':
    main()
