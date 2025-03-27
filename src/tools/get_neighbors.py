import numpy as np

def get_neighbors(grid: np.ndarray, current_node: tuple) -> list[tuple]:
    """
        Obtiene los nodos permitidos donde se puede mover el algoritmo
    """
    neighbors: list = []
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        neighbor_x, neighbor_y = current_node[0] + x, current_node[1] + y
        if (0 <= neighbor_x < grid.shape[0] and 
            0 <= neighbor_y < grid.shape[1] and 
            grid[neighbor_x, neighbor_y] == 0):
            neighbors.append((neighbor_x, neighbor_y))
    return neighbors