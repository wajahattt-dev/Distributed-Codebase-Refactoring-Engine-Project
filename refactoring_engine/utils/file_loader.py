# Load python files recursively from repo
import os

def load_python_files(root_dir):
    py_files = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.endswith('.py'):
                fpath = os.path.join(dirpath, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    py_files[fpath] = f.read()
    return py_files
