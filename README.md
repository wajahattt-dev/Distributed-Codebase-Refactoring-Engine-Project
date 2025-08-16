
# Distributed Codebase Refactoring Engine

**Author:** Wajahat Hussain

---

## Overview

Distributed Codebase Refactoring Engine is a modular, agent-based system for automated Python codebase refactoring. It leverages static analysis (AST), OpenAI GPT (LLM), and Git to analyze, suggest, and apply advanced refactorings to any Python project—at scale.

---

## Features

- **Recursive codebase analysis**: Loads and parses all Python files in a repo
- **AST-based pattern detection**: Finds code smells, anti-patterns, and large classes/functions
- **LLM-powered suggestions**: Uses GPT-4o for actionable, context-aware refactor plans
- **Automated refactoring**: Applies safe, rule-based code transformations
- **Git integration**: Creates a new branch and commits all changes
- **Comprehensive reporting**: Generates before/after diffs and markdown reports
- **CLI and REST API**: Use from the command line or integrate with other tools

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/wajahattt-dev/Distributed-Codebase-Refactoring-Engine-Project.git
cd Distributed-Codebase-Refactoring-Engine-Project
```

### 2. Install dependencies
```bash
pip install -r refactoring_engine/requirements.txt
```

### 3. Configure your OpenAI API key
- Copy `refactoring_engine/configs/settings.yaml.example` to `settings.yaml` and add your key.
- **Never commit your real API key!**

### 4. Run the CLI
```bash
python -m refactoring_engine.cli.run refactoring_engine/examples/automl_repo --settings refactoring_engine/configs/settings.yaml
```

### 5. Run the REST API
```bash
uvicorn refactoring_engine.api.main:app --reload
# Visit http://127.0.0.1:8000/docs for Swagger UI
```

---

## Configuration

- `refactoring_engine/configs/settings.yaml`: API keys, agent toggles (never commit secrets)
- `refactoring_engine/configs/rules.yaml`: Refactor patterns and rule toggles

---

## Project Structure

```
refactoring_engine/
├── core/           # Orchestration, AST, Git, reporting
├── agents/         # Loader, pattern, suggest, apply agents
├── api/            # FastAPI REST server
├── cli/            # CLI entry point
├── configs/        # YAML configs (settings, rules)
├── utils/          # File loading, AST helpers, logging
├── tests/          # Unit tests
├── examples/       # Example repos for testing
├── requirements.txt
├── README.md
└── pyproject.toml
```

---

## Example Usage

**Refactor a local repo:**
```bash
python -m refactoring_engine.cli.run refactoring_engine/examples/automl_repo --settings refactoring_engine/configs/settings.yaml
```

**Refactor a public GitHub repo via API:**
1. Start the API:
	```bash
	uvicorn refactoring_engine.api.main:app --reload
	```
2. Use `/docs` to POST a JSON body like:
	```json
	{
	  "repo_path": "https://github.com/someuser/some-python-repo"
	}
	```

---

## Security & Best Practices

- **Never commit secrets or API keys.** Always use `.gitignore` for sensitive files.
- Use a separate `settings.yaml` for each environment.
- Review all refactor suggestions before merging to production.

---

## Credits

- **Developed by:** Wajahat Hussain
- **AI/LLM integration:** OpenAI GPT-4o
- **Core libraries:** Python, ast, astor, gitpython, fastapi, pydantic

---

## License

MIT
