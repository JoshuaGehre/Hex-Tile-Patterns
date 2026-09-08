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

# Version 2
angle = 5

d2 = Hex.add(d, Hex.polarPos(Hex.TrackWidth, -angle))
a2 = Hex.add(a, Hex.polarPos(Hex.TrackWidth, 60 + angle))

rv2 = 10
center2 = Hex.add(Hex.intersect(d2, -90 - angle, a2, 150 + angle), Hex.polarPos(rv2, 30))
rv2 *= math.sin((60 - angle) / 180.0 * math.pi)

offset2 = 2.5

smallCorner2 = [
	plate[1], c,
	["arc"] + Hex.add(d, Hex.polarPos(Hex.TrackWidth, -0.5 * angle)),
	d2,
	Hex.add(center2, Hex.polarPos(rv2, 180 - angle)),
	["arc"] + Hex.add(center2, Hex.polarPos(rv2, -150)),
	Hex.add(center2, Hex.polarPos(rv2, -120 + angle)),
	a2,
	["arc"] + Hex.add(a, Hex.polarPos(Hex.TrackWidth, 60 + 0.5 * angle)),
	b, plate[0]]

a3 = Hex.intersect(d2, -90 - angle, a, 150 + angle)
d3 = Hex.intersect(d, -90 - angle, a2, 150 + angle)

tw_sqrt2 = Hex.TrackWidth / math.sqrt(2)

trapPartD = [
	a3, 
	["arc"] + Hex.add(a3, Hex.polarPos(tw_sqrt2, 180 - angle + 45)),
	Hex.add(a3, Hex.polarPos(Hex.TrackWidth, 180 - angle)),
]

trapOffsetD = Hex.polarPos(offset2, -90 - angle)
trapOffsetL = Hex.polarPos(offset2, 150 + angle)

trapPartL = [
	Hex.add(d3, Hex.polarPos(Hex.TrackWidth, -120 + angle)),
	["arc"] + Hex.add(d3, Hex.polarPos(tw_sqrt2, -120 + angle - 45)),
	d3,
]

largeCorner2 = [
	plate[4], plate[5],
	a, a3
	] + Hex.transform(trapPartD, trapOffsetD[0], trapOffsetD[1], 0) + [
	Hex.intersect(d, -90 - angle, a, 150 + angle)
	] + Hex.transform(trapPartL, trapOffsetL[0], trapOffsetL[1], 0) + [
	d3, d,
	plate[2], plate[3]]

if __name__ == "__main__":
	tile2Trap = Hex.loadTemplate()
	tile2Trap2 = Hex.loadTemplate()

	print("Writing 2 Trap")
	for tile in [tile2Trap, tile2Trap2]:
		Hex.transformInsert(tile, "3mm", plate, 50, 50)
		Hex.transformInsert(tile, "3mm", plate, 250, 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
	
	Hex.transformInsert(tile2Trap, "10mm", smallCorner, [150, 250], 50, 0)
	Hex.transformInsert(tile2Trap, "10mm", largeCorner, [150, 250], 50, 0)

	Hex.transformInsert(tile2Trap2, "10mm", smallCorner2, [150, 250], 50, 0)
	Hex.transformInsert(tile2Trap2, "10mm", largeCorner2, [150, 250], 50, 0)

	#Hex.saveXML(tile2Trap, "Tiles/2Trap.svg")
	Hex.saveXML(tile2Trap2, "Tiles/2Trap_v2.svg")
