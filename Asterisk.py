import Hex
import math

plate = Hex.basePlate()
iPlate = Hex.indexedPlate(6)

a = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0)
b = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)
c = Hex.relativeToCenter(plate[4], plate[5], 0.5 * Hex.TrackWidth, 0)
d = Hex.relativeToCenter(plate[0], plate[1], 0.5 * Hex.TrackWidth, 0)
e = Hex.relativeToCenter(plate[2], plate[3], -0.5 * Hex.TrackWidth, 0)

x = [Hex.TrackWidth, 0]
y = Hex.polarPos(Hex.TrackWidth / math.sqrt(3), -30)

corner = [plate[0], a, x, b]
bigCorner = [plate[0], a, y, c, plate[5]]

szTop = [d, plate[1], plate[2], e]

sLowered = d[1] + Hex.TrackWidth

#print(sLowered)
fraction = (sLowered - e[1]) / (b[1] - e[1])
#print([b[0] * fraction + e[0] * (1 - fraction), b[1] * fraction + e[1] * (1 - fraction)])

sCorner = [plate[0], a,
	[
		"arc", d[0] + Hex.TrackWidth * math.sin(15 / 180 * math.pi),
		d[1] + Hex.TrackWidth * math.cos(15 / 180 * math.pi)
	],
	[d[0], sLowered], [b[0] * fraction + e[0] * (1 - fraction), sLowered], b]

zCorner = Hex.flipY(sCorner)

trapC1 = Hex.polarPos(Hex.TrackWidth, -60)
trapC2 = Hex.polarPos(Hex.TrackWidth, -120)

trapSize = 2

trapCorner = [plate[5],
	Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, 0),
	trapC1,
	[trapC1[0], trapC1[1] + trapSize],
	["arc", 0, trapC1[1] + trapSize + Hex.TrackWidth * 0.5],
	[trapC2[0], trapC2[1] + trapSize],
	trapC2,
	Hex.relativeToCenter(plate[3], plate[4], 0.5 * Hex.TrackWidth, 0),
	plate[4]]


if __name__ == "__main__":
	tileAsterisk = Hex.loadTemplate()
	tileX = Hex.loadTemplate()
	tilePeace = Hex.loadTemplate()
	tileS = Hex.loadTemplate()
	tileZ = Hex.loadTemplate()
	tile3Trap = Hex.loadTemplate()
	

	for tile in [tileAsterisk, tileX, tilePeace, tileS, tileZ, tile3Trap]:
		Hex.transformInsert(tile, "3mm", plate, 50, 50)
		Hex.transformInsert(tile, "3mm", plate, 250, 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)

	Hex.transformInsert(tileAsterisk, "10mm", corner, [150, 250], 50, [60 * i for i in range(6)])
	
	Hex.transformInsert(tileX, "10mm", corner, [150, 250], 50, [60, 240])
	Hex.transformInsert(tileX, "10mm", bigCorner, [150, 250], 50, [0, 180])

	Hex.transformInsert(tilePeace, "10mm", corner, [150, 250], 50, [60, 120])
	Hex.transformInsert(tilePeace, "10mm", bigCorner, [150, 250], 50, [0, -120])

	Hex.transformInsert(tileS, "10mm", szTop, [150, 250], 50, [0, 180])
	Hex.transformInsert(tileS, "10mm", sCorner, [150, 250], 50, [0, 180])

	Hex.transformInsert(tileZ, "10mm", szTop, [150, 250], 50, [0, 180])
	Hex.transformInsert(tileZ, "10mm", zCorner, [150, 250], 50, [0, 180])

	Hex.transformInsert(tile3Trap, "10mm", trapCorner, [150, 250], 50, [0, 120, 240])

	Hex.saveXML(tileAsterisk, "Tiles/Asterisk.svg")
	Hex.saveXML(tileX, "Tiles/X.svg")
	Hex.saveXML(tilePeace, "Tiles/Peace.svg")
	Hex.saveXML(tileS, "Tiles/S.svg")
	Hex.saveXML(tileZ, "Tiles/Z.svg")
	Hex.saveXML(tile3Trap, "Tiles/3Trap.svg")
