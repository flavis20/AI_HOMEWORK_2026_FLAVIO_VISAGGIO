import time 
from constraint import Problem, AllDifferentConstraint

def solve_nqueens_csp(n):
    problem = Problem()

    cols = range(n) # Columns represent the queens
    rows = range(n) # Rows represent the possible positions for queens

    problem.addVariables(cols, rows) # Each column can take any row value
    problem.addConstraint(AllDifferentConstraint()) # No two queens can be in the same row

    # Diagonal constraints
    for c1 in cols:
        for c2 in cols:
            if c1 < c2:
                problem.addConstraint(lambda r1, r2, col1=c1, col2=c2: abs(r1 - r2) != abs(col1 - col2), (c1, c2)) # No two queens can be on the same diagonal
    start_time = time.time()
    solution= problem.getSolution() # Get the solution
    end_time = time.time() 

    return {
        'status': 'success' if solution else 'failure',
        'solution': solution,
        'time': end_time - start_time,
    }