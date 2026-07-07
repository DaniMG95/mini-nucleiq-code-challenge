from pytest import fixture

from mini_nucleiq.algorithms.contiguous_ones import ContiguousOnesAlgorithm
from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName, AnalysisResult


@fixture()
def algorithm() -> ContiguousOnesAlgorithm:
    return ContiguousOnesAlgorithm()


def test_contiguous_ones(algorithm: ContiguousOnesAlgorithm):
    result = algorithm.run([0, 0, 1, 0, 0, 1, 0, 1, 1, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.CONTIGUOUS_ONES,
        positive_cells=3,
        positivity_percentage=30.0,
        result=AnalysisResult.POSITIVE,
    )


def test_contiguous_ones_counts_both_cells(algorithm: ContiguousOnesAlgorithm):
    result = algorithm.run([1, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.CONTIGUOUS_ONES,
        positive_cells=2,
        positivity_percentage=100.0,
        result=AnalysisResult.POSITIVE,
    )


def test_contiguous_ones_counts_all_cells(algorithm: ContiguousOnesAlgorithm):

    result = algorithm.run([1, 1, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.CONTIGUOUS_ONES,
        positive_cells=3,
        positivity_percentage=100.0,
        result=AnalysisResult.POSITIVE,
    )


def test_contiguous_ones_counts_separate(algorithm: ContiguousOnesAlgorithm):

    result = algorithm.run([1, 1, 0, 1, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.CONTIGUOUS_ONES,
        positive_cells=4,
        positivity_percentage=80.0,
        result=AnalysisResult.POSITIVE,
    )


def test_contiguous_ones_ignores(algorithm: ContiguousOnesAlgorithm):

    result = algorithm.run([1, 0, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.CONTIGUOUS_ONES,
        positive_cells=0,
        positivity_percentage=0.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_contiguous_ones_limit(algorithm: ContiguousOnesAlgorithm):

    result = algorithm.run([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.CONTIGUOUS_ONES,
        positive_cells=2,
        positivity_percentage=20.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_contiguous_ones_empty_cells(algorithm: ContiguousOnesAlgorithm):

    result = algorithm.run([])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.CONTIGUOUS_ONES,
        positive_cells=0,
        positivity_percentage=0.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_contiguous_ones_single_cell(algorithm: ContiguousOnesAlgorithm):

    result = algorithm.run([1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.CONTIGUOUS_ONES,
        positive_cells=0,
        positivity_percentage=0.0,
        result=AnalysisResult.NEGATIVE,
    )
