# Common AST helper functions
import ast

def get_function_names(tree):
    return [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]

def get_class_names(tree):
    return [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
