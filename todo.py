import argparse
import json
from pathlib import Path


TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Read saved tasks from tasks.json."""
    if not TASKS_FILE.exists():
        return []

    with TASKS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    """Save the current task list to tasks.json."""
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def get_next_id(tasks):
    """Pick the next task number."""
    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


def add_task(description):
    tasks = load_tasks()
    task = {
        "id": get_next_id(tasks),
        "description": description,
        "complete": False,
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task {task['id']}: {task['description']}")


def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks yet.")
        return

    for task in tasks:
        status = "x" if task["complete"] else " "
        print(f"{task['id']}. [{status}] {task['description']}")


def complete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["complete"] = True
            save_tasks(tasks)
            print(f"Completed task {task_id}: {task['description']}")
            return

    print(f"No task found with id {task_id}.")


def build_parser():
    parser = argparse.ArgumentParser(description="A simple command-line todo app.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="What you need to do")

    subparsers.add_parser("list", help="List all tasks")

    complete_parser = subparsers.add_parser("complete", help="Mark a task complete")
    complete_parser.add_argument("task_id", type=int, help="The task id to complete")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.task_id)


if __name__ == "__main__":
    main()
