from abc import ABC, abstractmethod

from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName, AnalysisResult


class AlgorithmBase(ABC):
    PERCENTAGE_THRESHOLD: float
    ALGORITHM_NAME: AlgorithmName

    @classmethod
    def _generate_result(cls, positive_cells: int, positivity_percentage: float) -> AlgorithmAnalysis:
        result = AnalysisResult.POSITIVE if positivity_percentage > cls.PERCENTAGE_THRESHOLD\
            else AnalysisResult.NEGATIVE

        return AlgorithmAnalysis(
            name=cls.ALGORITHM_NAME,
            positive_cells=positive_cells,
            positivity_percentage=positivity_percentage,
            result=result
        )

    @abstractmethod
    def run(self, cells: list[int]) -> AlgorithmAnalysis:
        raise NotImplementedError("Subclasses should implement this method.")
    
