import Hex
import math

rows = 6
holeHeight = 35.5
tileMargin = 1.5
TrackWall = 6

boardSize = [130, 75 + 0.5 * (Hex.TileHeight + tileMargin) * rows]
hexCount = rows * 5 + 2
holeEdge = holeHeight / math.sqrt(3)

rectangle = [
	[boardSize[0], boardSize[1]],
	[boardSize[0], -boardSize[1]],
	[-boardSize[0], -boardSize[1]],
	[-boardSize[0], boardSize[1]]]

xVec = Hex.polarPos(Hex.TileHeight + tileMargin, 30)
yVec = Hex.polarPos(Hex.TileHeight + tileMargin, 90)

def makeHole(x, y):
	center = [xVec[0] * x + yVec[0] * y, xVec[1] * x + yVec[1] * y]
	return [Hex.add(center, Hex.polarPos(holeEdge, i * 60)) for i in range(6)]

def insertHole(xml, center, x, y):
	name = "10mm" if "10mm" in xml else "mid"
	Hex.transformInsert(xml, name, makeHole(x, y), center[0], center[1])

positions = [[-1, 0], [1, -1]]

for i in range(rows):
	positions += [[-2, 1 + i], [-1, 1 + i], [0, i], [1, i], [2, i - 1]]

for p in positions:
	p[1] -= (rows - 1) / 2

def makeBaseHoles(board, center):
	for p in positions:
		insertHole(board, center, p[0], p[1])

	#name1 = "10mm" if "10mm" in board else "mid"
	#name2 = "10mm" if "10mm" in board else "late"

	#for i in range(6):
	#	Hex.transformInsert(board, name1, outerBaseHole, center[0], center[1], i * 60)
	
	#Hex.transformInsert(board, name2, rectangle, center[0], center[1])

def insertIndexPlate(xml, center, x, y, indents):
	center = Hex.add(center, [xVec[0] * x + yVec[0] * y, xVec[1] * x + yVec[1] * y])

	if indents == 1:
		indents = "x-----"
	elif indents == 2:
		indents = "x--x--"
	elif indents == 3:
		indents = "x-x-x-"
	elif indents == 6:
		indents = "xxxxxx"

	r = (Hex.TileHeight - Hex.EdgeIndent * 2) / math.sqrt(3)
	p = [Hex.polarPos(r, -120)]

	name1 = "3mm" if "3mm" in xml else "early"
	name2 = "3mm" if "3mm" in xml else "mid"

	for i in range(6):
		a = p[len(p) - 1]
		b = Hex.polarPos(r, (i - 1) * 60)
		if indents[i] == "x":
			c1 = Hex.relativeToCenter(a, b, -6.35, 0)
			c2 = Hex.relativeToCenter(a, b, +6.35, 0)
			p.append(c1)
			p.append(Hex.relativeToCenter(a, b, -6.35, -5))
			p.append(Hex.relativeToCenter(a, b, +6.35, -5))
			p.append(c2)
			if i > 0:
				Hex.transformInsert(xml, name2, [c1, c2], center[0], center[1])
		p.append(b)
	
	Hex.transformInsert(xml, name1, p, center[0], center[1])

def makeIndents(board, center, index = []):
	index += [6 for j in range(len(positions) - len(index))]
	for i in range(len(positions)):
		insertIndexPlate(board, center, positions[i][0], positions[i][1], index[i])

def outerEdgeSmall(x, y, pos, out=True):
	center = [xVec[0] * x + yVec[0] * y, xVec[1] * x + yVec[1] * y]
	r = (Hex.TileHeight - Hex.EdgeIndent * 2) / math.sqrt(3)
	if out:
		r += (Hex.EdgeIndent * 2 + tileMargin) * 2 / math.sqrt(3)
	return Hex.add(center, Hex.polarPos(r, pos * 60))


outPattern = []
for i in range(rows):
	outPattern += [[2, i - rows * 0.5 - 0.5, 0, True], [3, i - rows * 0.5 - 0.5, 3, False]]

outTop = rows * 0.5 - 1.5
outPattern[len(outPattern) - 1] = [2, outTop, 1, True]
outPattern += [[2, outTop + 1, 4, False], [1, outTop + 1, 1, True], [1, outTop + 1, 2, True], [0, outTop + 2, 5, False],
		[0, outTop + 2, 4, False], [-1, outTop + 2, 1, True], [-1, outTop + 2, 2, True],
		[-2, outTop + 3, 5, False], [-2, outTop + 2, 2, True]]

outerEdgeX = [outerEdgeSmall(i[0], i[1], i[2], i[3]) for i in outPattern]

outerEdge = outerEdgeX + Hex.transform(outerEdgeX, 0, 0, 180)

plate = Hex.basePlate()

specialPoints = [[[
	Hex.relativeToCenter(plate[i], plate[(i + 1) % 6], j, k) for k in [tileMargin, tileMargin + Hex.EdgeIndent]
	] for j in [-0.5 * Hex.TrackWidth - TrackWall, -0.5 * Hex.TrackWidth, 0.5 * Hex.TrackWidth, 0.5 * Hex.TrackWidth + TrackWall]
	] for i in range(6)]

test = [specialPoints[0][0][0], specialPoints[0][0][1], specialPoints[0][1][1], specialPoints[0][1][0]]

rampCircleCenter = Hex.add(specialPoints[0][2][1], Hex.polarPos(5, 120))
rampR1 = Hex.dist(rampCircleCenter, specialPoints[0][0][1])
rampR2 = Hex.dist(rampCircleCenter, specialPoints[0][1][1])
rampR3 = Hex.dist(rampCircleCenter, specialPoints[0][2][1])

rampLength = 45

onRampBase = [specialPoints[0][0][1],
	["arc"] + Hex.add(rampCircleCenter, Hex.polarPos(rampR1, -30)),
	Hex.add(rampCircleCenter, [rampR1, 0]),
	Hex.add(rampCircleCenter, [rampR1, -rampLength])]
onRampFlip = Hex.transform(Hex.flipY(onRampBase), 0, 0, 180)
onRampFlip.reverse()
onRampBase += onRampFlip

r1 = Hex.TileEdge + tileMargin * 2 / math.sqrt(3)
r2 = Hex.TileEdge + (tileMargin + Hex.EdgeIndent) * 2 /  math.sqrt(3)
onRampLow = [Hex.polarPos(r2, 120), Hex.polarPos(r2, 60)] + onRampBase
onRampHigh = [specialPoints[2][3][0], Hex.polarPos(r1, 120), Hex.polarPos(r1, 60), specialPoints[0][0][0]] + onRampBase

onRampWallRight = [specialPoints[0][0][0], specialPoints[0][0][1],
	["arc"] + Hex.add(rampCircleCenter, Hex.polarPos(rampR1, -30)),
	Hex.add(rampCircleCenter, [rampR1, 0]),
	Hex.add(rampCircleCenter, [rampR1, -rampLength]),
	Hex.add(rampCircleCenter, [rampR2, -rampLength]),
	Hex.add(rampCircleCenter, [rampR2, 0]),
	["arc"] + Hex.add(rampCircleCenter, Hex.polarPos(rampR2, -30)),
	specialPoints[0][1][1], specialPoints[0][1][0]]
onRampWallLeft = Hex.transform(Hex.flipY(onRampWallRight),0,0,180)

outerTopPoint = Hex.add(rampCircleCenter, [rampR3, -rampLength])
innerTopPoint = Hex.intersect(specialPoints[1][1][1], 90, outerTopPoint, 0)
topIndentX = 5.5
topIndentY = 10

onRampWallR2 = [
	specialPoints[1][1][1], specialPoints[1][1][0],
	Hex.polarPos(r1, 60),
	specialPoints[0][2][0], specialPoints[0][2][1],
	["arc"] + Hex.add(rampCircleCenter, Hex.polarPos(rampR3, -30)),
	Hex.add(rampCircleCenter, [rampR3, 0]),
	Hex.add(outerTopPoint, [0, topIndentY + topIndentX * math.tan(math.pi / 6)]),
	Hex.add(outerTopPoint, [-topIndentX, topIndentY]),
	Hex.add(outerTopPoint, [-topIndentX, 0]),
	Hex.add(innerTopPoint, [topIndentX, 0]),
	Hex.add(innerTopPoint, [topIndentX, topIndentY]),
	Hex.add(innerTopPoint, [0, topIndentY + topIndentX * math.tan(math.pi / 6)]),
]

onRampWallL2 = Hex.transform(Hex.flipY(onRampWallR2),0,0,180)

goalOut = onRampWallRight[0 : 5] + Hex.reverse(onRampWallLeft[0 : 5]) + Hex.reverse(onRampWallLeft[6 : 10]) + [
		Hex.add(onRampWallLeft[4], [-rampR2 + rampR1, -rampR2 + rampR1]),
		Hex.add(onRampWallRight[4], [rampR2 - rampR1, -rampR2 + rampR1]),
	] + onRampWallRight[6 : 10]

goalA = Hex.add(onRampWallR2[0], [0, -4])
goalB = Hex.intersect(goalA, 0, onRampWallR2[6], 90)
goalC = [0.5 * (goalA[0] + goalB[0]), goalA[1] - math.tan(math.pi / 6) * 0.5 * (goalB[0] - goalA[0])]

goalR = onRampWallR2[1 : 7] + [
		goalB,
		goalC,
		goalA,
	]
goalL = Hex.transform(Hex.flipY(goalR),0,0,180)


goalVHex = Hex.polarPos(Hex.TileHeight + tileMargin, 150)
ir = (Hex.TileHeight - Hex.EdgeIndent * 2) / math.sqrt(3)
#goalGap = onRampWallLeft[1:4] + [False] + Hex.reverse(Hex.transform(onRampWallRight[1:4], -xVec[0] * 2, 0, 0)) + [
#	Hex.add(goalVHex, Hex.polarPos(ir, -120)),
#	Hex.add(goalVHex, Hex.polarPos(ir, -60))]

#goalGap[3] = ["arc", 0.5 * (goalGap[2][0] + goalGap[4][0]), goalGap[2][1] - 0.5 * (goalGap[2][0] - goalGap[4][0])]

goalGap = [specialPoints[0][0][1],
	["arc"] + Hex.add(rampCircleCenter, Hex.polarPos(rampR1, -40)),
	Hex.add(rampCircleCenter, Hex.polarPos(rampR1, -20)),
	]
goalGap = Hex.transform(Hex.flipY(goalGap),0,0,180) + [False] + Hex.transform(Hex.reverse(goalGap), -xVec[0] * 2, 0, 0) + [
	Hex.add(goalVHex, Hex.polarPos(ir, -120)),
	Hex.add(goalVHex, Hex.polarPos(ir, -60))
	]

goalGapC = Hex.intersect(goalGap[2], 20, goalGap[4], -20)
goalGap[3] = ["arc"] + Hex.add(goalGapC, [0, -Hex.dist(goalGapC, goalGap[2])])




xDiff = boardSize[0] - outerEdge[0][0]
outerRad = xDiff / (1 - math.cos(math.pi / 6))
c1 = Hex.add(outerEdgeX[0], Hex.polarPos(outerRad, -150))
c2 = Hex.add(outerEdgeX[2 * rows - 2], Hex.polarPos(outerRad, 150))
outside = [
	[boardSize[0], boardSize[1]],
	Hex.add(c1, Hex.polarPos(outerRad, 0)),
	["arc"] + Hex.add(c1, Hex.polarPos(outerRad, 15)),
	] + outerEdgeX[0 : 2 * rows - 1] + [
	["arc"] + Hex.add(c2, Hex.polarPos(outerRad, -15)),
	Hex.add(c2, Hex.polarPos(outerRad, 0)),
	[boardSize[0], -boardSize[1]],
]

print(outerRad)

outside += Hex.transform(outside, 0, 0, 180)


if __name__ == "__main__":
	print("Writing " + str(hexCount) + "Hex Board")
	center = Hex.add(boardSize, [5,5])
	board = Hex.loadTemplate(clear = True)

	Hex.resetLength()

	makeBaseHoles(board, center)

	length10mm = Hex.getLength()
	Hex.resetLength()

	makeIndents(board, center, [1 for i in range(hexCount)])

	Hex.transformInsert(board, "3mm", outerEdge, center[0], center[1])

	y = 0.5 * (rows - 1)
	Hex.transformInsert(board, "3mm", onRampHigh, center[0] + xVec[0] + yVec[0] * y, center[1] + xVec[1] + yVec[1] * y)
	Hex.transformInsert(board, "3mm", onRampHigh, center[0] - xVec[0] + yVec[0] * (y + 1), center[1] - xVec[1] + yVec[1] * (y + 1))
	
	Hex.transformInsert(board, "3mm", onRampHigh, center[0] - xVec[0] - yVec[0] * y, center[1] - xVec[1] - yVec[1] * y, 180)
	Hex.transformInsert(board, "3mm", onRampHigh, center[0] + xVec[0] - yVec[0] * (y + 1), center[1] + xVec[1] - yVec[1] * (y + 1), 180)
	
	length3mm = Hex.getLength()
	Hex.resetLength()


	wallsX = [center[0] + xVec[0] + yVec[0] * y, center[0] - xVec[0] + yVec[0] * (y + 1)]	
	wallsY = center[1] + xVec[1] + yVec[1] * y

	wallsY2 = center[1] - xVec[1] - yVec[1] * y

	Hex.transformInsert(board, "10mm", onRampWallRight, wallsX, wallsY)
	Hex.transformInsert(board, "10mm", onRampWallLeft, wallsX, wallsY)
	Hex.transformInsert(board, "10mm", onRampWallR2, wallsX, wallsY)
	Hex.transformInsert(board, "10mm", onRampWallL2, wallsX, wallsY)
	
	Hex.transformInsert(board, "10mm", goalGap, wallsX[1], wallsY2, 180)
	
	Hex.transformInsert(board, "10mm", goalOut, wallsX, wallsY2, 180)
	Hex.transformInsert(board, "10mm", goalR, wallsX, wallsY2, 180)
	Hex.transformInsert(board, "10mm", goalL, wallsX, wallsY2, 180)
	
	Hex.transformInsert(board, "10mm", outside, center[0], center[1])
	
	length10mm += Hex.getLength()


	print("10mm Length: " + str(int(length10mm)) + "\tTime: " + str(int(length10mm / 4.1)))
	print("3mm  Length: " + str(int(length3mm)) + "\tTime: " + str(int(length3mm / 47)))
	print("Price: ~" + str(int((length3mm / 47 +  length10mm / 4.1) / 60 * 1.5) + 1) + "€")

	Hex.saveXML(board, "Board/LargeBoard_" + str(hexCount) + "Hex.svg")
