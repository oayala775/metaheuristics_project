from sklearn.metrics import mean_squared_error
# from skimage.metrics import peak_signal_noise_ratio
# from skimage.metrics import structural_similarity
from test_cases.maze import Maze
from time import time
import numpy as np

class Metrics:

    def __init__(self):
        pass

    def evaluate_algorithm(self, algorithm, algorithm_name: str, plot_grid: Maze = None) -> None:
        time_start: float = time()
        best_path, best_lenght, convergence_iteration, all_lenghts = algorithm.Start()
        time_end: float = time()
        duration: float = time_end - time_start

        print(f"Datos obtenidos en la evaluación de {algorithm_name}")
        print(f"Se llegó a la convergencia en la iteración: {convergence_iteration}")
        print(f"La mejor distancia hecha es de: {round(best_lenght, 2)} unidades")
        print(f"Promedio de distancia obtenidas: {round(np.mean(all_lenghts), 2)} unidades")
        print(f"Tiempo de ejecución del algoritmo: {round(duration, 2)}s")
        print(f"Desviación Éstandar: {round(np.std(all_lenghts), 2)} unidades\n")

        if plot_grid != None:
            plot_grid.best_path, plot_grid.best_length = best_path, best_lenght
            plot_grid.plot_maze()
    
    # def mse(self, true_solution, predicted_solution) -> float: 
        # return mean_squared_error(true_solution, predicted_solution)
    
    # def psnr(self, true_image:np.ndarray, test_image:np.ndarray) -> float:
        # return peak_signal_noise_ratio(true_image, test_image)
    # 
    # def ssim(self, true_image:np.ndarray, test_image:np.ndarray) -> float:
        # return structural_similarity(true_image, test_image)
    
    # def std(self):
    #     return np.std()

