import Hex
import Deco
import math

plate = Hex.basePlate()
iPlate1 = Hex.indexedPlate(1)
iPlate4 = Hex.indexedPlate("x-xx-x")
iPlate6 = Hex.indexedPlate(6)

star = Deco.makeStar()
star2 = ["group", Deco.makeStar(8), Deco.makeStar(4)]

def makeGear(r1, r2, x):
	n = (int)(0.5 + math.pi * (r1 + r2) / x)
	a = 360 / n
	g = []
	for i in range(n):
		phi = a * i;
		g += [Hex.polarPos(r1, phi), Hex.polarPos(r2, phi + 0.1 * a),
			["arc"] + Hex.polarPos(r2, phi + 0.25 * a),
			Hex.polarPos(r2, phi + 0.5 * a), Hex.polarPos(r1, phi + 0.6 * a),
			["arc"] + Hex.polarPos(r1, phi + 0.75 * a)]
	return g + [g[0]]

inset = 6
a1 = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0)
a1x = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, -inset)
a2 = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)
a2x = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -inset)

gearCorner = [plate[0], a1, a1x, ["arc", Hex.dist(a1x, [0, 0]), 0], a2x, a2]

gearR = 7
gearBottom = makeGear(10, 12, 4.5)
gearTop = makeGear(11, 13, 4.5)
gearPillar = [[gearR, 0], ["arc", 0, -gearR], [-gearR, 0], ["arc", 0, gearR], [gearR, 0]]

gearRipple = Deco.makeArcRipple(a2x, a1x, [0, 0])
gearBase = ["group"] + [
		Hex.transform(gearRipple, 0, 0, i * 60) for i in range(6)
	] + [
		[Hex.polarPos(gearR, i * 60 - 10), ["arc"] + Hex.polarPos(gearR, i * 60), Hex.polarPos(gearR, i * 60 + 10)] for i in range(6)
	]
b1 = Hex.relativeToCenter(plate[4], plate[5], -0.5 * Hex.TrackWidth, 0)
b2 = Hex.relativeToCenter(plate[4], plate[5], 0.5 * Hex.TrackWidth, 0)

iwCenter = [0, -3.5]
iwRad = 12
iwPart = [b1,
	Hex.circleLineIntersect(b1, -90, iwCenter, iwRad),
	["arc"] + Hex.add(iwCenter, [-iwRad, 0]),
	Hex.add(iwCenter, [0, -iwRad]),
	["arc"] + Hex.add(iwCenter, [iwRad, 0]),
	Hex.circleLineIntersect(b2, -90, iwCenter, iwRad),
	b2,
	plate[5]] + plate[0:5]

iwRi = 8
iwRo = iwRi + 4
iwInnerHole = Hex.transform([[iwRi, 0], ["arc", 0, -iwRi], [-iwRi, 0], ["arc", 0, iwRi], [iwRi, 0]], 0, iwCenter[1], 0)
iwOuterHole = Hex.transform([[iwRo, 0], ["arc", 0, -iwRo], [-iwRo, 0], ["arc", 0, iwRo], [iwRo, 0]], 0, iwCenter[1], 0)

iwRr = iwRi + Deco.rippleIndent + 1
iwRipple = Deco.makeArcRipple([iwRr, 0], [-iwRr, 0], [0, 0]) + Deco.makeArcRipple([-iwRr, 0], [iwRr, 0], [0, 0])
iwRipple = Hex.transform(iwRipple, 0, iwCenter[1], 0)

d = 10
iwArc = [
		[d + 1.5, 0], [d + 1.5, 11], ["arc", 0, 11 + d + 1.5], [-d - 1.5, 11], [-d -1.5, 0],
		[-d + 1.5, 0], [-d + 1.5, 11], ["arc", 0, 11 + d - 1.5], [d - 1.5, 11], [d -1.5, 0],
	]

square = [[1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5], [1.5, -1.5]]

iwHoles = ["group",
	Hex.transform(square, -d, 21, 0), Hex.transform(square, d, 21, 0),
	Hex.transform(square, -d, 15.5, 0), Hex.transform(square, d, 15.5, 0),
	Hex.transform(square, -d, 10, 0), Hex.transform(square, d, 10, 0),
]

discardCenter = Hex.polarPos(Hex.TileHeight, -30)

discardR1 = Hex.dist(discardCenter, b1)
discardR2 = Hex.dist(discardCenter, b2)

discardSmall = [plate[5], plate[0], a1, ["arc"] + Hex.add(discardCenter, Hex.polarPos(discardR2, 150)), b2]
discardLarge = [Hex.add(discardCenter, Hex.polarPos(discardR1, 180)), ["arc"] + Hex.add(discardCenter, Hex.polarPos(discardR1, 150)), Hex.add(discardCenter, Hex.polarPos(discardR1, 120))] + plate[1:5]

dw = 3
discardCeil1 = [Hex.add(discardCenter, Hex.polarPos(discardR1 - dw, 180)), ["arc"] + Hex.add(discardCenter, Hex.polarPos(discardR1 - dw, 150)), Hex.add(discardCenter, Hex.polarPos(discardR1 - dw, 120)),
	Hex.add(discardCenter, Hex.polarPos(discardR1 + dw, 120)), ["arc"] + Hex.add(discardCenter, Hex.polarPos(discardR1 + dw, 150)), Hex.add(discardCenter, Hex.polarPos(discardR1 + dw, 180))]
discardCeil2 = [Hex.add(discardCenter, Hex.polarPos(discardR2 - dw, 180)), ["arc"] + Hex.add(discardCenter, Hex.polarPos(discardR2 - dw, 150)), Hex.add(discardCenter, Hex.polarPos(discardR2 - dw, 120)),
	Hex.add(discardCenter, Hex.polarPos(discardR2 + dw, 120)), ["arc"] + Hex.add(discardCenter, Hex.polarPos(discardR2 + dw, 150)), Hex.add(discardCenter, Hex.polarPos(discardR2 + dw, 180))]

recIn = 4
recOut = 7
recSpacing = 2
rArrow = 1.5

lIn = Hex.add(Hex.polarPos(recIn, 150), Hex.polarPos(recSpacing, 60))
lOut = Hex.add(Hex.polarPos(recOut, 150), Hex.polarPos(recSpacing, 60))
rIn = Hex.add(Hex.polarPos(recIn, 30), Hex.polarPos(recSpacing, 120))
rOut = Hex.add(Hex.polarPos(recOut, 30), Hex.polarPos(recSpacing, 120))

rTL = Hex.intersect(lOut, 60, rIn, -60)
rTR = Hex.intersect(lIn, 60, rOut, -60)

recPart = ["group",
	[rTL, rIn, Hex.add(rIn, Hex.polarPos(rArrow, -150)), Hex.relativeToCenter(rIn, rOut, 0, 2), Hex.add(rOut, Hex.polarPos(rArrow, 30)), rOut, rTR],
	[Hex.add(rTL, Hex.polarPos(recSpacing, -120)), lOut, Hex.relativeToCenter(lIn, lOut, 0, 1), lIn, Hex.add(Hex.intersect(lIn, 60, rIn, -60), Hex.polarPos(recSpacing, -120))]]

recPart = ["group"] + [Hex.transform(recPart, -13.5, -0.5 * (recIn + recOut), i * 120) for i in range(3)]

if __name__ == "__main__":
	print("Writing Tiles")
	tileInstantWin = Hex.loadTemplate()
	tileGear = Hex.loadTemplate()
	tileDiscard = Hex.loadTemplate()
	
	for tile, iPlate in [(tileInstantWin, iPlate1), (tileGear, iPlate6), (tileDiscard, iPlate4)]:
		Hex.transformInsert(tile, "3mm", iPlate, 50, 120)
		Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
		Hex.transformInsert(tile, "3mm", plate, [50, 250], 50)

	Hex.transformInsert(tileGear, "10mm", gearCorner, [150, 250], 50, [i * 60 for i in range(6)])
	Hex.transformInsert(tileGear, "3mm", gearBottom, 70, 170, 0)
	Hex.transformInsert(tileGear, "3mm", gearPillar, 70, 170, 0)
	Hex.transformInsert(tileGear, "3mm", gearBottom, 250, 50, 0)
	Hex.transformInsert(tileGear, "3mm", gearTop, 30, 170, 0)
	Hex.transformInsert(tileGear, "3mm", gearTop, 250, 50, 0)
	Hex.transformInsert(tileGear, "10mm", gearPillar, [150, 250], 50, 0)
	
	Hex.transformInsert(tileGear, "3mm", star, 238.5, 30, 0)
	Hex.transformInsert(tileGear, "3mm", star, 50, 85, 0)

	Hex.transformInsert(tileGear, "3mm", gearBase, [50, 250], 50, 0, z=False)
	
	Hex.transformInsert(tileInstantWin, "10mm", iwPart, [150, 250], 50, 0)
	Hex.transformInsert(tileInstantWin, "3mm", iwInnerHole, 250, 50, 0)
	Hex.transformInsert(tileInstantWin, "3mm", iwInnerHole, 50, 120, 0)
	Hex.transformInsert(tileInstantWin, "3mm", iwOuterHole, 250, 50, 0)

	Hex.transformInsert(tileInstantWin, "10mm", iwInnerHole, 150, 110, 0)
	Hex.transformInsert(tileInstantWin, "10mm", iwOuterHole, 150, 110, 0)

	Hex.transformInsert(tileInstantWin, "3mm", iwOuterHole, 50, 170, 0)
	Hex.transformInsert(tileInstantWin, "3mm", iwRipple, [50, 250], 50, 0)
	Hex.transformInsert(tileInstantWin, "10mm", iwHoles, [150, 250], 50, 0)
	
	Hex.transformInsert(tileInstantWin, "3mm", star, 261, 33, 0)
	Hex.transformInsert(tileInstantWin, "3mm", star, 50, 85, 0)

	Hex.transformInsert(tileInstantWin, "3mm", iwArc, [30, 60, 90], 185, 0)
	
	Hex.transformInsert(tileDiscard, "10mm", discardSmall, [150, 250], 50, 0)
	Hex.transformInsert(tileDiscard, "10mm", discardLarge, [150, 250], 50, 0)

	Hex.transformInsert(tileDiscard, "3mm", discardCeil1, 250, 50, 0)
	Hex.transformInsert(tileDiscard, "3mm", discardCeil2, 250, 50, 0)
	
	Hex.transformInsert(tileDiscard, "3mm", discardCeil1, 50, 170, 0)
	Hex.transformInsert(tileDiscard, "3mm", discardCeil2, 50, 170, 0)

	Hex.transformInsert(tileDiscard, "10mm", recPart, [150, 250], 50, 0, z = False)
	
	Hex.transformInsert(tileDiscard, "3mm", star2, 40, 160, 0)
	Hex.transformInsert(tileDiscard, "3mm", star2, 249, 34, 0)

	#Hex.saveXML(tileInstantWin, "Tiles/InstantWin.svg")
	#Hex.saveXML(tileGear, "Tiles/Gear.svg")
	Hex.saveXML(tileDiscard, "Tiles/Discard.svg")
