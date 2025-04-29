#BFS AND DFS

#function for BFS
from collections import deque
def bfs(graph,start,goal):
    queue = deque([(start,[start])])
    visited = set()
    traversed_nodes = []

    while queue:
        current_node,path = queue.popleft()
        traversed_nodes.append(current_node)

        if current_node == goal:
            return path,traversed_nodes
        
        visited.add(current_node)

        for neighbor in graph.get(current_node,[]):
            if neighbor not in visited:
                queue.append((neighbor,path + [neighbor]))
    return None,traversed_nodes

#function foe dfs
def dfs(graph,start,goal):
    stack = [(start,[start])]
    visited = set()
    traversed_nodes = []

    while stack:
        current_node,path = stack.pop()
        traversed_nodes.append(current_node)

        if current_node ==   goal:
            return path,traversed_nodes
        
        visited.add(current_node)

        for neighbors in reversed(graph.get(current_node,[])):
            if neighbors not in visited:
                stack.append((neighbors, path + [neighbors]))

    return None,traversed_nodes

def get_user_input():
    # Initialize an empty graph dictionary
    graph = {}
    
    # Get the number of edges from the user
    num_edges = int(input("Enter the number of edges in the graph: "))
    
    # Collect edges from the user
    print("Enter each edge as two space-separated nodes (e.g., 'A B'):")
    for _ in range(num_edges):
        edge = input().split()
        if len(edge) != 2:
            print("Invalid input. Please enter two nodes for each edge.")
            continue
        node1, node2 = edge
        
        # Add the edge to the graph (bidirectional by default)
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    # Get the start and goal nodes
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")
    
    return graph, start, goal

# Use the input function with BFS and DFS
graph, start, goal = get_user_input()

# Call BFS and DFS with the user-provided input
print("BFS:")
bfs_path, bfs_traversed = bfs(graph, start, goal)
print("Path found by BFS:", bfs_path)
print("Nodes traversed by BFS:", bfs_traversed)

print("\nDFS:")
dfs_path, dfs_traversed = dfs(graph, start, goal)
print("Path found by DFS:", dfs_path)
print("Nodes traversed by DFS:", dfs_traversed)




