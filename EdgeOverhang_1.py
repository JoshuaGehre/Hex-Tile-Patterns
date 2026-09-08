import Hex
import math
import DIC
import Deco

star = ["group", Deco.makeStar(8), Deco.makeStar(4)]
plate = Hex.basePlate()
i2Plate = Hex.indexedPlate(2)

indent = 12
width = 10
tileMargin = 1.5
wallWidth = 5
holeOffsetY = 4
holeOffsetX = -6
pillarWidth = 5
pillarHeight = 19

holdPartD = [
	Hex.relativeToCenter(plate[5], plate[0], -0.5 * width - 6, 0),
	Hex.relativeToCenter(plate[5], plate[0], -0.5 * width - 6, -indent - 3),
	Hex.relativeToCenter(plate[5], plate[0], -0.5 * width, -indent - 3),
	Hex.relativeToCenter(plate[5], plate[0], -0.5 * width, -indent),
	Hex.relativeToCenter(plate[5], plate[0], +0.5 * width, -indent),
	Hex.relativeToCenter(plate[5], plate[0], +0.5 * width, 0)]

holdPartU = Hex.flipY(holdPartD)
holdPartU.reverse()

holdPlate = [plate[5]] + holdPartD + [plate[0]] + holdPartU + [
	plate[1], plate[2],
	Hex.relativeToCenter(plate[2], plate[3], -0.5 * Hex.TrackWidth, 0),
	["arc"] + Hex.add(plate[3], [0.5 * (Hex.TileEdge + Hex.TrackWidth), 0]),
	Hex.relativeToCenter(plate[4], plate[3], -0.5 * Hex.TrackWidth, 0),
	plate[4]]

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

rampCenter = Hex.intersect([0, -0.5 * tileMargin], 0, rampLI, 60)

rLI = Hex.dist(rampLI, rampCenter)
rLO = Hex.dist(rampLO, rampCenter)
rRI = Hex.dist(rampRI, rampCenter)
rRO = Hex.dist(rampRO, rampCenter)

innerWall = [
	rampLO, ["arc"] + Hex.add(rampCenter, Hex.polarPos(rLO, 30)), Hex.add(rampCenter, [rLO, 0]),
	Hex.add(rampCenter, [rLI, 0]), ["arc"] + Hex.add(rampCenter, Hex.polarPos(rLI, 30)), rampLI
]

outerWall = [
	rampRI, ["arc"] + Hex.add(rampCenter, Hex.polarPos(rRI, 30)), Hex.add(rampCenter, [rRI, 0]),
	Hex.add(rampCenter, [rRI + 3, 0]),
	Hex.add(rampCenter, [rRI + 3, -pillarWidth]),
	Hex.add(rampCenter, [rRI + 6, -pillarWidth]),
	Hex.add(rampCenter, [rRI + 6, 0]),
	Hex.add(rampCenter, [rRI + 9, 0]),
	Hex.add(rampCenter, [rRI + 9, -pillarWidth - 3]),
	Hex.circleLineIntersect(Hex.add(rampCenter, [0, -pillarWidth - 3]), 0, rampCenter, rRO),
	["arc"] + Hex.add(rampCenter, Hex.polarPos(rRO, 30)), rampRO
]

outerBase = [innerWall[i] for i in range(3)] + [outerWall[i] for i in range(7, len(outerWall))]

connector = Hex.flipY(holdPartD) + [
	Hex.circleLineIntersect(holdPartU[0], 30, rampCenter, rLO),
	["arc"] + Hex.add(rampCenter, Hex.polarPos(rLO, 10)),
	innerWall[2], innerWall[3], innerWall[4], innerWall[5],
	innerWall[0],
	["arc"] + Hex.add(rampCenter, Hex.polarPos(rLO, 50)),
	Hex.circleLineIntersect(holdPartU[2], 30, rampCenter, rLO),
	Hex.relativeToCenter(plate[0], plate[1], +0.5 * width, 0)]

def makeHolePair(width):
	u = [[holeOffsetX, holeOffsetY], [holeOffsetX + width, holeOffsetY], [holeOffsetX + width, holeOffsetY + 3], [holeOffsetX, holeOffsetY + 3]]
	return ["group", u, Hex.flipY(u)]

lowerHoles = makeHolePair(6.5)
upperHoles = makeHolePair(6.5 + indent)

pillar = [[0, 0], [pillarWidth, 0], [pillarWidth, -pillarHeight], [0, -pillarHeight]]

def centeredRect(x, y):
	x *= 0.5
	y *= 0.5
	return [[x, y], [-x, y], [-x, -y], [x, -y]]

pillarConnect = ["group", centeredRect(3.2, pillarWidth * 2 + tileMargin + 0.5), centeredRect(9.2, pillarWidth * 2 + tileMargin + 6.5)]

upperHoles += [Hex.transform(centeredRect(9.2, 3), 0, 20.5, 0)]

def outerDoublePrint(tile, shape, x):
	Hex.transformInsert(tile, "3mm", shape, 50 + x, 170)
	Hex.transformInsert(tile, "3mm", shape, 250, 50)
	Hex.transformInsert(tile, "3mm", Hex.flipY(shape), 50 + x, 170)
	Hex.transformInsert(tile, "3mm", Hex.flipY(shape), 250, 50)

holeHeight = 35.5
holeEdge = holeHeight / math.sqrt(3)
baseInfill = [Hex.polarPos(holeEdge, i * 60) for i in range(6)]

if __name__ == "__main__":
	print("Writing Edge Overhang")
	tile = Hex.loadTemplate()

	Hex.transformInsert(tile, "3mm", plate, [50, 250], 50)

	Hex.transformInsert(tile, "3mm", i2Plate, 50, 110)
	Hex.transformInsert(tile, "3mm", i2Plate, 250, 50)

	Hex.transformInsert(tile, "10mm", DIC.roundCorner, [150, 250], 50, 180)
	Hex.transformInsert(tile, "10mm", largePart, [150, 250], 50, 0)
	
	Hex.transformInsert(tile, "3mm", holdPlate, 50, 170)
	Hex.transformInsert(tile, "3mm", lowerHoles, 50, 170)
	Hex.transformInsert(tile, "3mm", holdPlate, 250, 50)
	Hex.transformInsert(tile, "3mm", lowerHoles, 250, 50)
	
	Hex.transformInsert(tile, "10mm", upperHoles, [150, 250], 50, 0)

	Hex.transformInsert(tile, "10mm", innerWall, [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", outerWall, [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", Hex.flipY(innerWall), [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", Hex.flipY(outerWall), [150, 250], 50, 0)

	Hex.transformInsert(tile, "3mm", DIC.roundCorner, 250, 50, 180)
	Hex.transformInsert(tile, "3mm", DIC.roundCorner, 50, 170, 180)
	
	Hex.transformInsert(tile, "3mm", pillar, [80, 90], 110)
	Hex.transformInsert(tile, "3mm", pillarConnect, 105, 100)

	outerDoublePrint(tile, connector, 0)
	outerDoublePrint(tile, outerBase, 15)
	outerDoublePrint(tile, outerWall, 30)
	
	Hex.transformInsert(tile, "3mm", star, [85, 250], 35)
	
	Hex.transformInsert(tile, "10mm", baseInfill, 250, 50, 0)
	Hex.transformInsert(tile, "10mm", baseInfill, 150, 100, 0)
	
	Hex.saveXML(tile, "Tiles/EdgeOverhang_v1.svg")
