import pytest

from mini_nucleiq.algorithms.algorithm_factory import AlgorithmFactory
from mini_nucleiq.analysis import Analysis
from mini_nucleiq.exceptions import NoAlgorithmsSelectedError
from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName, AnalysisResult, Sample, SampleAnalysis
from mini_nucleiq.samples_client import SamplesClient


class FakeSamplesClient(SamplesClient):
    def __init__(self, sample: Sample, **_):
        self.sample = sample

    def get_sample(self, sample_name: str) -> Sample:
        return self.sample



def test_analyze_sample():
    samples_client = FakeSamplesClient(
        Sample(name="sample-test", cells=[0, 0, 1, 0, 0, 1, 0, 1, 1, 1]),
    )
    analysis = Analysis(samples_client=samples_client, algorithm_factory=AlgorithmFactory())

    result = analysis.analyze_sample(
        sample_name="sample-test",
        algorithm_names=[
            AlgorithmName.EVEN_ZEROES,
            AlgorithmName.CONTIGUOUS_ONES,
            AlgorithmName.SURROUNDED_ONES,
        ],
    )

    assert result == SampleAnalysis(
        sample_name="sample-test",
        algorithms=[
            AlgorithmAnalysis(
                name=AlgorithmName.EVEN_ZEROES,
                positive_cells=3,
                positivity_percentage=30.0,
                result=AnalysisResult.NEGATIVE,
            ),
            AlgorithmAnalysis(
                name=AlgorithmName.CONTIGUOUS_ONES,
                positive_cells=3,
                positivity_percentage=30.0,
                result=AnalysisResult.POSITIVE,
            ),
            AlgorithmAnalysis(
                name=AlgorithmName.SURROUNDED_ONES,
                positive_cells=2,
                positivity_percentage=20.0,
                result=AnalysisResult.POSITIVE,
            ),
        ],
        final_result=AnalysisResult.POSITIVE,
    )


def test_analyze_sample_different_sample_name():
    samples_client = FakeSamplesClient(Sample(name="sample-from-api", cells=[0, 1, 0]))
    analysis = Analysis(samples_client=samples_client, algorithm_factory=AlgorithmFactory())

    result = analysis.analyze_sample("requested-sample", [AlgorithmName.SURROUNDED_ONES])

    assert result.sample_name == "sample-from-api"


def test_analyze_sample_negative():
    samples_client = FakeSamplesClient(
        Sample(name="sample-c", cells=[0, 0, 1, 0, 0, 1, 0, 1, 1, 1]),
    )
    analysis = Analysis(samples_client=samples_client, algorithm_factory=AlgorithmFactory())

    result = analysis.analyze_sample(
        sample_name="sample-c",
        algorithm_names=[AlgorithmName.EVEN_ZEROES, AlgorithmName.CONTIGUOUS_ONES],
    )

    assert result.final_result == AnalysisResult.NEGATIVE


def test_analyze_sample_error_no_algorithms():
    samples_client = FakeSamplesClient(Sample(name="sample-c", cells=[0, 1, 0]))
    analysis = Analysis(samples_client=samples_client, algorithm_factory=AlgorithmFactory())

    with pytest.raises(NoAlgorithmsSelectedError, match="No algorithms selected for analysis."):
        analysis.analyze_sample("sample-c", [])
