import Hex
import math

rows = 4
holeHeight = 35.5
tileMargin = 1.5

boardSize = [170, 70 + 0.5 * (Hex.TileHeight + tileMargin) * rows]
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

	name1 = "10mm" if "10mm" in board else "mid"
	name2 = "10mm" if "10mm" in board else "late"

	#for i in range(6):
	#	Hex.transformInsert(board, name1, outerBaseHole, center[0], center[1], i * 60)
	
	Hex.transformInsert(board, name2, rectangle, center[0], center[1])

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

if __name__ == "__main__":
	print("Writing " + str(hexCount) + "Hex Board")
	board = Hex.loadTemplate(clear = True)
	center = Hex.add(boardSize, [5,5])

	Hex.resetLength()

	makeBaseHoles(board, center)

	length10mm = Hex.getLength()
	Hex.resetLength()

	makeIndents(board, center, [1 for i in range(hexCount)])

	Hex.transformInsert(board, "3mm", outerEdge, center[0], center[1])

	length3mm = Hex.getLength()

	print("10mm Length: " + str(int(length10mm)) + "\tTime: " + str(int(length10mm / 4.1)))
	print("3mm  Length: " + str(int(length3mm)) + "\tTime: " + str(int(length3mm / 47)))
	print("Price: ~" + str(int((length3mm / 47 +  length10mm / 4.1) / 60 * 1.5) + 1) + "€")

	Hex.saveXML(board, "Board/LargeBoard_" + str(hexCount) + "Hex.svg")
