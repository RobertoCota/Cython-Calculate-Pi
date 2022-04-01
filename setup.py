from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True

ext=[
    Extension(
        name="src.cython.pi_cython", # location of the resulting .so
        sources=["src/cython/pi_cython.pyx"],
             ),
    ]

setup(packages=find_packages(),
      cmdclass = {'build_ext': build_ext},
      ext_modules = cythonize(ext, language_level="3"),
     )

# python setup.py build_ext --inplace
