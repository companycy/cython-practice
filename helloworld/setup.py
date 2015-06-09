from distutils.core import setup
from Cython.Build import cythonize

# python setup.py build_ext --inplace
# >>> import helloworld
# >>> helloworld.addtest(1,2)
# >>> helloworld.fib(2000)

setup(
    ext_modules = cythonize("helloworld.pyx")
)
