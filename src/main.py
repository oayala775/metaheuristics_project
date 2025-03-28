from test_cases.mazes import mazes
from algorithms.Enhanced_ACO import EnhancedACO as EACO
from algorithms.ACO import ACO
from metrics.metrics import Metrics
from algorithms.PSO import PSO



def main():
    grid = mazes[1]
    metrics = Metrics()
    algorithms = [
        (ACO(grid.maze, grid.start, grid.goal), "ACO"),
        (EACO(grid.maze, grid.start, grid.goal), "EACO"), 
        (PSO(grid.maze, grid.start, grid.goal), "PSO")
    ]

    for algorithm in algorithms:
        metrics.evaluate_algorithm(algorithm[0], algorithm[1], grid)        
    
    #algorithm = ABC(grid.maze, grid.start, grid.goal)
    #best_path, best_lenght = algorithm.optimize()
    #algorithm = ABC(grid.maze, grid.start, grid.goal)
    #best_path, best_lenght = algorithm.optimize()
    #grid = mazes[4]
    # algorithm = ACO(50, 150, grid.maze, grid.start, grid.goal)



    """algorithm = PSO(grid.maze, grid.start, grid.goal)
    best_path, best_lenght = algorithm.Start()
    grid.best_path, grid.best_length = best_path, best_lenght
    print(grid.best_path, grid.best_length)
    grid.plot_maze()"""

if __name__ == "__main__":
    main()