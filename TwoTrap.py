import Hex
import math


plate = Hex.basePlate()
iPlate = Hex.indexedPlate("xx-xx-")

a = Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, 0)
b = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)

c = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, 0)
d = Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth, 0)

smallRadius = 25
trapSize = 2.5
offset = 0.5

center = Hex.polarPos((Hex.TrackWidth * 0.5 + smallRadius) * 2 / math.sqrt(3), 30)

smallCorner = [
	plate[1], c,
	Hex.add(center, [-smallRadius, 0]),
	["arc"] + Hex.add(center, Hex.polarPos(smallRadius, -150)),
	Hex.add(center, Hex.polarPos(smallRadius, -120)),
	b, plate[0]]

trapC1 = Hex.add(Hex.polarPos(Hex.TrackWidth, -60), Hex.polarPos(offset, 150))


trapLeft = trapC1[0] - Hex.TrackWidth

largeCorner = [plate[4], plate[5], a, trapC1,
	Hex.add(trapC1, [0, trapSize]),
	["arc"] + Hex.add(trapC1, [-0.5 * Hex.TrackWidth, trapSize + 0.5 * Hex.TrackWidth]),
	Hex.add(trapC1, [-Hex.TrackWidth, trapSize]),
	[trapLeft, -trapLeft * math.tan(30 / 180 * math.pi)]
	]

largeCornerX = Hex.transform(Hex.flipY(largeCorner), 0, 0, 60)

for i in range(len(largeCornerX) - 1):
	largeCorner.append(largeCornerX[len(largeCornerX) - 2 - i])


if __name__ == "__main__":
	tile2Trap = Hex.loadTemplate()

	print("Writing 2 Trap")
	for tile in [tile2Trap]:
		Hex.transformInsert(tile, "3mm", plate, 50, 50)
		Hex.transformInsert(tile, "3mm", plate, 250, 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
	
	Hex.transformInsert(tile2Trap, "10mm", smallCorner, [150, 250], 50, 0)
	Hex.transformInsert(tile2Trap, "10mm", largeCorner, [150, 250], 50, 0)

	Hex.saveXML(tile2Trap, "Tiles/2Trap.svg")
