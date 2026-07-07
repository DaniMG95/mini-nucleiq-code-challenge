from typing import cast

import pytest

from mini_nucleiq.algorithms.algorithm_factory import AlgorithmFactory
from mini_nucleiq.algorithms.contiguous_ones import ContiguousOnesAlgorithm
from mini_nucleiq.algorithms.even_zeroes import EvenZeroesAlgorithm
from mini_nucleiq.algorithms.surrounded_ones import SurroundedOnesAlgorithm
from mini_nucleiq.exceptions import InvalidAlgorithmNameError
from mini_nucleiq.models import AlgorithmName


def test_create_algorithm_even_zeroes():
    algorithm = AlgorithmFactory.create_algorithm(AlgorithmName.EVEN_ZEROES)

    assert isinstance(algorithm, EvenZeroesAlgorithm)


def test_create_algorithm_contiguous_ones():
    algorithm = AlgorithmFactory.create_algorithm(AlgorithmName.CONTIGUOUS_ONES)

    assert isinstance(algorithm, ContiguousOnesAlgorithm)


def test_create_algorithm_surrounded_ones():
    algorithm = AlgorithmFactory.create_algorithm(AlgorithmName.SURROUNDED_ONES)

    assert isinstance(algorithm, SurroundedOnesAlgorithm)


def test_create_algorithm_unknown_name():
    invalid_algorithm_name = cast(AlgorithmName, "unknown")

    with pytest.raises(InvalidAlgorithmNameError, match="Unknown algorithm name: unknown"):
        AlgorithmFactory.create_algorithm(invalid_algorithm_name)
