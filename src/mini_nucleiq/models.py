from dataclasses import dataclass
from enum import StrEnum
from typing import cast


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


@dataclass
class Sample:
    name: str
    cells: list[int]

    @classmethod
    def from_raw(cls, raw: object) -> Sample:
        if not isinstance(raw, dict):
            raise ValueError("Sample response must be an dict.")

        raw_data = cast(dict[str, object], raw)
        name = raw_data.get("name")
        raw_cells = raw_data.get("cells")

        if not isinstance(name, str):
            raise ValueError("Sample name must be a string.")

        if not isinstance(raw_cells, list):
            raise ValueError("Sample cells must be a list.")

        raw_cells = cast(list[object], raw_cells)
        cells: list[int] = []

        for cell in raw_cells:
            if isinstance(cell, bool) or not isinstance(cell, int) or cell not in (0, 1):
                raise ValueError("Sample cells must contain only 0 and 1.")
            cells.append(cell)

        return cls(name=name, cells=cells)