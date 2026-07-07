# CellsIA's Code Challenge

Small Python solution for the CellsIA mini-nucleiq code challenge.

## Requirements

To launch this project, the following are required:

- Python 3.14
- uv

## Installation

Install dependencies:

```bash
uv sync
```

## Run the CLI

Analyze a sample with one or more algorithms, at least one algorithm must be selected.

```bash
uv run mini-nucleiq -n sample-c -a even-zeroes contiguous-ones surrounded-ones
```

Available samples:

```text
sample-a
sample-b
sample-c
sample-d
sample-e
```

Available algorithms:

```text
even-zeroes
contiguous-ones
surrounded-ones
```

Example output:

```text
Sample: sample-c
even-zeroes: positive_cells=3, positivity=30.0%, result=negative
contiguous-ones: positive_cells=3, positivity=30.0%, result=positive
surrounded-ones: positive_cells=2, positivity=20.0%, result=positive
Final result: positive
```

## Run tests

```bash
uv run pytest
```

