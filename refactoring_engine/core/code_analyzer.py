# Static code analyzer & metrics

import ast

class CodeAnalyzer:
    def __init__(self, code: str):
        self.tree = ast.parse(code)

    def count_functions(self):
        return len([n for n in ast.walk(self.tree) if isinstance(n, ast.FunctionDef)])

    def count_classes(self):
        return len([n for n in ast.walk(self.tree) if isinstance(n, ast.ClassDef)])

    def get_metrics(self):
        return {
            'functions': self.count_functions(),
            'classes': self.count_classes(),
        }
