from test_cases.mazes import mazes
from algorithms.Enhanced_ACO import EnhancedACO as EACO
from algorithms.ACO import ACO
from test_cases.maze import Maze

def main():
    grid = mazes[4]
    algorithm = ACO(50, 150, grid.maze, grid.start, grid.goal)
    best_path, best_lenght, convergence_iteration = algorithm.ant_colony()
    grid.best_path, grid.best_length = best_path, best_lenght
    
    print(f"Se llegó a la convergencia en la iteración: {convergence_iteration}")
    print(f"La distancia hecha es de: {best_lenght} unidades")
    grid.plot_maze()
    

if __name__ == "__main__":
    main()