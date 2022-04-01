import math
import time
import random


def sample(num_samples):
    num_inside = 0
    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if math.hypot(x, y) <= 1:
            num_inside += 1
    return num_inside


def approximate_pi_purepy(num_samples):
    
    start_time = time.time()
    num_inside = sample(num_samples)
    end_time = time.time()
    
    pi = (4*num_inside)/num_samples
    
    print("Pure python implementation:")
    print(f"pi ~= {round(pi, 6)}")
    print(f"Finished in: {round(end_time-start_time, 4)} s",  "\n")
