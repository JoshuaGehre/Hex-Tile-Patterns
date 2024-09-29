import Hex
import math


plate = Hex.basePlate()
iPlate = Hex.indexedPlate("xx---x")

a = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, 0)
b = Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth, 0)
c = Hex.relativeToCenter(plate[4], plate[5], -0.5 * Hex.TrackWidth, 0)
d = Hex.relativeToCenter(plate[4], plate[5], 0.5 * Hex.TrackWidth, 0)

r1 = 14
r1x = r1 + Hex.TrackWidth
r2 = 9.5
r2x = r2 + Hex.TrackWidth

h = 7
hr = 10.5

center1 = Hex.add(a, [r1, 0])
center2 = Hex.add(c, [-r2, -h])
center3 = Hex.add(c, [-r2, -hr])

trap1 = [8.7, -8]
trap2 = [-12, 8.5]
trapR = 6.5

lineAngle = 62
lineOffset = 5.25
linePad = 0.5

lineAnchorR = Hex.polarPos(lineOffset - (Hex.TrackWidth + linePad) * 0.5, lineAngle + 90)
lineAnchorL = Hex.polarPos(lineOffset + (Hex.TrackWidth + linePad) * 0.5, lineAngle + 90)

rightPart = [
	d, plate[5], plate[0], plate[1], a,
	["arc"] + Hex.add(center1, Hex.polarPos(r1, 190)),
	Hex.circleIntersect(center1, r1, trap1, trapR),
	["arc"] + Hex.add(trap1, [trapR, 0]),
	Hex.add(trap1, Hex.polarPos(trapR, -30)),
	["arc"] + Hex.add(trap1, [0, trapR]),
	Hex.circleLineIntersect(lineAnchorR, lineAngle, trap1, trapR, low=True),
	Hex.circleLineIntersect(lineAnchorR, lineAngle, center3, r2x),
	["arc"] + Hex.add(center3, Hex.polarPos(r2x, 5)),
	Hex.add(d, [0, -hr]),
	]
leftPart = [
	plate[2], plate[3], plate[4], c,
	Hex.add(c, [0, -h]),
	["arc"] + Hex.add(center2, Hex.polarPos(r2, 5)),
	Hex.circleIntersect(center2, r2, trap2, trapR),
	["arc"] + Hex.add(trap2, Hex.polarPos(trapR, 200)),
	Hex.add(trap2, [-trapR, 0]),
	["arc"] + Hex.add(trap2, Hex.polarPos(trapR, 175)),
	Hex.circleLineIntersect(lineAnchorL, lineAngle, trap2, trapR),
	Hex.circleLineIntersect(lineAnchorL, lineAngle, center1, r1x, low=True),
	["arc"] + Hex.add(center1, Hex.polarPos(r1x, 190)),
	b
	]


if __name__ == "__main__":
	print("Writing Linear Trap")
	tileLinearTrap = Hex.loadTemplate()

	for tile in [tileLinearTrap]:
		Hex.transformInsert(tile, "3mm", plate, 50, 50)
		Hex.transformInsert(tile, "3mm", plate, 250, 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
	
	Hex.transformInsert(tileLinearTrap, "10mm", rightPart, [150, 250], 50, 0)
	Hex.transformInsert(tileLinearTrap, "10mm", leftPart, [150, 250], 50, 0)

	Hex.saveXML(tileLinearTrap, "Tiles/LinearTrap.svg")
