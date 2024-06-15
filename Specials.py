import Hex
import Deco
import math

plate = Hex.basePlate()
iPlate1 = Hex.indexedPlate(1)
iPlate3 = Hex.indexedPlate("xx---x")
iPlate6 = Hex.indexedPlate(6)

a = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, 0)
b = Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth, 0)

c = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)

recHexEdge = 8.5
recHexPad = 3

recHexCenter = [0, -recHexPad - recHexEdge * math.sqrt(3)]
smallHex = [Hex.add(recHexCenter, Hex.polarPos(recHexEdge, 60 - 60 * i)) for i in range(6)]

recursionPiece = [plate[1], a, Hex.intersect(smallHex[1], 120, a, 90), smallHex[1], smallHex[2], smallHex[3], smallHex[4], Hex.intersect(smallHex[4], 60, b, 90), b]

recursionRipple = Deco.makeRipple(smallHex[2], smallHex[3], outwards=True)

recursion = []
for i in range(6):
	recursion += Hex.transform(recursionPiece, 0, 0, 60 * i)

star = Deco.makeStar()

bombRadius = 18

bombPiece = [plate[1], a, Hex.circleLineIntersect(a, 90, [0, 0], bombRadius),
	["arc", bombRadius, 0], [0, bombRadius], ["arc", -bombRadius, 0],
	Hex.circleLineIntersect(b, 90, [0, 0], bombRadius), b]

bombOutside = [plate[1]] + Deco.makeRipple(a, b)

bombRadiusI = bombRadius - 4
bombRadiusO = bombRadius + 4

a1 = Hex.add(a, [2, 0])
a2 = Hex.add(a, [-3.5, 0])
b1 = Hex.add(b, [-2, 0])
b2 = Hex.add(b, [3.5, 0])

bombShield = [a2, Hex.circleLineIntersect(a2, 90, [0,0], bombRadiusI),
	["arc", bombRadiusI, 0], [0, bombRadiusI], ["arc", -bombRadiusI, 0],
	Hex.circleLineIntersect(b2, 90, [0,0], bombRadiusI), b2,
	b1, Hex.circleLineIntersect(b1, 90, [0,0], bombRadiusO),
	["arc", -bombRadiusO, 0], [0, bombRadiusO], ["arc", bombRadiusO, 0],
	Hex.circleLineIntersect(a1, 90, [0,0], bombRadiusO), a1,
]

bombTop = [a, Hex.circleLineIntersect(a, 90, [0, 0], bombRadiusI),
	["arc", 0, -bombRadiusI],
	Hex.circleLineIntersect(b, 90, [0, 0], bombRadiusI), b]

for i in range(5):
	bombPiece += Hex.transform(bombOutside, 0, 0, 60 * (i + 1))

rhsbtPart = [plate[0], plate[1]] + Deco.makeArcRipple(a, c, Hex.polarPos(Hex.TileHeight, 30))

arcPositions = [4.5, 9.5, 14.5]
for i in range(len(arcPositions)):
	x = Hex.TileEdge * 1.5
	r = 32
	arcPositions[i] = [arcPositions[i], x - math.sqrt(r**2 - arcPositions[i]**2)]

print(arcPositions)

arcs = []

for i in range(len(arcPositions)):
	d = arcPositions[i][1]
	arcs.append([
		[d + 1.5, 0], [d + 1.5, 11], ["arc", 0, 11 + d + 1.5], [-d - 1.5, 11], [-d -1.5, 0],
		[-d + 1.5, 0], [-d + 1.5, 11], ["arc", 0, 11 + d - 1.5], [d - 1.5, 11], [d -1.5, 0],
		])

square = [[1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5], [1.5, -1.5]]

flameR1 = 9
flameR2 = 8
flameA1 = 140
flameA2 = 45
flameCX = Hex.polarPos(flameR1 + flameR2, flameA2)
flame = [
	Hex.polarPos(flameR1, flameA1),
	["arc"] + Hex.polarPos(flameR1, -135),
	Hex.polarPos(flameR1, -90),
	["arc"] + Hex.polarPos(flameR1, -45),
	Hex.polarPos(flameR1, flameA2),
	["arc"] + Hex.add(flameCX, Hex.polarPos(flameR2, -170)),
	Hex.add(flameCX, Hex.polarPos(flameR2, 150)),
	["arc", -2, -12],
	[-2, -2],
	["arc", -5, -4],
	Hex.polarPos(flameR1, flameA1),
]

rhsbtLeft = ["group", Hex.transform(rhsbtPart, 0, 0, 180)]
rhsbtRight = ["group", Hex.flipY(rhsbtPart)]

for x in arcPositions:
	rhsbtRight.append(Hex.transform(square, +x[1], 25 - x[0], 0))
	rhsbtLeft.append(Hex.transform(square, -x[1], 25 - x[0], 0))

plateRHSBT = ["group", plate, flame]
plateBomb = ["group", plate, star]

if __name__ == "__main__":
	print("Writing Tiles")
	tileRHSBT = Hex.loadTemplate()
	tileRecursion = Hex.loadTemplate()
	tileBomb = Hex.loadTemplate()

	for tile, iPlate in [(tileRHSBT, iPlate1), (tileRecursion, iPlate6), (tileBomb, iPlate3)]:
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)

	Hex.transformInsert(tileRecursion, "3mm", plate, [50, 250], 50)
	Hex.transformInsert(tileBomb, "3mm", plateBomb, [50, 250], 50)
	Hex.transformInsert(tileRHSBT, "3mm", plateRHSBT, [50, 250], 50)

	Hex.transformInsert(tileRecursion, "10mm", recursion, [250, 150], 50)
	Hex.transformInsert(tileRecursion, "3mm", recursionRipple, [250, 50], 50, [i * 60 for i in range(6)], z=False)
	Hex.transformInsert(tileRecursion, "3mm", star, 250, 50)
	Hex.transformInsert(tileRecursion, "3mm", star, 50, 85)
	
	Hex.transformInsert(tileBomb, "10mm", bombPiece, [250, 150], 50)
	Hex.transformInsert(tileBomb, "3mm", bombShield, 250, 50)
	Hex.transformInsert(tileBomb, "3mm", bombShield, 50, 190)
	Hex.transformInsert(tileBomb, "3mm", bombTop, 250, 50)
	Hex.transformInsert(tileBomb, "3mm", bombTop, 50, 210)
	
	Hex.transformInsert(tileRHSBT, "10mm", rhsbtLeft, [250, 150], 50)
	Hex.transformInsert(tileRHSBT, "10mm", rhsbtRight, [250, 150], 50)
	
	Hex.transformInsert(tileRHSBT, "3mm", star, 229, 52)
	Hex.transformInsert(tileRHSBT, "3mm", star, 50, 85)
	
	for i in range(len(arcs)):
		Hex.transformInsert(tileRHSBT, "3mm", arcs[i], 50, 150 + 30 * i)
	
	Hex.saveXML(tileRHSBT, "Tiles/RHSBT.svg")
	Hex.saveXML(tileRecursion, "Tiles/Recursion.svg")
	Hex.saveXML(tileBomb, "Tiles/Bomb.svg")
