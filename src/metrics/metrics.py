from sklearn.metrics import mean_squared_error
from test_cases.maze import Maze
from time import time
import numpy as np
from algorithms.Algorithm import Algorithm


class Metrics:

    def __init__(self):
        pass

    def evaluate_algorithm(self, algorithm: Algorithm, algorithm_name: str, plot_grid: Maze = None) -> None:
        time_start: float = time()
        best_path, best_lenght, convergence_iteration, all_lenghts = algorithm.optimize()
        time_end: float = time()
        duration: float = time_end - time_start

        print(f"Datos obtenidos en la evaluación de {algorithm_name}")
        print(
            f"Se llegó a la convergencia en la iteración: {convergence_iteration}")
        print(
            f"La mejor distancia hecha es de: {round(best_lenght, 2)} unidades")
        print(
            f"Promedio de distancia obtenidas: {round(np.mean(all_lenghts), 2)} unidades")
        print(f"Tiempo de ejecución del algoritmo: {round(duration, 2)}s")
        print(
            f"Desviación Éstandar: {round(np.std(all_lenghts), 2)} unidades\n")

        if plot_grid != None:
            plot_grid.best_path, plot_grid.best_length = best_path, best_lenght
            plot_grid.plot_maze(algorithm_name)
