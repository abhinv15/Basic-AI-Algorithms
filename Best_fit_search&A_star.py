# BEST FIT SEARCH AND A* 

#define a class
class Node:
    def __init__(self,state,parent = None,cost = 0,heuristic = 0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
    
    def __lt__(self,other):
        return (self.cost+self.heuristic) < (other.cost+other.heuristic)
    
#define best fit function
def best_fit_(graph,start,goal,heuristic):
    open_list = [Node(start,heuristic = heuristic[start])]
    closed_list = []

    while open_list:
        open_list.sort(key=lambda x : x.heuristic)
        current_node = open_list.pop(0)
        current_state = current_node.state
      
        if current_state == goal:
            return path_bfs(current_node)
        
        closed_list.append(current_state)

        for neighbor,cost in graph[current_state]:
            if neighbor in closed_list:
                continue
            if not any (node.state == neighbor for node in open_list):
                open_list.append(Node(neighbor,parent = current_node,cost = cost,heuristic = heuristic[neighbor]))

    return None

#finding the path
def path_bfs(node):
    total = 0
    path = []
    while node:
        total += node.cost
        path.append(node.state)
        node = node.parent
    print(f"Total cost : {total}")
    return path[::-1]

#define A*
def A_star(graph,start,goal,heuristic):
    open_list = [Node(start,cost = 0,heuristic=heuristic[start])]
    closed_list = []

    while open_list:
        open_list.sort(key = lambda x : x.heuristic+x.cost)
        current_node = open_list.pop(0)
        current_state = current_node.state

        if current_state == goal:
            return path_A(current_node)
        
        closed_list.append(current_state)

        for neighbor,cost in graph[current_state]:
            if neighbor in closed_list:
                continue
            g_cost = current_node.cost +cost
            if not any (node.state == neighbor for node in open_list):
                open_list.append(Node(neighbor,parent = current_node,cost =g_cost,heuristic = heuristic[neighbor] ))
            else:
                for node in open_list:
                    if node.state == neighbor and g_cost < node.cost:
                        node.cost = g_cost
                        node.parent = current_node
    return None

#define path for a star
def path_A(node):
    path = []
    print(f"Total cost : {node.cost}")
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

graph ={'Arad':[('Zerind',75),('Timisora',118),('Sibiu',140)],
        'Zerind' : [('Arad',75),('Oradea',71)],
        'Timisora' :[('Arad',118),('Lugoj',111)],
        'Sibiu' :[('Arad',140),('Oradea',151),('Fagarasa',99),('Rimicu',80)],
        'Rimicu' : [('Sibiu',80),('Pitesti',97),('Debaeu',80)],
        'Fagarasa' : [('Sibiu',99),('Bucharest',211)],
        'Bucharest' : [('Fagarasa',99),('Pitesti',97)],
        'Pitesti': [('Bucharest',101),('Rimicu',97)],
        'Oradea' :[('Zerind',101),('Sibiu',97)],
        'Debaeu' :[('Rimicu',80)],
        'Lugoj': [('Timisora',111)]
    }

heuristic = {
        'Arad' : 366,
        'Zerind' : 374,
        'Timisora' : 329,
        'Sibiu' : 253,
        'Rimicu' : 193,
        'Fagarasa' : 176,
        'Bucharest' : 0,
        'Pitesti' :100,
        'Oradea' :380,
        'Debaeu'  : 256,
        'Lugoj' :244,

    }
start_node = "Arad"
goal_node = "Bucharest"

print("Best Fit search\n")
print(best_fit_(graph,start_node,goal_node,heuristic))

print("A Star\n")
print(A_star(graph,start_node,goal_node,heuristic))



