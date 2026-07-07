

class SamplesClientError(Exception):
    pass


class SampleNotFoundError(SamplesClientError):
    pass


class InvalidSampleResponseError(SamplesClientError):
    pass