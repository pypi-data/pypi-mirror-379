from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.patches import PathPatch

import numpy as np

def verticesSegno():
    vertices = np.array([[7.04181487e-01, 2.42229208e-01],
       [7.04181487e-01, 1.77206670e-01],
       [6.83102518e-01, 1.21114619e-01],
       [6.40944580e-01, 7.39546126e-02],
       [5.96642921e-01, 2.46510397e-02],
       [5.42337746e-01, 3.11112602e-08],
       [4.78029055e-01, 3.11112602e-08],
       [4.34442022e-01, 3.11112602e-08],
       [3.95142275e-01, 1.32223176e-02],
       [3.60129816e-01, 3.96575571e-02],
       [3.22259165e-01, 6.82379182e-02],
       [3.03323762e-01, 1.03608312e-01],
       [3.03323762e-01, 1.45767184e-01],
       [3.03323762e-01, 2.01501454e-01],
       [3.39050847e-01, 2.29367812e-01],
       [4.10505016e-01, 2.29367812e-01],
       [4.39801092e-01, 2.29367812e-01],
       [4.59808278e-01, 2.11503725e-01],
       [4.70526419e-01, 1.75777107e-01],
       [4.86960788e-01, 1.20042836e-01],
       [5.04824408e-01, 9.21764789e-02],
       [5.24116968e-01, 9.21764789e-02],
       [5.74849481e-01, 9.21764789e-02],
       [6.00215738e-01, 1.22186402e-01],
       [6.00215738e-01, 1.82207805e-01],
       [6.00215738e-01, 4.10443136e-01],
       [2.78882910e-02, 3.84547677e-01],
       [1.08889418e-06, 7.55627257e-01],
       [1.08889418e-06, 8.19221788e-01],
       [2.10800580e-02, 8.75670063e-01],
       [6.32379961e-02, 9.24973636e-01],
       [1.05395934e-01, 9.74991212e-01],
       [1.57557388e-01, 1.00000000e+00],
       [2.19722512e-01, 1.00000000e+00],
       [2.67596678e-01, 1.00000000e+00],
       [3.09040146e-01, 9.87851052e-01],
       [3.44052605e-01, 9.63559379e-01],
       [3.83352351e-01, 9.35691465e-01],
       [4.03002224e-01, 8.98893064e-01],
       [4.03002224e-01, 8.53162620e-01],
       [4.03002224e-01, 8.29581839e-01],
       [3.93713957e-01, 8.09217962e-01],
       [3.75135245e-01, 7.92069434e-01],
       [3.57271624e-01, 7.75634910e-01],
       [3.36192655e-01, 7.67416870e-01],
       [3.11898337e-01, 7.67416870e-01],
       [2.71169495e-01, 7.67416870e-01],
       [2.42945047e-01, 7.90639872e-01],
       [2.27225148e-01, 8.37084320e-01],
       [2.12220186e-01, 8.84244327e-01],
       [1.93998942e-01, 9.07825108e-01],
       [1.72562816e-01, 9.07825108e-01],
       [1.53270256e-01, 9.07825108e-01],
       [1.37193044e-01, 8.97822837e-01],
       [1.24331182e-01, 8.77813629e-01],
       [1.11469786e-01, 8.58521535e-01],
       [1.05038621e-01, 8.38513882e-01],
       [1.05038621e-01, 8.17792226e-01],
       [1.05038621e-01, 5.91753350e-01],
       [6.78084894e-01, 6.16279914e-01],
       [7.04181487e-01, 2.42229208e-01],
       [7.04181487e-01, 2.42229208e-01],
       [7.04181487e-01, 2.42229208e-01]])
    return vertices

def Segno(xPos, yPos, height, xyRatio, color):

    vertices = verticesSegno()

    vertices *= height
    vertices *= np.array([1/xyRatio, 1])

    vertices += [xPos, yPos]

    codes = [ 1,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,
        4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,
        4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,
        4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  2, 79]

    path = Path(vertices, codes)

    patch1 = patches.PathPatch(path, facecolor=color, linewidth=0)

    xPosEnd = vertices[:,0].max()
    widthSegno = xPosEnd - xPos
    widthLine = widthSegno * 0.1
    corners = [(xPos, yPos),
               (xPosEnd - widthLine, yPos + height),
               (xPosEnd, yPos + height),
               (xPos + widthLine, yPos)]
    patch2 = patches.Polygon(corners, fill=True, color=color, linewidth=0)
    radiusX = widthSegno * 0.1
    radiusY = radiusX * xyRatio
    offsetYCircle = 2 * radiusY
    patch3 = patches.Ellipse((xPos + radiusX, yPos + .5 * height - offsetYCircle), width=2 * radiusX, height= 2 * radiusY,
                             color=color, linewidth=0)
    patch4 = patches.Ellipse((xPos + widthSegno - radiusX, yPos + .5 * height + offsetYCircle), width=2 * radiusX, height=2 * radiusY,
                             color=color, linewidth=0)

    return [patch1, patch2, patch3, patch4]

def relativeWidthSegno():
    return verticesSegno()[:,0].max()

def Coda(xPos, yPos, height, width, xyRatio, color):

    diameterOuterY = height * .75
    diameterInnerY = 0.9 * diameterOuterY

    diameterOuterX = width * .7
    diameterInnerX = 0.5 * diameterOuterX

    xCenter = xPos + width / 2
    yCenter = yPos + height / 2
    center = (xCenter, yCenter)

    patch1 = _DoughnutEllipseFlexible(center, diameterOuterX / 2, diameterOuterY / 2, diameterInnerX / 2,
                                      diameterInnerY / 2, colorText=color)

    linewidthY = 0.06 * height
    linewidthX = linewidthY / xyRatio

    # patch1 = patches.Ellipse((xCenter, yCenter), width=diameterOuterX,
    #                  height=diameterOuterY, color='black', linewidth=0)
    # patch2 = patches.Ellipse((xCenter, yCenter), width=diameterInnerX,
    #                  height=diameterInnerY, color='white', linewidth=0)

    patch3 = patches.Rectangle((xPos, yPos + .5 * height - 0.5 * linewidthY), width=width, height=linewidthY, fill=True,
                       color=color, linewidth=0)
    patch4 = patches.Rectangle((xPos + .5 * width - 0.5 * linewidthX, yPos), width=linewidthX, height=height, fill=True,
                       color=color, linewidth=0)

    return [patch1, patch3, patch4]


def Doughnut(xPos, yPos, height, xyRatio, colorText='black'):
    width = height / xyRatio
    radiusX = width / 2
    radiusY = height / 2
    center = (xPos + radiusX, yPos + radiusY)

    linewidth = 0.1 * height

    return DoughnutEllipse(center, radiusX, radiusY, linewidth, xyRatio, colorText=colorText)

def DoughnutEllipse(center, radiusX, radiusY, linewidth, xyRatio, colorText='black'):
    radiusXInner = radiusX -  linewidth / xyRatio
    radiusYInner = radiusY -  linewidth
    return _DoughnutEllipseFlexible(center, radiusX, radiusY, radiusXInner, radiusYInner, colorText=colorText)


def _DoughnutEllipseFlexible(center, radiusXOuter, radiusYOuter, radiusXInner, radiusYInner, colorText='black'):

    ellipseOuterV = _makeEllipse(center, radiusXOuter, radiusYOuter)
    ellipseInnerV = _makeEllipse(center, radiusXInner, radiusYInner)

    ellipseOuterC = [Path.LINETO for p in ellipseOuterV]
    ellipseOuterC[0] = Path.MOVETO
    ellipseInnerC = [Path.LINETO for p in ellipseInnerV]
    ellipseInnerC[0] = Path.MOVETO

    vertices = []
    vertices.extend(ellipseOuterV)
    vertices.extend(ellipseInnerV[::-1])

    codes = []
    codes.extend(ellipseOuterC)
    codes.extend(ellipseInnerC)

    path = Path(vertices, codes)
    patch = PathPatch(path, facecolor=colorText, linewidth=0)
    return patch

def _makeEllipse(center, radiusX, radiusY):
    phi = np.linspace(0, 2 * np.pi, 100)
    circle = np.exp(1j * phi)

    vertices = [[center[0] + p.real * radiusX , center[1] + p.imag * radiusY] for p in circle]

    return vertices