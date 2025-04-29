#map colouring using backtracking

#define function for backtracking
import random
def random_coloring(variables,domains):
    return {region : random.choice(domains) for region in variables}

#define function to count the conflicts
def count_conflicts(graph,coloring):
    count = 0
    for region,neighbors in graph.items():
        for neighbor in neighbors:
            if coloring[region] == coloring[neighbor]:
                count += 1
    return count

#define hill climbing algorithm
def hill_climbing(graph,variables,domains):
    current_coloring = random_coloring(variables,domains)
    current_conflicts = count_conflicts(graph,current_coloring)

    print(f"Initial Coloring: {current_coloring}")
    print(f"Initial Conflict : {current_conflicts}")

    #when conflict exists
    step  = 0
    while current_conflicts > 0:
        Improved = False

        for region in variables:
            original_color = current_coloring[region]

            for color in domains:
                if original_color != color:
                    current_coloring[region] = color
                    new_conflicts = count_conflicts(graph,current_coloring)

                    if new_conflicts < current_conflicts:
                        current_conflicts = new_conflicts
                        Improved = True
                        print(f"Node {region} changed colour to {color}")
                        print(f"Current coloring : {current_coloring}")
                        print(f"Current conflict : {current_conflicts}")
                        break
            if Improved:
                break
            else:
                current_coloring[region] = original_color
        if not Improved:
            print(f"Optimim reached at step {step} and the current color is {current_coloring}")
            break
        step += 1

    print(f"Final coloring : {current_coloring}")
    print(f"Final conflict : {current_conflicts}")
    return current_coloring

def get_input():
    variables = input("Enter the set of variables (comma-separated): ").split(",")
    variables = [var.strip() for var in variables]

    domains = input("Enter the set of colors (comma-separated): ").split(",")
    domains = [color.strip() for color in domains]

    graph = {}
    for region in variables:
        neighbors = input(f"Enter the adjacent variables for {region} (comma-separated, or leave blank if none): ")
        graph[region] = [neighbor.strip() for neighbor in neighbors.split(",") if neighbor.strip()]

    return variables, domains, graph

# Main execution
variables, domains, graph = get_input()
final_coloring = hill_climbing(graph, variables, domains)
