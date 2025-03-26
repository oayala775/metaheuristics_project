import numpy as np

def euclidean_distance(position1: tuple[int,int], position2: tuple[int,int]) -> float:
    """
        Mide la distancia euclideana de un punto A a un punto B
    """
    return np.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)
