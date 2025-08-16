# Abstract agent

from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, settings):
        self.settings = settings

    @abstractmethod
    def run(self, *args, **kwargs):
        pass

    def callback(self, *args, **kwargs):
        pass
