from abc import ABC, abstractmethod


class BaseCaptchaSolver(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def solve(self):
        pass
