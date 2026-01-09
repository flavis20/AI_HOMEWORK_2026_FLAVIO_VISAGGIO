from abc import ABC, abstractmethod 

class Problem(ABC):
    @abstractmethod 
    def get_initial_state(self):
        pass

    @abstractmethod
    def is_goal_state(self, state):
        pass

    @abstractmethod
    def get_successors(self, state):
        pass
    
    @abstractmethod
    def heuristic(self, state):
        pass