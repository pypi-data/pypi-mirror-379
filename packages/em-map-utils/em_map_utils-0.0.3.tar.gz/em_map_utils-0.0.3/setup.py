from pathlib import Path
from setuptools import setup

# read the contents of your README file

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='em_map_utils',
    version='0.0.3',
    packages=['em_map_utils', 'em_map_utils.demos'],
    url='https://github.com/ardanpat/em-map-utils.git',
    license='Apache License 2.0',
    author='Ardan Patwardhan',
    author_email='ardan@ebi.ac.uk',
    description='Python package for creating and manipulating cryoEM maps in EMDB (mrc) map format.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Image Processing',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    keywords=[
        '3D',
        'CCP4 format',
        'EMDB',
        'EMDB format',
        'MRC format',
        'asphericity',
        'contour',
        'covariance',
        'cryo EM',
        'cryo electron microscopy',
        'cuboid',
        'cylinder',
        'download map',
        'electron cryo microscopy',
        'electron microscopy data bank'
        'electron microscopy',
        'line projection',
        'map',
        'map alignment',
        'map principal axes',
        'multiprocessing'
        'rotate',
        'sphere',
        'structure shape',
        'structure size',
        'structure',
        'threshold',
        'volume',
    ]
)
