# %%
from build123d import *
from ocp_vscode import *
import math

from defs import *

# overall length
L = 245.9

hole_coords = [ (-50, 0), (50, 0) ]

with BuildPart() as o:
    Box(L, TH, H)
    # bottom inserts
    with BuildSketch(Location((0, 0, -H/2))):
        with Locations(hole_coords):
            Circle(radius = LARGE_INSERT_R)
    extrude(amount=LARGE_INSERT_L, mode=Mode.SUBTRACT)
    # top inserts
    with BuildSketch(Location((0, 0, H/2))) as o_sk:
        with Locations(hole_coords):
            Circle(radius = SMALL_INSERT_R)
    extrude(amount=-SMALL_INSERT_L, mode=Mode.SUBTRACT)
    chamfer(o.edges().filter_by(Axis.Z), length=1)
    # tongue
    with BuildSketch(o.faces().sort_by(Axis.Z)[0]) as sk:
        with GridLocations(L, 1, 2, 1):
            Circle(radius=TONGUE_DIA/2)
    extrude(amount=-H)
    

show(o)    
export_step(o.part, "frame-side-topbot.step")
