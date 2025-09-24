"""
Free Fermion Library - A Python package for quantum free fermion systems

This package provides comprehensive tools for working with free fermion
quantum systems, including combinatorial functions, graph theory algorithms,
and quantum physics utilities.

Modules:
    ff_lib: Core quantum physics and linear algebra functions
    ff_combinatorics: Combinatorial matrix functions (pfaffian, hafnian, etc.)
    ff_graph_theory: Graph algorithms and visualization for planar graphs
    ff_utils: Common utility functions

Copyright 2025 James.D.Whitfield@dartmouth.edu
Licensed under MIT License.
"""

__version__ = "1.0.0"
__author__ = "James D. Whitfield"
__email__ = "James.D.Whitfield@dartmouth.edu"

# Combinatorial functions from ff_combinatorics
from .ff_combinatorics import sgn, pf, hf, pt, dt, dt_eigen

# Graph theory functions from ff_graph_theory
from .ff_graph_theory import (
    plot_graph_with_edge_weights,
    generate_random_planar_graph,
    plot_planar_embedding,
    dual_graph_H,
    faces,
    complete_face,
    pfo_algorithm,
    compute_tree_depth,
    count_perfect_matchings,
    find_perfect_matchings_brute,
    count_perfect_matchings_planar,
)

# Core quantum physics functions from ff_lib
from .ff_lib import (
    permutation_to_matrix,
    pauli_matrices,
    jordan_wigner_lowering,
    jordan_wigner_alphas,
    jordan_wigner_majoranas,
    rotate_operators,
    build_V,
    build_H,
    build_Omega,
    build_reordering_xx_to_xp,
    build_K,
    random_FF_rotation,
    random_FF_state,
    kitaev_chain,
    is_symp,
    check_canonical_form,
    generate_gaussian_state,
    build_op,
    random_H_generator,
    correlation_matrix,
    compute_cov_matrix,
    compute_2corr_matrix,
    compute_algebra_S,
    is_matchgate,
    eigh_sp,
    eigv_sp,
    eigm_sp_can,
    eigm_sp,
)

# Utility functions from ff_utils
from .ff_utils import (
    print_custom,
    clean,
    formatted_output,
    generate_random_bitstring,
    kron_plus,
)

# Define what gets imported with "from ff import *"
__all__ = [
    # Core quantum physics functions from ff_lib
    "permutation_to_matrix",
    "pauli_matrices",
    "jordan_wigner_lowering",
    "jordan_wigner_alphas",
    "jordan_wigner_majoranas",
    "rotate_operators",
    "build_V",
    "build_H",
    "build_Omega",
    "build_reordering_xx_to_xp",
    "build_K",
    "kitaev_chain",
    "random_FF_rotation",
    "random_FF_state",
    "random_H_generator",
    "correlation_matrix",
    "is_symp",
    "check_canonical_form",
    "generate_gaussian_state",
    "build_op",
    "compute_cov_matrix",
    "compute_2corr_matrix",
    "compute_algebra_S",
    "is_matchgate",
    "eigh_sp",
    "eigv_sp",
    "eigm_sp_can",
    "eigm_sp",
    # Combinatorial functions from ff_combinatorics
    "sgn",
    "pf",
    "hf",
    "pt",
    "dt",
    "dt_eigen",
    # Graph theory functions from ff_graph_theory
    "plot_graph_with_edge_weights",
    "generate_random_planar_graph",
    "plot_planar_embedding",
    "dual_graph_H",
    "faces",
    "complete_face",
    "count_perfect_matchings",
    "find_perfect_matchings_brute",
    "count_perfect_matchings_planar",
    "pfo_algorithm",
    "compute_tree_depth",
    # Utility functions from ff_utils
    "print_custom",
    "clean",
    "formatted_output",
    "generate_random_bitstring",
    "kron_plus",
]
