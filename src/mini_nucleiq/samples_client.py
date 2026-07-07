from httpx import Client

from mini_nucleiq.exceptions import InvalidSampleResponseError, SampleNotFoundError, SamplesClientError
from mini_nucleiq.models import Sample


class SamplesClient:

    def __init__(self, base_url: str, client: Client):
        self.base_url = base_url
        self.client = client

    def get_sample(self, sample_name: str) -> Sample:
        response = self.client.get(f"{self.base_url}/{sample_name}.json")
        if response.status_code == 404:
            raise SampleNotFoundError(f"Sample '{sample_name}' not found.")
        elif response.status_code != 200:
            raise SamplesClientError(f"Unexpected status code: {response.status_code}")
        try:
            sample: Sample = Sample.from_raw(raw=response.json())
        except (ValueError, TypeError) as err:
            raise InvalidSampleResponseError("Invalid JSON response from the server.") from err
        return sample
    