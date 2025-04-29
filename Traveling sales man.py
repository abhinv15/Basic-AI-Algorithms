#Traveling sales man 
from itertools import permutations
def total_dist(graph,path):
    total_distance = 0
    for i in range(len(path)-1):
        total_distance += graph[path[i]][path[i+1]]
    total_distance += graph[path[-1]][path[0]]
    return total_distance

def travelling_salesman(graph,start,city_names):
    cities = list(range(len(graph)))
    cities.remove(start)

    min_path = None
    min_dist = float('inf')
    all_path = []

    for perm in permutations:
        current_path = [start] + list(perm) + [start]
        current_dist = total_dist(graph,current_path)
        all_path.append(current_path,current_dist)

        if current_dist < min_dist:
            min_dist = current_dist
            min_path = current_path
    min_path_name = [city_names[i] for i in min_path]
    return min_path_name,min_dist,all_path

def main():
    city_names = []
    n = int(input("Enter the number of cities:"))
    for i in range(n):
        city_name = input(f"Enter the name of the city {i+1} : ")
        city_names.append(city_name)

    graph = {}
    for i in range(n):
        distance = list(map(int,input("Enter the distance to the neighbouring cities:").split()))
        graph.append(distance)

    start_city = input("Enter the starting city:")
    start = city_names.index(start_city)

    min_path,min_dist,all_path = travelling_salesman(graph,start,city_names)

    
