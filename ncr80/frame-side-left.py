# %%
from build123d import *
from ocp_vscode import *
import math
from defs import *

# overall length
L = 170
# overall width
W = 70

F = 3.2/2
hole_coords = [ (2.4+F, 133.444+F), (2.4+F, 33.444+F),
                (40.9+F, 2.702+F), (40.9+F, 164.098+F) ]

with BuildPart() as o:
    with BuildSketch(Plane.XY) as o_sk:
        with BuildLine() as o_ln:
            # top outer corner
            l1 = RadiusArc((R, 0), (0, R), R)
            # outer side
            l2 = Line((0, R), (0, L - R))
            # bottom outer corner
            l3 = RadiusArc((0, L - R), (R, L), R)
            # outer bottom
            l4 = Line((R, L), (W, L))
            # bottom end
            l5 = Line((W, L), (W, L - TH))
            # inner bottom
            l6 = Line((W, L - TH), (TH + R, L - TH))
            # bottom inner corner
            l7 = RadiusArc((TH, L - TH - R), (TH + R, L - TH), R)
            # inner side
            l8 = Line((TH, L - TH - R), (TH, TH + R))
            # top inner corner
            l9 = RadiusArc((TH + R, TH), (TH, TH + R), R)
            # top inner
            l10 = Line((TH + R, TH), (W, TH))
            l11 = Line((W, TH), (W, 0))
            l12 = Line((W, 0), (R, 0))
        make_face()
    extrude(amount=H)
    # bottom inserts
    with BuildSketch(Plane.XY):
        with Locations(hole_coords):
            Circle(radius = LARGE_INSERT_R)
    extrude(amount=LARGE_INSERT_L, mode=Mode.SUBTRACT)
    # top inserts
    with BuildSketch(Location((0, 0, H))) as o_sk:
        with Locations(hole_coords):
            Circle(radius = SMALL_INSERT_R)
    extrude(amount=-SMALL_INSERT_L, mode=Mode.SUBTRACT)

    chamfer(o.edges().filter_by(Axis.Z), length=1)
    # groove
    with BuildSketch(Plane.XY) as sk:
        with Locations((W, TH/2), (W, L - TH/2)):
            Circle(radius=TONGUE_DIA/2)
    extrude(amount=H, mode=Mode.SUBTRACT)    

show(o)    
export_step(o.part, "frame-side-left.step")
