import vg
import time
import numpy as np


def sample(num_samples):
    points = np.random.uniform(low=-1.0, high=1.0, size=(num_samples, 2))
    num_inside = (vg.magnitude(points) <= 1.0).sum()
    return num_inside
    

def approximate_pi_vectorized(num_samples):
    
    start_time = time.time()
    num_inside = sample(num_samples)
    end_time = time.time()
    
    pi = (4*num_inside)/num_samples
    
    print("Numpy vector implementation:")
    print(f"pi ~= {round(pi, 6)}")
    print(f"Finished in: {round(end_time-start_time, 4)} s", "\n")
