import Hex
import DIC
import Asterisk
import Deco

plate = Asterisk.plate
iPlate = Asterisk.iPlate

indentCorner = [DIC.b2,
	["arc"] + Hex.add(plate[0], Hex.polarPos(0.5 * (Hex.TileEdge + Hex.TrackWidth), -130)),
	Hex.circleLineIntersect(Asterisk.y, -150, plate[0], 0.5 * (Hex.TileEdge + Hex.TrackWidth)),
	Asterisk.y, Asterisk.c, plate[5]]

C3Part = DIC.partIC[2:-1]

C3Part = C3Part + Hex.transform(C3Part, 0, 0, 120) + Hex.transform(C3Part, 0, 0, 240)



bobbinPos = 15
bobbin = Hex.transform(["group", Deco.makeCircle(6.2 / 2), Deco.makeCircle(21 / 2)], -bobbinPos, 0, 0)

bobbins = ["group", bobbin, Hex.transform(bobbin, 0, 0, 120), Hex.transform(bobbin, 0, 0, -120)]

aligner = Hex.transform(Deco.makeAlignerCircle(2.9), -bobbinPos, 0, 0)
aligners = ["group", aligner, Hex.transform(aligner, 0, 0, 120), Hex.transform(aligner, 0, 0, -120)]

holdPin = Hex.transform(Deco.makeCircle(3), -bobbinPos, 0, 0)
holdPins = ["group", holdPin, Hex.transform(holdPin, 0, 0, 120), Hex.transform(holdPin, 0, 0, -120)]

if __name__ == "__main__":
	tileXefros = Hex.loadTemplate()
	tileBobbin = Hex.loadTemplate()
	
	for tile in [tileXefros, tileBobbin]:
		Hex.transformInsert(tile, "3mm", plate, [50, 250], 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
	
	Hex.transformInsert(tileXefros, "10mm", Asterisk.corner, [150, 250], 50, [60, -120])
	Hex.transformInsert(tileXefros, "10mm", DIC.roundCorner, [150, 250], 50, [0, 120])
	Hex.transformInsert(tileXefros, "10mm", indentCorner, [150, 250], 50, 0)
	Hex.transformInsert(tileXefros, "10mm", Hex.flipY(indentCorner), [150, 250], 50, 120)
	
	Hex.transformInsert(tileBobbin, "10mm", DIC.roundCorner, [150, 250], 50, [0, 120, 240])

	Hex.transformInsert(tileBobbin, "10mm", C3Part, [150, 250], 50, 0)
	Hex.transformInsert(tileBobbin, "10mm", aligners, [150, 250], 50, 0, z=False)
	Hex.transformInsert(tileBobbin, "10mm", holdPins, 150, 120, 0)
	Hex.transformInsert(tileBobbin, "10mm", holdPins, 250, 50, 0)
	
	Hex.saveXML(tileXefros, "Tiles/Xefros.svg")
	Hex.saveXML(tileBobbin, "Tiles/Bobbin.svg")
