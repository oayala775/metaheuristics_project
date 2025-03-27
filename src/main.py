from test_cases.mazes import mazes
from algorithms.Enhanced_ACO import EnhancedACO
from algorithms.ACO import ACO
from test_cases.maze import Maze
# from algorithms.ACO import ACO

def main():
    grid = mazes[4]
    algorithm = ACO(50, 150, grid.maze, grid.start, grid.goal)
    best_path, best_lenght = algorithm.ant_colony()
    grid.best_path, grid.best_length = best_path, best_lenght
    grid.plot_maze()
    

if __name__ == "__main__":
    main()