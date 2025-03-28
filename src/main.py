from test_cases.mazes import mazes
from algorithms.Enhanced_ACO import EnhancedACO as EACO
from algorithms.ACO import ACO
from metrics.metrics import Metrics

def main():
    grid = mazes[2]
    metrics = Metrics()
    algorithms = [
        (ACO(grid.maze, grid.start, grid.goal), "ACO"),
        (EACO(grid.maze, grid.start, grid.goal), "EACO"), 
    ]

    for algorithm in algorithms:
        metrics.evaluate_algorithm(algorithm[0], algorithm[1], grid)

    # best_path, best_lenght, convergence_iteration = algorithm.Start()
    # grid.best_path, grid.best_length = best_path, best_lenght
    
    # print(f"Se llegó a la convergencia en la iteración: {convergence_iteration}")
    # print(f"La distancia hecha es de: {best_lenght} unidades")
    # grid.plot_maze()

# from test_cases.maze import Maze
# from algorithms.ABC import ArtificialBeeColony as ABC
# from algorithms.ACO import ACO
# 
# def main():
    # grid = mazes[0]
    # algorithm = ABC(grid.maze, grid.start, grid.goal)
    # best_path, best_lenght = algorithm.optimize()
    # grid.best_path, grid.best_length = best_path, best_lenght
    # grid.plot_maze()
    

if __name__ == "__main__":
    main()