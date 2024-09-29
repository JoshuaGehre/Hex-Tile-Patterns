import Hex
import math
import DIC

plate = Hex.basePlate()
iPlate = Hex.indexedPlate(6)

cOuter = DIC.partIC[1:-1] + [plate[2], plate[3], plate[4]]

wallWidth = 5
innerEdge = (Hex.TileHeight - wallWidth * 2) / math.sqrt(3)

xPlate = [Hex.polarPos(innerEdge, i * 60) for i in range(6)]
cRadius = (Hex.TileEdge + Hex.TrackWidth) * 0.5 + wallWidth

cInner = [xPlate[2], xPlate[3], xPlate[4], xPlate[5],
	Hex.circleLineIntersect(xPlate[0], -120, plate[0], cRadius),
	["arc"] + Hex.add(plate[0], [-cRadius, 0]),
	Hex.circleLineIntersect(xPlate[0], 120, plate[0], cRadius),
	xPlate[1]]

legRad = 1
legCenter = Hex.add([7.5, 0], Hex.polarPos(legRad / math.sin(math.pi / 8), 157.5))
leg1 = Hex.add(legCenter, [0, legRad])
leg2 = Hex.add(legCenter, Hex.polarPos(1, 45))

armCenter = [5, -6.5]
arm1 = Hex.add(armCenter, Hex.polarPos(legRad, -75))
arm2 = Hex.add(armCenter, Hex.polarPos(legRad, 65))

headRad = 2
headPoint = Hex.intersect(arm2, 155, [headRad, 0], 90)

meeple = [[2, 0],
	leg1, ["arc"] + Hex.add(legCenter, [legRad, 0]), leg2,
	Hex.intersect(leg2, 135, arm1, -165),
	arm1, ["arc"] + Hex.add(armCenter, [legRad, 0]), arm2,
	headPoint, Hex.add(headPoint, [0, -0.5])]

meeple = [[0, -2]] + meeple + [["arc", 0, headPoint[1] - headRad - 0.5]] + Hex.flipY(Hex.transform(Hex.reverse(meeple), 0, 0, 180))

meepleDeco = Hex.scale(meeple, 0.8)

if __name__ == "__main__":
	tileC = Hex.loadTemplate()
	tile0 = Hex.loadTemplate()

	for tile in [tileC, tile0]:
		Hex.transformInsert(tile, "3mm", plate, 50, 50)
		Hex.transformInsert(tile, "3mm", plate, 250, 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
		Hex.transformInsert(tile, "3mm", meepleDeco, 50, 90, 0)

	Hex.transformInsert(tileC, "10mm", DIC.roundCorner, [150, 250], 50, 0)
	Hex.transformInsert(tileC, "10mm", cOuter, [150, 250], 50, 0)
	Hex.transformInsert(tileC, "10mm", cInner, [150, 250], 50, 0)
	
	Hex.transformInsert(tileC, "3mm", meepleDeco, 260, 42, 0)

	Hex.transformInsert(tile0, "10mm", plate, [150, 250], 50, 0)
	Hex.transformInsert(tile0, "10mm", xPlate, [150, 250], 50, 0)
	Hex.transformInsert(tile0, "3mm", meepleDeco, 271, 43, 30)

	Hex.saveXML(tileC, "Tiles/Carcassonne_C.svg")
	Hex.saveXML(tile0, "Tiles/Carcassonne_0.svg")
