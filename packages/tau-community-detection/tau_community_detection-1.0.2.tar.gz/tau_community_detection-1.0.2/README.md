# TAU Community Detection

[![PyPI](https://img.shields.io/pypi/v/tau-community-detection.svg)](https://pypi.org/project/tau-community-detection/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

`tau-community-detection` implements TAU, an evolutionary community detection algorithm
that couples genetic search with Leiden refinements. It is designed for scalable graph
clustering with configurable hyper-parameters and multiprocessing support.

---

## Highlights

- **Evolutionary search**: Maintains a population of candidate partitions and applies
  crossover/mutation tailored for graph clustering.
- **Leiden optimisation**: Refines every candidate with Leiden to ensure modularity gains.
- **Multiprocessing aware**: Utilises worker pools for population optimisation.
- **Deterministic options**: Accepts a user-specified random seed for reproducibility.
- **Simple API**: Access everything through the `TauClustering` class.

---

## Installation

The project targets Python 3.10 or newer (required for slot-based dataclasses).

```bash
pip install tau-community-detection
```

To work from a clone, install the package in editable mode inside a virtual environment:

```bash
git clone https://github.com/HillelCharbit/community_TAU.git
cd community_TAU
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

---

## Quick Start (Python API)

```python
from tau_community_detection import TauClustering

clustering = TauClustering(
    graph_source="path/to/graph.adjlist",
    population_size=80,
    max_generation=250,
)
membership, modularity_history = clustering.run()

print("community for node 0:", membership[0])
print("best modularity:", modularity_history[-1])
```

### Graph input

`TauClustering` accepts either an igraph/NetworkX graph object or the path to an adjacency
list that NetworkX can parse (see `nx.read_adjlist`). Nodes are internally remapped to
contiguous integers to maximise igraph performance.

---

## Example Script

The repository ships with a runnable example that uses the bundled
`src/tau_community_detection/examples/example.graph` file. To execute it from the project
root:

```bash
python3 src/tau_community_detection/run_clustering.py
```

The script prints the detected membership vector and the modularity score history.

> Note: multiprocessing may be restricted inside some sandboxed environments. Run the
> example on a local machine for best results.

---

## Configuration

All algorithm hyper-parameters live on the `TauConfig` dataclass. You can pass a custom
configuration instance to `TauClustering` or adjust attributes on the default one. Key
fields include:

- `population_size`: number of partitions maintained per generation.
- `max_generations`: upper bound on evolutionary iterations.
- `elite_fraction` / `immigrant_fraction`: govern selection pressure.
- `stopping_generations` / `stopping_jaccard`: convergence checks based on membership
  stability.
- `random_seed`: makes runs reproducible across processes.

See `src/tau_community_detection/config.py` for the complete list.

---

## Development Workflow

- Format imports and style according to your preferred tooling (no formatter is enforced).
- Validate new changes by executing the example script or custom experiments.
- When contributing, ensure dependency pins remain compatible with Python 3.10+.

Pull requests are welcome—please include context on parameter changes or performance
observations when proposing algorithmic tweaks.

---

## License

Released under the [MIT License](https://opensource.org/licenses/MIT). See `LICENSE` for
details.

