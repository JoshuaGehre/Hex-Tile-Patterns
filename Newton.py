import Hex
import math


plate = Hex.basePlate()
iPlate = Hex.indexedPlate(2)


a = Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, 0)
b = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)
c = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0)
d = Hex.relativeToCenter(plate[0], plate[1], 0.5 * Hex.TrackWidth, 0)
e = Hex.relativeToCenter(plate[2], plate[3], -0.5 * Hex.TrackWidth, 0)

contactRaise = 7
contactHeight = 7
wedgeAngle = 60
trackAngle = 15

wedgeAngleDeg = wedgeAngle
wedgeAngle *= math.pi / 360

beta = -math.atan2(contactRaise + 0.5 * Hex.TrackWidth + d[1], d[0])
wedgeHeight = (Hex.TrackWidth - contactHeight) * 0.5
wedgeX = wedgeHeight / (math.tan(math.pi * 0.5 - wedgeAngle) - math.tan(beta))
wedgeY = contactRaise + 0.5 * contactHeight + math.tan(0.5 * math.pi - wedgeAngle) * wedgeX

newtonTop = [plate[2], e,
	[-wedgeX, -wedgeY], [0, -contactRaise - 0.5 * contactHeight], [wedgeX, -wedgeY],
	d, plate[1]]

print(beta)
betaDeg = beta / math.pi * 180

sideLowered = Hex.add(d, Hex.polarPos(Hex.TrackWidth, -90 + betaDeg))

newtonSide = [b, plate[0], c,
	["arc"] + Hex.add(d, Hex.polarPos(Hex.TrackWidth, 0.5 * (-60 -90 + betaDeg * 0.5))),
	sideLowered,
	Hex.intersect(b, 90 + trackAngle, sideLowered, 180 + betaDeg)]

loweredCircle = Hex.add(b, Hex.polarPos(Hex.TrackWidth, 180 + trackAngle))

f = Hex.intersect(loweredCircle, 90 + trackAngle, sideLowered, 180 + betaDeg)
r = 1.5

newtonBottom = [plate[5], a,
	["arc"] + Hex.add(b, Hex.polarPos(Hex.TrackWidth, -170 + trackAngle)),
	loweredCircle,
	] + Hex.makeRoundCorner(f, -90 + trackAngle, -180 + betaDeg, r) + [
	Hex.add([0, -contactRaise - 0.5 * Hex.TrackWidth], Hex.polarPos(Hex.TrackWidth, -90 + betaDeg)),
	["arc"] + Hex.add([0, -contactRaise - 0.5 * Hex.TrackWidth], Hex.polarPos(Hex.TrackWidth, -90 + 0.9 * betaDeg)),
	Hex.circleLineIntersect([0, -contactRaise + 0.5 * contactHeight], -90 + 0.5 * wedgeAngleDeg, [0, -contactRaise - 0.5 * Hex.TrackWidth], Hex.TrackWidth),
	[0, -contactRaise + 0.5 * contactHeight]]


print(wedgeX)
print(wedgeY)

newtonFlip = Hex.transform(Hex.flipY(newtonBottom), 0, 0, 180)
for i in range(len(newtonFlip) - 1):
	newtonBottom.append(newtonFlip[len(newtonFlip) - 2 - i])

if __name__ == "__main__":
	print("Writing Newton")
	tileNewton = Hex.loadTemplate()

	Hex.transformInsert(tileNewton, "3mm", plate, [50, 250], 50)
	Hex.transformInsert(tileNewton, "3mm", iPlate, 50, 120)
	Hex.transformInsert(tileNewton, "3mm", iPlate, 250, 50)

	Hex.transformInsert(tileNewton, "10mm", newtonTop, [250, 150], 50)
	Hex.transformInsert(tileNewton, "10mm", newtonSide, [250, 150], 50)
	Hex.transformInsert(tileNewton, "10mm", Hex.flipY(newtonSide), [250, 150], 50, 180)
	Hex.transformInsert(tileNewton, "10mm", newtonBottom, [250, 150], 50)

	Hex.saveXML(tileNewton, "Tiles/Newton.svg")
