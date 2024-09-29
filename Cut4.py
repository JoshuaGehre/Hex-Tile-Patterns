import math
import Hex
import LargeBoard
import Flipper
import Specials
import Teleport
import Secret
import Carcassonne
import Asterisk
import DIC
import Newton
import QuadTrap
import Carcassonne
import LinearTrap
import Teleport

cut3mm = Hex.loadCutTemplate(True)
cut10mm = Hex.loadCutTemplate(True)

# Content
# Large Board (32 Hex)
#
# New Tiles:
#  Clone Tile x1
#  Teleport Tile (In x1 + Out x1)
#  King x1
#  Metastable
#  Carcasonne (C x1 + 0 x1)
#  OpenFlipper
#  Linear Trap
#  Flipper DR
#  [Redacted]
#
# Repeat:
#  Asterisk, Peace, DIC, XC, X (x3), DC (x3), Pisces, S, Z
#  2Trap (Maybe), 3Trap, Newton, 4Trap
#  Pachinko (x2), Flipper3 (x2), Flipper6 (x2)
#  Bomb, RHSBT

Hex.resetLength()

# TODO 10mm

center = Hex.add(LargeBoard.boardSize, [3,3])
Hex.transformInsert(cut10mm, "late", LargeBoard.outside, center[0], center[1])
LargeBoard.makeBaseHoles(cut10mm, center)
y = 0.5 * (LargeBoard.rows - 1)
Hex.transformInsert(cut10mm, "mid", LargeBoard.goalGap, center[0] - LargeBoard.xVec[0] + LargeBoard.yVec[0] * (y + 1), center[1] - LargeBoard.xVec[1] - LargeBoard.yVec[1] * y, 180)


Hex.transformInsert(cut10mm, "late", LargeBoard.onRampWallLeft, [310, 380], 72)
Hex.transformInsert(cut10mm, "late", LargeBoard.onRampWallL2, [305, 375], 72)
Hex.transformInsert(cut10mm, "late", LargeBoard.onRampWallR2, [300, 370], 72)
Hex.transformInsert(cut10mm, "late", LargeBoard.onRampWallRight, [295, 365], 72)
		
Hex.transformInsert(cut10mm, "late", LargeBoard.goalOut, 305, [72, 142], 180)
Hex.transformInsert(cut10mm, "mid", LargeBoard.goalR, 305, [72, 92], 180)
Hex.transformInsert(cut10mm, "mid", LargeBoard.goalL, 305, [72, 92], 180)

for i in range(6):
	n = Hex.polarPos(8, i * 60)
	Hex.transformInsert(cut10mm, "mid", Asterisk.corner, 295 - n[0], 175 - n[1], i * 60)
	Hex.transformInsert(cut10mm, "mid", Asterisk.corner, 265 - n[0], 233 - n[1], i * 60)
	Hex.transformInsert(cut10mm, "late", Flipper.smallCorner, 300 - n[0], 253 - n[1], i * 60)
	Hex.transformInsert(cut10mm, "late", Flipper.smallCorner, 335 - n[0], 233 - n[1], i * 60)
	Hex.transformInsert(cut10mm, "mid", DIC.roundCorner, 302 - n[0], 75 - n[1], i * 60)
	Hex.transformInsert(cut10mm, "late", Teleport.teleSmallCorner, 490 - n[0] * 1.5, 245 - n[1] * 1.5, i * 60 + 60)
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
		t = Asterisk.corner
	if t != None:
		Hex.transformInsert(cut10mm, "mid", t, 372 - n[0], 75 - n[1], i * 60 + r)
	r = 0
	if i % 3 == 0:
		t = Flipper.smallCorner
	if i % 3 == 1:
		t = Hex.flipY(Flipper.smallCornerIndent)
	if i % 3 == 2:
		t = Flipper.smallCornerIndent
	if t != None:
		Hex.transformInsert(cut10mm, "late", t, 340 - n[0], 387 - n[1], i * 60 + r)

for i in range(3):
	n = Hex.polarPos(5, i * 120 - 30)
	Hex.transformInsert(cut10mm, "late", Asterisk.bigCorner, 375 - n[0], 120 - n[1], i * 120)
	Hex.transformInsert(cut10mm, "late", Asterisk.bigCorner, 375 - n[0], 170 - n[1], i * 120)
	Hex.transformInsert(cut10mm, "late", Asterisk.bigCorner, 375 - n[0], 220 - n[1], i * 120)
	Hex.transformInsert(cut10mm, "late", Hex.transform(Asterisk.trapCorner, 0, 0, 60), 375 - n[0], 267 - n[1], i * 120)

Hex.transformInsert(cut10mm, "late", DIC.largeRoundCorner, [245, 260, 275], 300, 60)
Hex.transformInsert(cut10mm, "late", DIC.largeRoundCorner, [325, 340, 355], 282, -120)
Hex.transformInsert(cut10mm, "late", DIC.dcPart, [270, 290, 310], 340, -120)
Hex.transformInsert(cut10mm, "late", DIC.partIC, 350, 340, 0)
Hex.transformInsert(cut10mm, "late", DIC.partIC, 355, 340, 180)

Hex.transformInsert(cut10mm, "late", DIC.xcCenter, 370, 340, 0)


Hex.transformInsert(cut10mm, "early", Asterisk.sCorner, 74, 79)
Hex.transformInsert(cut10mm, "early", Asterisk.sCorner, 74, 129)
Hex.transformInsert(cut10mm, "early", Asterisk.zCorner, 164, 79)
Hex.transformInsert(cut10mm, "early", Asterisk.zCorner, 164, 129)

Hex.transformInsert(cut10mm, "mid", Asterisk.szTop, 386, [400, 412, 424, 436])

Hex.transformInsert(cut10mm, "mid", Newton.newtonTop, 292, 397)
Hex.transformInsert(cut10mm, "mid", Newton.newtonBottom, 292, 393)
Hex.transformInsert(cut10mm, "mid", Newton.newtonSide, 287, 393)
Hex.transformInsert(cut10mm, "mid", Hex.flipY(Newton.newtonSide), 297, 393, 180)

Hex.transformInsert(cut10mm, "early", DIC.piscesCorner, 106, 108, 30)
Hex.transformInsert(cut10mm, "early", Hex.flipY(DIC.piscesCorner), 106, 99, -30)
Hex.transformInsert(cut10mm, "early", DIC.piscesCorner, 159, 99, -150)
Hex.transformInsert(cut10mm, "early", Hex.flipY(DIC.piscesCorner), 159, 108, 150)

Hex.transformInsert(cut10mm, "early", DIC.piscesCenter, [40, 220], 120, 30)

Hex.transformInsert(cut10mm, "late", Flipper.largeCornerIndent, 386, [410, 425], -120)
Hex.transformInsert(cut10mm, "late", Flipper.largeCorner, [260, 275], 451)
Hex.transformInsert(cut10mm, "late", Flipper.largeCorner, [335, 350], 435, 120)

Hex.transformInsert(cut10mm, "early", Flipper.pachinkoCorner, [40, 220], 140, -60)
Hex.transformInsert(cut10mm, "early", Flipper.pachinkoCorner, [47, 227], 140, -120)

Hex.transformInsert(cut10mm, "late", Flipper.flipper, [430, 480], 20, 180)
Hex.transformInsert(cut10mm, "late", Flipper.flipper, [455, 505], 40, 0)
Hex.transformInsert(cut10mm, "mid", Flipper.flipperCircle, [430, 480], 20)
Hex.transformInsert(cut10mm, "mid", Flipper.flipperCircle, [455, 505], 40)

Hex.transformInsert(cut10mm, "late", Flipper.ofSwitch, 520, 25)
Hex.transformInsert(cut10mm, "mid", Flipper.flipperCircle, 520, 25)

Hex.transformInsert(cut10mm, "late", Flipper.smallFlipper, 418, 52, 90)
Hex.transformInsert(cut10mm, "mid", Flipper.flipperCircle, 418, 52)

Hex.transformInsert(cut10mm, "late", Flipper.drHalf, 418, 90, 0)
Hex.transformInsert(cut10mm, "late", Flipper.drRight, 410, 90, 0)
Hex.transformInsert(cut10mm, "late", Flipper.metastableHalf, 427, 90, 0)
Hex.transformInsert(cut10mm, "late", Hex.flipY(Flipper.metastableHalf), 442, 90, 0)

Hex.transformInsert(cut10mm, "early", Flipper.ofCorner, 120, 156, 0)
Hex.transformInsert(cut10mm, "early", Hex.flipY(Flipper.ofCorner), 145, 156, 180)

Hex.transformInsert(cut10mm, "late", Flipper.bottomPiece, 300, 201, 0)

Hex.transformInsert(cut10mm, "late", QuadTrap.centerPart, 485, 90, 0)
Hex.transformInsert(cut10mm, "late", Specials.kingPart, 420, 145, 0)

for i in range(1, 5):
	Hex.transformInsert(cut10mm, "mid" if i == 1 else "early", Specials.rhsbtLeft[i], 530, 85, 0)
	Hex.transformInsert(cut10mm, "mid" if i == 1 else "early", Specials.rhsbtRight[i], 308, 175, 0)

Hex.transformInsert(cut10mm, "late", Specials.cloneRight, 478, 145, 0)
Hex.transformInsert(cut10mm, "late", Specials.cloneLeft, 483, 145, 0)

Hex.transformInsert(cut10mm, "late", Flipper.msPart, 515, 125, 0)
Hex.transformInsert(cut10mm, "late", Flipper.msBallCircle, 515, 125, 0)
Hex.transformInsert(cut10mm, "late", Flipper.flipperCircle, 515, 125, 0)

Hex.transformInsert(cut10mm, "mid", Carcassonne.cInner, 424, 200, 0)
Hex.transformInsert(cut10mm, "late", Carcassonne.cOuter, 424, 200, 0)

Hex.transformInsert(cut10mm, "mid", Carcassonne.xPlate, 470, 200, 0)
Hex.transformInsert(cut10mm, "late", Carcassonne.plate, 470, 200, 0)

Hex.transformInsert(cut10mm, "late", LinearTrap.leftPart, 523, 180, 0)
Hex.transformInsert(cut10mm, "late", LinearTrap.rightPart, 400, 255, 0)

Hex.transformInsert(cut10mm, "late", Teleport.teleCatch, 425, 290, 0)

Hex.transformInsert(cut10mm, "late", Teleport.teleLargeCorner, 425, 295, 0)
Hex.transformInsert(cut10mm, "late", Hex.flipY(Teleport.teleLargeCorner), 425, 295, 180)

Hex.transformInsert(cut10mm, "late", Teleport.teleTop, 420, 350, 0)

#Hex.transformInsert(tile, "10mm", teleLargeCorner, [250, 150], 110)
#Hex.transformInsert(tile, "10mm", Hex.flipY(teleLargeCorner), [250, 150], 110, 180)
#Hex.transformInsert(tile, "10mm", teleTop, [250, 150], 110)

try:
	import Redacted
	Redacted.insert10mm_Cut4(cut10mm)
except ModuleNotFoundError:
	pass


length10mm = Hex.getLength()
Hex.resetLength()

# ===== 3mm =====

iPlate1 = Hex.indexedPlate(1)
plate = Hex.basePlate()

center = Hex.add(LargeBoard.boardSize, [-3,-42])
LargeBoard.makeIndents(cut3mm, center, [1]*4 + [2]*3+ ["x-x-x-"]*4 + ["xx---x"]*3 + ["xx-xx-"]*4)
Hex.transformInsert(cut3mm, "late", LargeBoard.outerEdge, center[0], center[1])

partCenters = []
for j in range(3):
	dx = 94 * j
	partCenters += [[268 + dx, 28 + 53 * i] for i in range(7)]
	partCenters += [[315 + dx, 54.5 + 53 * i] for i in range(6)]

def insert3mmPart(part, posIndex, layer="late", offset=[0, 0], z = True):
	Hex.transformInsert(cut3mm, layer, part, partCenters[posIndex][0] + offset[0], partCenters[posIndex][1] + offset[1], z = z)

for i in range(4):
	insert3mmPart(iPlate1, i)

for i in range(4, len(partCenters)):
	insert3mmPart(plate, i)

PachinkoPositions = [[0, 0], [Flipper.distance2, 0], [-Flipper.distance2, 0], [0, -Flipper.distance2 * 1.15]]
for k in [0, 1, 4, 5]:
	for i in PachinkoPositions:
		insert3mmPart(Flipper.pachinkoPin, k, layer="early", offset=i)

for i in [2, 3]:
	insert3mmPart(Teleport.text["Combo"], i, layer="early", offset=[0, 5])
	insert3mmPart(Teleport.star2[2], i, layer="early", offset=[0, -8])
	insert3mmPart(Teleport.star2[1], i, layer="mid", offset=[0, -8])

insert3mmPart(Teleport.teleInDeco[0], 6, layer="early", offset=[0, -1], z=False)
insert3mmPart(Teleport.teleOutDeco[0], 7, layer="early", z=False)

for i in [8, 9, 10, 11]:
	insert3mmPart(Flipper.flipperCircleBase, i, layer="early")

insert3mmPart(Flipper.flipperCircleBase, 12, offset=Flipper.metastableCenter, layer="early")

insert3mmPart(Flipper.flipperCircleBase, 13, offset=Flipper.sfCenter, layer="early")
insert3mmPart(Flipper.ofDecor, 14, layer="early", z = False)
insert3mmPart(Specials.flame, 15, layer="early")

insert3mmPart(Specials.star, 16, layer="early")

insert3mmPart(Specials.cloneArrow, 17, layer="early", z = False)

insert3mmPart(Specials.kingRipple, 18, layer="early", z = False)

Hex.transformInsert(cut3mm, "late", Secret.qCircle, [30, 43, 120, 133], 20)
Hex.transformInsert(cut3mm, "late", Specials.star, [210, 223], [12, 23])
Hex.transformInsert(cut3mm, "late", Carcassonne.meepleDeco, [305, 320], 20)

Hex.transformInsert(cut3mm, "mid", Teleport.star2[1], [398, 417], 16)
Hex.transformInsert(cut3mm, "early", Teleport.star2[2], [398, 417], 16)

Hex.transformInsert(cut3mm, "early", Specials.arcs[0], 37, 373, 180)
Hex.transformInsert(cut3mm, "early", Specials.arcs[1], 128, 375, 180)
Hex.transformInsert(cut3mm, "early", Specials.arcs[2], 222, 376, 180)

Hex.transformInsert(cut3mm, "mid", Specials.bombShield, 315, 376)
Hex.transformInsert(cut3mm, "early", Specials.bombTop, 315, 396)

Hex.transformInsert(cut3mm, "late", Teleport.teleWedge, 65, 388)
Hex.transformInsert(cut3mm, "late", Hex.flipY(Teleport.teleWedge), 65, 391)

Hex.transformInsert(cut3mm, "late", Specials.cloneRampPad, 30, 385)
Hex.transformInsert(cut3mm, "late", Specials.cloneWedge, 40, 388)
Hex.transformInsert(cut3mm, "late", Hex.flipY(Specials.cloneWedge), 40, 391)

try:
	Redacted.insert3mm_Cut4(cut3mm)
except:
	pass

Hex.transformInsert(cut3mm, "late", Specials.kingCircle, 410, 367)
Hex.transformInsert(cut3mm, "mid", Specials.kingDeco, 410, 367)
Hex.transformInsert(cut3mm, "late", Specials.kingRaise, 504, 360)

Hex.transformInsert(cut3mm, "late", LargeBoard.onRampHigh, [400, 485], 370, 180)
Hex.transformInsert(cut3mm, "late", LargeBoard.onRampLow, 577, [0, 70], 180)
Hex.transformInsert(cut3mm, "late", LargeBoard.onRampHigh, 577, [210, 280])
Hex.transformInsert(cut3mm, "late", LargeBoard.onRampLow, 577, [350, 420])

#????
#Hex.transformInsert(cut3mm, "late", Hex.makeCircle(7), 222, [375, 393])
#Hex.transformInsert(cut3mm, "mid", Hex.makeCircle(4), 222, [375, 393])

length3mm = Hex.getLength()

Hex.saveXML(cut3mm, "Cut/Cut4_3mm.svg")
Hex.saveXML(cut10mm, "Cut/Cut4_10mm.svg")

print("=======================")
print("10mm Length: " + str(length10mm))
print("3mm Length: " + str(length3mm))
print("Price: ~" + str(int((length3mm / 47 +  length10mm / 4.1) / 60 * 1.5) + 1) + "€")
