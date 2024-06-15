import Hex
import DIC
import Asterisk

plate = Asterisk.plate
iPlate = Asterisk.iPlate


indentCorner = [DIC.b2,
	["arc"] + Hex.add(plate[0], Hex.polarPos(0.5 * (Hex.TileEdge + Hex.TrackWidth), -130)),
	Hex.circleLineIntersect(Asterisk.y, -150, plate[0], 0.5 * (Hex.TileEdge + Hex.TrackWidth)),
	Asterisk.y, Asterisk.c, plate[5]]

if __name__ == "__main__":
	tileXefros = Hex.loadTemplate()
	
	for tile in [tileXefros]:
		Hex.transformInsert(tile, "3mm", plate, [50, 250], 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
	
	Hex.transformInsert(tileXefros, "10mm", Asterisk.corner, [150, 250], 50, [60, -120])
	Hex.transformInsert(tileXefros, "10mm", DIC.roundCorner, [150, 250], 50, [0, 120])
	Hex.transformInsert(tileXefros, "10mm", indentCorner, [150, 250], 50, 0)
	Hex.transformInsert(tileXefros, "10mm", Hex.flipY(indentCorner), [150, 250], 50, 120)
	
	Hex.saveXML(tileXefros, "Tiles/Xefros.svg")
