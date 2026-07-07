from mini_nucleiq.algorithms.algorithm_base import AlgorithmBase
from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName, AnalysisResult


class EvenZeroesAlgorithm(AlgorithmBase):
    PERCENTAGE_THRESHOLD = 30.0

    def run(self, cells: list[int]) -> AlgorithmAnalysis:
        if not cells:
            return AlgorithmAnalysis(
                name=AlgorithmName.EVEN_ZEROES,
                positive_cells=0,
                positivity_percentage=0.0,
                result=AnalysisResult.NEGATIVE
            )
        positive_cells = sum(1 for idx, cell in enumerate(cells) if cell == 0 and idx % 2 == 0)
        positivity_percentage = (positive_cells / len(cells)) * 100
        result = AnalysisResult.POSITIVE if positivity_percentage > self.PERCENTAGE_THRESHOLD\
            else AnalysisResult.NEGATIVE

        return AlgorithmAnalysis(
            name=AlgorithmName.EVEN_ZEROES,
            positive_cells=positive_cells,
            positivity_percentage=positivity_percentage,
            result=result
        )