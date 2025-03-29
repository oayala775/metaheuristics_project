import numpy as np
from test_cases.mazes import mazes
from abc import ABC, abstractmethod


class Algorithm(ABC):
    def __init__(self, grid: np.ndarray, start: tuple, goal: tuple):
        self.__grid = grid
        self.__start = start
        self.__goal = goal

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

    def path_length(self, path: list[tuple]) -> float:
        length: int = 0
        for i in range(len(path) - 1):
            length += self.euclidean_distance(path[i], path[i+1])
        return length

    # @abstractmethod
    def create_path(self, start: tuple, goal: tuple) -> list[tuple]:
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

            next_node = np.random.choice(len(valid_neighbors))
            current_node = valid_neighbors[next_node]

            path.append(current_node)
            visited_nodes.add(current_node)
            steps += 1

        if current_node == goal:
            return path
        return None

    @abstractmethod
    def optimize() -> tuple[list[tuple], float, int]:
        pass

    def euclidean_distance(self, position1: tuple[int, int], position2: tuple[int, int]) -> float:
        """
            Mide la distancia euclideana de un punto A a un punto B
        """
        return np.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

    def get_neighbors(self, current_node: tuple) -> list[tuple]:
        """
            Obtiene los nodos permitidos donde se puede mover el algoritmo
        """
        neighbors: list = []
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            neighbor_x, neighbor_y = current_node[0] + x, current_node[1] + y
            if (0 <= neighbor_x < self.grid.shape[0] and
                0 <= neighbor_y < self.grid.shape[1] and
                    self.grid[neighbor_x, neighbor_y] == 0):
                neighbors.append((neighbor_x, neighbor_y))
        return neighbors
