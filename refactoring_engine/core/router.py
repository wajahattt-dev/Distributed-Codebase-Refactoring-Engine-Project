# Dispatches tasks to agents

from ..agents.loader_agent import LoaderAgent
from ..agents.pattern_agent import PatternAgent
from ..agents.suggest_agent import SuggestAgent
from ..agents.apply_agent import ApplyAgent

class Router:
    def __init__(self, settings):
        self.settings = settings
        self.loader = LoaderAgent(settings)
        self.pattern = PatternAgent(settings)
        self.suggest = SuggestAgent(settings)
        self.apply = ApplyAgent(settings)

    def dispatch(self, repo_path):
        loaded = self.loader.run(repo_path)
        patterns = self.pattern.run(loaded)
        suggestions = self.suggest.run(patterns)
        results = self.apply.run(suggestions)
        return results
