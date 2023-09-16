import math
import Hex
import Asterisk
import DIC
import Flipper
import Newton
import TinyBoard

print("====================")

cut3mm = Hex.loadCutTemplate(True)
cut10mm = Hex.loadCutTemplate(True)

Hex.resetLength()

# 3mm
TinyBoard.make7Indents(cut3mm, [82, 85], [2, "x-xx-x", 6, 6, 6, 6, 6])
Hex.transformInsert(cut3mm, "late", TinyBoard.outerEdge, 82, 85)

Hex.transformInsert(cut3mm, "mid", Hex.indexedPlate(3), 175, 32)
Hex.transformInsert(cut3mm, "mid", Hex.indexedPlate(6), 175, 84)
Hex.transformInsert(cut3mm, "mid", Hex.indexedPlate(6), 175, 136)
pachinko = [219, 58]
Hex.transformInsert(cut3mm, "mid", Hex.indexedPlate(1), pachinko[0], pachinko[1])
Hex.transformInsert(cut3mm, "mid", Hex.basePlate(), pachinko[0], pachinko[1] + 52)

PachinkoPositions = [[0, 0], [Flipper.distance2, 0], [-Flipper.distance2, 0], [0, -Flipper.distance2 * 1.15]]
for i in PachinkoPositions:
	j = pachinko
	Hex.transformInsert(cut3mm, "early", Flipper.pachinkoPin, i[0] + j[0], i[1] + j[1], 0)
	Hex.transformInsert(cut3mm, "early", Flipper.pachinkoPin, i[0] + j[0], i[1] + j[1] + 52, 0)

for i in [[34, 169], [82, 194], [130, 169], [178, 194], [226, 169],
		[34, 223], [82, 248], [130, 223], [178, 248], [226, 223],
		[130, 277], [178, 302]]:
	Hex.transformInsert(cut3mm, "mid", Hex.basePlate(), i[0], i[1])

Hex.transformInsert(cut3mm, "mid", Hex.indexedPlate(6), 82, 302)
Hex.transformInsert(cut3mm, "mid", Hex.indexedPlate(6), 130, 330)

Hex.transformInsert(cut3mm, "early", Flipper.flipperCircleBase, 34, 169)

Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB1M, 262, 138)
Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB1M, 268, 198)
Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB2M, 275, 258)
Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB2M, 274, 313)

Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB1R, 272, 168)
Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB1R, 415, 111, 180)
Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB2R, 275, 305)
Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB2R, 125, 225, 180)

Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB1L, 407, 138)
Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB1L, 250, 230, 180)
Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB2L, 380, 375, 0)
Hex.transformInsert(cut3mm, "mid", TinyBoard.smallRampB2L, 163, 225, 180)

length3mm = Hex.getLength()
Hex.resetLength()

# 10mm
TinyBoard.make7Holes(cut10mm, [130, 140])
Hex.transformInsert(cut10mm, "mid", TinyBoard.smallRampM, 283, 133)
Hex.transformInsert(cut10mm, "mid", TinyBoard.smallRampM, 336, 133)
Hex.transformInsert(cut10mm, "mid", TinyBoard.smallRampL, 375, 188)
Hex.transformInsert(cut10mm, "mid", TinyBoard.smallRampL, 428, 188)
Hex.transformInsert(cut10mm, "mid", TinyBoard.smallRampR, 197, 295)
Hex.transformInsert(cut10mm, "mid", TinyBoard.smallRampR, 250, 295)

# Part
# Asterisk.corner 						x10		(x12)
# Asterisk.bigCorner					x4		(x4)
# Asterisk.szTop						x4		(x4)
# Asterisk.sCorner						x2		(x2)
# Asterisk.zCorner						x2		(x2)
# Asterisk.trapCorner					x3		(x3)

for i in range(6):
	n = Hex.polarPos(8, i * 60)
	Hex.transformInsert(cut10mm, "mid", Asterisk.corner, 28 - n[0], 298 - n[1], i * 60)
	Hex.transformInsert(cut10mm, "mid", Asterisk.corner, 73 - n[0], 298 - n[1], i * 60)
	Hex.transformInsert(cut10mm, "mid", Flipper.smallCorner, 118 - n[0], 298 - n[1], i * 60)
	t = None
	r = 0
	if i == 0:
		t = DIC.roundCorner
	if i == 3:
		t = DIC.xcSmallCorner
		r = 180
	if i == 2:
		t = DIC.xcLargeCorner
		r = 120
	if i == 4:
		t = DIC.xcLargeCorner2
		r = 240
	if i == 1 or i == 5:
		t = Flipper.pachinkoCorner
	if t != None:
		Hex.transformInsert(cut10mm, "mid", t, 163 - n[0], 298 - n[1], i * 60 + r)
		
Hex.transformInsert(cut10mm, "mid", Hex.flipY(Flipper.smallCornerIndent), 293, 1, -120)
Hex.transformInsert(cut10mm, "mid", Flipper.smallCornerIndent, 323, 1, -60)
Hex.transformInsert(cut10mm, "mid", Hex.flipY(Flipper.smallCornerIndent), 293, 56, -120)
Hex.transformInsert(cut10mm, "mid", Flipper.smallCornerIndent, 323, 56, -60)
Hex.transformInsert(cut10mm, "mid", Flipper.smallCorner, 330, 163, -60)
Hex.transformInsert(cut10mm, "mid", Flipper.smallCorner, 300, 163, -120)

Hex.transformInsert(cut10mm, "early", Asterisk.sCorner, 73, 115)
Hex.transformInsert(cut10mm, "early", Asterisk.sCorner, 73, 167)
Hex.transformInsert(cut10mm, "early", Asterisk.zCorner, 163, 115)
Hex.transformInsert(cut10mm, "early", Asterisk.zCorner, 163, 167)

for i in range(3):
	n = Hex.polarPos(65, i * 120)
	Hex.transformInsert(cut10mm, "early", Asterisk.trapCorner, 130 + n[0], 140 + n[1], 90 + 120 * i)

for i in range(3):
	n = Hex.polarPos(5, i * 120 - 30)
	Hex.transformInsert(cut10mm, "mid", Asterisk.bigCorner, 213 - n[0], 300 - n[1], i * 120)

Hex.transformInsert(cut10mm, "mid", Asterisk.bigCorner,300, 249, -60)

Hex.transformInsert(cut10mm, "mid", Asterisk.szTop, [28, 73, 118, 163], 344)

# DIC.largeRoundCorner					x2		(x2)
# DIC.dcPart							x1		(x1)
# DIC.roundCorner						x1		(x1)
# DIC.xcCenter							x1		(x1)
# DIC.xcSmallCorner						x1		(x1)
# DIC.xcLargeCorner						x1		(x1)
# DIC.xcLargeCorner2					x1		(x1)

Hex.transformInsert(cut10mm, "mid", DIC.dcPart,320, 136, 60)
Hex.transformInsert(cut10mm, "early", DIC.largeRoundCorner,150, 76, 60)
Hex.transformInsert(cut10mm, "mid", DIC.largeRoundCorner,287, 136, -120)
Hex.transformInsert(cut10mm, "mid", DIC.xcCenter,335, 290)

Hex.transformInsert(cut10mm, "early", DIC.piscesCorner, 103, 93, 30)
Hex.transformInsert(cut10mm, "early", Hex.flipY(DIC.piscesCorner), 103, 84, -30)
Hex.transformInsert(cut10mm, "early", DIC.piscesCorner, 156, 84, -150)
Hex.transformInsert(cut10mm, "early", Hex.flipY(DIC.piscesCorner), 156, 93, 150)
Hex.transformInsert(cut10mm, "mid", DIC.piscesCenter, 310, 61, 30)
Hex.transformInsert(cut10mm, "mid", DIC.piscesCenter, 315, 225, 30)

# Flipper.smallCorner					x6		(x6)
# Flipper.smallCornerIndent				x1		(x1)
# Hex.flipY(Flipper.smallCornerIndent)	x1		(x1)
# Flipper.pachinkoCorner				x2		(x2)
# Flipper.flipper						x1		(x1)

Hex.transformInsert(cut10mm, "mid", Flipper.flipper, 250, 300, 30)
Hex.transformInsert(cut10mm, "early", Flipper.flipperCircle, 250, 300, 0)

# Newton.newtonTop						x1		(x1)
# Newton.newtonBottom					x1		(x1)
# Newton.newtonSide						x1		(x1)
# Hex.flipY(Newton.newtonSide)			x1		(x1)

Hex.transformInsert(cut10mm, "mid", Newton.newtonTop, 302, 302)
Hex.transformInsert(cut10mm, "mid", Newton.newtonBottom, 302, 298)
Hex.transformInsert(cut10mm, "mid", Newton.newtonSide, 297, 298)
Hex.transformInsert(cut10mm, "mid", Hex.flipY(Newton.newtonSide), 307, 298, 180)

length10mm = Hex.getLength()

Hex.saveXML(cut3mm, "Cut/Board3mm.svg")
Hex.saveXML(cut10mm, "Cut/Board10mm.svg")

print("10mm Length: " + str(int(length10mm)) + "\tTime: " + str(int(length10mm / 4.1)))
print("3mm  Length: " + str(int(length3mm)) + "\tTime: " + str(int(length3mm / 47)))
print("Price: ~" + str(int((length3mm / 47 +  length10mm / 4.1) / 60 * 1.5) + 1) + "€")
