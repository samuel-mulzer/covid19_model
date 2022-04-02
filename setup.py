from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension('covid19_model.models.models', ['covid19_model/models/models.pyx'], include_dirs=[numpy.get_include()]),
    Extension('covid19_model.solver.solver', ['covid19_model/solver/solver.pyx'], include_dirs=[numpy.get_include()])
]

setup(
    name='covid19_model',
    version='1.0',
    description='A package including several compartmental models, that are solved and visualized based on real data',
    author='Samuel Mulzer',
    author_email='samuel.mulzer@icloud.com',
    packages=['covid19_model','covid19_model.models','covid19_model.solver','covid19_model.visualizer'],
    ext_modules = cythonize(extensions, language_level = "3")
)