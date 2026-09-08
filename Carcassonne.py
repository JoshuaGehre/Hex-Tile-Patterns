import Hex
import math
import DIC
import Asterisk
import Deco

plate = Hex.basePlate()
iPlate = Hex.indexedPlate(6)

star1 = Deco.makeStar()
star2 = ["group", Deco.makeStar(8), Deco.makeStar(4)]

# Meeple
legRad = 1
legCenter = Hex.add([7.5, 0], Hex.polarPos(legRad / math.sin(math.pi / 8), 157.5))
leg1 = Hex.add(legCenter, [0, legRad])
leg2 = Hex.add(legCenter, Hex.polarPos(1, 45))

armCenter = [5, -6.5]
arm1 = Hex.add(armCenter, Hex.polarPos(legRad, -75))
arm2 = Hex.add(armCenter, Hex.polarPos(legRad, 65))

headRad = 2
headPoint = Hex.intersect(arm2, 155, [headRad, 0], 90)

meeple = [[2, 0],
	leg1, ["arc"] + Hex.add(legCenter, [legRad, 0]), leg2,
	Hex.intersect(leg2, 135, arm1, -165),
	arm1, ["arc"] + Hex.add(armCenter, [legRad, 0]), arm2,
	headPoint, Hex.add(headPoint, [0, -0.5])]

meeple = [[0, -2]] + meeple + [["arc", 0, headPoint[1] - headRad - 0.5]] + Hex.flipY(Hex.transform(Hex.reverse(meeple), 0, 0, 180))

meepleDeco = Hex.scale(meeple, 0.8)

# Parts
cOuter = DIC.partIC[1:-1] + [plate[2], plate[3], plate[4]]

wallWidth = 5
innerEdge = (Hex.TileHeight - wallWidth * 2) / math.sqrt(3)

xPlate = [Hex.polarPos(innerEdge, i * 60) for i in range(6)]
cRadius = (Hex.TileEdge + Hex.TrackWidth) * 0.5 + wallWidth

cInner = [xPlate[2], xPlate[3], xPlate[4], xPlate[5],
	Hex.circleLineIntersect(xPlate[0], -120, plate[0], cRadius),
	["arc"] + Hex.add(plate[0], [-cRadius, 0]),
	Hex.circleLineIntersect(xPlate[0], 120, plate[0], cRadius),
	xPlate[1]]

dcInner = cInner[3:] + Hex.transform(cInner[3:], 0, 0, 180)
dcOuter = DIC.partIC[1:-1] + Hex.transform(DIC.partIC[1:-1], 0, 0, 180)

cornerStep = xPlate[1][0] - 0.5 * Hex.TrackWidth - wallWidth

bigCornerInner = [
	xPlate[0],
	Hex.add(xPlate[0], Hex.polarPos(cornerStep, 120)),
	0,
	Hex.add(xPlate[5], Hex.polarPos(cornerStep, 180)),
	xPlate[5],
]

bigCornerInner[2] = Hex.intersect(bigCornerInner[1], -150, bigCornerInner[3], 90)

halfPart = [plate[0], plate[1], [Asterisk.bigCorner[3][0], plate[1][1]], Asterisk.bigCorner[3], plate[5]]
halfPartInner = [xPlate[0], xPlate[1], Hex.add(xPlate[1], [-cornerStep, 0]), Hex.add(xPlate[5], [-cornerStep, 0]), xPlate[5]]

c = Hex.intersect(plate[5], 0, plate[0], 120)

a1 = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0)
a2 = Hex.relativeToCenter(plate[0], plate[1], 0.5 * Hex.TrackWidth, 0)

b1 = Hex.relativeToCenter(plate[5], plate[4], -0.5 * Hex.TrackWidth, 0)
b2 = Hex.relativeToCenter(plate[5], plate[4], 0.5 * Hex.TrackWidth, 0)

d1 = Hex.dist(a1, c)
d2 = Hex.dist(a2, c)

jSmall = [plate[0], a1, ["arc"] + Hex.add(c, Hex.polarPos(d1, 150)), b1, plate[5]]
jBig = [b2, ["arc"] + Hex.add(c, Hex.polarPos(d2, 150)), a2, plate[1], plate[2], plate[3], plate[4]]

jWall = 4.5
jSmallInner = [xPlate[0], Hex.circleLineIntersect(xPlate[0], 120, c, d1 - jWall), 
	["arc"] + Hex.add(c, Hex.polarPos(d1 - jWall, 150)),
	Hex.circleLineIntersect(xPlate[5], -180, c, d1 - jWall), xPlate[5]]
jBigInner = [
	xPlate[4], Hex.circleLineIntersect(xPlate[5], -180, c, d2 + wallWidth),
	["arc"] + Hex.add(c, Hex.polarPos(d2 + wallWidth, 150)),
	Hex.circleLineIntersect(xPlate[0], 120, c, d2 + wallWidth),
	xPlate[1], xPlate[2], xPlate[3]]

triggerInset = 12.5

triggerOut = [
	b2, Hex.add(b2, [0, -triggerInset]),
	["arc", 0, b2[1] - triggerInset - 0.5 * Hex.TrackWidth],
	Hex.add(b1, [0, -triggerInset]), b1,
	plate[5], plate[0], plate[1], plate[2], plate[3], plate[4]]
triggerIn = [
	Hex.add(b2, [-wallWidth, -wallWidth]),
	Hex.add(b2, [-wallWidth, -triggerInset]),
	["arc", 0, b2[1] - triggerInset - 0.5 * Hex.TrackWidth - wallWidth],
	Hex.add(b1, [wallWidth, -triggerInset]),
	Hex.add(b1, [wallWidth, -wallWidth]),
	xPlate[5], xPlate[0], xPlate[1], xPlate[2], xPlate[3], xPlate[4]
	]

triggerRipple = Deco.makeRipple(
		Hex.add(b2, [0, -triggerInset * 0.5]), triggerOut[1], outwards=True
	) + Deco.makeArcRipple(
		triggerOut[1], triggerOut[3], [0, triggerOut[1][1]], flip=True
	) + Deco.makeRipple(
		triggerOut[3], Hex.add(b1, [0, -triggerInset * 0.5]), outwards=True)
triggerRipple = Hex.transform(triggerRipple, 0, 0, 180)

shield = [[-3, -4], [3, -4], [3, 0], ["arc", 0, 3], [-3, 0]]

arrowStart = 9
arrowStep = 5
arrowBend = 1
claimAnyArrow = ["group",[
		[0, arrowStart],
		["arc", -arrowBend, arrowStart + arrowStep * 0.5],
		[0, arrowStart + arrowStep],
		["arc", arrowBend, arrowStart + arrowStep * 1.5],
		[0, arrowStart + arrowStep * 2],
	],Hex.transform([
		[-2, -3],
		[0, 0],
		[2, -3]
	], 0, arrowStart + arrowStep * 2, -20)]

arrowDeco = ["group"] + [Hex.transform(claimAnyArrow, 0, 0, 60 * i) for i in range(1,6)]


# Output
if __name__ == "__main__":
	tileC = Hex.loadTemplate()
	tile0 = Hex.loadTemplate()
	tileI = Hex.loadTemplate()
	tileY = Hex.loadTemplate()
	tileJ = Hex.loadTemplate()
	tileDC = Hex.loadTemplate()
	tileTrigger = Hex.loadTemplate()
	tileM = Hex.loadTemplate()

	for tile in [tileC, tile0, tileI, tileY, tileJ, tileTrigger, tileDC, tileM]:
		Hex.transformInsert(tile, "3mm", plate, 50, 50)
		Hex.transformInsert(tile, "3mm", plate, 250, 50)
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
		Hex.transformInsert(tile, "3mm", meepleDeco, 50, 90, 0)

	# C
	Hex.transformInsert(tileC, "10mm", DIC.roundCorner, [150, 250], 50, 0)
	Hex.transformInsert(tileC, "10mm", cOuter, [150, 250], 50, 0)
	Hex.transformInsert(tileC, "10mm", cInner, [150, 250], 50, 0)
	
	Hex.transformInsert(tileC, "3mm", meepleDeco, 260, 42, 0)

	# DC
	Hex.transformInsert(tileDC, "10mm", DIC.roundCorner, [150, 250], 50, [0, 180])
	Hex.transformInsert(tileDC, "10mm", dcOuter, [150, 250], 50, 0)
	Hex.transformInsert(tileDC, "10mm", dcInner, [150, 250], 50, 0)

	#0
	Hex.transformInsert(tile0, "10mm", plate, [150, 250], 50, 0)
	Hex.transformInsert(tile0, "10mm", xPlate, [150, 250], 50, 0)
	Hex.transformInsert(tile0, "3mm", meepleDeco, 271, 43, 30)
	
	#I
	Hex.transformInsert(tileI, "10mm", halfPart, [150, 250], 50, [0, 180])
	Hex.transformInsert(tileI, "10mm", halfPartInner, [150, 250], 50, [0, 180])

	#Y
	Hex.transformInsert(tileY, "10mm", Asterisk.bigCorner, [150, 250], 50, [0, 120, 240])
	Hex.transformInsert(tileY, "10mm", bigCornerInner, [150, 250], 50, [0, 120, 240])

	#J
	Hex.transformInsert(tileJ, "10mm", jSmall, [150, 250], 50, 0)
	Hex.transformInsert(tileJ, "10mm", jSmallInner, [150, 250], 50, 0)
	Hex.transformInsert(tileJ, "10mm", jBig, [150, 250], 50, 0)
	Hex.transformInsert(tileJ, "10mm", jBigInner, [150, 250], 50, 0)

	#Trigger
	Hex.transformInsert(tileTrigger, "10mm", triggerOut, [150, 250], 50, 180)
	Hex.transformInsert(tileTrigger, "10mm", triggerIn, [150, 250], 50, 180)
	Hex.transformInsert(tileTrigger, "3mm", triggerRipple, [50, 250], 50, 0, z=False)
	Hex.transformInsert(tileTrigger, "3mm", shield, 30, 86, 0)
	Hex.transformInsert(tileTrigger, "3mm", star1, 70, 86, 0)
	Hex.transformInsert(tileTrigger, "3mm", shield, 242, 35, 0)
	Hex.transformInsert(tileTrigger, "3mm", star1, 258, 35, 0)

	# M
	Hex.transformInsert(tileM, "10mm", DIC.roundCorner, [150, 250], 50, [i * 60 for i in range(6)])
	Hex.transformInsert(tileM, "10mm", meeple, [150, 250], 55, 0)
	Hex.transformInsert(tileM, "3mm", star2, [50, 250], 65, 0)
	Hex.transformInsert(tileM, "3mm", arrowDeco, [50, 250], 50, 0, z=False)

	Hex.saveXML(tileC, "Tiles/Carcassonne_C.svg")
	Hex.saveXML(tileDC, "Tiles/Carcassonne_DC.svg")
	Hex.saveXML(tile0, "Tiles/Carcassonne_0.svg")
	Hex.saveXML(tileI, "Tiles/Carcassonne_I.svg")
	Hex.saveXML(tileY, "Tiles/Carcassonne_Y.svg")
	Hex.saveXML(tileJ, "Tiles/Carcassonne_J.svg")
	Hex.saveXML(tileTrigger, "Tiles/Carcassonne_Trigger.svg")
	Hex.saveXML(tileM, "Tiles/Carcassonne_M.svg")
