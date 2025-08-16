# Entry point CLI → `python cli/run.py`
import argparse
from ..core.engine import RefactoringEngine

def main():
    parser = argparse.ArgumentParser(description='Distributed Codebase Refactoring Engine')
    parser.add_argument('repo_path', type=str, help='Path to the Python repository to refactor (e.g., refactoring_engine/examples/demo_repo)')
    parser.add_argument('--settings', type=str, default='configs/settings.yaml', help='Path to settings YAML')
    args = parser.parse_args()

    import os
    # Ensure repo_path is absolute
    repo_path = args.repo_path
    if not os.path.isabs(repo_path):
        candidate = os.path.abspath(os.path.join(os.getcwd(), repo_path))
        if os.path.exists(candidate):
            repo_path = candidate
        else:
            print(f"[ERROR] Could not find repo at {candidate}")
            print("[HINT] Use: refactoring_engine/examples/demo_repo as the path argument.")
            exit(1)
    print(f"[INFO] Using repo path: {repo_path}")
    engine = RefactoringEngine(args.settings)
    report_path = engine.run(repo_path)
    print(f'Refactoring complete. Report: {report_path}')

if __name__ == '__main__':
    main()
