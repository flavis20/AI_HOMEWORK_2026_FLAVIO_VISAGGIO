import heapq
import time

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = heuristic
        self.f = path_cost + heuristic

    def __lt__(self, other):
        return self.f < other.f
    
def astar_search(problem):
    start_time = time.time()

    nodes_expanded = 0
    nodes_generated = 0
    max_nodes_in_memory = 0

    initial_state = problem.get_initial_state()
    initial_h = problem.heuristic(initial_state)
    
    start_node = Node(initial_state, parent=None, action=None, path_cost=0, heuristic=initial_h)

    frontier = [] 
    heapq.heappush(frontier, start_node)

    explored = set()
    frontier_states = {initial_state: start_node.path_cost}

    nodes_generated += 1

    while frontier:
        current_memory = len(frontier) + len(explored)  #track current memory usage
        if current_memory > max_nodes_in_memory:
            max_nodes_in_memory = current_memory
        
        node = heapq.heappop(frontier)
        
        if node.state in explored:
            continue

        if problem.is_goal_state(node.state):
            execution_time = time.time() - start_time
            return {
                'solutions': reconstruct_path(node),
                'cost': node.path_cost,
                'time': execution_time,
                'nodes_expanded': nodes_expanded,
                'nodes_generated': nodes_generated,
                'max_nodes_in_memory': max_nodes_in_memory,
            }
        
        explored.add(node.state)
        if node.state in frontier_states:  
            del frontier_states[node.state]  # clean up frontier states
        
        nodes_expanded += 1

        for action, next_state, cost in problem.get_successors(node.state):
            if next_state in explored:
                continue

            new_cost = node.path_cost + cost
        
            if next_state not in frontier_states or new_cost < frontier_states[next_state]:
                h_val = problem.heuristic(next_state)
                child_node = Node(next_state, parent=node, action=action, path_cost=new_cost, heuristic=h_val)

                heapq.heappush(frontier, child_node)
                frontier_states[next_state] = new_cost
                nodes_generated += 1

    return None

def reconstruct_path(node):
    path = []
    while node.parent is not None:
        path.append(node.action)
        node = node.parent
    return path[::-1]