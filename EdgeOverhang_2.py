import Hex
import math
#import DIC
import Deco

star = ["group", Deco.makeStar(8), Deco.makeStar(4)]
plate = Hex.basePlate()
i2Plate = Hex.indexedPlate(2)

indent = 12
width = 10
tileMargin = 1.5
wallWidth = 5

pillarWidth = 5
pillarHeight = 20

holdConnect = [
	Hex.relativeToCenter(plate[5], plate[0], -0.5 * width, 0),
	Hex.relativeToCenter(plate[5], plate[0], +0.5 * width, 0),
	Hex.relativeToCenter(plate[0], plate[1], -0.5 * width, 0),
	Hex.relativeToCenter(plate[0], plate[1], +0.5 * width, 0)]

largePart = [
	plate[5], plate[0], plate[1], plate[2],
	Hex.relativeToCenter(plate[2], plate[3], -0.5 * Hex.TrackWidth, 0),
	["arc"] + Hex.add(plate[3], [0.5 * (Hex.TileEdge + Hex.TrackWidth), 0]),
	Hex.relativeToCenter(plate[4], plate[3], -0.5 * Hex.TrackWidth, 0),
	plate[4]]

rampLI = Hex.add(Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, tileMargin), [0, -tileMargin - Hex.TileHeight])
rampLO = Hex.add(rampLI, Hex.polarPos(-wallWidth, 60))
rampRI = Hex.add(rampLI, Hex.polarPos(Hex.TrackWidth, 60))
rampRO = Hex.add(rampLI, Hex.polarPos(Hex.TrackWidth + wallWidth, 60))

rampCenter = Hex.intersect([0, 0], 0, rampLI, 60)

rLI = Hex.dist(rampLI, rampCenter)
rLO = Hex.dist(rampLO, rampCenter)
rRI = Hex.dist(rampRI, rampCenter)
rRO = Hex.dist(rampRO, rampCenter)

plateHole = [plate[0], holdConnect[1],
	Hex.circleLineIntersect(holdConnect[1], -30, rampCenter, rLO),
	["arc", rampCenter[0] + rLO, 0],
	Hex.circleLineIntersect(holdConnect[2], 30, rampCenter, rLO),
	holdConnect[2]]

innerWall = [
	rampLO, ["arc", rampCenter[0] + rLO, 0], Hex.add(rampCenter, Hex.polarPos(rLO, -60)),
	Hex.add(rampCenter, Hex.polarPos(rLI, -60)), ["arc", rampCenter[0] + rLI, 0], rampLI]

pillarAngleOffset = 180.0 / math.pi * math.asin((pillarWidth + 6) / (2 * rRO))
#print(pillarAngleOffset)

outerWallBase = [
	Hex.add(rampCenter, Hex.polarPos(rRO, -30 - pillarAngleOffset)),
	Hex.add(rampCenter, Hex.polarPos(rRO, -30 + pillarAngleOffset)),
	Hex.add(rampCenter, Hex.polarPos(rRO, 30 - pillarAngleOffset)),
	Hex.add(rampCenter, Hex.polarPos(rRO, 30 + pillarAngleOffset)),
]

outerWall = [
	rampRI, ["arc", rampCenter[0] + rRI, 0], Hex.add(rampCenter, Hex.polarPos(rRI, -60)),
	Hex.add(rampCenter, Hex.polarPos(rRO, -60)),
	["arc"] + Hex.add(rampCenter, Hex.polarPos(rRO, -55)),
	outerWallBase[0],
	Hex.add(outerWallBase[0], Hex.polarPos(6, -30)),
	Hex.add(outerWallBase[1], Hex.polarPos(6, -30)),
	outerWallBase[1],
	["arc", rampCenter[0] + rRO, 0],
	outerWallBase[2],
	Hex.add(outerWallBase[2], Hex.polarPos(6, 30)),
	Hex.add(outerWallBase[3], Hex.polarPos(6, 30)),
	outerWallBase[3],
	["arc"] + Hex.add(rampCenter, Hex.polarPos(rRO, 55)),
	rampRO]

plateOut = [plate[1], plate[2], plate[3], plate[4], plate[5],
	holdConnect[0], Hex.circleLineIntersect(holdConnect[0], -30, rampCenter, rLO),
	["arc"] + Hex.add(rampCenter, Hex.polarPos(rLO, -50)),
	Hex.add(rampCenter, Hex.polarPos(rLO, -60))
	] + [outerWall[i] for i in range(3, len(outerWall))] + [
	Hex.add(rampCenter, Hex.polarPos(rLO, 60)),
	["arc"] + Hex.add(rampCenter, Hex.polarPos(rLO, 50)),
	Hex.circleLineIntersect(holdConnect[3], 30, rampCenter, rLO), holdConnect[3]]

edgeHole = [
	Hex.relativeToCenter(outerWallBase[2], outerWallBase[3], -0.5 * pillarWidth, 0),
	Hex.relativeToCenter(outerWallBase[2], outerWallBase[3], -0.5 * pillarWidth, 3),
	Hex.relativeToCenter(outerWallBase[2], outerWallBase[3], 0.5 * pillarWidth, 3),
	Hex.relativeToCenter(outerWallBase[2], outerWallBase[3], 0.5 * pillarWidth, 0)]

edgeHoles = ["group", edgeHole, Hex.flipY(edgeHole)]

holeHeight = 35.5
holeEdge = holeHeight / math.sqrt(3)
baseInfill = [Hex.polarPos(holeEdge, i * 60) for i in range(6)]

holeInner = 1.5 * (2 ** 0.5)
holeOuter = holeInner + 0.5 * pillarWidth * (2 ** 0.5)
pillar = ["group", [[-0.5 * pillarWidth, 0], [0.5 * pillarWidth, 0],
	Hex.intersect([0.5 * pillarWidth, 0], 90, [holeOuter, -pillarHeight], 45),
	[holeOuter, -pillarHeight],
	[0, -pillarHeight - holeOuter],
	[-holeOuter, -pillarHeight],
	Hex.intersect([-0.5 * pillarWidth, 0], 90, [-holeOuter, -pillarHeight], -45)],

	[[holeInner, -pillarHeight],
	[0, -pillarHeight - holeInner],
	[-holeInner, -pillarHeight],
	[0, -pillarHeight + holeInner],
	]]

pillarHole = [[1.5, 0.5 * pillarWidth], [1.5, -0.5 * pillarWidth], [-1.5, -0.5 * pillarWidth], [-1.5, 0.5 * pillarWidth]]

a = 18
b = a * 0.5
mainPlateHoles = ["group",
	Hex.transform(pillarHole, b, -a, 0),
	Hex.transform(pillarHole, b, a, 0),
	Hex.transform(pillarHole, -b, -a, 30),
	Hex.transform(pillarHole, -b, a, -30),
	]

roundCornerRad = 0.5 * (Hex.TileEdge - Hex.TrackWidth)

roundCorner = [plate[3],
	Hex.add(plate[3], Hex.polarPos(roundCornerRad, -60)),
	["arc"] + Hex.add(plate[3], Hex.polarPos(roundCornerRad, -40)),
	Hex.circleLineIntersect([0, 1.5], 0, plate[3], roundCornerRad),
	None,
	None,
	Hex.circleLineIntersect([0, -1.5], 0, plate[3], roundCornerRad),
	["arc"] + Hex.add(plate[3], Hex.polarPos(roundCornerRad, 40)),
	Hex.add(plate[3], Hex.polarPos(roundCornerRad, 60))]

roundCorner[4] = Hex.add(roundCorner[3], [-pillarWidth, 0])
roundCorner[5] = Hex.add(roundCorner[6], [-pillarWidth, 0])

rampShift = Hex.add(rampCenter, [Hex.EdgeIndent * 2 / math.sqrt(3), 0])

outerBase = [
	Hex.circleLineIntersect(rampShift, 60, rampCenter, rLO),
	["arc", rampCenter[0] + rLO, 0],
	Hex.circleLineIntersect(rampShift, -60, rampCenter, rLO),
	Hex.circleLineIntersect(rampShift, -60, rampCenter, rRO),
	["arc", rampCenter[0] + rRO, 0],
	Hex.circleLineIntersect(rampShift, 60, rampCenter, rRO)]

if __name__ == "__main__":
	print("Writing Edge Overhang")
	tile = Hex.loadTemplate()

	Hex.transformInsert(tile, "3mm", plateOut, 250, 50)
	Hex.transformInsert(tile, "3mm", plateOut, 50, 110)
	Hex.transformInsert(tile, "3mm", plateHole, 250, 50)
	Hex.transformInsert(tile, "3mm", plateHole, 50, 110)

	Hex.transformInsert(tile, "3mm", i2Plate, [50, 250], 50)

	Hex.transformInsert(tile, "10mm", roundCorner, [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", largePart, [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", mainPlateHoles, [150, 250], 50, 0)

	Hex.transformInsert(tile, "10mm", innerWall, [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", outerWall, [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", edgeHoles, [150, 250], 50, 0)
	
	Hex.transformInsert(tile, "3mm", star, [90, 255], 50)
	
	Hex.transformInsert(tile, "10mm", baseInfill, 250, 50, 0)
	Hex.transformInsert(tile, "10mm", baseInfill, 150, 100, 0)
	
	Hex.transformInsert(tile, "3mm", pillar, [20, 35, 50, 65, 80, 95, 110], 190)
	
	Hex.transformInsert(tile, "3mm", outerBase, 250, 50)
	Hex.transformInsert(tile, "3mm", outerBase, 70, 180, -90)
	
	Hex.saveXML(tile, "Tiles/EdgeOverhang_v2.svg")
