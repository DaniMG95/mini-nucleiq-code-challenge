from dataclasses import dataclass
from enum import StrEnum


class AlgorithmName(StrEnum):
    EVEN_ZEROES = "even-zeroes"
    CONTIGUOUS_ONES = "contiguous-ones"
    SURROUNDED_ONES = "surrounded-ones"


class AnalysisResult(StrEnum):
    POSITIVE = "positive"
    NEGATIVE = "negative"


@dataclass
class AlgorithmAnalysis:
    name: AlgorithmName
    positive_cells: int
    positivity_percentage: float
    result: AnalysisResult


@dataclass
class SampleAnalysis:
    sample_name: str
    algorithms: list[AlgorithmAnalysis]
    final_result: AnalysisResult