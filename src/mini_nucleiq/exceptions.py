

class SamplesClientError(Exception):
    pass


class SampleNotFoundError(SamplesClientError):
    pass


class InvalidSampleResponseError(SamplesClientError):
    pass


class InvalidAlgorithmNameError(Exception):
    pass


class NoAlgorithmsSelectedError(Exception):
    pass