import time
import csv
from src.nqueens import NQueensProblem
from src.search import astar_search
from src.csp_solver import solve_nqueens_csp

def runexperiments():
    n_values = range(4,12) # N values from 4 to 11
    
    results = []

    print(f"{'N':<5} | {'Algorithm':<10} | {'status':<10} | {'Time(s)':<10} | {'Nodes Expanded':<10} | {'Max Nodes in Memory':<10}")

    for n in n_values:
        print("Running experiments for N =", n)
        print("A* Search:")

        problem = NQueensProblem(n)
        res_astar = astar_search(problem)

        if res_astar:
            print(f"{n:<5} | {'A*':<10} | {'success':<10} | {res_astar['time']:<10.4f} | {res_astar['nodes_expanded']:<10} | {res_astar['max_nodes_in_memory']:<10}")
            results.append({
                'N':n,
                'Algorithm':'A*',
                'Time(s)':res_astar['time'],
                'Nodes Expanded':res_astar['nodes_expanded'],
                'Max Nodes in Memory':res_astar['max_nodes_in_memory'],
                'status':'success'
            })
        else:
            print(f"{n:<5} | {'A*':<10} | {'failure':<10} | {'-':<10} | {'-':<10} | {'-':<10}")
            
        print("CSP Solver:")
        res_csp = solve_nqueens_csp(n)
        if res_csp['status'] == 'success':
            print(f"{n:<5} | {'CSP':<10} | {'success':<10} | {res_csp['time']:<10.4f} | {'-':<10} | {'-':<10}")
            results.append({
                'N':n,
                'Algorithm':'CSP',
                'Time(s)':res_csp['time'],
                'Nodes Expanded':'-',
                'Max Nodes in Memory':'-',
                'status':'success'
            })
        else:
            print(f"{n:<5} | {'CSP':<10} | {'failure':<10} | {'-':<10} | {'-':<10} | {'-':<10}")
    
    return results

if __name__ == "__main__":
    data = runexperiments()
    
    keys = data[0].keys()
    with open('nqueens_experiments.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print("Experiment results saved to 'nqueens_experiments.csv' using csv module.")
else:
    print("no data collected")   