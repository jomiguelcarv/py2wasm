from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name="bsp_test",
    version="1.0.0",
    ext_modules=cythonize(Extension("bsp_test", ["bsp_test.py"])),
)