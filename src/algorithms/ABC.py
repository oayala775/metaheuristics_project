import numpy as np
from test_cases.mazes import mazes
from tools.euclidean_distance import euclidean_distance
from tools.get_neighbors import get_neighbors
import random


class ArtificialBeeColony:
    def __init__(self, grid: np.ndarray, start: tuple, goal: tuple, num_bees:int = 30, max_iter:int = 500):
        self.__grid = grid
        self.__start = start
        self.__goal = goal
        self.__num_bees = num_bees
        self.__max_iter = max_iter
        self.__best_bee:float = float('inf')
        
        self.__num_params:int = 2  # x and y coordinates
        # Initialize the population with random paths
        self.__population = np.full(shape=(self.__num_bees, self.__num_params),
                                  fill_value=self.__start)

        # self.fitness = np.apply_along_axis(self.euclidean_distance, 1, self.population)
    
    @property
    def grid(self) -> np.ndarray:
        return self.__grid
    
    @grid.setter
    def grid(self, grid: np.ndarray):
        self.__grid = grid

    @property
    def start(self) -> tuple:
        return self.__start
    
    @start.setter
    def start(self, start: tuple):
        self.__start = start
    
    @property
    def goal(self) -> tuple:
        return self.__goal
    
    @goal.setter
    def goal(self, goal: tuple):
        self.__goal = goal
    
    @property
    def num_bees(self) -> int:
        return self.__num_bees
    
    @num_bees.setter
    def num_bees(self, num_bees: int):
        self.__num_bees = num_bees
    
    @property
    def max_iter(self) -> int:
        return self.__max_iter
    
    @max_iter.setter
    def max_iter(self, max_iter: int):
        self.__max_iter = max_iter
    
    @property
    def best_bee(self) -> float:
        return self.__best_bee
    
    @best_bee.setter
    def best_bee(self, best_bee: float):
        self.__best_bee = best_bee
    
    @property
    def population(self) -> np.ndarray:
        return self.__population
    
    @population.setter
    def population(self, population: np.ndarray):
        self.__population = population

    def path_length(self, path: list[tuple]) -> float:
        length:int = 0
        for i in range(len(path) - 1):
            length += euclidean_distance(path[i], path[i+1])
        return length
    
    def create_path(self, start: tuple, goal: tuple) -> list[tuple]:
        path: list[tuple] = [start]
        visited_nodes: set[tuple] = set([start])
        current_node: tuple = start
        max_steps = self.grid.shape[0] * self.grid.shape[1]
        steps = 0

        while current_node != goal and steps < max_steps:
            neighbors = get_neighbors(self.grid, current_node)
            if not neighbors:
                return None
            valid_neighbors = [n for n in neighbors if n not in visited_nodes]
            if not valid_neighbors:
                return None
            
            next_node = np.random.choice(len(valid_neighbors))
            current_node = valid_neighbors[next_node]

            path.append(current_node)
            visited_nodes.add(current_node)
            steps += 1
        
        if current_node == goal:
            return path
        return None

    def optimize(self):
        best_path: tuple = None
        # self.best_bee: float = float('inf')
        best_lengths:list[float] = []
        best_iter: int = 0

        positions = []
        for _ in range(self.num_bees):
            positions.append(self.create_path(self.start, self.goal))

        for iteration in range(self.max_iter):
            for i in range(self.num_bees):
                if positions[i] is not None:
                    length = self.path_length(positions[i])
                    if length < self.best_bee:
                        self.best_bee = length
                        best_lengths.append(self.best_bee)
                        best_iter = iteration
                        best_path = positions

                new_path = self.create_path(self.start, self.goal)
                if new_path is not None:
                    new_length = self.path_length(new_path)
                    if positions[i] is None:
                        if new_length < self.best_bee:
                            self.best_bee = new_length
                            best_lengths.append(self.best_bee)
                            best_iter = iteration
                        positions[i] = new_path
                        
                        
            for i in range(self.num_bees):
                if np.random.random() < 0.5:  # Decidir si explorar
                    new_path = self.create_path(self.start, self.goal)
                    if new_path is not None:
                        new_length = len(new_path)
                        if new_length < self.best_bee:
                            self.best_bee = new_length
                            best_iter = iteration
                            best_path = new_path

            

        return best_path, self.best_bee, best_iter, best_lengths