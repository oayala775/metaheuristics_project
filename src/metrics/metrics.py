from sklearn.metrics import mean_squared_error
from skimage.metrics import peak_signal_noise_ratio
from skimage.metrics import structural_similarity
import numpy as np


class Metrics:

    def __init__(self):
        pass

    def mse(self, true_solution, predicted_solution) -> float: 
        return mean_squared_error(true_solution, predicted_solution)
    
    def psnr(self, true_image:np.ndarray, test_image:np.ndarray) -> float:
        return peak_signal_noise_ratio(true_image, test_image)
    
    def ssim(self, true_image:np.ndarray, test_image:np.ndarray) -> float:
        return structural_similarity(true_image, test_image)
    
    # def std(self):
    #     return np.std()

