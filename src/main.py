from test_cases.mazes import mazes
from algorithms.Enhanced_ACO import EnhancedACO
# from algorithms.ACO import ACO

def main():
    grid = mazes[4]
    algorithm = EnhancedACO(50, 150, grid.maze, grid.start, grid.goal)
    # algorithm = ACO(50, 150, grid.maze, grid.start, grid.goal)
    best_path, best_lenght = algorithm.ant_colony()

    grid.plot_maze(best_path)
    

if __name__ == "__main__":
    main()