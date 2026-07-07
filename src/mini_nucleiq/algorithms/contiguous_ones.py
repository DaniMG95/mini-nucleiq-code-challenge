from mini_nucleiq.algorithms.algorithm_base import AlgorithmBase
from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName


class ContiguousOnesAlgorithm(AlgorithmBase):
    PERCENTAGE_THRESHOLD: float = 20.0
    ALGORITHM_NAME: AlgorithmName = AlgorithmName.CONTIGUOUS_ONES

    def run(self, cells: list[int]) -> AlgorithmAnalysis:
        positive_cells = 0
        positivity_percentage = 0.0
        if cells and len(cells) > 1:
            for idx in range(len(cells)):
                if cells[idx] != 1:
                    continue
                elif 0 < idx < len(cells) - 1 and (cells[idx - 1] == 1 or cells[idx + 1] == 1):
                    positive_cells += 1
                elif idx == 0 and cells[idx + 1] == 1:
                    positive_cells += 1
                elif idx == len(cells) - 1 and cells[idx - 1] == 1:
                    positive_cells += 1
            positivity_percentage = (positive_cells / len(cells)) * 100
        return self._generate_result(positive_cells, positivity_percentage)
