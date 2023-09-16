import Hex
import math

tileMargin = 1.5
holeHeight = 35.5
boardSize = [125, 137.5]
TrackWall = 8

holeEdge = holeHeight / math.sqrt(3)

xVec = Hex.polarPos(Hex.TileHeight + tileMargin, 30)
yVec = Hex.polarPos(Hex.TileHeight + tileMargin, 90)


def makeHole(x, y):
	center = [xVec[0] * x + yVec[0] * y, xVec[1] * x + yVec[1] * y]
	return [Hex.add(center, Hex.polarPos(holeEdge, i * 60)) for i in range(6)]

def insertHole(xml, center, x, y):
	name = "10mm" if "10mm" in xml else "mid"
	Hex.transformInsert(xml, name, makeHole(x, y), center[0], center[1])

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

def outerEdgeSmall(x, y, pos, out=True):
	center = [xVec[0] * x + yVec[0] * y, xVec[1] * x + yVec[1] * y]
	r = (Hex.TileHeight - Hex.EdgeIndent * 2) / math.sqrt(3)
	if out:
		r += (Hex.EdgeIndent * 2 + tileMargin) * 2 / math.sqrt(3)
	return Hex.add(center, Hex.polarPos(r, pos * 60))

outerEdgeX = [outerEdgeSmall(i[0], i[1], i[2], i[3]) for i in [
	[2, -1, 3, False],
	[1, 0, 0, True],
	[1, 0, 1, True],
	]]

outerEdge = []
for i in range(6):
	outerEdge += Hex.transform(outerEdgeX, 0, 0, 60 * i)

#print(Hex.dist(outerEdge[4], outerEdge[5]))

offset = [Hex.dist(outerEdge[0], outerEdge[1]) * 0.5, 0]
#print(offset[0])

outerBaseTmpPoint = Hex.add(offset, outerEdge[1])
outerBaseCenter = Hex.intersect([0,0], 0, outerBaseTmpPoint, -150)
outerBaseHole = [
	outerEdge[17],outerEdge[0], outerEdge[1],
	outerBaseTmpPoint,
	["arc"] + Hex.add(outerBaseCenter, [Hex.dist(outerBaseCenter, outerBaseTmpPoint), 0]),
	#Hex.add(offset, outerEdge[0]),
	Hex.add(offset, outerEdge[17])]

rectangle = [
	[boardSize[0], boardSize[1]],
	[boardSize[0], -boardSize[1]],
	[-boardSize[0], -boardSize[1]],
	[-boardSize[0], boardSize[1]]]

def make7Holes(board, center):
	insertHole(board, center, -1, 0)
	insertHole(board, center, -1, 1)
	insertHole(board, center, 0, 0)
	insertHole(board, center, 0, 1)
	insertHole(board, center, 0, -1)
	insertHole(board, center, 1, 0)
	insertHole(board, center, 1, -1)

	name1 = "10mm" if "10mm" in board else "mid"
	name2 = "10mm" if "10mm" in board else "late"

	for i in range(6):
		Hex.transformInsert(board, name1, outerBaseHole, center[0], center[1], i * 60)
	
	Hex.transformInsert(board, name2, rectangle, center[0], center[1])


def make7Indents(board, center, i):
	insertIndexPlate(board, center, -1, 0, i[0])
	insertIndexPlate(board, center, -1, 1, i[1])
	insertIndexPlate(board, center, 0, -1, i[2])
	insertIndexPlate(board, center, 0, 0, i[3])
	insertIndexPlate(board, center, 0, 1, i[4])
	insertIndexPlate(board, center, 1, 0, i[5])
	insertIndexPlate(board, center, 1, -1, i[6])

t4 = outerEdge[4]
t5 = outerEdge[5]
a = Hex.relativeToCenter(t4, t5, -Hex.TrackWidth * 0.5 - TrackWall, 0)
b = Hex.relativeToCenter(t4, t5, -Hex.TrackWidth * 0.5, 0)
c = Hex.relativeToCenter(t4, t5, Hex.TrackWidth * 0.5, 0)
d = Hex.relativeToCenter(t4, t5, Hex.TrackWidth * 0.5 + TrackWall, 0)

mInset = [0, Hex.EdgeIndent]

aX = Hex.add(a, mInset)


"""
m = [0, c[1] - 35]
r = 15
x = 5
smallRampM = [
	Hex.add(d, mInset), Hex.add(c, mInset),
	Hex.circleLineIntersect(c, -90, m, r),
	["arc"] + Hex.add(m, Hex.polarPos(r, -135)),
	[-r, m[1]],
	[-r, m[1] - x],
	[r, m[1] - x],
	[r, m[1]],
	["arc"] + Hex.add(m, Hex.polarPos(r, -45)),
	Hex.circleLineIntersect(b, -90, m, r),
	Hex.add(b, mInset), aX,
	Hex.circleLineIntersect(a, -90, m, r + 10),
	["arc"] + Hex.add(m, Hex.polarPos(r + 10, -45)),
	[r + 10, m[1]],
	Hex.add(m, [r + 10, -10 - x]),
	Hex.add(m, [-r - 10, -10 - x]),
	[-r - 10, m[1]],
	["arc"] + Hex.add(m, Hex.polarPos(r + 10, -135)),
	Hex.circleLineIntersect(d, -90, m, r + 10),
	]
"""

m = [0, c[1] - 37]
r = 15
x = 3

y1 = Hex.add(m, Hex.polarPos(r, -120))
y2 = Hex.add(m, Hex.polarPos(r, -60))

y3 = Hex.add(m, Hex.polarPos(r + 10, -130))
y4 = Hex.add(m, Hex.polarPos(r + 10, -50))

smallRampM = [
	Hex.add(d, mInset), Hex.add(c, mInset),
	Hex.intersect(y1, -30, c, 90),
	Hex.intersect(y1, 150, [-r, m[1]], 90),
	[-r, m[1] - x],
	[r, m[1] - x],
	Hex.intersect(y2, -150, [r, m[1]], 90),
	Hex.intersect(y2, 30, b, 90),
	Hex.add(b, mInset), aX,
	Hex.intersect(y4, 30, a, 90),
	Hex.intersect(y4, 30, [r +10, m[1]], 90),
	[r + 10, m[1] - 10 - x],
	[-r - 10, m[1] - 10 - x],
	Hex.intersect(y3, -30, [-r - 10, m[1]], 90),
	y3,
	Hex.intersect(y3, -30, d, 90),
	]

#print(Hex.add(m, [-r - 10, -10 - x]))

aPos = 0
for i in range(len(smallRampM)):
	if smallRampM[i] == aX:
		aPos = i

smallRampB1M = [Hex.add(d, mInset)]
for i in range(aPos, len(smallRampM)):
	smallRampB1M += [smallRampM[i]]

smallRampB2M = [i for i in smallRampB1M]
for i in range(2):
	smallRampB2M[i] = Hex.add(smallRampB2M[i], [0, -Hex.EdgeIndent])

rampCenter = [t4[0] + outerEdge[2][0] - outerEdge[3][0], t4[1]]

da = Hex.dist(rampCenter, d)
db = Hex.dist(rampCenter, c)
dc = Hex.dist(rampCenter, b)
dd = Hex.dist(rampCenter, a)

rInset = Hex.polarPos(Hex.EdgeIndent, -150)

sRRD = Hex.add(rampCenter, Hex.polarPos(dd, -60))
sRRC = Hex.add(rampCenter, Hex.polarPos(dc, -60))
sRRB = Hex.add(rampCenter, Hex.polarPos(db, -60))
sRRA = Hex.add(rampCenter, Hex.polarPos(da, -60))

smallRampR = [
	Hex.add(rampCenter, Hex.polarPos(dd, 0)),
	["arc"] + Hex.add(rampCenter, Hex.polarPos(dd, -30)),
	sRRD,
	Hex.add(rInset, sRRD),
	Hex.add(rInset, sRRC),
	sRRC,
	["arc"] + Hex.add(rampCenter, Hex.polarPos(dc, -30)),
	Hex.add(rampCenter, Hex.polarPos(dc, 0)),
] + Hex.transform([smallRampM[i] for i in range(2, aPos - 1)], da + dd, 0, 0) + [
	Hex.add(rampCenter, Hex.polarPos(db, 0)),
	["arc"] + Hex.add(rampCenter, Hex.polarPos(db, -30)),
	sRRB,
	Hex.add(rInset, sRRB),
	Hex.add(rInset, sRRA),
	sRRA,
	["arc"] + Hex.add(rampCenter, Hex.polarPos(da, -30)),
	Hex.add(rampCenter, Hex.polarPos(da, 0))
] + Hex.transform([smallRampM[i] for i in range(aPos + 1, len(smallRampM))], da + dd, 0, 0)

smallRampB1R = [smallRampR[i] for i in range(4)] + [smallRampR[i] for i in range(aPos + 9, len(smallRampR))]
smallRampB2R = [smallRampR[i] for i in range(3)] + [smallRampR[i] for i in range(aPos + 10, len(smallRampR))]

smallRampL = Hex.transform(Hex.flipY(smallRampR), 0, 0, 180)
smallRampB1L = Hex.transform(Hex.flipY(smallRampB1R), 0, 0, 180)
smallRampB2L = Hex.transform(Hex.flipY(smallRampB2R), 0, 0, 180)

if __name__ == "__main__":
	print("Writing Tiny Board")
	board = Hex.loadTemplate(clear = True)

	center = Hex.add(boardSize, [5,5])
	Hex.resetLength()

	make7Holes(board, center)
	Hex.transformInsert(board, "10mm", smallRampM, center[0], center[1], [0, 180])
	Hex.transformInsert(board, "10mm", smallRampR, center[0], center[1], [0, 180])
	Hex.transformInsert(board, "10mm", smallRampL, center[0], center[1], [0, 180])

	length10mm = Hex.getLength()
	Hex.resetLength()

	make7Indents(board, center, [2, 3, "x-xx-x", 6, 6, 6, 6])
	Hex.transformInsert(board, "3mm", outerEdge, center[0], center[1])
	Hex.transformInsert(board, "3mm", smallRampB1M, center[0], center[1], [0, 180])
	Hex.transformInsert(board, "3mm", smallRampB2M, center[0], center[1], [0, 180])
	Hex.transformInsert(board, "3mm", smallRampB1R, center[0], center[1], [0, 180])
	Hex.transformInsert(board, "3mm", smallRampB2R, center[0], center[1], [0, 180])
	Hex.transformInsert(board, "3mm", smallRampB1L, center[0], center[1], [0, 180])
	Hex.transformInsert(board, "3mm", smallRampB2L, center[0], center[1], [0, 180])

	length3mm = Hex.getLength()

	print("10mm Length: " + str(int(length10mm)) + "\tTime: " + str(int(length10mm / 4.1)))
	print("3mm  Length: " + str(int(length3mm)) + "\tTime: " + str(int(length3mm / 47)))
	print("Price: ~" + str(int((length3mm / 47 +  length10mm / 4.1) / 60 * 1.5) + 1) + "€")

	Hex.saveXML(board, "Board/TinyBoard.svg")
