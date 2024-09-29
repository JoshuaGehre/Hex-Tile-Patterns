import Hex
import math


plate = Hex.basePlate()
iPlate = Hex.indexedPlate(1)


inset = 3
inset2 = 7
inset3 = 12

a1 = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0)
a1x = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, -inset)
a1y = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, -inset2)
a1z = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, -inset3)
b1 = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, 0)
b1x = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, -inset)

a2 = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)
a2x = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -inset)
a2y = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -inset2)
a2z = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -inset3)

a3 = Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, 0)
a4 = Hex.relativeToCenter(plate[3], plate[4], 0.5 * Hex.TrackWidth, 0)

a5 = Hex.relativeToCenter(plate[0], plate[1], +0.5 * Hex.TrackWidth, 0)
a6 = Hex.relativeToCenter(plate[4], plate[5], +0.5 * Hex.TrackWidth, 0)


radius = math.sqrt(a1x[0]**2 + a1x[1]**2)
radius2 = math.sqrt(a1y[0]**2 + a1y[1]**2)

#print((radius * 2 - 42) / 3)

smallCorner = [plate[0], a1, a1x, ["arc", radius, 0], a2x, a2]
largeCorner = [plate[0], plate[1], b1, b1x, ["arc", radius, 0], a2x, a2]


indentAngle = math.atan2(a1y[1], a1y[0]) * 180 / math.pi

#print(indentAngle)

smallCornerIndent = [plate[0], a1, a1x, ["arc", radius, 0],
	Hex.polarPos(radius, indentAngle / 3),
	Hex.polarPos(radius2, indentAngle / 3),
	["arc"] + Hex.polarPos(radius2, indentAngle * 2 / 3),
	a2y, a2]

indentAngle *= -1

largeCornerIndent = [plate[0], plate[1], b1, b1x,
	["arc"] + Hex.polarPos(radius, 60),
	Hex.polarPos(radius, 60 - indentAngle / 3), Hex.polarPos(radius2, 60 - indentAngle / 3),
	["arc"] + Hex.polarPos(radius2, 60 - indentAngle / 2),
	Hex.polarPos(radius2, 40), Hex.polarPos(radius, 40),
	["arc"] + Hex.polarPos(radius, 30),
	Hex.polarPos(radius, 20), Hex.polarPos(radius2, 20),
	["arc"] + Hex.polarPos(radius2, indentAngle / 2),
	Hex.polarPos(radius2, indentAngle / 3), Hex.polarPos(radius, indentAngle / 3),
	["arc", radius, 0],
	a2x, a2]



pchCenter = Hex.TileEdge - inset3 * 2 / math.sqrt(3)
pchRadius = Hex.dist(a1z, [pchCenter, 0])

pachinkoCorner = [plate[0], a1, a1z, ["arc", pchCenter - pchRadius, 0], a2z, a2]


flipperAngle = 17
flipperRadius = radius - 1

angleTmp = (60 - flipperAngle / 2) / 180 * math.pi
flipperInnerArc = flipperRadius / math.cos(angleTmp) - flipperRadius * math.tan(angleTmp) + 2.5
#print(flipperInnerArc)

flipper = [
	Hex.polarPos(flipperRadius, 90 - flipperAngle / 2),
	["arc", 0, -flipperRadius],
	Hex.polarPos(flipperRadius, 90 + flipperAngle / 2),
	["arc"] + Hex.polarPos(flipperInnerArc, 120),
	]

flipper = flipper + Hex.transform(flipper, 0, 0, 120) + Hex.transform(flipper, 0, 0, 240) + [flipper[0]]


flipperCircle = Hex.makeCircle(2.0) #1.5

flipperCircleBase = Hex.makeCircle(0.75)

pachinkoPinRadius = 0.5
distance = (radius * 2 - pachinkoPinRadius * 6) / 4
#print(distance)
pachinkoPin = Hex.makeCircle(pachinkoPinRadius)

distance2 = pachinkoPinRadius * 2 + distance
#print(distance2)

openCenterOffset = -1.5


bottomHeight = 13.2
ofBottomRadius = 20

ofCenter = [0, openCenterOffset]
ofBottomPeak = [0, bottomHeight]
ofBottomAngle = math.atan2(a3[1] - bottomHeight, a3[0])
print(ofBottomAngle)
x = math.tan(ofBottomAngle) * ofBottomRadius
print(x)


bottomPiece = [plate[5], a3,
	Hex.add(ofBottomPeak, Hex.polarPos(x, -ofBottomAngle * 180 / math.pi)),
	["arc", 0, bottomHeight + ofBottomRadius * (1/math.cos(ofBottomAngle) - 1)],
	Hex.add(ofBottomPeak, Hex.polarPos(x, 180 + ofBottomAngle * 180 / math.pi)),
	a4, plate[4]]

ofSwitchA = 14
ofSwitchB = 20
ofSwitchW = 2.2

ofLargeRadius = (ofSwitchW**2 + ofSwitchB**2)**0.5
ofSmallRadius = (ofSwitchW**2 + ofSwitchA**2)**0.5

ofSwitch = [[4, 0], [ofSwitchW, -ofSwitchB], ["arc", 0, -ofLargeRadius], [-ofSwitchW, -ofSwitchB], [-4, 0], [-ofSwitchW, ofSwitchA], ["arc", 0, ofSmallRadius], [ofSwitchW, ofSwitchA]]

ofA1 = Hex.add(ofCenter, Hex.polarPos(ofLargeRadius + 1, 2))
ofA2 = Hex.add(a3, Hex.polarPos(Hex.TrackWidth, 90 - ofBottomAngle * 180 / math.pi))
ofAngleB = math.atan2(4, ofSwitchB) * 180 / math.pi

ofCorner = [plate[0], a1,
	["arc"] + Hex.add(a5, Hex.polarPos(Hex.TrackWidth, -65)),
	Hex.circleIntersect(ofCenter, ofLargeRadius + 1, a5, Hex.TrackWidth),
	["arc"] + Hex.add(ofCenter, Hex.polarPos(ofLargeRadius + 1, 4)),
	ofA1,
	Hex.circleLineIntersect(ofA1, ofAngleB + 2, ofCenter, ofSmallRadius + 1.5),
	["arc"] + Hex.add(ofCenter, Hex.polarPos(ofSmallRadius + 1.5, -10)),
	Hex.circleLineIntersect(ofA2, -ofBottomAngle * 180 / math.pi, ofCenter, ofSmallRadius + 1.5),
	ofA2,
	["arc"] + Hex.add(a3, Hex.polarPos(Hex.TrackWidth, 65)),
	a2]

ofDecorRad = 15
ofDecorAng = 50
ofArrowAng = 40
ofB1 = Hex.add(ofCenter, Hex.polarPos(ofDecorRad, 90 - ofDecorAng))
ofB2 = Hex.add(ofCenter, Hex.polarPos(ofDecorRad, 90 + ofDecorAng))

ofDecor = ["group",
	Hex.transform(flipperCircleBase, 0, openCenterOffset, 0),
	[ofB1, ["arc"] + Hex.add(ofCenter, Hex.polarPos(ofDecorRad, 90)), ofB2],
	[Hex.add(ofB1, Hex.polarPos(3, 180 - ofArrowAng - ofDecorAng)), ofB1, Hex.add(ofB1, Hex.polarPos(3, 180 + ofArrowAng - ofDecorAng))],
	[Hex.add(ofB2, Hex.polarPos(3, ofDecorAng + ofArrowAng)), ofB2, Hex.add(ofB2, Hex.polarPos(3, ofDecorAng - ofArrowAng))],
]


c1 = Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth, 0)
c2 = Hex.relativeToCenter(plate[4], plate[5], -0.5 * Hex.TrackWidth, 0)
halfInset = 3
halfAngle = 45
halfDown = 18

drHalf = [
	c1,
	plate[2], plate[3], plate[4],
	c2,
	Hex.add(c2, [0, -2]),
	Hex.add(c2, Hex.add([0, -2], Hex.polarPos(halfInset, 90 + halfAngle))),
	Hex.add(c1, Hex.add([0, halfDown], Hex.polarPos(halfInset, -90 - halfAngle))),
	Hex.add(c1, [0, halfDown]),
	]


sfR1 = 10
sfR2 = 20
sfEdgeAngle_2 = 7
sfEdgeAngle_1 = sfEdgeAngle_2 * sfR2 / sfR1
sfInset = 4.5

sfAngle = 125

sfFlipLeft = 42
sfFlipRight = 27

sfCenter = Hex.polarPos(12, -45)

drRightAngle = 49
drDist = Hex.dist(a2, sfCenter)
drOuterCurveMarker = Hex.add(sfCenter, Hex.polarPos(drDist + 5,  drRightAngle + 5))
drOuterCenter = [0, 4]
drOuterRad = Hex.dist(drOuterCenter, drOuterCurveMarker)
drRight = [
	a2, plate[0], plate[1], b1,
	Hex.circleLineIntersect(b1, 90, drOuterCenter, drOuterRad),
	["arc"] + Hex.add(drOuterCenter, Hex.polarPos(drOuterRad, 45)),
	drOuterCurveMarker,
	Hex.add(sfCenter, Hex.polarPos(drDist,  drRightAngle)),
	["arc"] + Hex.add(sfCenter, Hex.polarPos(drDist,  drRightAngle - 5)),
	a2]

smallFlipper = [
	Hex.polarPos(sfR2, -sfEdgeAngle_2),
	["arc", sfR2, 0],
	Hex.polarPos(sfR2, +sfEdgeAngle_2),
#	None,
	Hex.polarPos(sfInset, 0.5 * sfAngle),
#	None,
	Hex.polarPos(sfR1, sfAngle - sfEdgeAngle_1),
	["arc"] + Hex.polarPos(sfR1, sfAngle),
	Hex.polarPos(sfR1, sfAngle + sfEdgeAngle_1),
#	None,
	Hex.polarPos(sfInset, -180),
#	None,
	Hex.polarPos(sfR1, -sfAngle - sfEdgeAngle_1),
	["arc"] + Hex.polarPos(sfR1, -sfAngle),
	Hex.polarPos(sfR1, -sfAngle + sfEdgeAngle_1),
#	None,
	Hex.polarPos(sfInset, -0.5 * sfAngle),
#	None,
	Hex.polarPos(sfR2, -sfEdgeAngle_2),
]

#def setSmallFlipperCurve(index, angleInset, edgePos, angleEdge):
#	center = Hex.intersect([0, 0], angleInset, edgePos, angleEdge)
#	radius = Hex.dist(center, [0, 0]) - sfInset
#	smallFlipper[index] = ["arc"] + Hex.add(center, Hex.polarPos(-radius, 0.5 * (angleInset + angleEdge)))

#setSmallFlipperCurve(3, 0.5 * sfAngle, smallFlipper[2], 90)
#setSmallFlipperCurve(5, 0.5 * sfAngle, smallFlipper[6], sfAngle - 90)
#setSmallFlipperCurve(9, 180, smallFlipper[8], sfAngle + 90)
#setSmallFlipperCurve(11, -180, smallFlipper[12], -sfAngle - 90)
#setSmallFlipperCurve(15, -0.5 * sfAngle, smallFlipper[14], -sfAngle + 90)
#setSmallFlipperCurve(17, -0.5 * sfAngle, smallFlipper[18], -90)

msAngle = (math.acos(radius / Hex.dist(a6, [0, 0])) + math.atan2(Hex.TrackWidth * 0.5, 25)) * 180 / math.pi

metastableHalf = [
	plate[0], plate[1], b1, b1x, ["arc", radius, 0], Hex.polarPos(radius, -90 + msAngle), a6, plate[5],
]

metastableCenter = [0, 3]

msw = 7
msd = 14
msu = 6
msin = 4
msAngle = 40
msc1 = Hex.intersect([0, 0], 90, [msin, -msu], 90 + msAngle)
msr1 = Hex.dist(msc1, [msin, -msu])
msc2 = Hex.intersect([msw, 0], 90, [msin, -msu], 90 + msAngle)
msr2 = Hex.dist(msc2, [msin, -msu])
msc2l = [-msc2[0], msc2[1]]

msBallOffset = 12
msBallCircle = Hex.transform(Hex.makeCircle(Hex.TrackWidth * 0.5), 0, msBallOffset, 0)
msPart = [
	Hex.add(msc2, [0, -msr2]),
	["arc"] + Hex.add(msc2, Hex.polarPos(msr2, 95)),
	[msin, -msu],
	["arc", 0, msc1[1] + msr1],
	[-msin, -msu],
	["arc"] + Hex.add(msc2l, Hex.polarPos(msr2, 85)),
	Hex.add(msc2l, [0, -msr2]),
	[-msw, msd], ["arc", 0, msBallOffset + (msw**2+(msd - msBallOffset)**2)**0.5], [msw, msd]]

	
if __name__ == "__main__":
	print("Writing Flippers + Pachinko")
	tileFlipper3 = Hex.loadTemplate()
	tileFlipper6 = Hex.loadTemplate()
	tilePachinko = Hex.loadTemplate()
	tileFlipperOpen = Hex.loadTemplate()
	tileFlipperDR = Hex.loadTemplate()
	tileMetastable = Hex.loadTemplate()


	for tile in [tileFlipper3, tileFlipper6, tilePachinko, tileFlipperOpen, tileFlipperDR, tileMetastable]:
		Hex.transformInsert(tile, "3mm", plate, [50, 250], 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)


	Hex.transformInsert(tileFlipper3, "10mm", largeCorner, [150, 250], 50, [0, 120])
	Hex.transformInsert(tileFlipper6, "10mm", smallCorner, [150, 250], 50, [i * 60 for i in range(4)])
	Hex.transformInsert(tilePachinko, "10mm", smallCorner, [150, 250], 50, [0, 180])

	Hex.transformInsert(tileFlipper3, "10mm", largeCornerIndent, [150, 250], 50, -120)
	Hex.transformInsert(tileFlipper6, "10mm", smallCornerIndent, [150, 250], 50, -60)	
	Hex.transformInsert(tileFlipper6, "10mm", Hex.flipY(smallCornerIndent), [150, 250], 50, -120)

	Hex.transformInsert(tileFlipper3, "10mm", flipper, [150, 250], 50, flipperAngle * 1.4)
	Hex.transformInsert(tileFlipper6, "10mm", flipper, [150, 250], 50, flipperAngle * 1.4)

	Hex.transformInsert(tileFlipper3, "10mm", flipperCircle, [150, 250], 50, 0)
	Hex.transformInsert(tileFlipper6, "10mm", flipperCircle, [150, 250], 50, 0)
	Hex.transformInsert(tileFlipperOpen, "10mm", flipperCircle, [150, 250], 50 + openCenterOffset, 0)
	
	Hex.transformInsert(tileFlipperOpen, "10mm", bottomPiece, [150, 250], 50, 0)
	Hex.transformInsert(tileFlipperOpen, "10mm", ofSwitch, [150, 250], 50 + openCenterOffset, 0)#[81, -81, 0])
	
	#Hex.transformInsert(tileFlipperOpen, "10mm", smallCorner, [150, 250], 50, 60)
	Hex.transformInsert(tileFlipperOpen, "10mm", ofCorner, [150, 250], 50, 0)
	Hex.transformInsert(tileFlipperOpen, "10mm", Hex.flipY(ofCorner), [150, 250], 50, 180)

	for i in [tileFlipper3, tileFlipper6]:
		Hex.transformInsert(i, "3mm", flipperCircleBase, [50, 250], 50, 0)
	
	Hex.transformInsert(tileFlipperOpen, "3mm", ofDecor, [50, 250], 50, 0, z = False)
	
	Hex.transformInsert(tilePachinko, "10mm", pachinkoCorner, [150, 250], 50, [-60, -120])

	for i in [[0, 0], [distance2, 0], [-distance2, 0], [0, -distance2 * 1.15]]:
		for j in [[50, 50], [50, 120], [250, 50]]:
			Hex.transformInsert(tilePachinko, "3mm", pachinkoPin, i[0] + j[0], i[1] + j[1], 0)
	
	Hex.transformInsert(tileFlipperDR, "10mm", drHalf, [150, 250], 50, 0)
	Hex.transformInsert(tileFlipperDR, "10mm", drRight, [150, 250], 50, 0)

	Hex.transformInsert(tileFlipperDR, "10mm", smallFlipper, [150 + sfCenter[0], 250 + sfCenter[0]], 50 + sfCenter[1], 90)#[90 - sfFlipRight, 90, 90 + sfFlipLeft, 90 + sfFlipLeft * 0.5])
	Hex.transformInsert(tileFlipperDR, "10mm", flipperCircle, [150 + sfCenter[0], 250 + sfCenter[0]], 50 + sfCenter[1], 0)
	
	Hex.transformInsert(tileFlipperDR, "10mm", smallCorner, [150, 250], 50, -60)
	
	Hex.transformInsert(tileFlipperDR, "3mm", flipperCircleBase, [50 + sfCenter[0], 250 + sfCenter[0]], 50 + sfCenter[1], 50, 0)

	Hex.transformInsert(tileMetastable, "10mm", metastableHalf, [150, 250], 50, 0)
	Hex.transformInsert(tileMetastable, "10mm", Hex.flipY(metastableHalf), [150, 250], 50, 180)
	msXInsert = [150 + metastableCenter[0], 250 + metastableCenter[0]]
	msYInsert = 50 + metastableCenter[1]
	Hex.transformInsert(tileMetastable, "3mm", flipperCircleBase, [50, 250], msYInsert, 0)
	Hex.transformInsert(tileMetastable, "10mm", flipperCircle, msXInsert, msYInsert, 0)
	Hex.transformInsert(tileMetastable, "10mm", msBallCircle, msXInsert, msYInsert, 0)
	Hex.transformInsert(tileMetastable, "10mm", msPart, msXInsert, msYInsert, 0)

	Hex.saveXML(tileFlipper3, "Tiles/Flipper3.svg")
	Hex.saveXML(tileFlipper6, "Tiles/Flipper6.svg")
	Hex.saveXML(tilePachinko, "Tiles/Pachinko.svg")
	Hex.saveXML(tileFlipperOpen, "Tiles/FlipperOpen.svg")
	Hex.saveXML(tileFlipperDR, "Tiles/FlipperDR.svg")
	Hex.saveXML(tileMetastable, "Tiles/Metastable.svg")
