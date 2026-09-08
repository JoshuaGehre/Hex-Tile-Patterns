import Hex
import math

pad = 7
displayAngle = 42
edgeOverhang = 15
displayHeight = 10

boardSize = [0.5 * (Hex.TileEdge * 4 + pad * 3), 0.5 * (Hex.TileHeight + pad * 2)]

rectangle = [
	[boardSize[0], boardSize[1]],
	[boardSize[0], -boardSize[1]],
	[-boardSize[0], -boardSize[1]],
	[-boardSize[0], boardSize[1]]]

center = Hex.add(boardSize, [3, 3])

holeHeight = 35.5
holeEdge = holeHeight / math.sqrt(3)

hole10mm = [Hex.polarPos(holeEdge, i * 60) for i in range(6)]

holeOffset = 0.5 * pad + Hex.TileEdge

iPlate = Hex.indexedPlate(1)

displayLong = 2 * (edgeOverhang + boardSize[1])
displayBottom = displayLong * math.cos(displayAngle * math.pi / 180.0)

a = [0, -displayHeight]
b = Hex.add(a, Hex.polarPos(displayLong, displayAngle))

leg = [[0, 0], [displayBottom, 0], b,
	Hex.relativeToCenter(b, a, -boardSize[1], 0),
	Hex.relativeToCenter(b, a, -boardSize[1], -10),
	Hex.relativeToCenter(b, a, boardSize[1], -10),
	Hex.relativeToCenter(b, a, boardSize[1], 0),
	a]



if __name__ == "__main__":
	print("Writing Tile Stand")
	board = Hex.loadTemplate(clear = True)
	
	Hex.transformInsert(board, "10mm", rectangle, center[0], center[1])
	Hex.transformInsert(board, "10mm", hole10mm, center[0] - holeOffset, center[1])
	Hex.transformInsert(board, "10mm", hole10mm, center[0] + holeOffset, center[1])
	Hex.transformInsert(board, "10mm", leg, displayBottom + 6, 145)
	Hex.transformInsert(board, "10mm", Hex.flipY(leg), displayBottom + 3, 145, 180)

	Hex.transformInsert(board, "3mm", rectangle, center[0], center[1])
	Hex.transformInsert(board, "3mm", iPlate, center[0] - holeOffset, center[1])
	Hex.transformInsert(board, "3mm", iPlate, center[0] + holeOffset, center[1])
	
	Hex.saveXML(board, "Board/TileStand.svg")
