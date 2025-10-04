Problem: 02_binpacking_gurobi

What this is

A small example of binpacking model in Gurobi. packing items into bins in a way that the total size of items packed in a bin never exceeds the bin's capacity.

How I set it up

Variables: x[i,j] x\in {0,1}     //item i is assigned to bin j

           y[j]   y\in {0,1}    // bin j is used

Constraints: sum(sizes[i] * x[i,j]) <= C * y[j] // total weight in each bin

             sum(x[i,j] == 1)                  //  item packed in one bin 


Objective: minimize sum(y[j]) // minimize the number of used bins

How to run

Activate my venv, then: python binpacking.py

How to change things

Edit the list "sizes" and the capacity "C" at the top of the file.

There’s an optional "symbreak" constraint to force bins to be used in index order; you can comment it out.

Output

Prints which the number of used bins and the items assigned to each bin.