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

if __name__ == "__main__":
    main()