import cython
from libc.math cimport hypot
from libc.stdlib cimport rand, RAND_MAX
from libc.stdio cimport printf
from libc.time cimport clock, CLOCKS_PER_SEC


@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
cdef int sample(int num_samples):
    cdef int num_inside = 0
    cdef double x, y
    for _ in range(num_samples):
        x = 2.0 * rand()/RAND_MAX - 1
        y = 2.0 * rand()/RAND_MAX - 1
        if hypot(x, y) <= 1:
            num_inside += 1
    return num_inside


@cython.cdivision(True)
def approximate_pi_cython(int num_samples):

    cdef double start_time = clock()
    cdef int num_inside = sample(num_samples)
    cdef double end_time = clock()
    
    cdef double pi = (4.0 * num_inside) / num_samples
    
    printf("Cython implementation:\n")
    printf("pi ~= %.6f\n", pi)
    printf("Finished in: %.4f s\n", (end_time - start_time) / CLOCKS_PER_SEC)
