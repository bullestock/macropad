import cadquery as cq

w = 117.5
h = 8
th = 2.5
d = 10

result = (cq.Workplane("XY")
          .tag("o")
          .vLine(w)
          .hLine(d)
          .vLine(-th)
          .hLine(-(d - th))
          .vLine(-(w - 2*th))
          .hLine(d - th)
          .vLine(-th)
          .close()
          .extrude(h)
          .workplaneFromTagged("o")
          .transformed(rotate=(0, 90, 0), offset=(th, w/2, h - 2))
          .rarray(1, w - 20, 1, 2)
          .circle(0.7).cutThruAll()
)

show_object(result)

