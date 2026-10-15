# recurrence-solver
# Recurrence Tree Cost Solver

A Python program that calculates and visualizes recurrence-tree costs for `T(n) = aT(n/b) + n^p`.

**Name:** Mayank Mudgal
**SAP ID:** 590027556
**Course:** Design and Analysis of Algorithms (CSEG3053)

## 1. What It Does

The program takes the values of `a`, `b`, `p` and `n` as input. For each recursion level it calculates the number of nodes, the subproblem size, the cost per node and the level cost. It prints the level-wise table and the total cost, then shows an animated bar chart with one bar per level.

## 2. Requirements

- Python 3
- Matplotlib

Install the required package using:

```
pip install -r requirements.txt
```

## 3. How to Run

Open a terminal in the project directory and run:

```
python recurrence_solver.py
```

When prompted, enter four numbers separated by spaces, for example:

```
3 4 1 256
```

The program prints the level-wise cost table and the total cost, then a matplotlib window opens and animates the level costs. Close the window to end the program.

## 4. Examples

**Example 1:** `a = 3, b = 4, p = 1, n = 64`

```
Level   Nodes   Size    Cost/Node   Level Cost
0       1.00    64.00   64.00       64.00
1       3.00    16.00   16.00       48.00
2       9.00    4.00    4.00        36.00
3       27.00   1.00    1.00        27.00

Total cost = 175.00
```

The total cost is 175, which matches the closed form `T(n) = 4n - 3 * n^(log_4 3)` for this recurrence when `T(1) = 1` (256 - 3 * 27 = 175).

**Example 2:** `a = 2, b = 2, p = 1, n = 64`

Every level costs 64, there are 7 levels, and the total cost is 448.

## 5. Assumptions

- The recurrence is `T(n) = aT(n/b) + n^p`, so f(n) is always `n^p`. Other forms such as `n log n` are not supported.
- The base case is `T(1) = 1`.
- The subproblem size decreases by a factor of `b` at each level.
- The recursion tree stops when the subproblem size drops below 1.
- Input values must satisfy `a > 0`, `b > 1`, `n >= 1` and `p >= 0`.

## 6. Files

- `recurrence_solver.py`: main Python program for calculating and visualizing recurrence costs
- `requirements.txt`: lists the required Python packages
- `README.md`: explains the program, requirements, usage, examples and assumptions
