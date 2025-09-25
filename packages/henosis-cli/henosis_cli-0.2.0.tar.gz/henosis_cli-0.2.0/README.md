## Henosis Tools (CLI)

Standalone CLI and reusable Python library for local machine interactions extracted from the Henosis FastAPI server.

Features
- Filesystem: read, write, append, list, apply simplified patches
- Commands: run whitelisted commands (no shell) with timeout
- Sandboxing: workspace vs host scope with allowed roots

Quick start
- Install locally: pip install -e .
- Run: henosis-tools --help

Examples
- List directory: henosis-tools fs ls .
- Read a file: henosis-tools fs read CODEBASE_MAP.md
- Write from stdin: echo hello | henosis-tools fs write notes/todo.txt --content -
- Run a command: henosis-tools cmd run "git status" --allow "git"
- Apply a patch: henosis-tools patch apply --patch-file changes.patch

Environment variables
- HENOSIS_WORKSPACE_DIR, HENOSIS_ALLOW_EXTENSIONS, HENOSIS_MAX_FILE_BYTES
- HENOSIS_MAX_EDIT_BYTES, HENOSIS_EDIT_SAFEGUARD_MAX_LINES
- HENOSIS_ALLOW_COMMANDS, HENOSIS_COMMAND_TIMEOUT_SEC

Security notes
- host scope requires allowed roots or host_base, and commands require an allowlist.
- No shell is used to run commands; only the base executable is checked against allowlist.
