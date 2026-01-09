from src.problem import Problem

class NQueensProblem(Problem):
    def __init__(self, n):
        self.n = n
        self.initial_state= () #empty board

    def get_initial_state(self): 
        return self.initial_state

    def is_goal_state(self, state):
        return len(state) == self.n

    def get_successors(self, state): 
        col = len(state)
        if col == self.n:
            return []
        successors = []
        for row in range(self.n):
            if not self._is_under_attack(state,row,col):
                next_state = state + (row,)
                action = f"Row {row}"
                successors.append((action, next_state, 1))
        return successors

    def _is_under_attack(self, state, new_row, new_col): # Check if the new queen is under attack
        for col, row in enumerate(state):
            if row == new_row: # Same row attack
                return True
            if abs(row - new_row) == abs(col - new_col): # Diagonal attack
                return True
        return False
    
    def heuristic(self, state):
        return self.n - len(state)


    