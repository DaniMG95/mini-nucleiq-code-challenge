from mini_nucleiq.algorithms.algorithm_factory import AlgorithmFactory
from mini_nucleiq.exceptions import NoAlgorithmsSelectedError
from mini_nucleiq.models import AlgorithmAnalysis, AlgorithmName, AnalysisResult, SampleAnalysis
from mini_nucleiq.samples_client import SamplesClient


class Analysis:

    def __init__(self, samples_client: SamplesClient, algorithm_factory: AlgorithmFactory):
        self.samples_client = samples_client
        self.algorithm_factory = algorithm_factory

    def analyze_sample(self, sample_name: str, algorithm_names: list[AlgorithmName]) -> SampleAnalysis:
        sample_data = self.samples_client.get_sample(sample_name)
        if not algorithm_names:
            raise NoAlgorithmsSelectedError("No algorithms selected for analysis.")

        analysis_results: list[AlgorithmAnalysis] = []
        for algorithm_name in algorithm_names:
            algorithm = self.algorithm_factory.create_algorithm(algorithm_name)
            result = algorithm.run(sample_data.cells)
            analysis_results.append(result)

        count_positive = sum(1 for result in analysis_results if result.result == AnalysisResult.POSITIVE)
        final_result = AnalysisResult.POSITIVE if count_positive > len(analysis_results) / 2\
                else AnalysisResult.NEGATIVE

        return SampleAnalysis(sample_name=sample_data.name, algorithms=analysis_results, final_result=final_result)