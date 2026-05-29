import math
import time
import random

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
                self.euclidean_distance[i][j] = self.distance(i, j) #Distance from i-th city to j-th city

instance = Instance()
with open("kroB100.tsp", 'r') as file: #Process data
    for line in file:
        if line == "" or line[0].isalpha():
            continue
        
        nodes, x, y = line.split()
        x = float(x)
        y = float(y)
        instance.nodes.append((x, y))

# Calculate all distances in data set
instance.euclidean_distance_calculation()


num_cities = len(instance.nodes)

# 1. Cấu hình các Siêu tham số (Hyperparameters) của Đàn kiến
num_ants = 30           # Số lượng kiến trong bầy
max_iterations = 60     # Số thế hệ kiến chạy tiến hóa
alpha = 1.0             # Độ quan trọng của Pheromone (Mùi hương)
beta = 2.0              # Độ quan trọng của Heuristic (Độ gần của khoảng cách)
evaporation_rate = 0.5  # Tốc độ bay hơi của Pheromone (50% sau mỗi thế hệ)
Q = 100.0               # Hằng số điều phối lượng mùi tiết ra khi kiến đi qua

#Initial pheromone matrix
pheromone = [[1.0] * num_cities for _ in range(num_cities)]

# Calculate length of road which ant go through
def calculate_total_length_of_ant(tour):
    total_length = 0
    for i in range(len(tour) - 1):
        total_length += instance.euclidean_distance[tour[i]][tour[i + 1]]
    return total_length

best_length = float('inf')
best_tour = []
#ACO algorithm
start_time = time.time() #Get starting time

for iteration in range(max_iterations):
    all_ants_tours = []
    
    for ant in range(num_ants):
        start_city = random.randint(0, num_cities - 1)
        visited_cities = [False] * num_cities
        visited_cities[start_city] = True
        tour = [start_city]
        current_city = start_city
        while len(tour) < num_cities:
            probabilities = []
            total_prob = 0.0
            
            for next_city in range(num_cities):
                if not visited_cities[next_city]:
                    dist = max(instance.euclidean_distance[current_city][next_city], 0.000001)
                    
                    p_val = (pheromone[current_city][next_city] ** alpha) * ((1.0 / dist) ** beta)
                    probabilities.append((next_city, p_val))
                    total_prob += p_val
            
            pick = random.uniform(0, total_prob)
            current_sum = 0.0
            selected_city = probabilities[-1][0]
            
            for next_city, p_val in probabilities:
                current_sum += p_val
                if current_sum >= pick:
                    selected_city = next_city
                    break
            tour.append(selected_city)
            visited_cities[selected_city] = True
            current_city = selected_city
        tour.append(start_city)
        all_ants_tours.append(tour)
        
        length_of_tour = calculate_total_length_of_ant(tour)
        if length_of_tour < best_length:
            best_length = length_of_tour
            best_tour = tour.copy()
        
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone[i][j] *= (1.0 - evaporation_rate)
    
    for tour in all_ants_tours:
        tour_lenght = calculate_total_length_of_ant(tour)
        pheromone_to_add = Q / tour_lenght
        
        for i in range(len(tour) - 1):
            c1 = tour[i]
            c2 = tour[i+1]
            pheromone[c1][c2] += pheromone_to_add
            pheromone[c2][c1] += pheromone_to_add  # TSP đối xứng cập nhật cả 2 chiều

total_time = (time.time() - start_time) * 1000
print(f"Answer with ACO algorithm is: {best_length}. Running time is: {total_time}.")#Answers
print(f"Road is: {best_tour}")#Optimized tour
