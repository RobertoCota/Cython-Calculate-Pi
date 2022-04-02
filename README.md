# Cython-Calculate-Pi

A benchmark between pure python, numpy and C-level python (Cython)


### To install

To intall the required libraries run the following command: `pip install -r requirements.txt`

### To compile 

In order for changes in the Cython script `*.pyx` file to take place, run the following command: `python setup.py build_ext --inplace`

### To run the benchmark engine

Run the `benchmarck.py` script. The number of samples to try can changed by changing the number in line 33.

# The algorithm

In order to calculate the value of pi one can consider a unit circle embeded in a box delimited by `[-1, 1]`. Therefore, one can establisg the following relations:

<img src="https://render.githubusercontent.com/render/math?math={\Large A_{\text{square}}=4 r^2} \quad \text{and} \quad {\Large  A_{\text{circle}}=\pi r^2}">

which are the area of the unit square and the area of the unit circle respectively.