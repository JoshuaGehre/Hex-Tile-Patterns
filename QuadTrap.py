import Hex
import math


plate = Hex.basePlate()
iPlate = Hex.indexedPlate(2)

a = Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, 0)
b = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)
c = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0)

r = 25

rInner = r - 0.5 * Hex.TrackWidth
rOuter = r + 0.5 * Hex.TrackWidth

cUp = Hex.add(b, Hex.polarPos(rInner, 60))
cDown = Hex.add(c, Hex.polarPos(rInner, -60))

#print((cDown[0] - rOuter) * 2)

x = Hex.circleIntersect(cUp, rOuter, cDown, rInner)
ang = math.atan2(x[1] - cDown[1], x[0] - cDown[0]) / math.pi * 180

#print(ang)

"""
centerPart = [plate[5], a, 
	["arc"] + Hex.add(cUp, Hex.polarPos(rOuter, -121)),
	x,
	Hex.add(cDown, Hex.polarPos())
	Hex.circleIntersect(cUp, rOuter, cDown, rOuter)]

corner = [plate[0], c,
	["arc"] + Hex.add(cDown, Hex.polarPos(rInner, 130)),
	Hex.circleIntersect(cUp, rInner, cDown, rInner),
	["arc"] + Hex.add(cUp, Hex.polarPos(rInner, -130)),
	b]
"""

corner = [plate[0], c, ["arc", (Hex.TileEdge + Hex.TrackWidth) * 0.5, 0], b]

ang = 15
rInc = 19
cAng = 12.5

x = Hex.add(plate[0], Hex.polarPos(0.5 * (Hex.TileEdge + Hex.TrackWidth), -120 - ang))
y = Hex.add(plate[0], Hex.polarPos(0.5 * (Hex.TileEdge - Hex.TrackWidth), -120 - ang))

c = Hex.add(plate[0], Hex.polarPos(rInc, 60 - ang))
c2 = [c[0], -c[1]]

r1 = Hex.dist(c, x)
r2 = Hex.dist(c, y)




centerPartX = [plate[5], a,
	["arc"] + Hex.add(plate[0], Hex.polarPos(0.5 * (Hex.TileEdge + Hex.TrackWidth), -120 - ang * 0.5 )),
	x,
	["arc"] + Hex.add(c, Hex.polarPos(r1, -170)),
	Hex.add(c, [-r1, 0]),
	["arc"] + Hex.add(c, [-0.5 * (r1 + r2), -0.5 * Hex.TrackWidth]),
	Hex.add(c, [-r2, 0]),
	["arc"] + Hex.add(c, Hex.polarPos(r2, -170)),
	y,
	["arc"] + Hex.add(plate[0], Hex.polarPos(0.5 * (Hex.TileEdge - Hex.TrackWidth), -120 - ang * 0.5 )),
	b, plate[0]]

z = Hex.add(c2, Hex.polarPos(r1, 180 - cAng))
cc = Hex.intersect(z, 180 - cAng, [0, 0], 0)

centerPart = [plate[5], a,
	["arc"] + Hex.add(plate[0], Hex.polarPos(0.5 * (Hex.TileEdge + Hex.TrackWidth), -120 - ang * 0.5 )),
	x,
	Hex.circleIntersect(Hex.add(c2, [-0.5 * (r1 + r2), 0]), 0.5 * Hex.TrackWidth, c, r1),
	["arc"] + Hex.add(c2, [-0.5 * (r1 + r2), 0.5 * Hex.TrackWidth]),
	Hex.add(c2, [-r1, 0]),	
	["arc"] + Hex.add(c2, Hex.polarPos(r1, 180 - 0.5 * cAng)),
	z,
	["arc", cc[0] + Hex.dist(cc, z), 0],
	#["arc"] + Hex.add(c2, Hex.polarPos(r1, 170)),
	#Hex.circleIntersect(c, r1, c2, r1)]
	]


print("Dist: " + str(2 * (c[0] - r1)))

cFlip = Hex.flipY(centerPart)

centerPart = centerPart + [cFlip[len(centerPart) - i - 2] for i in range(len(centerPart) - 1)]
centerPart = centerPart + Hex.transform(centerPart, 0, 0, 180)

cFlipX = Hex.flipY(centerPartX)

centerPartX = centerPartX + [cFlipX[len(centerPartX) - i - 2] for i in range(len(centerPartX) - 1)]
centerPartX = centerPartX + Hex.transform(centerPartX, 0, 0, 180)

if __name__ == "__main__":
	print("Writing Q Trap")
	tileQTrap = Hex.loadTemplate()

	for tile in [tileQTrap]:
		Hex.transformInsert(tile, "3mm", plate, 50, 50)
		Hex.transformInsert(tile, "3mm", plate, 250, 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
	
	Hex.transformInsert(tileQTrap, "10mm", centerPart, [150, 250], 50, 0)	
	#Hex.transformInsert(tileQTrap, "10mm", centerPartX, [150, 250], 50, 0)	
	Hex.transformInsert(tileQTrap, "10mm", corner, [150, 250], 50, [0, 180])

	Hex.saveXML(tileQTrap, "Tiles/QuadTrap.svg")
