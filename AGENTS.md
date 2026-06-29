# AGENTS.md

Root guidance for agents working in this repository.

## Repo Layout

- `todo.py` - stdlib Python command-line todo app.
- `tests/test_todo.py` - unittest coverage for task loading, saving, listing, and completion.
- `README.md` - user-facing usage and test instructions.
- `tasks.json` - local runtime data created by the app; ignored by Git.

## Commands

- Add a task: `python todo.py add "Task"`
- List tasks: `python todo.py list`
- Complete a task: `python todo.py complete 1`
- Run tests: `py -m unittest discover -s tests`
- Test fallback: `python -m unittest discover -s tests`
- Build: none configured.
- Lint: no linter is configured.

## Conventions

- Keep changes simple, readable, and stdlib-only unless asked otherwise.
- Preserve the task JSON shape: `id`, `description`, `complete`.
- Update or add tests when behavior changes.
- Update relevant `README.md` files whenever adding new files, commands, features, or workflows.
- Do not commit local/generated files such as `tasks.json`, `__pycache__/`, `*.pyc`, or `tests/tmp_todo_tests_*/`.
- Keep README commands accurate when CLI behavior changes.

## Definition of Done

- Relevant unittest tests pass.
- Relevant `README.md` files account for the repo changes and still match app behavior.
- No local task data or generated files are included.
- The change fits the beginner-practice nature of this repo.
