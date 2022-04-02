import time
import cython
from libc.math cimport hypot
from libc.stdlib cimport rand, RAND_MAX


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cdef int sample(int num_samples):
    """
    Using pure C definitions.

    Genarate num_samples number of random points within a box defined in the
    range [-1, 1], and extract the amount of points that fall within the area
    of a unit circle.

    Args:
        num_samples (int): Number of samples to try.

    Returns:
        num_inside (int): Number of samples that fall within the unit circle.

    """
    cdef int num_inside = 0
    cdef double x, y
    for _ in range(num_samples):
        x = 2.0 * rand()/RAND_MAX - 1
        y = 2.0 * rand()/RAND_MAX - 1
        if hypot(x, y) <= 1:
            num_inside += 1
    return num_inside


def approximate_pi_cython(num_samples):

    start_time = time.time()
    num_inside = sample(num_samples)
    end_time = time.time()

    pi = (4.0 * num_inside) / num_samples

    print("Cython implementation:")
    print(f"\tpi ~= {round(pi, 6)}")
    print(f"\tElapsed time: {round(end_time-start_time, 4)} s", "\n")
