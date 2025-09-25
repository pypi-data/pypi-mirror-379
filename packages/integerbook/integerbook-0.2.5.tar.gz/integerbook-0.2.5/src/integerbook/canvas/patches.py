from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np


def Parallelogram(left_bottom, left_top, right_bottom, right_top, alpha=1, facecolor='blue', hatch=None, shape='straight', zorder=0.5):

    left_bottom = np.array(left_bottom)
    left_top = np.array(left_top)
    right_bottom = np.array(right_bottom)
    right_top = np.array(right_top)

    delta_x = right_bottom[0] - left_bottom[0]
    delta_y = right_bottom[1] - left_bottom[1]
    if delta_x > 0:
        slope = delta_y / delta_x
    else:
        slope = 0

    v_dist = 0.0015
    v_dist = min(v_dist, left_top[1] - left_bottom[1])
    h_dist = 0.004
    h_dist = min(h_dist, right_bottom[0] - left_bottom[0])
    v_shift = np.array([0, v_dist])
    h_shift = np.array([h_dist, 0]) + np.array([0, h_dist * slope])
    v_shift_aux = 0.4 * v_shift
    h_shift_aux = 0.5 * h_shift

    if shape == 'rounded':
        path = rounded_path(left_bottom, left_top, right_bottom, right_top, v_shift, h_shift, v_shift_aux, h_shift_aux)
    elif shape == 'left_rounded':
        path = left_rounded_path(left_bottom, left_top, right_bottom, right_top, v_shift, h_shift, v_shift_aux, h_shift_aux)
    elif shape == 'right_rounded':
        path = right_rounded_path(left_bottom, left_top, right_bottom, right_top, v_shift, h_shift, v_shift_aux, h_shift_aux)
    elif shape == 'straight':
        path = straight_path(left_bottom, left_top, right_bottom, right_top, v_shift, h_shift, v_shift_aux, h_shift_aux)
    elif shape == 'squiggly':
        path = squiggly_path(left_bottom, left_top, right_bottom, right_top)
    else:
        print("undefined shape")
        return

    patch = patches.PathPatch(path, facecolor=facecolor, alpha=alpha, hatch=hatch, lw=0, zorder=zorder)
    return patch


def rounded_path(left_bottom, left_top, right_bottom, right_top, v_shift, h_shift, v_shift_aux, h_shift_aux):
    vertsBase = [left_bottom + v_shift,
                 left_top - v_shift,
                 left_top - v_shift_aux,
                 left_top + h_shift_aux,
                 left_top + h_shift,
                 right_top - h_shift,
                 right_top - h_shift_aux,
                 right_top - v_shift_aux,
                 right_top - v_shift,
                 right_bottom + v_shift,
                 right_bottom + v_shift_aux,
                 right_bottom - h_shift_aux,
                 right_bottom - h_shift,
                 left_bottom + h_shift,
                 left_bottom + h_shift_aux,
                 left_bottom + v_shift_aux,
                 left_bottom + v_shift
                 ]

    verts = [(point[0], point[1]) for point in vertsBase]

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.CURVE4,
             Path.CURVE4,
             Path.CURVE4,
             Path.LINETO,
             Path.CURVE4,
             Path.CURVE4,
             Path.CURVE4,
             Path.LINETO,
             Path.CURVE4,
             Path.CURVE4,
             Path.CURVE4,
             Path.LINETO,
             Path.CURVE4,
             Path.CURVE4,
             Path.CURVE4]

    path = Path(verts, codes)
    return path

def left_rounded_path(left_bottom, left_top, right_bottom, right_top, v_shift, h_shift, v_shift_aux, h_shift_aux):
    vertsBase = [left_bottom + v_shift,
                 left_top - v_shift,
                 left_top - v_shift_aux,
                 left_top + h_shift_aux,
                 left_top + h_shift,
                 right_top,
                 right_bottom,
                 left_bottom + h_shift,
                 left_bottom + h_shift_aux,
                 left_bottom + v_shift_aux,
                 left_bottom + v_shift
                 ]

    verts = [(point[0], point[1]) for point in vertsBase]

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.CURVE4,
             Path.CURVE4,
             Path.CURVE4,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.CURVE4,
             Path.CURVE4,
             Path.CURVE4]

    path = Path(verts, codes)
    return path

def right_rounded_path(left_bottom, left_top, right_bottom, right_top, v_shift, h_shift, v_shift_aux, h_shift_aux):

    vertsBase = [left_bottom,
                 left_top,
                 right_top - h_shift,
                 right_top - h_shift_aux,
                 right_top - v_shift_aux,
                 right_top - v_shift,
                 right_bottom + v_shift,
                 right_bottom + v_shift_aux,
                 right_bottom - h_shift_aux,
                 right_bottom - h_shift,
                 left_bottom
                 ]

    verts = [(point[0], point[1]) for point in vertsBase]

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.CURVE4,
             Path.CURVE4,
             Path.CURVE4,
             Path.LINETO,
             Path.CURVE4,
             Path.CURVE4,
             Path.CURVE4,
             Path.LINETO,
             ]

    path = Path(verts, codes)
    return path

def straight_path(left_bottom, left_top, right_bottom, right_top, v_shift, h_shift, v_shift_aux, h_shift_aux ):

    vertsBase = [left_bottom,
                 left_top,
                 right_top,
                 right_bottom,
                 left_bottom
                 ]

    verts = [(point[0], point[1]) for point in vertsBase]

    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             ]

    path = Path(verts, codes)
    return path

def squiggly_path(left_bottom, left_top, right_bottom, right_top):
    num_squiggles = 20
    amplitude = .15 * (left_top[1] - left_bottom[1])

    # squiggle params
    width_corner_squiggle_relative = 0.4
    relative_distance_aux_squiggle = 0.3

    # corner params
    v_dist = 0.001
    h_dist = 0.001
    v_relative_distance_aux = 0.4
    h_relative_distance_aux = 0.5

    parity_num_squiggles = (-1) ** (num_squiggles % 2)
    length_squiggle = (right_bottom[0] - left_bottom[0]) / num_squiggles
    length_half_squiggle = length_squiggle / 2
    slope = amplitude / length_half_squiggle

    width_corner_squiggle = width_corner_squiggle_relative * length_squiggle

    amplitude = np.array([0, amplitude])

    v_dist = min(v_dist, left_top[1] - left_bottom[1])
    h_dist = min(h_dist, right_bottom[0] - left_bottom[0])
    v_shift = np.array([0, v_dist])
    h_shift_corner = np.array([h_dist, 0])
    h_shift_corner_vertical = np.array([0, h_dist * slope])
    v_shift_aux = v_relative_distance_aux * v_shift
    h_shift_corner_aux = h_relative_distance_aux * h_shift_corner
    h_shift_corner_aux_vertical = h_relative_distance_aux * h_shift_corner_vertical

    verts_base_1 = [left_bottom + v_shift,
                  left_top - v_shift,
                  left_top - v_shift_aux,
                  left_top + h_shift_corner_aux + h_shift_corner_aux_vertical,
                  left_top + h_shift_corner + h_shift_corner_vertical]

    verts_base_2 = verts_base_part(left_top, num_squiggles, length_half_squiggle, amplitude, width_corner_squiggle, slope, relative_distance_aux_squiggle)

    verts_base_3 = [right_top - h_shift_corner - parity_num_squiggles * h_shift_corner_vertical,
                  right_top - h_shift_corner_aux - parity_num_squiggles * h_shift_corner_aux_vertical,
                  right_top - v_shift_aux,
                  right_top - v_shift,
                  right_bottom + v_shift,
                  right_bottom + v_shift_aux,
                  right_bottom - h_shift_corner_aux - parity_num_squiggles * h_shift_corner_aux_vertical,
                  right_bottom - h_shift_corner - parity_num_squiggles * h_shift_corner_vertical]

    verts_base_4 = verts_base_part(left_bottom, num_squiggles, length_half_squiggle, amplitude, width_corner_squiggle, slope, relative_distance_aux_squiggle, invert=True)

    verts_base_5 = [left_bottom + h_shift_corner + h_shift_corner_vertical,
                  left_bottom + h_shift_corner_aux + h_shift_corner_aux_vertical,
                  left_bottom + v_shift_aux,
                  left_bottom + v_shift
                  ]

    verts_base = verts_base_1 + verts_base_2 + verts_base_3 + verts_base_4 + verts_base_5

    verts = [(point[0], point[1]) for point in verts_base]

    codes1 = [Path.MOVETO,
              Path.LINETO,
              Path.CURVE4,
              Path.CURVE4,
              Path.CURVE4]

    codes2 = num_squiggles * [Path.LINETO,
                             Path.CURVE4,
                             Path.CURVE4,
                             Path.CURVE4]

    codes3 = [Path.LINETO,
              Path.CURVE4,
              Path.CURVE4,
              Path.CURVE4,
              Path.LINETO,
              Path.CURVE4,
              Path.CURVE4,
              Path.CURVE4]

    codes4 = num_squiggles * [Path.LINETO,
                             Path.CURVE4,
                             Path.CURVE4,
                             Path.CURVE4]

    codes5 = [Path.LINETO,
              Path.CURVE4,
              Path.CURVE4,
              Path.CURVE4]

    codes = codes1 + codes2 + codes3 + codes4 + codes5

    path = Path(verts, codes)

    return path


def verts_base_part(left_corner, num_squiggles, length_half_squiggle, amplitude, width_corner_squiggle, slope, relative_distance_aux_squiggle, invert=False):
    h_shift_squiggle = np.array([width_corner_squiggle / 2, 0])
    v_shift_squiggle = np.array([0, slope * h_shift_squiggle[0]])
    h_shift_squiggle_aux = relative_distance_aux_squiggle * h_shift_squiggle
    v_shift_squiggle_aux = np.array([0, slope * h_shift_squiggle_aux[0]])

    verts_base_part = []
    for i in range(num_squiggles):
        h_shift = np.array([(2 * i + 1) * length_half_squiggle, 0])
        is_top = (-1)**(i % 2)
        a = [left_corner + is_top * amplitude + h_shift - h_shift_squiggle - is_top * v_shift_squiggle,
             left_corner + is_top * amplitude + h_shift - h_shift_squiggle_aux - is_top * v_shift_squiggle_aux,
             left_corner + is_top * amplitude + h_shift + h_shift_squiggle_aux - is_top * v_shift_squiggle_aux,
             left_corner + is_top * amplitude + h_shift + h_shift_squiggle - is_top * v_shift_squiggle]
        verts_base_part += a
    if invert:
        verts_base_part = list(reversed(verts_base_part))
    return verts_base_part

