from collections.abc import Callable

import pytest
from httpx import Client, MockTransport, Request, Response

from mini_nucleiq.exceptions import InvalidSampleResponseError, SampleNotFoundError, SamplesClientError
from mini_nucleiq.samples_client import SamplesClient


def create_mock_handler(response: Response) -> Callable[[Request], Response]:
    def handler(_request: Request) -> Response:
        return response
    return handler

def create_client_with_mock_handler(response: Response) -> SamplesClient:
    handler = create_mock_handler(response)
    http_client = Client(transport=MockTransport(handler))
    return SamplesClient(base_url="https://example.com/samples", client=http_client)


def test_get_sample():
    requested_urls: list[str] = []

    def handler(request: Request) -> Response:
        requested_urls.append(str(request.url))
        return Response(200, json={"name": "sample-c", "cells": [0, 1, 0, 1, 0, 1, 0]})

    http_client = Client(transport=MockTransport(handler))
    samples_client = SamplesClient(base_url="https://example.com/samples", client=http_client)

    samples_client.get_sample("sample-c")

    assert requested_urls == ["https://example.com/samples/sample-c.json"]


def test_get_sample_raises_not_found_error():
    samples_client = create_client_with_mock_handler(Response(404))
    
    with pytest.raises(SampleNotFoundError, match="Sample 'sample-c' not found."):
        samples_client.get_sample("sample-c")


def test_get_sample_raises_error_for_status_code():
    samples_client = create_client_with_mock_handler(Response(500))

    with pytest.raises(SamplesClientError, match="Unexpected status code: 500"):
        samples_client.get_sample("sample-c")


def test_get_sample_raises_error_for_invalid_json():
    samples_client = create_client_with_mock_handler(Response(200, content=b"not-json"))

    with pytest.raises(InvalidSampleResponseError, match="Invalid JSON response from the server."):
        samples_client.get_sample("sample-c")


def test_get_sample_raises_error_for_invalid_sample_data():
    samples_client = create_client_with_mock_handler(Response(200,
                                                              json={"name": "sample-c", "cells": [0, 2, 1]}))

    with pytest.raises(InvalidSampleResponseError, match="Invalid JSON response from the server."):
        samples_client.get_sample("sample-c")
