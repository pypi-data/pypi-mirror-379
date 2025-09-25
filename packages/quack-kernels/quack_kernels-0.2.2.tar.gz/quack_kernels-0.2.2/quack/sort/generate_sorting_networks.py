#!/usr/bin/env python3
"""
Generate optimized sorting network code from the optimal sorting network data.
Based on data from: https://bertdobbelaere.github.io/sorting_networks.html

This script generates CUTE DSL functions for optimal sorting networks of various sizes.
"""

import argparse
import os
import re
from typing import List, Tuple, Dict

# Network strings from bertdobbelaere.github.io/sorting_networks.html
# Copy-paste network strings here, then run initialize_networks() to parse them
NETWORK_STRINGS = {
    # Size 2: 1 CE, depth 1
    2: """
[(0,1)]
    """,
    # Size 4: 5 CEs, depth 3
    4: """
[(0,2),(1,3)]
[(0,1),(2,3)]
[(1,2)]
    """,
    # Size 8: 19 CEs, depth 6
    8: """
[(0,2),(1,3),(4,6),(5,7)]
[(0,4),(1,5),(2,6),(3,7)]
[(0,1),(2,3),(4,5),(6,7)]
[(2,4),(3,5)]
[(1,4),(3,6)]
[(1,2),(3,4),(5,6)]
    """,
    # Size 16: 60 CEs, depth 10
    16: """
[(0,13),(1,12),(2,15),(3,14),(4,8),(5,6),(7,11),(9,10)]
[(0,5),(1,7),(2,9),(3,4),(6,13),(8,14),(10,15),(11,12)]
[(0,1),(2,3),(4,5),(6,8),(7,9),(10,11),(12,13),(14,15)]
[(0,2),(1,3),(4,10),(5,11),(6,7),(8,9),(12,14),(13,15)]
[(1,2),(3,12),(4,6),(5,7),(8,10),(9,11),(13,14)]
[(1,4),(2,6),(5,8),(7,10),(9,13),(11,14)]
[(2,4),(3,6),(9,12),(11,13)]
[(3,5),(6,8),(7,9),(10,12)]
[(3,4),(5,6),(7,8),(9,10),(11,12)]
[(6,7),(8,9)]
    """,
    # Size 32: 185 CEs, depth 14
    32: """
[(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(12,13),(14,15),(16,17),(18,19),(20,21),(22,23),(24,25),(26,27),(28,29),(30,31)]
[(0,2),(1,3),(4,6),(5,7),(8,10),(9,11),(12,14),(13,15),(16,18),(17,19),(20,22),(21,23),(24,26),(25,27),(28,30),(29,31)]
[(0,4),(1,5),(2,6),(3,7),(8,12),(9,13),(10,14),(11,15),(16,20),(17,21),(18,22),(19,23),(24,28),(25,29),(26,30),(27,31)]
[(0,8),(1,9),(2,10),(3,11),(4,12),(5,13),(6,14),(7,15),(16,24),(17,25),(18,26),(19,27),(20,28),(21,29),(22,30),(23,31)]
[(0,16),(1,8),(2,4),(3,12),(5,10),(6,9),(7,14),(11,13),(15,31),(17,24),(18,20),(19,28),(21,26),(22,25),(23,30),(27,29)]
[(1,2),(3,5),(4,8),(6,22),(7,11),(9,25),(10,12),(13,14),(17,18),(19,21),(20,24),(23,27),(26,28),(29,30)]
[(1,17),(2,18),(3,19),(4,20),(5,10),(7,23),(8,24),(11,27),(12,28),(13,29),(14,30),(21,26)]
[(3,17),(4,16),(5,21),(6,18),(7,9),(8,20),(10,26),(11,23),(13,25),(14,28),(15,27),(22,24)]
[(1,4),(3,8),(5,16),(7,17),(9,21),(10,22),(11,19),(12,20),(14,24),(15,26),(23,28),(27,30)]
[(2,5),(7,8),(9,18),(11,17),(12,16),(13,22),(14,20),(15,19),(23,24),(26,29)]
[(2,4),(6,12),(9,16),(10,11),(13,17),(14,18),(15,22),(19,25),(20,21),(27,29)]
[(5,6),(8,12),(9,10),(11,13),(14,16),(15,17),(18,20),(19,23),(21,22),(25,26)]
[(3,5),(6,7),(8,9),(10,12),(11,14),(13,16),(15,18),(17,20),(19,21),(22,23),(24,25),(26,28)]
[(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26),(27,28)]
    """,
    # Size 64: 512 CEs, depth 21
    64: """
[(0,2),(1,3),(4,6),(5,7),(8,10),(9,11),(12,14),(13,15),(16,18),(17,19),(20,22),(21,23),(24,26),(25,27),(28,30),(29,31),(32,34),(33,35),(36,38),(37,39),(40,42),(41,43),(44,46),(45,47),(48,50),(49,51),(52,54),(53,55),(56,58),(57,59),(60,62),(61,63)]
[(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(12,13),(14,15),(16,17),(18,19),(20,21),(22,23),(24,25),(26,27),(28,29),(30,31),(32,33),(34,35),(36,37),(38,39),(40,41),(42,43),(44,45),(46,47),(48,49),(50,51),(52,53),(54,55),(56,57),(58,59),(60,61),(62,63)]
[(0,52),(1,2),(3,55),(4,48),(5,6),(7,51),(8,60),(9,10),(11,63),(12,56),(13,14),(15,59),(16,32),(17,18),(19,35),(20,24),(21,22),(23,27),(25,26),(28,44),(29,30),(31,47),(33,34),(36,40),(37,38),(39,43),(41,42),(45,46),(49,50),(53,54),(57,58),(61,62)]
[(0,20),(1,53),(2,54),(3,23),(4,28),(5,49),(6,50),(7,31),(8,36),(9,61),(10,62),(11,39),(12,16),(13,57),(14,58),(15,19),(17,33),(18,34),(21,25),(22,26),(24,52),(27,55),(29,45),(30,46),(32,56),(35,59),(37,41),(38,42),(40,60),(43,63),(44,48),(47,51)]
[(0,4),(1,21),(2,22),(3,7),(5,29),(6,30),(8,12),(9,37),(10,38),(11,15),(13,17),(14,18),(16,20),(19,23),(24,32),(25,53),(26,54),(27,35),(28,36),(31,39),(33,57),(34,58),(40,44),(41,61),(42,62),(43,47),(45,49),(46,50),(48,52),(51,55),(56,60),(59,63)]
[(0,8),(1,5),(2,6),(3,11),(4,12),(7,15),(9,13),(10,14),(16,40),(17,21),(18,22),(19,43),(20,44),(23,47),(24,28),(25,33),(26,34),(27,31),(29,37),(30,38),(32,36),(35,39),(41,45),(42,46),(48,56),(49,53),(50,54),(51,59),(52,60),(55,63),(57,61),(58,62)]
[(1,9),(2,10),(4,8),(5,13),(6,14),(7,11),(12,48),(15,51),(16,24),(17,41),(18,42),(19,27),(20,28),(21,45),(22,46),(23,31),(25,29),(26,30),(32,40),(33,37),(34,38),(35,43),(36,44),(39,47),(49,57),(50,58),(52,56),(53,61),(54,62),(55,59)]
[(4,16),(5,9),(6,10),(7,19),(8,24),(11,27),(13,49),(14,50),(17,25),(18,26),(20,32),(21,29),(22,30),(23,35),(28,40),(31,43),(33,41),(34,42),(36,52),(37,45),(38,46),(39,55),(44,56),(47,59),(53,57),(54,58)]
[(1,4),(5,17),(6,18),(8,16),(9,25),(10,26),(11,19),(12,24),(15,27),(21,33),(22,34),(29,41),(30,42),(36,48),(37,53),(38,54),(39,51),(44,52),(45,57),(46,58),(47,55),(59,62)]
[(2,8),(9,17),(10,18),(12,20),(13,25),(14,26),(15,23),(24,32),(27,35),(28,36),(31,39),(37,49),(38,50),(40,48),(43,51),(45,53),(46,54),(55,61)]
[(2,4),(12,16),(13,21),(14,22),(15,19),(20,24),(23,27),(25,33),(26,34),(28,32),(29,37),(30,38),(31,35),(36,40),(39,43),(41,49),(42,50),(44,48),(47,51),(59,61)]
[(4,16),(5,20),(10,40),(13,17),(14,18),(21,25),(22,26),(23,53),(24,28),(27,31),(29,33),(30,34),(32,36),(35,39),(37,41),(38,42),(43,58),(45,49),(46,50),(47,59)]
[(3,17),(6,36),(7,21),(8,32),(9,24),(11,41),(13,28),(14,44),(15,45),(18,48),(19,49),(22,52),(25,29),(26,30),(27,57),(31,55),(33,37),(34,38),(35,50),(39,54),(42,56),(46,60)]
[(6,20),(8,16),(10,24),(11,25),(14,28),(15,29),(17,33),(18,32),(21,37),(22,36),(26,42),(27,41),(30,46),(31,45),(34,48),(35,49),(38,52),(39,53),(43,57),(47,55)]
[(3,18),(5,8),(6,12),(7,22),(15,21),(17,32),(19,33),(23,37),(26,40),(30,44),(31,46),(41,56),(42,48),(45,60),(51,57),(55,58)]
[(3,16),(7,20),(11,26),(18,24),(19,25),(22,28),(23,29),(27,33),(30,36),(34,40),(35,41),(37,52),(38,44),(39,45),(43,56),(47,60)]
[(3,9),(7,13),(10,16),(11,17),(14,20),(15,30),(19,34),(21,36),(23,38),(25,40),(26,32),(27,42),(29,44),(31,37),(33,48),(43,49),(46,52),(47,53),(50,56),(54,60)]
[(3,8),(7,10),(9,12),(11,18),(13,14),(15,24),(17,22),(19,28),(21,26),(23,25),(27,34),(29,36),(30,32),(31,33),(35,44),(37,42),(38,40),(39,48),(41,46),(45,52),(49,50),(51,54),(53,56),(55,60)]
[(3,6),(7,12),(11,16),(15,17),(18,20),(19,24),(21,22),(23,30),(25,32),(26,28),(27,29),(31,38),(33,40),(34,36),(35,37),(39,44),(41,42),(43,45),(46,48),(47,52),(51,56),(57,60)]
[(3,5),(6,8),(7,9),(10,12),(11,13),(14,16),(15,18),(17,20),(19,21),(22,24),(23,26),(25,28),(27,30),(29,32),(31,34),(33,36),(35,38),(37,40),(39,41),(42,44),(43,46),(45,48),(47,49),(50,52),(51,53),(54,56),(55,57),(58,60)]
[(3,4),(7,8),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26),(27,28),(29,30),(31,32),(33,34),(35,36),(37,38),(39,40),(41,42),(43,44),(45,46),(47,48),(49,50),(51,52),(55,56),(59,60)]
    """,
}

# This will be populated by initialize_networks()
OPTIMAL_NETWORKS: Dict[int, Tuple[int, int, List[List[Tuple[int, int]]]]] = {}


def parse_network_string(network_str: str) -> List[List[Tuple[int, int]]]:
    """
    Parse a sorting network string from bertdobbelaere.github.io format.

    Examples:
    Input: "[(0,2),(1,3)], [(0,1),(2,3)], [(1,2)]"
    Output: [[(0, 2), (1, 3)], [(0, 1), (2, 3)], [(1, 2)]]

    Input: "[(0,1)], [(1,2)], [(0,1)]"
    Output: [[(0, 1)], [(1, 2)], [(0, 1)]]
    """
    # Remove whitespace and split by '], ['
    network_str = network_str.strip()
    if not network_str:
        return []

    # Split into layer strings
    layer_pattern = r"\[((?:\(\d+,\d+\)(?:,\(\d+,\d+\))*)?)\]"
    layers = []

    for match in re.finditer(layer_pattern, network_str):
        layer_str = match.group(1)
        if not layer_str.strip():
            layers.append([])
            continue

        # Parse comparisons in this layer: (i,j), (k,l), ...
        comparisons = []
        comp_pattern = r"\((\d+),(\d+)\)"

        for comp_match in re.finditer(comp_pattern, layer_str):
            i, j = int(comp_match.group(1)), int(comp_match.group(2))
            comparisons.append((i, j))

        layers.append(comparisons)

    return layers


def calculate_network_stats(layers: List[List[Tuple[int, int]]]) -> Tuple[int, int, int]:
    """Calculate depth, total comparisons, and max index from network layers."""
    depth = len(layers)
    total_comparisons = sum(len(layer) for layer in layers)

    # Find maximum index to determine network size
    max_index = 0
    for layer in layers:
        for i, j in layer:
            max_index = max(max_index, i, j)

    network_size = max_index + 1  # Since indices are 0-based
    return depth, total_comparisons, network_size


def add_network_from_string(size: int, network_str: str, description: str = ""):
    """
    Add a network from a string representation to the OPTIMAL_NETWORKS dictionary.

    Args:
        size: Size of the network (number of elements)
        network_str: Network string in bertdobbelaere.github.io format
        description: Optional description for debugging
    """
    try:
        layers = parse_network_string(network_str)
        depth, comparisons, detected_size = calculate_network_stats(layers)

        if detected_size != size:
            print(f"Warning: Network size mismatch! Expected {size}, detected {detected_size}")
            print(f"Network string: {network_str[:100]}...")
            return False

        OPTIMAL_NETWORKS[size] = (depth, comparisons, layers)

        if description:
            print(f"Added network for size {size}: {description}")
        print(f"  Depth: {depth}, Comparisons: {comparisons}")
        return True

    except Exception as e:
        print(f"Error parsing network for size {size}: {e}")
        print(f"Network string: {network_str[:100]}...")
        return False


def generate_networks_dict(
    networks_data: Dict[int, Tuple[int, int, List[List[Tuple[int, int]]]]]
) -> str:
    """Generate the global networks dictionary."""
    lines = ["networks = {"]

    for size, (depth, num_comparisons, layers) in sorted(networks_data.items()):
        # Format the network with proper indentation and newlines
        network_lines = []
        for i, layer in enumerate(layers):
            if i == 0:
                network_lines.append(f"            {layer}")
            else:
                network_lines.append(f",\n            {layer}")

        if len(layers) == 1:
            network_str = f"[{network_lines[0].strip()}]"
        else:
            network_str = "[\n" + "".join(network_lines) + "\n        ]"

        lines.append(f"    # Size {size}: {num_comparisons} CEs, depth {depth}")
        lines.append(f"    {size}: {network_str},")
        lines.append("")

    lines.append("}")
    return "\n".join(lines)


def generate_optimal_sort_function() -> str:
    """Generate the single optimal_sort function that looks up networks by size."""
    return """@cute.jit
def optimal_sort(
    arr: cute.Tensor,
    n: cutlass.Constexpr[int],
    start: cutlass.Constexpr[int] = 0,
    ascending: cutlass.Constexpr[bool] = True
) -> None:
    \"\"\"
    Optimal sorting network dispatcher.

    Args:
        arr: Array to sort
        n: Size of array (must be power of 2 and available in networks)
        start: Starting index (default 0)
        ascending: Sort in ascending order (default True)

    Source: https://bertdobbelaere.github.io/sorting_networks.html
    \"\"\"
    assert n in networks
    for level in networks[n]:
        for i, j in level:
            compare_and_swap(arr, start + i, start + j, ascending)
"""


def generate_sorting_networks_file(max_size: int = 64):
    """Generate a complete sorting networks file with optimal networks up to max_size."""

    output_file = os.path.join(os.path.dirname(__file__), "sorting_networks.py")

    # Header
    header = '''# Copyright (c) 2025, Wentao Guo, Mayank Mishra, Tri Dao.
"""
Optimal sorting networks generated from: https://bertdobbelaere.github.io/sorting_networks.html

This file was auto-generated by quack/sort/generate_sorting_networks.py. Do not edit it directly.
"""

# fmt: off
# ruff: noqa
# isort: skip_file

import cutlass
import cutlass.cute as cute

from quack.sort.utils import compare_and_swap


'''

    # Generate networks dictionary and optimal_sort function
    sizes = [n for n in range(2, max_size + 1) if n in OPTIMAL_NETWORKS]
    networks_dict = generate_networks_dict(OPTIMAL_NETWORKS)
    optimal_sort_func = generate_optimal_sort_function()

    # Combine everything
    content = header + networks_dict + "\n\n\n" + optimal_sort_func

    with open(output_file, "w") as f:
        f.write(content)

    print(f"Generated optimal sorting networks for sizes {sizes}")
    print(f"Output written to: {output_file}")
    return sizes


def initialize_networks():
    """Initialize the OPTIMAL_NETWORKS dictionary by parsing NETWORK_STRINGS."""
    global OPTIMAL_NETWORKS
    OPTIMAL_NETWORKS.clear()

    for size, network_str in NETWORK_STRINGS.items():
        success = add_network_from_string(size, network_str, f"Size {size} optimal network")
        if not success:
            print(f"Warning: Failed to parse network for size {size}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate optimal sorting network code from bertdobbelaere.github.io data"
    )
    parser.add_argument(
        "--max-size",
        "-m",
        type=int,
        default=64,
        help="Maximum sorting network size to generate (default: 32)",
    )
    parser.add_argument(
        "--stats", "-s", action="store_true", help="Print statistics about the optimal networks"
    )

    args = parser.parse_args()

    # Initialize networks from strings
    initialize_networks()

    if args.stats:
        print("Optimal Sorting Network Statistics:")
        print("Size\tDepth\tComparisons\tLayers")
        print("-" * 35)
        for n in sorted(OPTIMAL_NETWORKS.keys()):
            if n <= args.max_size:
                depth, comparisons, layers = OPTIMAL_NETWORKS[n]
                print(f"{n}\t{depth}\t{comparisons}\t\t{len(layers)}")

    # Generate the sorting networks file
    sizes = generate_sorting_networks_file(args.max_size)

    print(f"\nGenerated optimal sorting networks for {len(sizes)} sizes")
    print(f"Total networks: {len(sizes)}")
    print(f"Max network size: {max(sizes)}")


if __name__ == "__main__":
    main()
