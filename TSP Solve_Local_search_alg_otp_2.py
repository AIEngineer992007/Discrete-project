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
        instance.inital_tour.append(int(nodes) - 1)#Index of city in Python

instance.inital_tour.append(instance.inital_tour[0])#Come back to start city

# Calculate all dítances in data set
instance.euclidean_distance_calculation()

#lobal variables
total_length = 0

#Local search
improved = True #Statis variable

start_time = time.time()# Get starting time
while improved:
    improved = False
    
    for i in range(1, len(instance.inital_tour) - 2):
        for j in range(i + 1, len(instance.inital_tour) - 1):
            a = instance.inital_tour[i - 1]
            b = instance.inital_tour[i]
            c = instance.inital_tour[j]
            d = instance.inital_tour[j + 1] #A, B, C, D
            
            old_dist = instance.euclidean_distance[a][b] + instance.euclidean_distance[c][d]
            new_dist = instance.euclidean_distance[a][c] + instance.euclidean_distance[b][d]
            # Make comparion between A-B-C-D and A-C-B-D
            if new_dist < old_dist:
                instance.inital_tour[i:j + 1] = reversed(instance.inital_tour[i:j + 1])
                improved = True #Update status to continue while loop

for i in range(len(instance.inital_tour) - 1):
    #Calculate total length from tour after calculating
    total_length += instance.euclidean_distance[instance.inital_tour[i]][instance.inital_tour[i + 1]]
    
total_time = (time.time() - start_time) * 1000 #Convert running time to ms
print(f"Answer with local search algorithm is: {total_length}. Running time is: {total_time}.")#Answers
print(f"Road is: {instance.inital_tour}")#Optimized tour

