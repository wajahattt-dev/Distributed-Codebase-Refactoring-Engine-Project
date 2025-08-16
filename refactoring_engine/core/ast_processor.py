# AST transform utilities

import ast
import astor

class ASTProcessor:
    @staticmethod
    def parse_code(code: str):
        return ast.parse(code)

    @staticmethod
    def to_source(tree):
        return astor.to_source(tree)

    @staticmethod
    def find_nodes(tree, node_type):
        return [n for n in ast.walk(tree) if isinstance(n, node_type)]
