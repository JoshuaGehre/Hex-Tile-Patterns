import math
import Hex

tileSpacing = 7
height = tileSpacing * 2 + Hex.TileHeight
width = tileSpacing * 3 + Hex.TileEdge * 4
centerOffset = tileSpacing * 0.5 + Hex.TileEdge

thickness = 12
bottom = [0, 7]
angle = 37.5

displayRect = [[width * 0.5, height * 0.5], [width * 0.5, -height * 0.5], [-width * 0.5, -height * 0.5], [-width * 0.5, height * 0.5]]
iPlate = Hex.indexedPlate(1)
slots = ["group", Hex.transform(iPlate, -centerOffset, 0, 0), Hex.transform(iPlate, centerOffset, 0, 0)]
holeHeight = 35.5
holeEdge = holeHeight / math.sqrt(3)
hole = [Hex.polarPos(holeEdge, i * 60) for i in range(6)]
holes = ["group", Hex.transform(hole, -centerOffset, 0, 0), Hex.transform(hole, centerOffset, 0, 0)]

stand = [Hex.polarPos(height - 1, angle), [0,0], Hex.polarPos(thickness, angle + 90)]
stand += [Hex.intersect(bottom, 0, stand[2], 90), Hex.intersect(bottom, 0, stand[0], 90)]

bHeight = stand[0][0] - stand[2][0]
baseRect = [[width * 0.5, bHeight * 0.5], [width * 0.5, -bHeight * 0.5], [-width * 0.5, -bHeight * 0.5], [-width * 0.5, bHeight * 0.5]]

edgeHeight = 5
edgeWidth = width - 19.5
edgeRect = [[edgeWidth * 0.5, edgeHeight * 0.5], [edgeWidth * 0.5, -edgeHeight * 0.5], [-edgeWidth * 0.5, -edgeHeight * 0.5], [-edgeWidth * 0.5, edgeHeight * 0.5]]

if __name__ == "__main__":
	print("Writing Board")
	board = Hex.loadTemplate(clear = True)
	x0 = 0.5 * width + 10
	y0 = 0.5 * height + 10
	
	Hex.transformInsert(board, "3mm", displayRect, x0, y0, 0)
	Hex.transformInsert(board, "3mm", slots, x0, y0, 0)
	Hex.transformInsert(board, "10mm", displayRect, x0, y0, 0)
	Hex.transformInsert(board, "10mm", holes, x0, y0, 0)

	Hex.transformInsert(board, "10mm", stand, 10 - stand[2][0], 140, 0)
	Hex.transformInsert(board, "10mm", Hex.flipY(stand), 140, 140, 180)
	
	Hex.transformInsert(board, "3mm", baseRect, x0 * 3, y0, 0)
	Hex.transformInsert(board, "3mm", edgeRect, x0 * 3, [90, 100], 0)

	Hex.saveXML(board, "Board/Display.svg")
