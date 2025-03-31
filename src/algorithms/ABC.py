import numpy as np
from algorithms.Algorithm import Algorithm


class ArtificialBeeColony(Algorithm):
    def __init__(self, grid: np.ndarray, start: tuple, goal: tuple, num_bees: int = 30, max_iter: int = 500):
        super().__init__(grid, start, goal)
        self.__num_bees = num_bees
        self.__max_iter = max_iter
        self.__best_bee: float = float('inf')

        self.__num_params: int = 2  # x and y coordinates
        # Initialize the population with random paths
        self.__population = np.full(shape=(self.__num_bees, self.__num_params),
                                    fill_value=self.start)

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

    def optimize(self):
        best_path: tuple = None
        best_lengths: list[float] = []
        best_iter: int = 0

        positions = []
        for _ in range(self.num_bees):
            temporary_path = self.create_path(self.start, self.goal)
            if temporary_path is not None:
                positions.append(temporary_path)

        for iteration in range(self.max_iter):
            for i in range(len(positions)):
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
                            best_lengths.append(self.best_bee)
                            best_iter = iteration
                            best_path = new_path

        return best_path, self.best_bee, best_iter, best_lengths
