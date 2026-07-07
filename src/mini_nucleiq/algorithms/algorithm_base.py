from abc import ABC, abstractmethod

from mini_nucleiq.models import AlgorithmAnalysis


class AlgorithmBase(ABC):

    @abstractmethod
    def run(self, cells: list[int]) -> AlgorithmAnalysis:
        raise NotImplementedError("Subclasses should implement this method.")