# Nicklaus Roach
# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = None

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = None

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = None

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = None

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = None

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = None

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def bfs(graph, start, goal):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
            
        
        last_node = path[-1]
        
        if last_node == goal:
                return path
                
        for node in graph.get_connected_nodes(last_node):
            if node not in path:
                new_path = []
                new_path.extend(path)
                new_path.append(node)
                queue.append(new_path)
            
        
        
## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop()
            
        
        last_node = path[-1]
        
        if last_node == goal:
                return path
                
        for node in graph.get_connected_nodes(last_node):
            if node not in path:
                new_path = []
                new_path.extend(path)
                new_path.append(node)
                queue.append(new_path)


## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    queue = []
    queue.append([start])
    
    while queue:
        path = queue.pop(0)
            
        last_node = path[-1]
        
        if last_node == goal:
                return path
                
        paths = {}
        for node in graph.get_connected_nodes(last_node):
            if node not in path:
                new_path = []
                new_path.extend(path)
                new_path.append(node)
                paths[graph.get_heuristic(node, goal)] = new_path
        to_front = []
        for path_distance in sorted(paths):
            to_front.append(paths[path_distance])
        queue = to_front + queue    

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    best_paths = [[start]]
    
    while best_paths:
        
        paths_to_extend = []
        paths_to_extend.extend(best_paths)
        best_paths = []
        all_extended_paths = {}
        
        for path in paths_to_extend:
            
            last_node = path[-1]
            
            if last_node == goal:
                return path
            
            neighbors = graph.get_connected_nodes(last_node)
            
            for neighbor in neighbors:
                if neighbor not in path:
                    new_path = []
                    new_path.extend(path)
                    new_path.append(neighbor)
                    all_extended_paths[graph.get_heuristic(neighbor, goal)] = new_path
                    
        to_front = []
        for path_distance in sorted(all_extended_paths)[:beam_width]:
            to_front.append(all_extended_paths[path_distance])
        best_paths.extend(to_front) 
        
        

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    length = 0
    if len(node_names) == 1:
        return 0
        
    for i in range(len(node_names) - 1):
        length += graph.get_edge(node_names[i], node_names[i+1]).length
    return length

def branch_and_bound(graph, start, goal):
    queue = [(0,start)]
    
    while queue:
        length, path = queue.pop(0)
        if goal in path:
            return path
        last_node = path[-1]
        neighbors = graph.get_connected_nodes(last_node)
        for neighbor in neighbors:
            if neighbor not in path:
                new_path = []
                new_path.extend(path)
                new_path.append(neighbor)
                queue.append((path_length(graph, new_path), new_path))
        queue.sort()       
            

def a_star(graph, start, goal):
    extended_set = []
    queue = [(graph.get_heuristic(start, goal), [start])]
    
    while queue:
        cost, path = queue.pop(0)
        if goal in path:
            return path
        last_node = path[-1]
        neighbors = graph.get_connected_nodes(last_node)
        for neighbor in neighbors:
            if neighbor not in path:
                new_path = []
                new_path.extend(path)
                new_path.append(neighbor)
                new_cost = graph.get_heuristic(neighbor, goal) + path_length(graph, new_path)
                queue.append((new_cost, new_path))
            # check if neighbor shows up in more than one path, if yes then remove
            # the path with the longer distance from start to neighbor
            
            
        


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
