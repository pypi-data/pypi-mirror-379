# TAU: Parallel Genetic Clustering with Louvain and Leiden

[![PyPI](https://img.shields.io/pypi/v/community_TAU.svg)](https://pypi.org/project/community_TAU/)
[![Build](https://github.com/HillelCharbit/community_TAU/actions/workflows/build.yml/badge.svg)](https://github.com/myusername/community_TAU/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

**TAU** is a high-performance Python package for modularity-based community detection using a hybrid of genetic algorithms and graph clustering methods (Louvain and Leiden). It is built for scalability, parallelism, and usability across research and applied machine learning settings.

---

## Features

- **Genetic Initialization**: Enhances clustering quality by optimizing initial conditions with evolutionary search.
- **Pluggable Clustering Engines**: Supports Louvain and Leiden algorithms.
- **Parallel Execution**: Uses Python's multiprocessing/threading for speed-up across CPUs.
- **Flexible Graph Input**: Read from adjacency lists, edge lists, CSVs, or pandas DataFrames.
- **CLI and API Access**: Run from the terminal or call programmatically in Python.
- **Reproducible Runs**: Optional random seed parameter for repeatable experiments.

---

## Installation

### From PyPI

```bash
pip install community_TAU
```

### From Source

```bash
git clone https://github.com/HillelCharbit/community_TAU.git
cd community_TAU
pip install .
```

---

## Quick Start

### Command-Line Interface

```bash
python -m community_TAU --graph data/example.graph --size 80 --workers 4 --max_generations 300
```

### Command-Line Arguments

| Argument           | Description                                           | Default             |
|--------------------|-------------------------------------------------------|---------------------|
| `--graph`          | Path to graph file (adjacency list, edge list, etc.) | **Required**        |
| `--size`           | Population size for genetic algorithm                | 60                  |
| `--workers`        | Number of parallel workers                           | All available cores |
| `--max_generations`| Maximum number of generations                        | 500                 |
| `--seed`           | Random seed (optional)                               | None                |

---

## Python API Example

```python
from community_TAU import community_TAU
import networkx as nx

G = nx.read_edgelist("example.graph")
result = community_TAU(G, size=100, workers=8, max_generations=400)

# Access results
print(result.partition)
print(result.modularity)
```

---

## Input Formats Supported

- Adjacency list (`.graph`)
- Edge list (`.csv`, `.txt`)
- Adjacency matrix (CSV or DataFrame)

Conversion tools are available in the `graph_loader` module.

---

## Output

- Final partition (dictionary of node → community)
- Final modularity score
- Optional generation logs and fitness history

---

## Testing

To run unit tests:

```bash
pytest tests/
```

Test coverage includes input parsing, genetic algorithm logic, clustering evaluation, and parallel execution.

---

## Contributing

We welcome contributions! To get started:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

Please review the [contributing guidelines](CONTRIBUTING.md) before submitting changes.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Acknowledgments

- Louvain and Leiden algorithms based on work by Blondel et al. and Traag et al.
- Graph handling inspired by NetworkX and igraph interfaces.

---

## Project Status

TAU is actively maintained and under continuous development. Feedback and issues are welcome on the [GitHub issue tracker](https://github.com/HillelCharbit/tau/issues).
