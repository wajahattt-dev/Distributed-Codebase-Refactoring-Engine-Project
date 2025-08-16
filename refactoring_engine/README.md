# Distributed Codebase Refactoring Engine (Python-only MVP)

## Overview
A modular, agent-based engine for automated Python codebase refactoring using AST, GPT, and Git.

## Features
- Loads and analyzes Python codebases
- Detects code smells and patterns
- Suggests and applies refactorings
- Commits changes to a new Git branch
- Generates before/after diff reports

## Usage
### CLI
```bash
python -m refactoring_engine.cli.run <repo_path>
```

### API
```bash
uvicorn refactoring_engine.api.main:app --reload
```

## Configuration
- `configs/settings.yaml`: API keys, agent toggles
- `configs/rules.yaml`: Refactor patterns

## Requirements
- Python 3.8+
- OpenAI API key (for GPT features)
- `pip install -r requirements.txt`

## License
MIT
