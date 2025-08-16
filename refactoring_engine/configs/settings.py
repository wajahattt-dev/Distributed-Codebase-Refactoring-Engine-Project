# Settings loader for YAML config
import yaml

class Settings:
    def __init__(self, data):
        self.data = data
        for k, v in data.items():
            setattr(self, k, v)

    @classmethod
    def load(cls, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return cls(data)
