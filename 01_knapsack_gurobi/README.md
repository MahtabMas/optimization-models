Problem: 01_knapsack_gurobi

What this is

A tiny 0/1 knapsack model in Gurobi. Pick items to maximize value without exceeding a weight limit.

How I set it up

Variables: x[i] x \in {0,1}
Constraint: sum(weights[i] * x[i]) <= C
Objective: maximize sum(values[i] * x[i])

How to run

Activate my venv, then: python knapsack.py

How to change things

Edit the lists "values", "weights", and the capacity "C" at the top of the file.

There’s an optional “at most 2 items” constraint and a tiny tie-breaker that prefers lighter packs. I can comment them in/out.

Output

Prints which items were chosen and the total value/weight.
