import pandas as pd
import gurobipy as gp
from gurobipy import GRB

if __name__ == "__main__":
    sizes = [2, 5, 4, 7, 1, 3, 8]
    C = 10
    n = len(sizes)
    UB = n
    # create an empty optimization model:
    m = gp.Model("binpacking")

    #variables:
    x = m.addVars(n, UB, vtype = GRB.BINARY, name = "x")
    y = m.addVars(UB, vtype = GRB.BINARY, name = "y")

    #constraints:
    m.addConstrs((gp.quicksum(x[i,j] for j in range(UB)) == 1 for i in range(n)), name = "assign")
    m.addConstrs((gp.quicksum(sizes[i] * x[i,j] for i in range(n))  <= C * y[j] for j in range(UB)), name = "cap")
    m.addConstrs((y[j] >= y[j+1] for j in range(UB-1)), name="symbreak")

    #objective:
    m.setObjective(gp.quicksum(y[j] for j in range(UB)), GRB.MINIMIZE)
    
    #solve:
    m.optimize()

    #solution
    if m.Status == GRB.OPTIMAL:
        used_bins = [j for j in range(UB) if y[j].X > 0.5]
        print("bins used:", len(used_bins))
        for j in used_bins:
            items_in_j = [i for i in range(n) if x[i,j].X > 0.5]
            load = sum(sizes[i] for i in items_in_j)
            print(f"bin {j}: load = {load}/{C} ->items {items_in_j}")
    else:
        print("Solve status:", m.Status)









    