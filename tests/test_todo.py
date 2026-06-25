import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import todo


class TodoAppTests(unittest.TestCase):
    def setUp(self):
        tests_folder = Path(__file__).resolve().parent
        self.temp_folder = tempfile.TemporaryDirectory(
            prefix="tmp_todo_tests_",
            dir=tests_folder,
        )
        self.original_tasks_file = todo.TASKS_FILE
        todo.TASKS_FILE = Path(self.temp_folder.name) / "tasks.json"

    def tearDown(self):
        todo.TASKS_FILE = self.original_tasks_file
        self.temp_folder.cleanup()

    def capture_output(self, function, *args):
        output = io.StringIO()

        with redirect_stdout(output):
            function(*args)

        return output.getvalue().strip()

    def read_saved_tasks(self):
        with todo.TASKS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    def test_load_tasks_returns_empty_list_when_file_does_not_exist(self):
        self.assertEqual(todo.load_tasks(), [])

    def test_add_task_saves_a_new_incomplete_task(self):
        message = self.capture_output(todo.add_task, "Learn unit tests")

        self.assertEqual(message, "Added task 1: Learn unit tests")
        self.assertEqual(
            self.read_saved_tasks(),
            [
                {
                    "id": 1,
                    "description": "Learn unit tests",
                    "complete": False,
                }
            ],
        )

    def test_list_tasks_shows_saved_tasks(self):
        todo.save_tasks(
            [
                {"id": 1, "description": "Write tests", "complete": False},
                {"id": 2, "description": "Run tests", "complete": True},
            ]
        )

        message = self.capture_output(todo.list_tasks)

        self.assertEqual(message, "1. [ ] Write tests\n2. [x] Run tests")

    def test_list_tasks_shows_message_when_there_are_no_tasks(self):
        message = self.capture_output(todo.list_tasks)

        self.assertEqual(message, "No tasks yet.")

    def test_complete_task_marks_matching_task_complete(self):
        todo.save_tasks(
            [
                {"id": 1, "description": "Write tests", "complete": False},
                {"id": 2, "description": "Run tests", "complete": False},
            ]
        )

        message = self.capture_output(todo.complete_task, 2)

        self.assertEqual(message, "Completed task 2: Run tests")
        self.assertEqual(
            self.read_saved_tasks(),
            [
                {"id": 1, "description": "Write tests", "complete": False},
                {"id": 2, "description": "Run tests", "complete": True},
            ],
        )

    def test_complete_task_shows_message_when_id_is_missing(self):
        todo.save_tasks(
            [{"id": 1, "description": "Write tests", "complete": False}]
        )

        message = self.capture_output(todo.complete_task, 99)

        self.assertEqual(message, "No task found with id 99.")
        self.assertEqual(
            self.read_saved_tasks(),
            [{"id": 1, "description": "Write tests", "complete": False}],
        )


if __name__ == "__main__":
    unittest.main()
