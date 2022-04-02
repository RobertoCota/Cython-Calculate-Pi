from src.python.pi_pure_python import approximate_pi_purepy
from src.numpy.pi_vectorize import approximate_pi_vectorized
from src.cython.pi_cython import approximate_pi_cython


def run_benchmark(nsamples: int):
    """
    Run the three different algo approaches to calculate the value of pi,
    print each of the results and the time that it took to each method to
    compute the result.

    Args:
        nsamples (int): The number of random samples that would help to
            calculate the value of pi.

    Returns:
        None.

    """

    print(f"\nNumber of samples: {nsamples}\n")

    approximate_pi_purepy(nsamples)

    approximate_pi_vectorized(nsamples)

    approximate_pi_cython(nsamples)


if __name__ == "__main__":

    # Define the numbers of random samples to create
    nsamples = 5_000_000

    run_benchmark(nsamples)
