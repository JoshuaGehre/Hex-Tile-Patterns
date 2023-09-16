import Hex
import math


plate = Hex.basePlate()
i2Plate = Hex.indexedPlate(2)
i4aPlate = Hex.indexedPlate("x-xx-x")
i4bPlate = Hex.indexedPlate("xxxx--")
i6Plate = Hex.indexedPlate(6)

a1 = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0)
b1 = Hex.relativeToCenter(plate[0], plate[1], 0.5 * Hex.TrackWidth, 0)
c1 = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, 0)
a2 = Hex.relativeToCenter(plate[0], plate[5], -0.5 * Hex.TrackWidth, 0)
b2 = Hex.relativeToCenter(plate[0], plate[5], 0.5 * Hex.TrackWidth, 0)
c2 = Hex.relativeToCenter(plate[5], plate[4], -0.5 * Hex.TrackWidth, 0)
d2 = Hex.relativeToCenter(plate[5], plate[4], 0.5 * Hex.TrackWidth, 0)

roundCorner = [plate[0], a1, ["arc", (Hex.TileEdge + Hex.TrackWidth) * 0.5, 0], a2]
partIC = [c2, plate[5], b2, ["arc", (Hex.TileEdge - Hex.TrackWidth) * 0.5, 0], b1, plate[1], c1]


outerPointDistance = Hex.TileHeight * 1.3
outerPoint = Hex.polarPos(outerPointDistance, -30)
innerRadius = Hex.dist(outerPoint, c2)
arcPoint1 = Hex.polarPos(outerPointDistance - innerRadius, -30)
arcPoint2 = Hex.polarPos(outerPointDistance - innerRadius - Hex.TrackWidth, -30)

dcCornerAngle = math.atan2(outerPoint[1] - c2[1], outerPoint[0] - c2[0])

dcCornerAngle *= 180 / math.pi

#print(dcCornerAngle)

dcPart = [d2,
	["arc"] + Hex.add(c2, Hex.polarPos(Hex.TrackWidth, 180 - 0.5 * dcCornerAngle)),
	Hex.add(c2, Hex.polarPos(Hex.TrackWidth, 180 - dcCornerAngle)),
	["arc", arcPoint2[0], arcPoint2[1]],
	Hex.add(a1, Hex.polarPos(Hex.TrackWidth, 120 + dcCornerAngle)),
	["arc"] + Hex.add(a1, Hex.polarPos(Hex.TrackWidth, 120 + 0.5 * dcCornerAngle)),
	b1,
	plate[1]]

dcPart += Hex.transform(dcPart, 0, 0, 180)

largeRoundCorner = [plate[0], a1, ["arc", arcPoint1[0], arcPoint1[1]], c2, plate[5]]

piscesCorner = [plate[0], a1,
	["arc"] + Hex.add(outerPoint, Hex.polarPos(innerRadius, 130)),
	Hex.circleLineIntersect(a2, 150, outerPoint, innerRadius),
	a2]

piscesCenter = [
	Hex.circleLineIntersect(a2, 150, outerPoint, innerRadius + Hex.TrackWidth),
	["arc"] + Hex.add(outerPoint, Hex.polarPos(innerRadius + Hex.TrackWidth, 130)),
	Hex.add(a1, Hex.polarPos(Hex.TrackWidth, 120 + dcCornerAngle)),
	["arc"] + Hex.add(a1, Hex.polarPos(Hex.TrackWidth, 120 + 0.5 * dcCornerAngle)),
	b1,
	plate[1],
	[c2[0], -c2[1]],
] + Hex.transform([
	["arc"] + Hex.add(c2, Hex.polarPos(Hex.TrackWidth, 180 - 0.5 * dcCornerAngle)),
	Hex.add(c2, Hex.polarPos(Hex.TrackWidth, 180 - dcCornerAngle)),
	["arc"] + Hex.add(outerPoint, Hex.polarPos(innerRadius + Hex.TrackWidth, 170)),
	Hex.circleLineIntersect(b2, 150, outerPoint, innerRadius + Hex.TrackWidth),
], 0, 0, 180)


xcCenter = [
	plate[5], b2,
	["arc", (Hex.TileEdge - Hex.TrackWidth) * 0.5, 0],
	b1, plate[1], c1,
	["arc", -dcPart[1][1], -dcPart[1][2]],
	[-dcPart[2][0], -dcPart[2][1]],
	["arc", -arcPoint2[0], -arcPoint2[1]],
	[math.sqrt((innerRadius + Hex.TrackWidth) ** 2 - outerPoint[1] ** 2) - outerPoint[0], 0],
	["arc", -arcPoint2[0], arcPoint2[1]],
	[-dcPart[2][0], dcPart[2][1]],
	["arc", -dcPart[1][1], dcPart[1][2]],
	c2]

arcPoint3 = Hex.add(outerPoint, Hex.polarPos(innerRadius, 120 + dcCornerAngle + 5))

xcSmallCorner = [
	plate[3],
	Hex.relativeToCenter(plate[3], plate[4], -0.5 * Hex.TrackWidth, 0),
	["arc", -arcPoint3[0], -arcPoint3[1]],
	[math.sqrt(innerRadius ** 2 - outerPoint[1] ** 2) - outerPoint[0], 0],
	["arc", -arcPoint3[0], arcPoint3[1]],
	Hex.relativeToCenter(plate[3], plate[2], -0.5 * Hex.TrackWidth, 0),
]

outerPoint2 = Hex.polarPos(outerPointDistance, -90)

xcLargeCorner = [
	plate[4], d2, dcPart[1], dcPart[2],
	["arc"] + Hex.add(outerPoint, Hex.polarPos(innerRadius + Hex.TrackWidth, 180 - dcCornerAngle * 1.1)),
	Hex.circleIntersect(outerPoint, innerRadius + Hex.TrackWidth, outerPoint2, innerRadius),
	["arc"] + Hex.add(outerPoint2, Hex.polarPos(innerRadius, 100)),
	[-b2[0], b2[1]]]

xcLargeCorner2 = Hex.flipY(xcLargeCorner)

if __name__ == "__main__":
	print("Writing Files")
	tileDIC = Hex.loadTemplate()
	tileDC = Hex.loadTemplate()
	tileXC = Hex.loadTemplate()
	tilePisces = Hex.loadTemplate()

	Hex.transformInsert(tileDIC, "3mm", plate, [50, 250], 50)
	Hex.transformInsert(tileDIC, "3mm", i2Plate, 50, 120)
	Hex.transformInsert(tileDIC, "3mm", i2Plate, 250, 50)
	Hex.transformInsert(tileDIC, "10mm", roundCorner, [150, 250], 50, [0, 180])
	Hex.transformInsert(tileDIC, "10mm", partIC, [150, 250], 50, [0, 180])


	Hex.transformInsert(tileDC, "3mm", plate, [50, 250], 50)
	Hex.transformInsert(tileDC, "3mm", i4aPlate, 50, 120)
	Hex.transformInsert(tileDC, "3mm", i4aPlate, 250, 50)

	Hex.transformInsert(tileDC, "10mm", largeRoundCorner, [150, 250], 50, [0, 180])
	Hex.transformInsert(tileDC, "10mm", dcPart, [150, 250], 50, 0)


	Hex.transformInsert(tileXC, "3mm", plate, [50, 250], 50)
	Hex.transformInsert(tileXC, "3mm", i4bPlate, 50, 120)
	Hex.transformInsert(tileXC, "3mm", i4bPlate, 250, 50)

	Hex.transformInsert(tileXC, "10mm", roundCorner, [150, 250], 50, 0)
	Hex.transformInsert(tileXC, "10mm", xcCenter, [150, 250], 50, 0)
	Hex.transformInsert(tileXC, "10mm", xcSmallCorner, [150, 250], 50, 0)
	Hex.transformInsert(tileXC, "10mm", xcLargeCorner, [150, 250], 50, -120)

	Hex.transformInsert(tileXC, "10mm", xcLargeCorner2, [150, 250], 50, 120)

	Hex.transformInsert(tilePisces, "3mm", plate, [50, 250], 50)
	Hex.transformInsert(tilePisces, "3mm", i6Plate, 50, 120)
	Hex.transformInsert(tilePisces, "3mm", i6Plate, 250, 50)
	
	Hex.transformInsert(tilePisces, "10mm", piscesCenter, [150, 250], 50, [0, 180])
	Hex.transformInsert(tilePisces, "10mm", piscesCorner, [150, 250], 50, [0, 180])
	Hex.transformInsert(tilePisces, "10mm", Hex.flipY(piscesCorner), [150, 250], 50, [-60, 120])
	
	#Hex.saveXML(tileDIC, "Tiles/DIC.svg")
	#Hex.saveXML(tileDC, "Tiles/DC.svg")
	#Hex.saveXML(tileXC, "Tiles/XC.svg")
	Hex.saveXML(tilePisces, "Tiles/Pisces.svg")
