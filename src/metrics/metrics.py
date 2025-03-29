from sklearn.metrics import mean_squared_error
from test_cases.maze import Maze
from test_cases.mazes import mazes
from time import time
import numpy as np
from algorithms.Algorithm import Algorithm
from algorithms.ABC import ArtificialBeeColony as ABC
from algorithms.ACO import ACO
from algorithms.Enhanced_ACO import EnhancedACO as EACO
from algorithms.PSO import PSO
import os


class Metrics:

    def __init__(self):
        self.__csv_path = "your_route_to_results/csv"

    @property
    def csv_path(self) -> str:
        return self.__csv_path

    @csv_path.setter
    def csv_path(self, path: str):
        self.__csv_path = path

    def calculate_metrics(self, duration: float, last_iter: int, best_length: float, lengths: list[float], algo_name: str) -> str:
        result: str = algo_name + ','

        result += f"{round(duration, 2)},"
        result += f"{last_iter},"
        result += f"{round(best_length, 2)},"
        result += f"{round(np.mean(lengths), 2)},"
        result += f"{round(np.std(lengths), 2)},"
        return result

    def create_file(self, maze_number: int, results: str) -> None:

        # filename: str = "metrics_maze_" + str(maze_number) + ".csv"
        filename: str = "metrics.csv"
        filename = os.path.join(self.csv_path, filename)
        header: str = "algorithm,execution_time,convergence,best_length,length_avg,std,maze_number\n"
        results += f"{maze_number}\n"

        if os.path.exists(filename):
            with open(filename, 'a+') as f:
                f.write(results)
        else:
            with open(filename, 'w+') as f:
                f.write(header)
                f.write(results)

    def evaluate_algorithm(self, algorithm: Algorithm, algorithm_name: str, maze_number: int, plot_grid: Maze = None) -> None:
        time_start: float = time()
        best_path, best_lenght, convergence_iteration, all_lenghts = algorithm.optimize()
        time_end: float = time()
        duration: float = time_end - time_start

        results = self.calculate_metrics(
            duration, convergence_iteration, best_lenght, all_lenghts, algorithm_name)
        self.create_file(maze_number, results)

        if plot_grid != None:
            plot_grid.best_path, plot_grid.best_length = best_path, best_lenght
            plot_grid.plot_maze(algorithm_name, maze_number)

    def start(self) -> None:
        maze_array = mazes
        algorithms: list[list[tuple]] = []
        sublist: list[tuple] = []

        for maze in maze_array:
            sublist.append(
                (ACO(maze.maze, maze.start, maze.goal), "ACO", maze_array.index(maze), maze))
            sublist.append(
                (EACO(maze.maze, maze.start, maze.goal), "EACO", maze_array.index(maze), maze))
            sublist.append(
                (ABC(maze.maze, maze.start, maze.goal), "ABC", maze_array.index(maze), maze))
            sublist.append(
                (PSO(maze.maze, maze.start, maze.goal), "PSO", maze_array.index(maze), maze))
            algorithms.append(sublist[:])
            sublist.clear()

        for list_algo in algorithms:
            for algo in list_algo:
                self.evaluate_algorithm(
                    algo[0], algo[1], algo[2], algo[3])
