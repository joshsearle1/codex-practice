# codex-practice

This is my safe practice repository for learning Codex.

## Goals

- Learn how Codex edits code
- Practice reviewing changes
- Learn Git and GitHub basics

## Todo app

This repo includes a small Python command-line todo app.

Add a task:

```powershell
python todo.py add "Buy groceries"
```

List tasks:

```powershell
python todo.py list
```

Mark a task complete:

```powershell
python todo.py complete 1
```

Tasks are saved in `tasks.json`, which is created automatically the first time
you add a task. That file is ignored by Git so your personal todo list stays
local.
