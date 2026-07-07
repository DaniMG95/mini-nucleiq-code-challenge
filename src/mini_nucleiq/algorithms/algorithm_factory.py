from mini_nucleiq.algorithms.algorithm_base import AlgorithmBase
from mini_nucleiq.algorithms.contiguous_ones import ContiguousOnesAlgorithm
from mini_nucleiq.algorithms.even_zeroes import EvenZeroesAlgorithm
from mini_nucleiq.algorithms.surrounded_ones import SurroundedOnesAlgorithm
from mini_nucleiq.exceptions import InvalidAlgorithmNameError
from mini_nucleiq.models import AlgorithmName


class AlgorithmFactory:
    ALGORITHMS = {
        AlgorithmName.SURROUNDED_ONES: SurroundedOnesAlgorithm,
        AlgorithmName.CONTIGUOUS_ONES: ContiguousOnesAlgorithm,
        AlgorithmName.EVEN_ZEROES: EvenZeroesAlgorithm,
    }

    @classmethod
    def create_algorithm(cls, algorithm_name: AlgorithmName) -> AlgorithmBase:
        if algorithm_name not in AlgorithmFactory.ALGORITHMS:
            raise InvalidAlgorithmNameError(f"Unknown algorithm name: {algorithm_name}")
        algorithm_class: type[AlgorithmBase] = cls.ALGORITHMS[algorithm_name]
        return algorithm_class()