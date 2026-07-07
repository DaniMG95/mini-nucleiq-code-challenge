import pytest

from mini_nucleiq.models import Sample


def test_sample_from_raw():
    raw: object = {"name": "sample-c", "cells": [0, 0, 1, 0, 1]}

    sample = Sample.from_raw(raw)

    assert sample == Sample(name="sample-c", cells=[0, 0, 1, 0, 1])


def test_sample_from_raw_error_not_dict():
    raw = [1, 2, 3]

    with pytest.raises(ValueError, match="Sample response must be an dict."):
        Sample.from_raw(raw)


def test_sample_from_raw_error_missing_name():
    raw = {"cells": [0, 1]}

    with pytest.raises(ValueError, match="Sample name must be a string."):
        Sample.from_raw(raw)


def test_sample_from_raw_error_name():
    raw: object = {"name": 123, "cells": [0, 1]}

    with pytest.raises(ValueError, match="Sample name must be a string."):
        Sample.from_raw(raw)


def test_sample_from_raw_error_missing_cells():
    raw: object = {"name": "sample-c"}

    with pytest.raises(ValueError, match="Sample cells must be a list."):
        Sample.from_raw(raw)


def test_sample_from_raw_error_cells():
    raw: object = {"name": "sample-c", "cells": "0101"}

    with pytest.raises(ValueError, match="Sample cells must be a list."):
        Sample.from_raw(raw)


def test_sample_from_raw_error_cells_with_invalid_values():
    raw: object = {"name": "sample-c", "cells": [0, 1, 2]}

    with pytest.raises(ValueError, match="Sample cells must contain only 0 and 1."):
        Sample.from_raw(raw)


def test_sample_from_raw_error_boolean_cells():
    raw: object = {"name": "sample-c", "cells": [0, True, 1]}

    with pytest.raises(ValueError, match="Sample cells must contain only 0 and 1."):
        Sample.from_raw(raw)

def test_sample_from_raw_error_string_cells():
    raw: object = {"name": "sample-c", "cells": [0, "test", 1]}

    with pytest.raises(ValueError, match="Sample cells must contain only 0 and 1."):
        Sample.from_raw(raw)
