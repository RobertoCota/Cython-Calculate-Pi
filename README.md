# Cython-Calculate-Pi

A benchmark between pure python, numpy and C-level python (Cython)


### To install

To intall the required libraries run the following command: `pip install -r requirements.txt`

### To compile 

In order for changes in the Cython script `*.pyx` file to take place, run the following command: `python setup.py build_ext --inplace`

### To run the benchmark engine

Run the `benchmarck.py` script. The number of samples to try can changed by changing the number in line 33.

# The algorithm

In order to calculate the value of <img src="https://render.githubusercontent.com/render/math?math={\large \pi}"> one can consider a unit circle embeded in a box delimited by <img src="https://render.githubusercontent.com/render/math?math={\large [-1, 1]}">. Therefore, one can establish the following relations:

<img src="https://render.githubusercontent.com/render/math?math={\Large A_{\text{square}}=4 r^2} \quad \text{and} \quad {\Large  A_{\text{circle}}=\pi r^2}">

which are the area of the unit square and the area of the unit circle respectively, which can combine to estimate the value of <img src="https://render.githubusercontent.com/render/math?math={\large \pi}"> as:

<img src="https://render.githubusercontent.com/render/math?math={\Large \pi = {4 \cdot A_{\text{circle}}} / {A_{\text{square}}}}">.

One can use a Monte Carlo approach to calculate both the area of the circle and the area of the square. While the area of the square can be calculated by N points (2D vectors) defined as <img src="https://render.githubusercontent.com/render/math?math={\large s_i = (x_i, y_i)}"> with <img src="https://render.githubusercontent.com/render/math?math={\large x_i}"> and <img src="https://render.githubusercontent.com/render/math?math={\large y_i}"> with values within the range of <img src="https://render.githubusercontent.com/render/math?math={\large [-1, 1]}">, the area of the circle is defined by the amount of samples that satisfy <img src="https://render.githubusercontent.com/render/math?math={\large x_i^2 \+ y_i^2 \leq 1}">.