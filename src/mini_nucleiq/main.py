import argparse

import httpx

from mini_nucleiq.algorithms.algorithm_factory import AlgorithmFactory
from mini_nucleiq.analysis import Analysis
from mini_nucleiq.models import AlgorithmName
from mini_nucleiq.samples_client import SamplesClient

SAMPLES_BASE_URL = (
    "https://raw.githubusercontent.com/cellsia/mini-nucleiq-code-challenge/main/samples"
)

def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--sample-name", required=True)
    parser.add_argument(
        "-a",
        "--algorithms",
        nargs="+",
        choices=[algorithm.value for algorithm in AlgorithmName],
    )
    return parser.parse_args(args)



def main(args: list[str] | None = None) -> None:
    parsed_args = parse_args(args)
    algorithm_names = []
    if parsed_args.algorithms:
        algorithm_names = [AlgorithmName(raw_algorithm_name) for raw_algorithm_name in parsed_args.algorithms]

    with httpx.Client() as http_client:
        samples_client = SamplesClient(base_url=SAMPLES_BASE_URL, client=http_client)
        analysis = Analysis(samples_client=samples_client, algorithm_factory=AlgorithmFactory())
        analysis_result = analysis.analyze_sample(parsed_args.sample_name, algorithm_names)

    print(f"Sample: {analysis_result.sample_name}")

    for algorithm_result in analysis_result.algorithms:
        print(
            f"{algorithm_result.name.value}: "
            f"positive_cells={algorithm_result.positive_cells}, "
            f"positivity={algorithm_result.positivity_percentage}%, "
            f"result={algorithm_result.result.value}",
        )

    print(f"Final result: {analysis_result.final_result.value}")


if __name__ == "__main__":
    main()