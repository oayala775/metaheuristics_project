from test_cases.mazes import mazes
from algorithms.Enhanced_ACO import EnhancedACO
from algorithms.ACO import ACO
from test_cases.maze import Maze
from algorithms.ABC import ArtificialBeeColony as ABC
# from algorithms.ACO import ACO

def main():
    grid = mazes[0]
    algorithm = ABC(grid.maze, grid.start, grid.goal)
    best_path, best_lenght = algorithm.optimize()
    grid.best_path, grid.best_length = best_path, best_lenght
    grid.plot_maze()
    

if __name__ == "__main__":
    main()