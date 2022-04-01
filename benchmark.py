from src.python.pi_pure_python import approximate_pi_purepy
from src.numpy.pi_vectorize import approximate_pi_vectorized
from src.cython.pi_cython import approximate_pi_cython


def run_benchmark(nsamples):
    
    approximate_pi_purepy(nsamples)
    
    approximate_pi_vectorized(nsamples)

    approximate_pi_cython(nsamples)


if __name__ == "__main__":
    
    nsamples = 100_000
    
    run_benchmark(nsamples)
