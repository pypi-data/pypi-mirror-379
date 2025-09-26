from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension("mac_tdavec.tdavec_core", ["mac_tdavec/tdavec_core.pyx"],
              include_dirs=[numpy.get_include()])
]

setup(
    name="mac_tdavec",
    version="0.9.1",
    packages=["mac_tdavec"],
    ext_modules=cythonize(extensions),
    zip_safe=False,
    setup_requires=["Cython", "numpy"]
)
