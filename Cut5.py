import math
import Hex
import Asterisk
import DIC
import Teleport
import Specials
import Specials_2
import Carcassonne
import TwoTrap
import LinearTrap
import Flipper
import Display
import EdgeOverhang_2 as EdgeOverhang
import Misc
import Ternary

cut3mm = Hex.loadCutTemplate(True)
cut10mm = Hex.loadCutTemplate(True)

# Content:
#
# Display Stand
#
# New Tiles
#  Edge Overhang
#  Ternary
#  Gear
#  Instant Win
#  Carcasonne J x2 + I (x2 ??) + Y x 1 + DC x 1 + X2 x 1
#  Carcasonne M
#  Discard x2
#
# Modified Repeats:
#  2 Trap
#  Teleport
#  LinearTrap
#  Flipper DL
#
# Repeats:
#  Bomb 10mm part 
#  Clone
#  Metastable
#  OpenFlipper
#  Carcasonne (0 x4 + C x2)
#
# x----- 7
# x--x-- 1
# xx---x 3
# xxxxxx 14
# xx-xx- 3

# ==== 10 mm ====

Hex.transformInsert(cut10mm, "late", Specials.bombPiece, 32, 30)

Hex.transformInsert(cut10mm, "late", Specials.cloneRight, 25, 83, 0)
Hex.transformInsert(cut10mm, "late", Specials.cloneLeft, 32, 83, 0)


for i in range(4):
	Hex.transformInsert(cut10mm, "mid", Carcassonne.xPlate, 32, 136 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "late", Carcassonne.plate, 32, 136 + 53 * i, 0)
for i in range(2):
	Hex.transformInsert(cut10mm, "mid", Carcassonne.cInner, 77, 56 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "late", Carcassonne.cOuter, 77, 56 + 53 * i, 0)
for i in range(2, 4):
	Hex.transformInsert(cut10mm, "mid", Carcassonne.jBigInner, 77, 56 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "late", Carcassonne.jBig, 77, 56 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "mid", Carcassonne.jSmallInner, 70, 56 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "late", Carcassonne.jSmall, 70, 56 + 53 * i, 0)
for i in [4]:
	Hex.transformInsert(cut10mm, "mid", Carcassonne.halfPartInner, 70, 56 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "late", Carcassonne.halfPart, 70, 56 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "mid", Carcassonne.halfPartInner, 77, 56 + 53 * i, 180)
	Hex.transformInsert(cut10mm, "late", Carcassonne.halfPart, 77, 56 + 53 * i, 180)
for i in [5]:
	Hex.transformInsert(cut10mm, "mid", Carcassonne.triggerIn, 77, 56 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "late", Carcassonne.triggerOut, 77, 56 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "early", Specials_2.iwHoles, 172, 56 + 53 * i, 0)
	Hex.transformInsert(cut10mm, "late", Specials_2.iwPart, 172, 56 + 53 * i, 0)

Hex.transformInsert(cut10mm, "mid", Carcassonne.bigCornerInner, 122, 30, [0, 120, 240])
Hex.transformInsert(cut10mm, "late", Asterisk.bigCorner, 122, 30, [0, 120, 240])

Hex.transformInsert(cut10mm, "mid", Carcassonne.dcInner, 112, 83, 0)
Hex.transformInsert(cut10mm, "late", Carcassonne.dcOuter, 112, 83, 0)

Hex.transformInsert(cut10mm, "early", Carcassonne.meeple, 32, 30, 0)

Hex.transformInsert(cut10mm, "late", Hex.flipY(LinearTrap.rightPart), 115, 136, 0)
Hex.transformInsert(cut10mm, "late", Hex.flipY(LinearTrap.leftPart), 122, 136, 0)

Hex.transformInsert(cut10mm, "late", TwoTrap.smallCorner2, 115, 189, 0)
Hex.transformInsert(cut10mm, "late", TwoTrap.largeCorner2, 122, 189, 0)

Hex.transformInsert(cut10mm, "late", Hex.flipY(Flipper.drHalf), 118, 242, 0)
Hex.transformInsert(cut10mm, "late", Hex.flipY(Flipper.drRight), 110, 242, 0)
Hex.transformInsert(cut10mm, "late", Flipper.metastableHalf, 142, 242, 0)
Hex.transformInsert(cut10mm, "late", Hex.flipY(Flipper.metastableHalf), 127, 242, 0)

#Hex.transformInsert(cut10mm, "late", Teleport.teleSmallCorner, 490 - n[0] * 1.5, 245 - n[1] * 1.5, i * 60 + 60)

Hex.transformInsert(cut10mm, "late", Teleport.teleCatch, 125, 290, 0)

Hex.transformInsert(cut10mm, "late", Teleport.teleLargeCorner, 125, 295, 0)
Hex.transformInsert(cut10mm, "late", Hex.flipY(Teleport.teleLargeCorner), 125, 295, 180)

Hex.transformInsert(cut10mm, "late", Teleport.teleTop, 122, 350, 0)


Hex.transformInsert(cut10mm, "early", Flipper.ofCorner, 95, 47, 180)
Hex.transformInsert(cut10mm, "early", Hex.flipY(Flipper.ofCorner), 95, 65, 180)

Hex.transformInsert(cut10mm, "late", Flipper.bottomPiece, 77, 34, 180)

Hex.transformInsert(cut10mm, "late", Flipper.ofSwitch, 152, 55)
Hex.transformInsert(cut10mm, "mid", Flipper.flipperCircle, 152, 55)

Hex.transformInsert(cut10mm, "late", Flipper.smallFlipper, 153, 100, 90)
Hex.transformInsert(cut10mm, "mid", Flipper.flipperCircle, 153, 100)

Hex.transformInsert(cut10mm, "late", Flipper.msPart, 140, 77, 0)
Hex.transformInsert(cut10mm, "mid", Flipper.msBallCircle, 140, 77, 0)
Hex.transformInsert(cut10mm, "mid", Flipper.flipperCircle, 140, 77, 0)

Hex.transformInsert(cut10mm, "early", EdgeOverhang.roundCorner, [45, 60], 242, 0)
Hex.transformInsert(cut10mm, "late", EdgeOverhang.largePart, 158, 136, 0)
Hex.transformInsert(cut10mm, "early", EdgeOverhang.mainPlateHoles, 158, 136, 0)

Hex.transformInsert(cut10mm, "late", EdgeOverhang.innerWall, 142, 55, 0)
Hex.transformInsert(cut10mm, "late", EdgeOverhang.outerWall, 136, 55, 0)
Hex.transformInsert(cut10mm, "early", EdgeOverhang.edgeHoles, 136, 55, 0)

Hex.transformInsert(cut10mm, "late", Specials_2.gearPillar, 20, 330, 0)
Hex.transformInsert(cut10mm, "early", Specials_2.iwInnerHole, 40, 340, 0)
Hex.transformInsert(cut10mm, "late", Specials_2.iwOuterHole, 40, 340, 0)

Hex.transformInsert(cut10mm, "early", Specials_2.recPart, 158, 189, -120, z = False)
Hex.transformInsert(cut10mm, "late", Specials_2.discardLarge, 158, 189, -120)
Hex.transformInsert(cut10mm, "late", Specials_2.discardSmall, 125, 298, 120)

Hex.transformInsert(cut10mm, "early", Specials_2.recPart, 172, 267, 180, z = False)
Hex.transformInsert(cut10mm, "late", Specials_2.discardLarge, 172, 267, 180)
Hex.transformInsert(cut10mm, "late", Specials_2.discardSmall, 197, 230, 180)

for i in range(6):
	n = Hex.polarPos(8.5, i * 60)
	Hex.transformInsert(cut10mm, "early", DIC.roundCorner, 32 - n[0], 136 - n[1], i * 60)
	Hex.transformInsert(cut10mm, "early", DIC.roundCorner, 32 - n[0], 189 - n[1], i * 60)
	Hex.transformInsert(cut10mm, "early", Specials_2.gearCorner, 32 - n[0], 295 - n[1], i * 60)

Hex.transformInsert(cut10mm, "early", Display.holes, 230, 75, 90)
Hex.transformInsert(cut10mm, "late", Display.displayRect, 230, 75, 90)
Hex.transformInsert(cut10mm, "late", Display.stand, 247, 155, 180)
Hex.transformInsert(cut10mm, "late", Hex.flipY(Display.stand), 247, 235, 180)


Hex.transformInsert(cut10mm, "late", Ternary.leftFlipper, 204, 340)
Hex.transformInsert(cut10mm, "mid", Ternary.flipperCircle, 204, 340)

Hex.transformInsert(cut10mm, "late", Ternary.rightFlipperMod, 225, 252, 90)
Hex.transformInsert(cut10mm, "mid", Ternary.flipperCircle, 225, 252, 90)

Hex.transformInsert(cut10mm, "late", Ternary.smallCorner, [215, 230], 290)
Hex.transformInsert(cut10mm, "late", Hex.flipY(Ternary.smallCorner), [215, 230], 320)
Hex.transformInsert(cut10mm, "late", Ternary.topLeftCorner, 218, 294)
Hex.transformInsert(cut10mm, "late", Ternary.topRightMod1, 202, 284)
Hex.transformInsert(cut10mm, "late", Ternary.topRightMod2, 195, 336)

Hex.transformInsert(cut10mm, "late", Misc.C3Part, 235, 195)
Hex.transformInsert(cut10mm, "mid", Misc.aligners, 235, 195, z=False)
Hex.transformInsert(cut10mm, "late", Misc.holdPin, 205, [179, 170, 161, 152])
Hex.transformInsert(cut10mm, "late", Misc.holdPin, 197, [168, 159])

length10mm = Hex.getLength()
Hex.resetLength()

# ===== 3 mm =====

platePositionsBase = [
		[32, 30],
		[77, 56],
		[122, 30],
		[167, 56],
		[212, 30],
		[257 , 56],
		[302 , 30],
]
indexTypes = [1]*7 + [2] + ["xx---x"]*3 + ["xx-xx-"]*3 + [6]*14
basePlate = Hex.basePlate();

for i in range(len(indexTypes)):
	y = i // 7
	basePos = platePositionsBase[i % 7]
	if i == 13:
		Hex.transformInsert(cut3mm, "early", EdgeOverhang.plateHole, basePos[0], basePos[1] + 53 * y)
		Hex.transformInsert(cut3mm, "late", EdgeOverhang.plateOut, basePos[0], basePos[1] + 53 * y)
	else:
		Hex.transformInsert(cut3mm, "late", basePlate, basePos[0], basePos[1] + 53 * y)
	Hex.transformInsert(cut3mm, "late", Hex.indexedPlate(indexTypes[i]), basePos[0], basePos[1] + 210 + 50 * y)

def insert3mmPart(part, posIndex, layer="late", offset=[0, 0], z = True, base = False):
	yIndex = posIndex // 7
	basePos = platePositionsBase[posIndex % 7]
	if base:
		y = basePos[1] + 210 + 50 * yIndex
	else:
		y = basePos[1] + 53 * yIndex
	Hex.transformInsert(cut3mm, layer, part, basePos[0] + offset[0], y + offset[1], z = z)

for i in [0, 1]:
	insert3mmPart(Teleport.text["Combo"], i, layer="early", offset=[0, 5], base=True)
	insert3mmPart(Teleport.star2[2], i, layer="early", offset=[0, -8], base=True)
	insert3mmPart(Teleport.star2[1], i, layer="mid", offset=[0, -8], base=True)

insert3mmPart(Teleport.teleInDeco[2], 0, layer="early", offset=[0, -1], z=False)
insert3mmPart(Teleport.teleOutDeco[2], 1, layer="early", z=False)
insert3mmPart(Specials.cloneArrow, 2, layer="early", z = False)
insert3mmPart(Carcassonne.arrowDeco, 3, layer="early", z = False)
insert3mmPart(Carcassonne.star2[2], 3, layer="early", offset=[0, 15])
insert3mmPart(Carcassonne.star2[1], 3, layer="mid", offset=[0, 15])
insert3mmPart(Flipper.flipperCircleBase, 4, offset=Flipper.metastableCenter, layer="early")
insert3mmPart(Flipper.ofDecor, 5, layer="early", z = False)
insert3mmPart(Flipper.flipperCircleBase, 6, offset=[-Flipper.sfCenter[0], Flipper.sfCenter[1]], layer="early")
insert3mmPart(Carcassonne.triggerRipple, 7, layer="early", z=False)
insert3mmPart(Specials_2.gearBase, 8, layer="early", z = False)
insert3mmPart(Specials_2.iwRipple, 9, layer="early")
insert3mmPart(Specials_2.iwInnerHole, 2, layer="early", base=True)
insert3mmPart(Ternary.baseHoles, 10, layer="early", base=False)
insert3mmPart(Ternary.baseHoles[3], 3, layer="early", base=True)


Hex.transformInsert(cut3mm, "mid", Teleport.star2[1], [248, 265], 16)
Hex.transformInsert(cut3mm, "early", Teleport.star2[2], [248, 265], 16)

Hex.transformInsert(cut3mm, "late", Teleport.teleWedge, 29, 423)
Hex.transformInsert(cut3mm, "late", Hex.flipY(Teleport.teleWedge), 29, 426)

Hex.transformInsert(cut3mm, "late", Specials.cloneWedge, 70, 20)
Hex.transformInsert(cut3mm, "late", Hex.flipY(Specials.cloneWedge), 160, 10)
Hex.transformInsert(cut3mm, "late", Specials.cloneRampPad, 350, 20)

Hex.transformInsert(cut3mm, "late", Carcassonne.shield, [110, 120, 130], 425)

Hex.transformInsert(cut3mm, "late", EdgeOverhang.outerBase, 302, 30 + 53 * 3)

Hex.transformInsert(cut3mm, "early", EdgeOverhang.pillar[2], 385, [20, 35, 50, 65, 80, 95, 110, 125, 140], 90)
Hex.transformInsert(cut3mm, "late", EdgeOverhang.pillar[1], 385, [20, 35, 50, 65, 80, 95, 110, 125, 140], 90)

Hex.transformInsert(cut3mm, "late", Specials_2.gearBottom, 345, 245, 0)
Hex.transformInsert(cut3mm, "early", Specials_2.gearPillar, 345, 245, 0)
Hex.transformInsert(cut3mm, "late", Specials_2.gearTop, 340, 272, 0)
Hex.transformInsert(cut3mm, "late", Specials_2.iwOuterHole, 340, 304, 0)
Hex.transformInsert(cut3mm, "late", Specials_2.iwArc, 373, [150, 174, 198, 222], 0)

Hex.transformInsert(cut3mm, "late", Specials_2.discardCeil2, [347, 357], 340, -150)
Hex.transformInsert(cut3mm, "late", Specials_2.discardCeil1, [357, 367], 340, -150)

Hex.transformInsert(cut3mm, "early", Display.slots, 427, 74, 90)
Hex.transformInsert(cut3mm, "late", Display.displayRect, 427, 74, 90)
Hex.transformInsert(cut3mm, "late", Display.baseRect, 422, 215, 90)
Hex.transformInsert(cut3mm, "late", Display.edgeRect, [376, 386], 309, 90)

length3mm = Hex.getLength()

Hex.saveXML(cut3mm, "Cut/Cut5_3mm.svg")
Hex.saveXML(cut10mm, "Cut/Cut5_10mm.svg")

print("=======================")
print("10mm Length: " + str(length10mm))
print("3mm Length: " + str(length3mm))
print("Price: ~" + str(int((length3mm / 47 +  length10mm / 4.1) / 60 * 1.5) + 1) + "€")
