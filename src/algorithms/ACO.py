import numpy as np
from algorithms.Algorithm import Algorithm


class ACO(Algorithm):
    def __init__(self, grid: np.ndarray, start: tuple, goal: tuple):
        super().__init__(grid, start, goal)
        self.n_ants: int = 50
        self.n_iterations: int = 150
        self.alpha: int = 1
        self.beta: int = 5
        self.rho: float = 0.8
        self.Q: int = 100

        self.best_path: list[tuple] = None
        self.best_length: float = float('inf')

    def inspiration_function(self, current_node: tuple, neighbor_node: tuple) -> float:
        node_distance = self.euclidean_distance(current_node, neighbor_node)
        return 1 / node_distance if node_distance > 0 else 1e-6

    def transition_probabilities(self, current_node: tuple, valid_neighbors: list[tuple], pheromones: np.array):
        probabilities = []
        total = 0
        for n in valid_neighbors:
            tau = pheromones[n[0], n[1]]
            eta = self.inspiration_function(current_node, n)
            probability = (tau ** self.alpha) * (eta ** self.beta)
            probabilities.append(probability)
            total += probability
        if total == 0:
            return [1/len(valid_neighbors) * len(valid_neighbors)]
        return [probability / total for probability in probabilities]

    def create_path(self, start: tuple, goal: tuple, pheromones: np.ndarray):
        path: list[tuple] = [start]
        visited_nodes: set[tuple] = set([start])
        current_node: tuple = start
        max_steps = self.grid.shape[0] * self.grid.shape[1]
        steps = 0

        while current_node != goal and steps < max_steps:
            neighbors = self.get_neighbors(current_node)
            if not neighbors:
                return None
            valid_neighbors = [n for n in neighbors if n not in visited_nodes]
            if not valid_neighbors:
                return None

            probabilities = self.transition_probabilities(
                current_node, valid_neighbors, pheromones)
            next_node = np.random.choice(len(valid_neighbors), p=probabilities)
            current_node = valid_neighbors[next_node]

            path.append(current_node)
            visited_nodes.add(current_node)
            steps += 1

        if current_node == goal:
            return path
        return None

    def optimize(self) -> tuple[list[tuple], float, int]:
        best_lenghts: list[float] = []
        pheromones: list = np.ones(
            (self.grid.shape[0], self.grid.shape[1])) * 0.1
        convergence_iteration: int = 0

        for iteration in range(self.n_iterations):
            paths = []
            lengths = []

            for _ in range(self.n_ants):
                path = self.create_path(self.start, self.goal, pheromones)
                if path:
                    length = self.path_length(path)
                    paths.append(path)
                    lengths.append(length)

            if not paths:
                continue

            current_best_length = min(lengths)
            best_lenghts.append(current_best_length)
            current_best_ant = lengths.index(current_best_length)
            current_best_path = paths[current_best_ant]

            if current_best_length < self.best_length:
                self.best_length = current_best_length
                self.best_path = current_best_path
                convergence_iteration = iteration + 1

            pheromones = pheromones * (1 - self.rho)
            for path, lenght in zip(paths, lengths):
                for i in range(len(path) - 1):
                    x1, y1 = path[i]
                    x2, y2 = path[i+1]
                    pheromones[x1, y1] += self.Q / lenght
                    pheromones[x2, y2] += self.Q / lenght
                    pheromones[x1, y1] = max(pheromones[x1, y1], 0.01)
                    pheromones[x2, y2] = max(pheromones[x2, y2], 0.01)

        return self.best_path, self.best_length, convergence_iteration, best_lenghts
        # return self.best_path, self.best_length, best_lenghts
