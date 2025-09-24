"""Example script demonstrating programmatic use of TAU clustering."""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

import networkx as nx
import numpy as np

# Add parent directory to path to import tau_clustering
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tau_clustering import TauClustering, TauConfig

DEFAULT_POPULATION_SIZE = 40
DEFAULT_MAX_GENERATIONS = 150
DEFAULT_OUTPUT_PATH = Path("best_partition.npy")
DEFAULT_GRAPH_PATH = Path(__file__).resolve().with_name("example.graph")
GraphInput = str | Path | nx.Graph


def run_clustering(
    graph: GraphInput,
    *,
    population_size: int = DEFAULT_POPULATION_SIZE,
    max_generations: int = DEFAULT_MAX_GENERATIONS,
    save_membership_to: Path | None = None,
) -> tuple[np.ndarray, float]:
    """Run TAU clustering and optionally persist the membership vector.

    Parameters
    ----------
    graph: Path | str | nx.Graph
        Either a path to an adjacency-list file or an in-memory NetworkX graph.
    population_size: int
        Population size for the evolutionary search.
    max_generations: int
        Maximum number of generations to run.
    save_membership_to: Path | None
        Optional path for saving the membership vector as a NumPy file.

    Returns
    -------
    tuple[np.ndarray, float]
        The best membership assignment and its modularity score.
    """
    if not isinstance(graph, (str, Path, nx.Graph)):
        raise TypeError(
            "graph must be a path-like object or a networkx.Graph instance."
        )

    config = TauConfig(population_size=population_size, max_generations=max_generations)
    clustering = TauClustering(graph, config)
    result = clustering.run()

    if save_membership_to is not None:
        output_path = Path(save_membership_to)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(output_path, result.membership)

    return result.membership, float(result.modularity)

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Run TAU clustering on a graph adjacency list."
    )
    parser.add_argument(
        "--graph",
        nargs="?",
        type=str,
        default="./examples/example.graph",
        help="Path to an adjacency-list file (default: ./examples/example.graph).",
    )
  
    args = parser.parse_args()
    GRAPH_PATH = args.graph
    POPULATION_SIZE = 60
    MAX_GENERATIONS = 500
    N_WORKERS = os.cpu_count()
    TARGET_PATH = './examples/best_partition.npy'

    print("Starting TAU clustering...")
    print(
        f"Parameters: pop_size={POPULATION_SIZE}, "
        f"workers={N_WORKERS}, max_generations={MAX_GENERATIONS}"
    )

    start_time = time.perf_counter()
    membership, modularity = run_clustering(
        GRAPH_PATH,
        population_size=POPULATION_SIZE,
        max_generations=MAX_GENERATIONS,
        save_membership_to=TARGET_PATH,
    )
    elapsed = time.perf_counter() - start_time

    print(f"Modularity: {modularity:.5f}")
    print(f"Execution time: {elapsed:.2f} seconds")
    print(f"Membership length: {len(membership)}")
    print("Membership vector:")
    print(membership)


if __name__ == "__main__":
    main()
