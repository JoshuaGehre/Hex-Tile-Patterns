import Hex
import math
#import Flipper

plate = Hex.basePlate()
iPlate = Hex.indexedPlate(1)

a1 = Hex.relativeToCenter(plate[3], plate[4], -0.5 * Hex.TrackWidth - 0.5, 0)
a2 = Hex.relativeToCenter(plate[3], plate[4], 0.5 * Hex.TrackWidth, 0)
b1 = Hex.relativeToCenter(plate[4], plate[5], -0.5 * Hex.TrackWidth, 0)
b2 = Hex.relativeToCenter(plate[4], plate[5], 0.5 * Hex.TrackWidth, 0)
c1 = Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, 0)
c2 = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth + 0.5, 0)
d1 = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, 0)
d2 = Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth, 0)

flipperCircle = Hex.makeCircle(1.85)
flipperCircleBase = Hex.makeCircle(0.75)
pachinkoPin = Hex.makeCircle(0.5)

def half(a1, a2):
	a = (a1 + a2) / 2
	if a1 > a2:
		a += 180
	return a

def aShift(r):
	return 90 / r

def makeFlipper(a1, r1, a2, r2, a3, r3, ri):
	d1 = aShift(r1)
	d2 = aShift(r2)
	d3 = aShift(r3)
	return [
		Hex.polarPos(r1, a1 - d1),
		["arc"] + Hex.polarPos(r1, a1),
		Hex.polarPos(r1, a1 + d1),
		Hex.polarPos(ri, half(a1, a2)),
		Hex.polarPos(r2, a2 - d2),
		["arc"] + Hex.polarPos(r2, a2),
		Hex.polarPos(r2, a2 + d2),
		Hex.polarPos(ri, half(a2, a3)),
		Hex.polarPos(r3, a3 - d3),
		["arc"] + Hex.polarPos(r3, a3),
		Hex.polarPos(r3, a3 + d3),
		Hex.polarPos(ri, half(a3, a1)),
	]

# Position of the flipper centers
lCenter = [-10, 11]
rCenter = [10, 11]

# Geometry of the flippers
leftLong = 17
rightLong = 27
lrShort = 8
leftFlipper = makeFlipper(90, leftLong, 210, lrShort, -30, lrShort, 4)
rightFlipper = makeFlipper(90, rightLong, 210, lrShort, -30, lrShort, 4)

# Minimum and maximum rotation of both flippers
leftRot = [-55, 25]
rightRot = [-20, 30]

rLeftInner = Hex.dist(a1, lCenter)
rRightInner = Hex.dist(c2, rCenter)

tShift = 2.5
pad = 1
rtCenter = Hex.add(rCenter, Hex.polarPos(tShift, rightRot[0]))
ltCenter = Hex.add(lCenter, Hex.polarPos(tShift, 180 + leftRot[1]))

topLeftA = 9
topLeftX = Hex.add(lCenter, Hex.polarPos(leftLong + pad, 90 + topLeftA))
topLeftCorner = [plate[2], plate[3], a1,
	["arc"] + Hex.add(lCenter, Hex.polarPos(rLeftInner, 110)),
	Hex.circleLineIntersect(ltCenter, 90 + leftRot[1], lCenter, rLeftInner),
	Hex.circleLineIntersect(ltCenter, 90 + leftRot[1], lCenter, leftLong + pad),
	["arc"] + Hex.add(lCenter, Hex.polarPos(leftLong + pad, 93 + topLeftA)),
	topLeftX,
	Hex.intersect(d2, 90, topLeftX, topLeftA),
	d2]

topRightCorner = [plate[0], plate[1], d1,
	Hex.circleLineIntersect(d1, 90, rCenter, rightLong + pad),
	["arc"] + Hex.add(rCenter, Hex.polarPos(rightLong + pad, 90)),
	Hex.circleLineIntersect(rtCenter, 90 + rightRot[0], rCenter, rightLong + pad),
	Hex.circleLineIntersect(rtCenter, 90 + rightRot[0], rCenter, rRightInner),
	["arc"] + Hex.add(rCenter, Hex.polarPos(rRightInner, 45)),
	c2]

cornerRad = lrShort + pad + 0.5
smallCorner = [plate[4], b1,
	[b1[0], lCenter[1] + cornerRad],
	Hex.add(lCenter, [0, cornerRad]),
	["arc"] + Hex.add(lCenter, Hex.polarPos(cornerRad, -95)),
	Hex.circleLineIntersect(a2, -150, lCenter, cornerRad),
	a2]

lCenterX = Hex.polarPos(rCenter[0] - lCenter[0], 180 - rightRot[1])

rModIndent = Hex.add(lCenterX, Hex.polarPos(leftLong + pad, -2))

rightFlipperMod = rightFlipper[3:] + [
		Hex.intersect(rightFlipper[2], -50, rightFlipper[len(rightFlipper) - 1], 90),
		rightFlipper[2],
		Hex.intersect(rightFlipper[2], -90 - rightRot[1], rightFlipper[3], 90),
		Hex.circleLineIntersect(rightFlipper[3], 90, lCenterX, leftLong + pad),
		["arc"] + Hex.add(lCenterX, Hex.polarPos(leftLong + pad, 10)),
		rModIndent,
		Hex.intersect(rModIndent, 42, rightFlipper[3], 90),
	]

baseHoles = ["group",
	Hex.transform(flipperCircleBase, lCenter[0], lCenter[1], 0),
	Hex.transform(flipperCircleBase, rCenter[0], rCenter[1], 0),
	Hex.transform(pachinkoPin, 4.2, 4.4, 0),
	]

trm1r = 20
trm1d = 5
trm1c = Hex.add(d1, [0, trm1r + trm1d])
topRightMod1 = [plate[1], d1,
		Hex.add(d1, [0, trm1d]),
		["arc"] + Hex.add(trm1c, Hex.polarPos(trm1r, 85)),
		Hex.circleLineIntersect(Hex.add(plate[1], Hex.polarPos(2, -120)), 120, trm1c, trm1r),
	]

topRightMod1 += [Hex.intersect(plate[1], -60, topRightMod1[4], 30)]

trm2x = Hex.add(Hex.add(Hex.transform([rightFlipperMod[len(rightFlipperMod) - 7]], 0, 0, rightRot[0])[0], rCenter), [0.8, 0])
trm2e = Hex.add(plate[0], Hex.polarPos(17, 120))

topRightMod2 = [plate[0],
		trm2e,
		Hex.intersect(trm2e, 30, trm2x, 90 + 22),
		trm2x,
		Hex.add(trm2x, Hex.polarPos(5, -110)),
		["arc"],
		c2]

trm2l = len(topRightMod2)

topRightMod2[trm2l - 2] += Hex.relativeToCenter(topRightMod2[trm2l - 3], topRightMod2[trm2l - 1], 0, -1)

def rotExpand(rot):
	d = (rot[1] - rot[0]) / 10
	return [rot[0] + d * i for i in range(11)]

if __name__ == "__main__":
	print("Writing Ternary")
	tile = Hex.loadTemplate()

	Hex.transformInsert(tile, "3mm", plate, [50, 250], 50)
	Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
	Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
	
	Hex.transformInsert(tile, "3mm", baseHoles, [50, 250], 50)
	Hex.transformInsert(tile, "3mm", baseHoles[3], 50, 120)
	#Hex.transformInsert(tile, "3mm", flipperCircleBase, [50 + lCenter[0], 250 + lCenter[0]], 50 + lCenter[1])
	#Hex.transformInsert(tile, "3mm", flipperCircleBase, [50 + rCenter[0], 250 + rCenter[0]], 50 + rCenter[1])
	
	Hex.transformInsert(tile, "10mm", flipperCircle, [150 + lCenter[0], 250 + lCenter[0]], 50 + lCenter[1])
	Hex.transformInsert(tile, "10mm", flipperCircle, [150 + rCenter[0], 250 + rCenter[0]], 50 + rCenter[1])

	Hex.transformInsert(tile, "10mm", leftFlipper, 150 + lCenter[0], 50 + lCenter[1])
	Hex.transformInsert(tile, "10mm", rightFlipperMod, 150 + rCenter[0], 50 + rCenter[1])

	Hex.transformInsert(tile, "10mm", leftFlipper, 250 + lCenter[0], 50 + lCenter[1], leftRot)
	Hex.transformInsert(tile, "10mm", rightFlipperMod, 250 + rCenter[0], 50 + rCenter[1], rightRot)

	Hex.transformInsert(tile, "10mm", smallCorner, [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", Hex.flipY(smallCorner), [150, 250], 50, 180)
	Hex.transformInsert(tile, "10mm", topLeftCorner, [150, 250], 50, 0)
	#Hex.transformInsert(tile, "10mm", topRightCorner, [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", topRightMod1, [150, 250], 50, 0)
	Hex.transformInsert(tile, "10mm", topRightMod2, [150, 250], 50, 0)

	Hex.saveXML(tile, "Tiles/Ternary.svg")
