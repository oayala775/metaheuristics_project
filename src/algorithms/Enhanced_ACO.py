import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from matplotlib.colors import ListedColormap

class EnhancedACO():
    def __init__(self, n_ants: int, n_iterations: int, grid: np.array, start: tuple, goal: tuple):
        self.n_ants: int = n_ants
        self.n_iterations: int = n_iterations
        self.alpha: int = 1
        self.beta: int  = 5
        self.rho: float = 0.5
        self.Q: int = 1
        
        self.best_path: list[tuple] = None
        self.best_lenght: float = float('inf')

        self.grid: np.array = grid
        self.start: tuple = start
        self.goal: tuple = goal
    
    def euclidean_distance(self, pos1, pos2):
        return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
    
    def inspiration_function(self, current_node, next_node, goal):
        distance_nodes = self.euclidean_distance(current_node, next_node)
        distance_goal = self.euclidean_distance(next_node, goal)
        C1, C2 = uniform(0,1), uniform(0,1)
        return (C1 / distance_nodes) + (C2 / distance_goal) if distance_nodes > 0 and distance_goal > 0 else 1e-6
    
    def transition_probabilities(self, current_node, valid_neighbors, goal, pheromones):
        probabilities = []
        total = 0
        for n in valid_neighbors:
            tau = pheromones[n[0], n[1]]
            eta = self.inspiration_function(current_node, n, goal)
            probability = (tau ** eta) * (eta ** self.beta)
            probabilities.append(probability)
            total += probability
        if total == 0:
            return [1/len(valid_neighbors)] * len(valid_neighbors)
        else:
            return [probability / total for probability in probabilities]
        
    def get_neighbors(self, current_node: tuple):
        neighbors: list = []
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            neighbor_x, neighbor_y = current_node[0] + x, current_node[1] + y
            if (0 <= neighbor_x < self.grid.shape[0] and 
                0 <= neighbor_y < self.grid.shape[1] and 
                self.grid[neighbor_x, neighbor_y] == 0):
                neighbors.append((neighbor_x, neighbor_y))
        return neighbors
    
    def create_path(self, start, goal, pheromones):
        path = [start]
        visited_nodes = set([start])
        current_node = start
        max_steps = self.grid.shape[0] * self.grid.shape[1]
        steps = 0

        while current_node != goal and steps < max_steps:
            node_neighbors: list[tuple] = self.get_neighbors(current_node)
            if not node_neighbors:
                return None
            valid_neighbors: list[tuple] = [n for n in node_neighbors if n not in visited_nodes]
            if not valid_neighbors:
                return None
            
            probabilities = self.transition_probabilities(current_node, valid_neighbors, goal, pheromones)
            next_node = np.random.choice(len(valid_neighbors), p=probabilities)
            current_node = valid_neighbors[next_node]

            path.append(current_node)
            visited_nodes.add(current_node)
            steps += 1

        if current_node == goal:
            return path
        return None
    
    def path_lenght(self, path):
        lenght = 0
        for i in range(len(path) - 1):
            lenght += self.euclidean_distance(path[i], path[i+1])
        return lenght
    
    def ant_colony(self):
        pheromones = np.ones((self.grid.shape[0], self.grid.shape[1])) * 0.1

        for _ in range(self.n_iterations):
            paths = []
            lenghts = [] 

            for _ in range(self.n_ants):
                path = self.create_path(self.start, self.goal, pheromones)
                if path:
                    lenght = self.path_lenght(path)
                    paths.append(path)
                    lenghts.append(lenght)
            
            if not paths:
                continue
        
            current_best_lenght = min(lenghts)
            current_best_ant = lenghts.index(current_best_lenght)
            current_best_path = paths[current_best_ant]

            if current_best_lenght < self.best_lenght:
                self.best_lenght = current_best_lenght
                self.best_path = current_best_path

            tau = (self.best_lenght - current_best_lenght) / self.best_lenght if self.best_lenght != float('inf') else 0
            pheromones = pheromones * (1 - self.rho)

            for i in range(len(current_best_path) - 1):
                x, y = current_best_path[i]
                pheromones[x, y] += tau
                pheromones[x, y] = max(pheromones[x,y], 0.01)

        return self.best_path, self.best_lenght