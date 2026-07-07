from pytest import fixture

from mini_nucleiq.algorithms.even_zeroes import EvenZeroesAlgorithm
from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName, AnalysisResult


@fixture()
def algorithm() -> EvenZeroesAlgorithm:
    return EvenZeroesAlgorithm()



def test_even_zeroes_limit_threshold(algorithm: EvenZeroesAlgorithm):

    result = algorithm.run([0, 0, 1, 0, 0, 1, 0, 1, 1, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.EVEN_ZEROES,
        positive_cells=3,
        positivity_percentage=30.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_even_zeroes_positive(algorithm: EvenZeroesAlgorithm):

    result = algorithm.run([0, 1, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.EVEN_ZEROES,
        positive_cells=1,
        positivity_percentage=33.33333333333333,
        result=AnalysisResult.POSITIVE,
    )


def test_even_zeroes_negative(algorithm: EvenZeroesAlgorithm):

    result = algorithm.run([0, 1, 0, 1, 0, 1, 1, 1, 1, 1])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.EVEN_ZEROES,
        positive_cells=3,
        positivity_percentage=30.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_even_zeroes_zeroes_odd(algorithm: EvenZeroesAlgorithm):

    result = algorithm.run([1, 0, 1, 0])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.EVEN_ZEROES,
        positive_cells=0,
        positivity_percentage=0.0,
        result=AnalysisResult.NEGATIVE,
    )


def test_even_zeroes_empty_cells(algorithm: EvenZeroesAlgorithm):

    result = algorithm.run([])

    assert result == AlgorithmAnalysis(
        name=AlgorithmName.EVEN_ZEROES,
        positive_cells=0,
        positivity_percentage=0.0,
        result=AnalysisResult.NEGATIVE,
    )
