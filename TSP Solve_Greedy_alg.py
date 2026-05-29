import math
import time
class Instance:
    def __init__(self):
        self.nodes = []
        self.euclidean_distance = []
        
    def distance(self, first_point, second_point):
        return math.sqrt((self.nodes[first_point][0] - self.nodes[second_point][0]) ** 2 + (self.nodes[first_point][1] - self.nodes[second_point][1]) ** 2)
    
    def euclidean_distance_calculation(self):
        self.euclidean_distance = [[0] * len(self.nodes) for _ in range(len(self.nodes))]
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                self.euclidean_distance[i][j] = self.distance(i, j)#Distance from i-th city to j-th city

instance = Instance()
with open("kroB100.tsp", 'r') as file:#Process data
    for line in file:
        if line == "" or line[0].isalpha():
            continue
        
        nodes, x, y = line.split()
        x = float(x)
        y = float(y)
        instance.nodes.append((x, y))

# Calculate all dítances in data set
instance.euclidean_distance_calculation()

#Global variables
start_node = 0
visited_cities = [False] * len(instance.nodes)
visited_cities[start_node] = True
current_node = start_node
unvisited_cities = len(instance.nodes) - 1
total_length = 0

#Greedy
greedy_tour = [start_node]#Tour
greedy_start_time = time.perf_counter()#Get starting time

while unvisited_cities > 0:#Check visited city
    next_node = None#Init a node
    min_dist = float('inf') #Init min dist to make comparision
    
    for j in range(len(instance.nodes)):
        if not visited_cities[j]: #Check visited cities
            dist = instance.euclidean_distance[current_node][j]
            if dist < min_dist:
                next_node = j #Update next node
                min_dist = dist #Update mindist
    
    total_length += min_dist
    unvisited_cities -= 1
    visited_cities[next_node] = True
    current_node = next_node #Update current node
    greedy_tour.append(next_node) #Update tour


total_length += instance.euclidean_distance[current_node][start_node]# Distance from last node to start node
total_time = (time.perf_counter() - greedy_start_time) * 1000#Convert time to ms
print(f"Answer with greedy algorithm is: {total_length}. Running time is: {total_time}.")#Answers
print(f"Road is: {greedy_tour}")#Optimized tour

