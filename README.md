# AI Homework: N-Queens Solver

## Description
This repository contains the solution for the Artificial Intelligence Homework (A.Y. 2025/2026).
The project implements a solver for the N-Queens Problem comparing two different AI techniques:

1. A* Search (Task 1)
2. CSP (Constraint Satisfaction Problem) (Task 2)

## Project Structure
The project is organized as follows:

- src/: Contains the source code modules.
    + problem.py: Abstract base class defining the problem interface.
    + nqueens.py: Models the N-Queens environment and rules.
    + search.py: Implementation of the A* Search algorithm.
    + csp_solver.py: Implementation of the CSP solver logic.
- main.py: Main entry point to run a single instance of the problem (defaults to N=8).
- experiments.py: Script to run benchmarks on increasing sizes of N (Task 3).
- requirements.txt: List of Python dependencies required to run the project.

## Requirements

- Python 3.x (Tested on 3.13.13)
- python-constraint library

## Installation

Before running the code, make sure to install the required dependencies:

pip install -r requirements.txt

## How to Run

### Run Single Instance (Task 1 & 2)
To solve the N-Queens problem for a fixed size (default N=8) using both A* and CSP methods, run:

python main.py

### Run Experiments (Task 3)
To run the benchmark suite on increasing sizes of N and generate the results CSV file (nqueens_experiments.csv), run:

python experiments.py

## Plot
To generate the plots used in the report, run: python plot_results.py


## Author
Flavio Visaggio - M: 2260384
