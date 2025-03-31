import numpy as np
import os
from time import time
import pandas as pd
import plotly.graph_objects as go
from algorithms.ABC import ArtificialBeeColony as ABC
from algorithms.ACO import ACO
from algorithms.Algorithm import Algorithm
from algorithms.Enhanced_ACO import EnhancedACO as EACO
from algorithms.PSO import PSO
from test_cases.maze import Maze
from test_cases.mazes import mazes


class Metrics:

    def __init__(self):
        self.__csv_path = "/home/someuserpc/Documents/metaheuristics_project/src/metrics/results/csv/metrics.csv"
        self.__table_path = "/home/someuserpc/Documents/metaheuristics_project/src/metrics/results/tables/"

    @property
    def csv_path(self) -> str:
        return self.__csv_path

    @csv_path.setter
    def csv_path(self, path: str):
        self.__csv_path = path

    @property
    def table_path(self) -> str:
        return self.__table_path

    @table_path.setter
    def table_path(self, path: str):
        self.__table_path = path

    def calculate_metrics(self, duration: float, last_iter: int, best_length: float, lengths: list[float], algo_name: str) -> str:
        result: str = algo_name + ','

        result += f"{round(duration, 2)},"
        result += f"{last_iter},"
        result += f"{round(best_length, 2)},"
        result += f"{round(np.mean(lengths), 2)},"
        result += f"{round(np.std(lengths), 2)},"
        return result

    def create_file(self, maze_number: int, results: str) -> None:

        header: str = "algorithm,execution_time,convergence,best_length,length_avg,std,maze_number\n"
        results += f"{maze_number}\n"

        if os.path.exists(self.csv_path):
            with open(self.csv_path, 'a+') as f:
                f.write(results)
        else:
            with open(self.csv_path, 'w+') as f:
                f.write(header)
                f.write(results)

    def create_tables(self):
        df: pd.DataFrame = pd.read_csv(self.csv_path)
        df.rename(columns={'algorithm': 'Nombre de algoritmo', 'execution_time': 'Tiempo de ejecución',
                           'convergence': 'Número de iteraciones',
                           'best_length': 'Mejor distancia', 'length_avg': 'Promedio de distancias',
                           'std': 'Desviación estándar de distancias', 'maze_number': 'Número de laberinto'}, inplace=True)
        for i in range(5):
            filename = f"maze_{i}_table.png"
            filename = os.path.join(self.table_path, filename)
            df_to_table = df[df["Número de laberinto"] == i]
            df_to_table.drop(columns=['Número de laberinto'], inplace=True)
            fig = go.Figure(data=[go.Table(
                header=dict(values=list(df_to_table.columns),
                            fill_color='darkturquoise',
                            align='center',
                            font=dict(weight='bold')),
                cells=dict(values=[df_to_table['Nombre de algoritmo'], df_to_table['Tiempo de ejecución'],
                                   df_to_table['Número de iteraciones'], df_to_table['Mejor distancia'],
                                   df_to_table['Promedio de distancias'], df_to_table['Desviación estándar de distancias']],
                           fill_color='aliceblue',
                           align='center'))
            ])
            fig.update_layout(height=(len(df_to_table) + 2)
                              * 30, margin=dict(l=10, r=10, t=10, b=10))
            fig.show()
            fig.write_image(filename)

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
                self.evaluate_algorithm(algo[0], algo[1], algo[2], algo[3])

        self.create_tables()
