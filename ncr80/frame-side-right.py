# %%
from build123d import *
from ocp_vscode import *
import copy, math

from defs import *

# overall length
L = 170
# overall width
W = 70

PCB_W = 43
CONN_W = 10

F = 3.2/2
hole_coords = [ (2.4+F, 133.444+F), (2.4+F, 33.444+F),
                (40.9+F, 2.702+F), (40.9+F, 164.098+F) ]

hole_coords2 = copy.copy(hole_coords)
h2 = hole_coords2[2]
h2 = (h2[0] + 17, h2[1])
hole_coords2[2] = h2

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
    # top inserts
    with BuildSketch(Location((0, 0, H))):
        with Locations(hole_coords2):
            Circle(radius = SMALL_INSERT_R)
    extrude(amount=-SMALL_INSERT_L, mode=Mode.SUBTRACT)
    chamfer(o.edges().filter_by(Axis.Z), length=1)
    # pcb support
    with BuildSketch(Location((0, 0, 0))):
        with Locations((PCB_W/2 + TH, 9)):
            Rectangle(PCB_W, 18)
    extrude(amount=10)
    # pcb cutout
    with BuildSketch(Location((0, 0, H))):
        with Locations((PCB_W/2 + TH, TH + 2)):
            Rectangle(PCB_W, 16 - 0)
    extrude(amount=-7.5, mode=Mode.SUBTRACT)
    # connector cutout
    with BuildSketch(Location((0, 0, H))):
        with Locations((PCB_W/2 + TH - 4, 0)):
            Rectangle(CONN_W, TH)
    extrude(amount=-7.5, mode=Mode.SUBTRACT)
    # bottom inserts
    with BuildSketch(Plane.XY):
        with Locations(hole_coords):
            Circle(radius = LARGE_INSERT_R)
    extrude(amount=LARGE_INSERT_L, mode=Mode.SUBTRACT)
    # groove
    with BuildSketch(Plane.XY) as sk:
        with Locations((W, TH/2), (W, L - TH/2)):
            Circle(radius=TONGUE_DIA/2)
    extrude(amount=H, mode=Mode.SUBTRACT)    


show(o)    
export_step(o.part, "frame-side-right.step")
