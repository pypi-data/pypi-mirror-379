# em_map_utils
Python package for create and manipulating cryoEM maps in EMDB (mrc) map format.

## Features
* Calculate and align the principal axes of a structure.
* Calculate the lengths of a structure along the principal axes.
* Calculate the asphericity (shape) of a structure.
* Calculate line (1D) projections from a map.
* Threshold masked and unmasked maps.
* Rotate maps.
* Use multiprocessing to efficiently download multiple maps from EMDB.
* Generate synthetic maps containing a cuboid, cylinder or sphere.

## [API documentation](https://em-map-utils.readthedocs.io/en/latest/index.html)

## Installation
For multiprocessing to work on a Mac, set:
OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

in your .zshrc file or equivalent and source it.

## In development - prerelease version!
