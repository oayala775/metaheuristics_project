import numpy as np

class ACO():
    def __init__(self, n_ants: int, n_iterations: int, grid: np.array, start: tuple, goal: tuple):
        self.n_ants: int = n_ants
        self.n_iterations: int = n_iterations
        self.alpha: int = 1
        self.beta: int  = 5
        self.rho: float = 0.5
        self.Q: int = 1
        
        self.best_path: list[tuple] = None
        self.best_length: float = float('inf')

        self.grid: np.array = grid
        self.start: tuple = start
        self.goal: tuple = goal
    
    def euclidean_distance(self, pos1, pos2):
        return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
    
    def get_neighbors(self, current_node: tuple):
        neighbors: list = []
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            neighbor_x, neighbor_y = current_node[0] + x, current_node[1] + y
            if (0 <= neighbor_x < self.grid.shape[0] and 
                0 <= neighbor_y < self.grid.shape[1] and 
                self.grid[neighbor_x, neighbor_y] == 0):
                neighbors.append((neighbor_x, neighbor_y))
        return neighbors
    
    def create_path(self, start: tuple, goal: tuple, pheremones: np.array):
        path = [start]
        visited_nodes = set([start])
        current_node = start
        max_steps = self.grid.shape[0] * self.grid.shape[1]
        steps = 0

        while current_node != goal and steps < max_steps:
            node_neighbors = self.get_neighbors(current_node)
    
    def ant_colony(self):
        pheromones = np.ones((self.grid.shape[0], self.grid.shape[1])) * 0.1

        for _ in range(self.n_iterations):
            paths = []
            lenghts = []

            for _ in range(self.n_ants):
                path = self.create_path(self.start, self.goal, pheromones)