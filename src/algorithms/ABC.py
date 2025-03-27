import numpy as np
from test_cases.mazes import mazes

class ArtificialBeeColony:
    def __init__(self, grid: np.ndarray, start: tuple, goal: tuple, num_bees:int = 100, max_iter:int = 1_000):
        self.grid = grid
        self.start_point = start
        self.goal_point = goal
        self.num_bees = num_bees
        self.max_iter = max_iter
        
        self.num_params:int = 2  # x and y coordinates
        # Initialize the population with random paths
        self.population = np.full(shape=(self.num_bees, self.num_params),
                                  fill_value=self.start_point)
        
        # for i in range(self.num_bees):
        #     self.population[i, 0] = np.random.randint(0, self.grid.shape[0])
        #     self.population[i, 1] = np.random.randint(0, self.grid.shape[1])

        # self.fitness = np.apply_along_axis(self.euclidean_distance, 1, self.population)
        # # Take the best bee (minimization case)
        # self.best_bee = self.population[np.argmin(self.fitness)]
        # self.best_path = self.find_path(self.start_point, self.best_bee)
    
    # def path_length(self, path: list[tuple]) -> float:
    #     length:int = 0
    #     for i in range(len(path) - 1):
    #         length += euclidean_distance(path[i], path[i+1])
    #     return length
    
    # def create_path(self, start: tuple, goal: tuple, pheromones: np.array):
    #     path: list[tuple] = [start]
    #     visited_nodes: set[tuple] = set([start])
    #     current_node: tuple = start
    #     max_steps = self.grid.shape[0] * self.grid.shape[1]
    #     steps = 0

    #     while current_node != goal and steps < max_steps:
    #         neighbors = get_neighbors(self.grid, current_node)
    #         if not neighbors:
    #             return None
    #         valid_neighbors = [n for n in neighbors if n not in visited_nodes]
    #         if not valid_neighbors:
    #             return None
            
    #         next_node = np.random.choice(len(valid_neighbors))
    #         current_node = valid_neighbors[next_node]

    #         path.append(current_node)
    #         visited_nodes.add(current_node)
    #         steps += 1
        
    #     if current_node == goal:
    #         return path
    #     return None

    # def optimize(self):
    #     for iteration in range(self.max_iter):
    #         for i in range(self.num_bees):
    #             # A random integer value, number of explorer bees, is used to select
    #             # a random bee
    #             k:int = np.random.randint(0, self.num_params)
    #             # A random noise value
    #             phi:float = np.random.uniform(-1, 1)
    #             """Both k and phi are used to add noise to the system"""
    #             new_solution:np.ndarray = np.copy(self.population[i])
    #             new_solution[k] = self.population[i, k] + phi
    #             # Ensure the new solution is within the grid boundaries
    #             new_solution[0] = max(0, min(new_solution[0], self.grid.shape[0] - 1))
    #             new_solution[1] = max(0, min(new_solution[1], self.grid.shape[1] - 1))
    #             new_fitness = euclidean_distance(new_solution)

    #             # If the new solution is better than the previous one, replace it
    #             if new_fitness < self.fitness[i]:
    #                 self.population[i] = new_solution
    #                 self.fitness[i] = new_fitness

    #             # If the new solution is better than the global minimum, replace it
    #             if new_fitness < np.min(self.fitness):
    #                 self.best_bee = new_solution
    #                 self.best_path = self.find_path(self.start_point, self.best_bee)

        # return self.best_bee, self.best_path