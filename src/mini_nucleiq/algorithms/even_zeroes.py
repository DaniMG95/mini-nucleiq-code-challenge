from mini_nucleiq.algorithms.algorithm_base import AlgorithmBase
from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName


class EvenZeroesAlgorithm(AlgorithmBase):
    PERCENTAGE_THRESHOLD: float = 30.0
    ALGORITHM_NAME: AlgorithmName = AlgorithmName.EVEN_ZEROES

    def run(self, cells: list[int]) -> AlgorithmAnalysis:
        positive_cells = 0
        positivity_percentage = 0.0
        if cells:
            positive_cells = sum(1 for idx, cell in enumerate(cells) if cell == 0 and idx % 2 == 0)
            positivity_percentage = (positive_cells / len(cells)) * 100
        return self._generate_result(positive_cells, positivity_percentage)
