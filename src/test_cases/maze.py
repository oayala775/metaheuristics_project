from algorithms.Enhanced_ACO import EnhancedACO
from algorithms.PSO import PSO

# from algorithms.PSO import generate_paths

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt 
import numpy as np


class Maze:
    def __init__(self, maze:np.ndarray, start: tuple, goal: tuple):
        """Start and goal tuples must be in (y,x) form, in order for the code to work properly"""
        self.cmap = ListedColormap(['white', 'black'])

        self.__maze = maze
        self.__start = start
        self.__goal = goal

        self.__ACO = EnhancedACO(maze, start, goal)
        self.__PSO = PSO(maze, start, goal)

        self.__best_path = None
        self.__best_length = None


        self.__x_length, self.__y_length = maze.shape

    @property
    def maze(self) -> np.ndarray:
        return self.__maze
    
    @maze.setter 
    def maze(self, maze:np.ndarray) -> None:
        self.__maze = maze

    @property
    def start(self) -> tuple:
        return self.__start
    
    @start.setter
    def start(self, start:tuple) -> None:
        self.__start = start
    
    @property
    def goal(self) -> tuple:
        return self.__goal

    @goal.setter
    def goal(self, goal:tuple) -> None:
        self.__goal = goal
    
    @property
    def best_path(self) -> list[tuple]:
        return self.__best_path
    
    @best_path.setter
    def best_path(self, path:list[tuple]) -> None:
        self.__best_path = path
    
    @property
    def best_length(self) -> float:
        return self.__best_length

    @best_length.setter
    def best_length(self, length:float) -> None:
        self.__best_length = length
    
    @property
    def x_length(self) -> int:
        return self.__x_length
    
    @x_length.setter
    def x_length(self, x_len:int) -> None:
        self.__x_length = x_len
    
    @property
    def y_length(self) -> int:
        return self.__y_length
    
    @y_length.setter
    def y_length(self, y_len:int) -> None:
        self.__y_length = y_len

    def use_ACO(self):
        path, length = self.__ACO.ant_colony()
        self.best_length = length
        self.best_path = path

    def use_PSO(self):
        path, length = self.__PSO.generate_paths()
        self.best_length = length
        self.best_path = path
    
    def plot_maze(self) -> None:
        if not self.best_length and not self.best_path:
            print("Best length or Best path are not defined")
            return
        
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.imshow(self.maze, cmap=self.cmap)

        # Configurar cuadrícula más fina
        ax.set_xticks(np.arange(-0.5, self.y_length, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, self.x_length, 1), minor=True)
        ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)
        ax.tick_params(which="minor", size=0)
        ax.tick_params(which="both", bottom=False, left=False, 
                    labelbottom=False, labelleft=False)
        
        if self.best_path:
            x = [pos[1] for pos in self.best_path]  # Columnas
            y = [pos[0] for pos in self.best_path]  # Filas

            ax.plot(x, y, color='red', linewidth=2, marker='o', markersize=4, label='Camino óptimo')
            ax.plot(self.goal[1],self.goal[0], marker='x', markersize=10, color='green', label='Objetivo')
            ax.plot(self.start[1],self.start[0], marker='o', markersize=10, color='blue', label='Inicio')
            ax.legend()

        plt.title(f"Laberinto {self.x_length}x{self.y_length} - Celdas Pequeñas")
        plt.tight_layout()  # Ajustar layout para que quede compacto
        plt.show()
