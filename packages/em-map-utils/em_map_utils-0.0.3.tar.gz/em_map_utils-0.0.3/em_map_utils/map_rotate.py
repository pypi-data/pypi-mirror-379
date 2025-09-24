"""
map_rotate.py

:Author: Ardan Patwardhan
:Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
:Date: 30/07/2025
:Description:
    Rotate map.
"""

import argparse
import mrcfile
import numpy as np
from scipy import ndimage
from scipy.spatial.transform import Rotation as R
from .util import save_map

def map_rotate(map_grid,
               rotation,
               rotation_centre = None,
               initial_translation = None,
               cubify_if_needed = False,
               interpolation_order = 5,
               fill_value = 0,
               dtype = np.float32):
    """
    Rotate map.

    :param map_grid: Map to rotate.
    :param rotation: Rotation specified as a SciPy rotation object.
    :param rotation_centre: Centre of rotation, taken as the centre of the box if not specified.
    :param initial_translation: A translation that can be applied to the map prior to rotation.
    :param interpolation_order: Spline interpolation order.
    :param cubify_if_needed: If the map box is non-cubic, add padding
        and make it cubic to the largest dimension before rotating the
        map.
    :param fill_value: Value to use when interpolation points lie outside the box.
    :param dtype: Data type of returned map
    :return: Rotated map.
    """
    initial_translation = np.asarray(initial_translation) if initial_translation is not None  else np.array([0.,0.,0.])
    rotation_centre = np.asarray(rotation_centre) if rotation_centre is not None else  (np.asarray(np.shape(map_grid)) - 1.0) / 2.0

    inp_map_shape = np.asarray(np.shape(map_grid))

    # Check if the output map will have different dimensions to the input map
    if not ((inp_map_shape == inp_map_shape[0]).all()) and cubify_if_needed:
        max_dim = np.max(inp_map_shape)
        out_map_shape = np.full(3, max_dim)
        box_padding = 0.5 * (max_dim - inp_map_shape)
    else:
        out_map_shape = inp_map_shape
        box_padding = np.zeros(3)

    out_grid_size = np.prod(out_map_shape)
    out_grid_ranges = [range(x) for x in out_map_shape]
    out_coos_grid = np.mgrid[out_grid_ranges]

    # Reshape coos_grid to 1D array of coordinates
    out_coos_vec = np.asarray(out_coos_grid).reshape(3, out_grid_size)

    # Rotate the coordinates with the inverse to the angle provided
    rot_coos_vec = rotation.apply(out_coos_vec.T - rotation_centre - box_padding, inverse=True) + rotation_centre - initial_translation

    # Interpolate map values at the rotated coordinates
    rot_map_value_vec = ndimage.map_coordinates(map_grid, rot_coos_vec.T, order=interpolation_order, mode='constant', cval=fill_value).astype(dtype)

    # Reshape rotated map values to grid with the shape of map grid and return
    rot_map_grid = rot_map_value_vec.reshape(out_map_shape)
    return rot_map_grid

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rotate map. Note: Coordinate system is (i,j,k) going from the slowest to fastest varying axis. (i,j,k) map to (Z,Y,X) here. Note: In Chimera anti-clockwise angles appear clockwise')
    parser.add_argument('infile', metavar='FILE', type=str, help="Map file to rotate.")
    parser.add_argument("outfile", metavar='FILE', type=str, help="Rotated map.")
    parser.add_argument('rotation', metavar='RRR', type=float, nargs=3, help="Relative Euler angle in degrees using Z-Y\'-Z\" order and a right handed convention.")
    parser.add_argument('-c', '--rot_cen', metavar='XXX', type=float, nargs=3, help='Rotation centre. If none specified, will default to centre of box.')
    parser.add_argument('-t', '--translation', metavar='YYY', type=float, nargs=3, help='Optional initial translation prior to rotation.')
    parser.add_argument('-i', '--int_order', metavar='VAL', type=int, default=5, help='Spline interpolation order.')
    parser.add_argument('-f', '--fill_value', metavar='VAL', type=float, default=0.0, help='Map value to use when interpolated points lie outside the box.')
    parser.add_argument('--cubify', action='store_true', help="If a map is not cubic, pad it to the largest dimension before rotating.")
    args = parser.parse_args()

    # Note: In scipy the axis order is reversed (i,j,k) map to (x,y,z)
    rot = R.from_euler('XYX', args.rotation, degrees=True)

    with mrcfile.open(args.infile) as mrc:

        rot_map = map_rotate(mrc.data,
                             rotation = rot,
                             rotation_centre = args.rot_cen,
                             initial_translation = args.translation,
                             interpolation_order = args.int_order,
                             cubify_if_needed = args.cubify,
                             fill_value = args.fill_value)

        # Save rotated map to file
        save_map(args.outfile, rot_map, mrc)
