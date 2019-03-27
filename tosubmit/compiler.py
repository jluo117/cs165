from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('passwordCracker.pyx'))
