from mini_nucleiq.algorithms.algorithm_base import AlgorithmBase
from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName


class SurroundedOnesAlgorithm(AlgorithmBase):
    PERCENTAGE_THRESHOLD: float = 10.0
    ALGORITHM_NAME: AlgorithmName = AlgorithmName.SURROUNDED_ONES

    def run(self, cells: list[int]) -> AlgorithmAnalysis:
        positive_cells = 0
        positivity_percentage = 0.0
        if cells and len(cells) > 2:
            positive_cells = sum(1 for idx in range(1, len(cells) - 1) if cells[idx] == 1 and cells[idx - 1] == 0
                                 and cells[idx + 1] == 0)
            positivity_percentage = (positive_cells / len(cells)) * 100
        return self._generate_result(positive_cells, positivity_percentage)
