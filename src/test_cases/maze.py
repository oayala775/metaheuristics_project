from algorithms.Enhanced_ACO import EnhancedACO
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt 
import numpy as np


class Maze:
    def __init__(self, maze, start, goal):
        self.cmap = ListedColormap(['white', 'black'])

        self.__maze = maze
        self.__start = start
        self.__goal = goal

        self.__ACO = EnhancedACO(100, 100, maze, start, goal)
        self.__best_path = None
        self.__best_length = None
    
    def set_maze(self, maze):
        self.__maze = maze
    
    def get_maze(self):
        return self.__maze

    def set_start(self, start):
        self.__start = start
    
    def get_start(self):
        return self.__start

    def set_goal(self, goal):
        self.__goal = goal
    
    def get_goal(self, ):
        return self.__goal
    
    def set_best_path(self, path):
        self.__best_path = path
    
    def get_best_path(self):
        return self.__best_path

    def set_best_length(self, length):
        self.__best_length = length
    
    def get_best_length(self):
        return self.__best_length
    
    def use_ACO(self):
        path, lenght = self.__ACO.ant_colony()
        self.set_best_length(lenght)
        self.set_best_path(path)
    
    def plot_maze(self):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.imshow(self.get_maze(), cmap=self.cmap)

        # Configurar cuadrícula más fina
        ax.set_xticks(np.arange(-0.5, 50, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, 20, 1), minor=True)
        ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)
        ax.tick_params(which="minor", size=0)
        ax.tick_params(which="both", bottom=False, left=False, 
                    labelbottom=False, labelleft=False)
        
        if self.get_best_path():
            x = [pos[1] for pos in self.get_best_path()]  # Columnas
            y = [pos[0] for pos in self.get_best_path()]  # Filas
            ax.plot(x, y, color='red', linewidth=2, marker='o', markersize=4, label='Camino óptimo')
            ax.legend()

        plt.title("Laberinto 20x20 - Celdas Pequeñas")
        plt.tight_layout()  # Ajustar layout para que quede compacto
        plt.show()
