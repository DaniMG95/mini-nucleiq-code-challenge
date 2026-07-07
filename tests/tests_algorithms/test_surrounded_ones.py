from pytest import fixture

from mini_nucleiq.algorithms.surrounded_ones import SurroundedOnesAlgorithm
from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName, AnalysisResult


@fixture
def algorithm():
    return SurroundedOnesAlgorithm()


def test_surrounded_ones(algorithm: SurroundedOnesAlgorithm):

    result = algorithm.run([0, 0, 1, 0, 0, 1, 0, 1, 1, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.SURROUNDED_ONES,
        positive_cells=2,
        positivity_percentage=20.0,
        result=AnalysisResult.POSITIVE,
    )


def test_surrounded_ones_between_zeroes(algorithm: SurroundedOnesAlgorithm):

    result = algorithm.run([0, 1, 0])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.SURROUNDED_ONES,
        positive_cells=1,
        positivity_percentage=33.33333333333333,
        result=AnalysisResult.POSITIVE,
    )


def test_surrounded_ones_multiples(algorithm: SurroundedOnesAlgorithm):

    result = algorithm.run([0, 1, 0, 1, 0])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.SURROUNDED_ONES,
        positive_cells=2,
        positivity_percentage=40.0,
        result=AnalysisResult.POSITIVE,
    )


def test_surrounded_ones_ignores_one(algorithm: SurroundedOnesAlgorithm):

    result = algorithm.run([0, 1, 1, 0])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.SURROUNDED_ONES,
        positive_cells=0,
        positivity_percentage=0.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_surrounded_ones_ignores_first_and_last_cells(algorithm: SurroundedOnesAlgorithm):

    result = algorithm.run([1, 0, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.SURROUNDED_ONES,
        positive_cells=0,
        positivity_percentage=0.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_surrounded_ones_limit_threshold(algorithm: SurroundedOnesAlgorithm):

    result = algorithm.run([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.SURROUNDED_ONES,
        positive_cells=1,
        positivity_percentage=10.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_surrounded_ones_empty_cells(algorithm: SurroundedOnesAlgorithm):

    result = algorithm.run([])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.SURROUNDED_ONES,
        positive_cells=0,
        positivity_percentage=0.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_surrounded_ones_cells_short(algorithm: SurroundedOnesAlgorithm):

    result = algorithm.run([0, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.SURROUNDED_ONES,
        positive_cells=0,
        positivity_percentage=0.0,
        result=AnalysisResult.NEGATIVE,
    )
