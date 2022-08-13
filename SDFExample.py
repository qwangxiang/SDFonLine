from d3 import *
from d2 import *

class SIM():
    def SIMValve(height = 400, radius = 100):
        c1 = capped_cylinder((0, 0, 0), (0, 0, height), radius)
        c2 = capped_cylinder((0, 0, - height / 10), (0, 0, 0), radius * 2)
        c3 = capped_cylinder((0, 0, height), (0, 0, height + height / 10), radius * 2)
        c4 = capped_cone((0, 0, height / 2), (height, 0, height / 2), radius, radius / 3)
        s1 = sphere(radius / 3, (height, 0, height / 2))
        f1 = c1 | c2 | c3 | c4 | s1
        return f1

class GIM():
    def GIMCircularGasket(OR, IR, H):
        c1 = capped_cylinder((0, 0, 0), (0, 0, H), OR)
        c2 = capped_cylinder((0, 0, 0), (0, 0, H), IR)
        cut1 = c1 - c2
        return cut1

    def GIMChannelSteel(B, H, D, T, L):
        points = []
        point1 = (0, H / 2)
        point2 = (- B, H / 2)
        point3 = (- B, H / 2 - T)
        point4 = (- D, H / 2 - T)
        point5 = (- D, T - H / 2)
        point6 = (- B, T - H / 2)
        point7 = (- B, - H / 2)
        point8 = (0, - H / 2)
        points.append(point1)
        points.append(point2)
        points.append(point3)
        points.append(point4)
        points.append(point5)
        points.append(point6)
        points.append(point7)
        points.append(point8)
        p1 = polygon(points).extrude(L)
        return p1

if __name__ == '__main__':
    obj = GIM.GIMChannelSteel(400, 500, 20, 20, 2000)
    obj.save("obj.stl")
