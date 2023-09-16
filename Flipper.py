import Hex
import math


plate = Hex.basePlate()
iPlate = Hex.indexedPlate(1)


inset = 3
inset2 = 7
inset3 = 12

a1 = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0)
a1x = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, -inset)
a1y = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, -inset2)
a1z = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, -inset3)
b1 = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, 0)
b1x = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, -inset)

a2 = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)
a2x = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -inset)
a2y = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -inset2)
a2z = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -inset3)


radius = math.sqrt(a1x[0]**2 + a1x[1]**2)
radius2 = math.sqrt(a1y[0]**2 + a1y[1]**2)

#print((radius * 2 - 42) / 3)

smallCorner = [plate[0], a1, a1x, ["arc", radius, 0], a2x, a2]
largeCorner = [plate[0], plate[1], b1, b1x, ["arc", radius, 0], a2x, a2]


indentAngle = math.atan2(a1y[1], a1y[0]) * 180 / math.pi

print(indentAngle)

smallCornerIndent = [plate[0], a1, a1x, ["arc", radius, 0],
	Hex.polarPos(radius, indentAngle / 3),
	Hex.polarPos(radius2, indentAngle / 3),
	["arc"] + Hex.polarPos(radius2, indentAngle * 2 / 3),
	a2y, a2]

indentAngle *= -1

largeCornerIndent = [plate[0], plate[1], b1, b1x,
	["arc"] + Hex.polarPos(radius, 60),
	Hex.polarPos(radius, 60 - indentAngle / 3), Hex.polarPos(radius2, 60 - indentAngle / 3),
	["arc"] + Hex.polarPos(radius2, 60 - indentAngle / 2),
	Hex.polarPos(radius2, 40), Hex.polarPos(radius, 40),
	["arc"] + Hex.polarPos(radius, 30),
	Hex.polarPos(radius, 20), Hex.polarPos(radius2, 20),
	["arc"] + Hex.polarPos(radius2, indentAngle / 2),
	Hex.polarPos(radius2, indentAngle / 3), Hex.polarPos(radius, indentAngle / 3),
	["arc", radius, 0],
	a2x, a2]



pchCenter = Hex.TileEdge - inset3 * 2 / math.sqrt(3)
pchRadius = Hex.dist(a1z, [pchCenter, 0])

pachinkoCorner = [plate[0], a1, a1z, ["arc", pchCenter - pchRadius, 0], a2z, a2]


flipperAngle = 17
flipperRadius = radius - 1

angleTmp = (60 - flipperAngle / 2) / 180 * math.pi
flipperInnerArc = flipperRadius / math.cos(angleTmp) - flipperRadius * math.tan(angleTmp) + 2.5
print(flipperInnerArc)

flipper = [
	Hex.polarPos(flipperRadius, 90 - flipperAngle / 2),
	["arc", 0, -flipperRadius],
	Hex.polarPos(flipperRadius, 90 + flipperAngle / 2),
	["arc"] + Hex.polarPos(flipperInnerArc, 120),
	]

flipper = flipper + Hex.transform(flipper, 0, 0, 120) + Hex.transform(flipper, 0, 0, 240) + [flipper[0]]


flipperCircle = Hex.makeCircle(2.0) #1.5

flipperCircleBase = Hex.makeCircle(0.75)

pachinkoPinRadius = 0.5
distance = (radius * 2 - pachinkoPinRadius * 6) / 4
print(distance)
pachinkoPin = Hex.makeCircle(pachinkoPinRadius)

distance2 = pachinkoPinRadius * 2 + distance
print(distance2)

	
if __name__ == "__main__":
	print("Writing Flippers + Pachinko")
	tileFlipper3 = Hex.loadTemplate()
	tileFlipper6 = Hex.loadTemplate()
	tilePachinko = Hex.loadTemplate()


	for tile in [tileFlipper3, tileFlipper6, tilePachinko]:
		Hex.transformInsert(tile, "3mm", plate, [50, 250], 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)


	Hex.transformInsert(tileFlipper3, "10mm", largeCorner, [150, 250], 50, [0, 120])
	Hex.transformInsert(tileFlipper6, "10mm", smallCorner, [150, 250], 50, [i * 60 for i in range(4)])
	Hex.transformInsert(tilePachinko, "10mm", smallCorner, [150, 250], 50, [0, 180])

	Hex.transformInsert(tileFlipper3, "10mm", largeCornerIndent, [150, 250], 50, -120)
	Hex.transformInsert(tileFlipper6, "10mm", smallCornerIndent, [150, 250], 50, -60)	
	Hex.transformInsert(tileFlipper6, "10mm", Hex.flipY(smallCornerIndent), [150, 250], 50, -120)

	Hex.transformInsert(tileFlipper3, "10mm", flipper, [150, 250], 50, flipperAngle * 1.4)
	Hex.transformInsert(tileFlipper6, "10mm", flipper, [150, 250], 50, flipperAngle * 1.4)

	Hex.transformInsert(tileFlipper3, "10mm", flipperCircle, [150, 250], 50, 0)
	Hex.transformInsert(tileFlipper6, "10mm", flipperCircle, [150, 250], 50, 0)

	for i in [tileFlipper3, tileFlipper6]:
		Hex.transformInsert(i, "3mm", flipperCircleBase, [50, 250], 50, 0)
	
	Hex.transformInsert(tilePachinko, "10mm", pachinkoCorner, [150, 250], 50, [-60, -120])

	for i in [[0, 0], [distance2, 0], [-distance2, 0], [0, -distance2 * 1.15]]:
		for j in [[50, 50], [50, 120], [250, 50]]:
			Hex.transformInsert(tilePachinko, "3mm", pachinkoPin, i[0] + j[0], i[1] + j[1], 0)

	Hex.saveXML(tileFlipper3, "Tiles/Flipper3.svg")
	Hex.saveXML(tileFlipper6, "Tiles/Flipper6.svg")
	Hex.saveXML(tilePachinko, "Tiles/Pachinko.svg")
