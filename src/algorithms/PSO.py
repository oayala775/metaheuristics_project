import numpy as np
import random
from collections import defaultdict
from algorithms.Algorithm import Algorithm


class Particle(Algorithm):
    def __init__(self, maze, start, goal, max_path_length):
        super().__init__(maze, start, goal)
        self.max_path_length = max_path_length
        self.path = self.generate_smart_path()
        self.best_path = self.path.copy()
        self.best_value = self.evaluate_path(self.path)
        self.velocity = np.random.uniform(-2, 2, max_path_length * 2)

    def generate_smart_path(self):
        """Genera camino aleatorio pero válido"""
        path = [self.start]
        current = self.start

        for _ in range(self.max_path_length-1):
            if current == self.goal:
                break

            neighbors = self.get_neighbors(current)
            if not neighbors:
                break

            if random.random() < 0.5:
                next_pos = min(neighbors, key=lambda p: (
                    abs(p[0]-self.goal[0]) + abs(p[1]-self.goal[1])))
            else:
                next_pos = random.choice(neighbors)

            path.append(next_pos)
            current = next_pos

        return path

    def evaluate_path(self, path):
        """Función de evaluación simplificada"""
        if not path:
            return float('inf')

        last_pos = path[-1]

        if last_pos == self.goal:
            return len(path)  # Usamos longitud como criterio

        return abs(last_pos[0]-self.goal[0]) + abs(last_pos[1]-self.goal[1])

    def update_velocity(self, global_best_path, w=0.6, c1=0.8, c2=0.8):
        current_vec = self.path_to_fixed_vector(self.path)
        personal_best_vec = self.path_to_fixed_vector(self.best_path)
        global_best_vec = self.path_to_fixed_vector(global_best_path)

        inertia = w * self.velocity
        cognitive = c1 * random.random() * (personal_best_vec - current_vec)
        social = c2 * random.random() * (global_best_vec - current_vec)

        self.velocity = inertia + cognitive + social
        self.velocity = np.clip(self.velocity, -3, 3)

    def path_to_fixed_vector(self, path):
        vec = np.zeros(self.max_path_length * 2)
        for i in range(min(len(path), self.max_path_length)):
            vec[i*2] = path[i][0]
            vec[i*2+1] = path[i][1]
        return vec

    def update_position(self):
        """Actualiza posición asegurando que siempre sea válida"""
        displacements = np.round(self.velocity).astype(int)
        new_path = [self.start]
        current = self.start

        for i in range(0, len(displacements), 2):
            if len(new_path) >= self.max_path_length:
                break

            dx, dy = displacements[i], displacements[i+1]
            new_pos = (current[0] + dx, current[1] + dy)

            if self.is_valid_position(new_pos):
                current = new_pos
                new_path.append(current)
                if current == self.goal:
                    break
            else:
                neighbors = self.get_neighbors(current)
                if neighbors:
                    current = random.choice(neighbors)
                    new_path.append(current)
                    if current == self.goal:
                        break
                else:
                    break

        self.path = new_path
        current_value = self.evaluate_path(new_path)

        if current_value <= self.best_value:
            self.best_value = current_value
            self.best_path = new_path.copy()

    def is_valid_position(self, pos):
        return (0 <= pos[0] < self.maze.shape[0] and
                0 <= pos[1] < self.maze.shape[1] and
                self.maze[pos] == 0)


class PSO(Algorithm):

    def __init__(self, grid: np.ndarray, start: tuple, goal: tuple):
        super().__init__(grid, start, goal)

        self.num_paths = 100
        self.max_path_length = 100

    def optimize(self):
        """Genera caminos válidos y retorna el mejor camino y su longitud"""
        paths = []
        lengths = []
        attempts = 0
        convergence_iteration = None
        max_attempts = self.num_paths * 10

        while len(paths) < self.num_paths and attempts < max_attempts:
            attempts += 1
            p = Particle(self.grid, self.start,
                         self.goal, self.max_path_length)
            if p.path[-1] == self.goal:
                path_tuple = tuple(p.path)
                unique = True
                for existing in paths:
                    if tuple(existing) == path_tuple:
                        unique = False
                        break
                if unique:
                    paths.append(p.path)
                    lengths.append(len(p.path))

                    # Si es el primer camino válido, registramos la iteración de convergencia
                    if convergence_iteration is None:
                        convergence_iteration = attempts

        if paths:
            optimal_path = min(paths, key=lambda x: len(x))
            return optimal_path, len(optimal_path), convergence_iteration, lengths
        else:
            return None, 0
