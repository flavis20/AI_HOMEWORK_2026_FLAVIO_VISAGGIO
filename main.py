from src.nqueens import NQueensProblem
from src.search import astar_search
from src.csp_solver import solve_nqueens_csp

def main():
    n=8  # Size of the chessboard and number of queens
    print("Task 1: A* Search for N-Queens Problem")
    try:
        problem = NQueensProblem(n)
        res_astar = astar_search(problem)
        if res_astar:
            print(f"time taken:{res_astar['time']:.4f}seconds")
            print(f"solution cost:{res_astar['cost']}")
            print(f"nodes expanded:{res_astar['nodes_expanded']}")
            print(f"max nodes in memory:{res_astar['max_nodes_in_memory']}")

            sol_astar = tuple(int(a.split()[1]) for a in res_astar['solutions'])
            print(f"Solution (A*): {sol_astar}")
        else:
            print("No solution found using A* search.")
    except Exception as e:
        print(f"An error occurred during A* search: {e}")

    print("\nTask 2: CSP Solver for N-Queens Problem")

    try:
        res_csp = solve_nqueens_csp(n)
        
        if res_csp['status'] == 'success':
            print(f"time taken:{res_csp['time']:.4f}seconds")
            solution = dict(sorted(res_csp['solution'].items())) # Sort solution by column
            print(f"solutions found:{solution}")
        else:
            print("No solution found using CSP solver.")

    except ImportError:
        print("something went wrong, please make sure you have 'python-constraint' library installed.")

if __name__ == "__main__": 
    main() # Entry point of the program
        
           
