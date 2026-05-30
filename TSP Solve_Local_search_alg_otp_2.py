import math
import time
class Instance:
    def __init__(self):
        self.inital_tour = [] #Initial tour
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
with open("kroB100.tsp", 'r') as file: #Process data
    for line in file :
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
start_time = time.time()#Get starting time

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
greedy_tour.append(start_node)
#lobal variables
total_length = 0

#Local search
improved = True #Statis variable

while improved:
    improved = False
    
    for i in range(1, len(greedy_tour) - 2):
        for j in range(i + 1, len(greedy_tour) - 1):
            a = greedy_tour[i - 1]
            b = greedy_tour[i]
            c = greedy_tour[j]
            d = greedy_tour[j + 1] #A, B, C, D
            
            old_dist = instance.euclidean_distance[a][b] + instance.euclidean_distance[c][d]
            new_dist = instance.euclidean_distance[a][c] + instance.euclidean_distance[b][d]
            # Make comparion between A-B-C-D and A-C-B-D
            if new_dist < old_dist:
                greedy_tour[i:j + 1] = reversed(greedy_tour[i:j + 1])
                improved = True #Update status to continue while loop

for i in range(len(greedy_tour) - 1):
    #Calculate total length from tour after calculating
    total_length += instance.euclidean_distance[greedy_tour[i]][greedy_tour[i + 1]]
    
total_time = (time.time() - start_time) * 1000 #Convert running time to ms
print(f"Answer with local search algorithm is: {total_length}. Running time is: {total_time}.")#Answers
print(f"Road is: {greedy_tour}")#Optimized tour

