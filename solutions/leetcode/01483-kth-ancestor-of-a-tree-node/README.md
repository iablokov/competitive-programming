# 1483. [Hard] Kth Ancestor of a Tree Node

In this problemm k-th ancestor of a tree node can be found in a series of steps (jumps), each one being of a size of some power of 2.
The sequence of jumps is determined by the binary (i.e., into powers of 2) decomposition of `k`, e.g., `14=8+4+2`.
For fast querying of the tree, we should precompute for each node a collection of ancestors with distances equal to powers of 2.

For Rust, run `rustc --test rust.rs`.