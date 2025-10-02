import pandas as pd
import gurobipy as gp
from gurobipy import GRB

if __name__ == "__main__":
    values = [10, 6, 7, 3, 18, 7, 9] 
    weights = [6, 4, 5, 2, 9, 3, 5]
    C = 15
    n = len(values)

    # print( "n = ", n, " ; capacity = ", C)

    # create an empty optimization model:
    m = gp.Model("knapsack")
    # print( "Model created:", m.ModelName)

    #variables:
    x = m.addVars(n, vtype = GRB.BINARY, name = "x")

    #capacity 
    m.addConstr(gp.quicksum(weights[i]* x[i] for i in range(n)) <= C, name = "capacity")

    #at most two items
    m.addConstr(gp.quicksum(x[i] for i in range(n)) <= 2, name = "at_most_two" )

    #objective:
    obj_main = gp.quicksum(values[i]* x[i] for i in range(n))
    tie_weight = gp.quicksum(weights[i] * x[i] for i in range(n))
    epsilon = 1e-6
    m.setObjective(obj_main - epsilon * tie_weight, GRB.MAXIMIZE)

    #solve
    m.optimize()

    #solution
    if m.Status == GRB.OPTIMAL:
        chosen = [i for i in range(n) if x[i].X > 0.5]
        tot_value = sum(values[i] for i in chosen)
        tot_weight = sum(weights[i] for i in chosen)

        print("Chosen items:", chosen)
        print(f"Total value = {tot_value}")
        print(f"Total weight = {tot_weight} / {C}")
    else:
        print("No optimal solution; status:", m.Status)

    print("Objective (m.Objective) =", m.ObjVal)


