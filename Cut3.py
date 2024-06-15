import math
import Hex
import QuadTrap
import Misc
import Specials
import TileForTwo
import Secret
import Asterisk
import DIC

cut3mm = Hex.loadCutTemplate(True)
cut6mm = Hex.loadCutTemplate(True)
cut10mm = Hex.loadCutTemplate(True)

Hex.resetLength()

# TODO 10mm
# rhsbt Left x1 	#
# rhsbt Right x1	#
# small Corner x2		#
# round Corner x4		#
# xefros corner L x1 	#
# xefros corner R x1	#
# quad trap center x1	#
# bomb part x1			#
# recursion part x1		#


for i in range(1, 5):
	Hex.transformInsert(cut10mm, "late" if i == 1 else "mid", Specials.rhsbtLeft[i], 32, 12)
	Hex.transformInsert(cut10mm, "late" if i == 1 else "mid", Specials.rhsbtRight[i], 27, 12)

for i in range(6):
	t = None
	if i == 1 or i == 4: 
		t = Asterisk.corner
	else:
		t = DIC.roundCorner
	n = Hex.polarPos(8, i * 60)
	if t != None:
		Hex.transformInsert(cut10mm, "late", t, 75 - n[0], 22 - n[1], i * 60)

Hex.transformInsert(cut10mm, "late", DIC.roundCorner, 95, 21, 0)

Hex.transformInsert(cut10mm, "late", Misc.indentCorner, 98, 17)
Hex.transformInsert(cut10mm, "late", Hex.flipY(Misc.indentCorner), 124, 12, 120)

Hex.transformInsert(cut10mm, "late", QuadTrap.centerPart, 72, 70)
Hex.transformInsert(cut10mm, "late", Specials.bombPiece, 32, 70)
Hex.transformInsert(cut10mm, "late", Specials.recursion, 112, 70)

length10mm = Hex.getLength()
Hex.resetLength()

# TODO 6mm
# secret pin x24			#
# secret holder x24			#
# small corner x4			#
# large corner with gap x2	#
# round corner x3			#
# dic part x2				#
# secret trigger part x2	#
# xc part x1				#
# xc corner 1 x1			#
# xc corner 2 x1			#
# xc corner 3 x1			#
# tft half bottom x1		#
# tft half top x1			#
# tft corner bottom x1		#
# tft corner top x1			#
# dcxl mid bottom x1		#
# dcxl side bottom L x1		#
# dcxl side bottom R x1		#
# dcxl mid top x1			#
# dcxl side top L x1		#
# dcxl side top R x1		#

for x in range(5):
	p = [25 + x * 35, 22 if (x % 2) == 0 else 40]
	for r in range(6):
		n = Hex.add(Hex.polarPos(-12, r * 60), p)
		Hex.transformInsert(cut6mm, "mid", Secret.secretPin, n[0], n[1], 60 * r)
		n = Hex.add(Hex.polarPos(-8, r * 60), p)
		Hex.transformInsert(cut6mm, "late", Secret.secretHolder, n[0], n[1], 60 * r)

for r in range(6):
	n = Hex.add(Hex.polarPos(-8, r * 60), [25, 62])
	Hex.transformInsert(cut6mm, "late", Asterisk.corner, n[0], n[1], 60 * r)
	n = Hex.add(Hex.polarPos(-8, r * 60), [95, 62])
	t = DIC.roundCorner
	rOff = 0
	if r == 3:
		t = DIC.xcSmallCorner
		rOff = 180
	if r == 2:
		t = DIC.xcLargeCorner
		rOff = 120
	if r == 4:
		t = DIC.xcLargeCorner2
		rOff = -120
	Hex.transformInsert(cut6mm, "late", t, n[0], n[1], 60 * r + rOff)
Hex.transformInsert(cut6mm, "mid", DIC.roundCorner, 122, 62, 180)

Hex.transformInsert(cut6mm, "mid", Secret.secretBigCorner, 60, 92, 120)
Hex.transformInsert(cut6mm, "mid", Secret.secretBigCorner, 130, 92, 120)
Hex.transformInsert(cut6mm, "mid", DIC.partIC, 160, 67, 0)
Hex.transformInsert(cut6mm, "mid", DIC.partIC, 167, 67, 180)

Hex.transformInsert(cut6mm, "mid", Secret.secretTriggerPart, 26, 107, 0)
Hex.transformInsert(cut6mm, "mid", Secret.secretTriggerPart, 33, 107, 180)

Hex.transformInsert(cut6mm, "mid", DIC.xcCenter, 63, 107, 0)

def doubleInsert(tile, pos, angle=0, backup=False):
	Hex.transformInsert(cut6mm, "mid", tile, pos[0][0], pos[0][1], angle)
	Hex.transformInsert(cut6mm, "mid", Hex.flipY(tile), pos[1][0], pos[1][1], angle)
	if backup != False:
		Hex.transformInsert(cut6mm, "mid", tile, backup[0], backup[1], angle)

def genCircle(radius):
	return [[-radius, 0], ["arc", 0, radius], [radius, 0], ["arc", 0, -radius], [-radius, 0]]

def makeAlignCircle(pos, offset, radius, spareCircle, backup=False):
	circle = genCircle(radius)
	aligner = [Hex.polarPos(radius, -20), ["arc", radius, 0], Hex.polarPos(radius, 20)]
	Hex.transformInsert(cut6mm, "early", circle, pos[1][0] + offset[0], pos[1][1] + offset[1])
	Hex.transformInsert(cut6mm, "early", aligner, pos[0][0] + offset[0], pos[0][1] - offset[1], [30, 150, -90], z = False)
	Hex.transformInsert(cut6mm, "early", circle, spareCircle[0], spareCircle[1])
	if backup != False:
		Hex.transformInsert(cut6mm, "early", circle, backup[0] + offset[0], backup[1] - offset[1])

halfPart = [[105, 108], [150, 110]]
doubleInsert(TileForTwo.halfPart, halfPart)
makeAlignCircle(halfPart, [-15, 0], 4.5, [53, 12])

thirdPart = [[142, 120], [98, 92]]
doubleInsert(TileForTwo.thirdPart, thirdPart)
makeAlignCircle(thirdPart, Hex.polarPos(15, -30), 3, [120, 12])

centerPart = [[198, 42], [198, 96]]
doubleInsert(TileForTwo.centerPart, centerPart)
makeAlignCircle(centerPart, [0, -15], 4.5, [67, 12])

def doubleAdd(a, b):
	return [Hex.add(a[0], b), Hex.add(a[1], b)]

leftPart = doubleAdd(centerPart, [8, 0])
backup1 = [234, 126]
doubleInsert(Hex.flipY(TileForTwo.rightPart), leftPart, 180, backup1)
makeAlignCircle(leftPart, Hex.polarPos(20, -165), 3, [140, 12], backup1)

backup2 = [161, 126]
rightPart = doubleAdd(centerPart, [-8, 0])
doubleInsert(TileForTwo.rightPart, rightPart, 0, backup2)
makeAlignCircle(rightPart, Hex.polarPos(20, -15), 3, [130, 12], backup2)

innerPad = TileForTwo.innerPad
anchorHeight = TileForTwo.anchorHeight
anchorWidth = TileForTwo.anchorWidth
test = [[10, 0], [10, innerPad], [10 + anchorHeight, innerPad], [10 + anchorHeight, innerPad + anchorWidth], [10, innerPad + anchorWidth], [10, 10],
		[-10, 10], [-10, innerPad + anchorWidth], [-10 - anchorHeight, innerPad + anchorWidth], [-10 - anchorHeight, innerPad], [-10, innerPad], [-10, 0]]

Hex.transformInsert(cut6mm, "late", test, 198, 4)

length6mm = Hex.getLength()
Hex.resetLength()

# TODO 3mm
# Quad Trap
# - 2 plate
# - solid plate
# Xefros
# - 6 plate
# - solid plate
# Bomb
# - 3 plate
# - solid plate
# RHSBT
# - 1 plate
# - solid plate + deco
# Recursion
# - 6 plate
# - solid plate + deco
# Secret DIC
# - 6 plate
# - solid plate x2
# Secret X
# - 6 plate
# - solid plate x2
# Secret XC
# - 6 plate
# - solid plate x2
# Secret Trigger
# - 6 plate
# - solid plate
# - solid plate + deco
# TFT
# - 6 plate DE
# - 6 plate EN
# - solid plate x2
# DCXL
# - 2 plate DE
# - 2 plate EN
# - solid plate x2

#==========
# 2 plate x1			#
# 6 plate x6			#
# 3 plate x1			#
# 1 plate x1			#
# 2 plate EN x1			#
# 2 plate DE x1			#
# 6 plate EN x1			#
# 6 plate DE x1			#
## solid plate x14 					#
# solid plate rhsbt x1				#
# solid plate recursion x1			#
# solid plate secret trigger x1		#
# circle gap x4						#
# questionmark x4					#
# rhsbt arc 1 x1		#
# rhsbt arc 2 x1		#
# rhsbt arc 3 x1		#
# bomb ceil 1 x1 		#
# bomb ceil 2 x1		#
# inner secret align x1		#
# outer secret align x1		#

basePlate = Hex.basePlate();

platePositions = [
		[32, 30], [32, 83], [32, 136], [32, 189],
		[77, 56], [77, 109], [77, 162], [77, 215],
		[122, 30], [122, 83], [122, 136], [122, 189],
		[167, 56], [167, 109], [167, 162], [167, 215],
		[212, 30], [387, 188]
]

platePositions2 = [
		[212, 83], [212, 136], [212, 189], [257, 56]
]


for i in platePositions:
	Hex.transformInsert(cut3mm, "late", basePlate, i[0], i[1])

Hex.transformInsert(cut3mm, "early", Specials.flame, platePositions[0][0], platePositions[0][1])
Hex.transformInsert(cut3mm, "early", Specials.recursionRipple, platePositions[2][0], platePositions[2][1], [i * 60 for i in range(6)], z=False)
Hex.transformInsert(cut3mm, "mid", Secret.star, platePositions[1][0], platePositions[1][1])
Hex.transformInsert(cut3mm, "early", Secret.qMark, platePositions[1][0], platePositions[1][1])
Hex.transformInsert(cut3mm, "early", Secret.triggerRipple, platePositions[1][0], platePositions[1][1], [0, 60, 180, 240], z=False)
Hex.transformInsert(cut3mm, "mid", Specials.star, platePositions[3][0], platePositions[3][1])

Hex.transformInsert(cut3mm, "mid", Secret.aligner[1], platePositions[17][0], platePositions[17][1])


for i in platePositions2:
	Hex.transformInsert(cut3mm, "late", basePlate, i[0], i[1])
	Hex.transformInsert(cut3mm, "mid", Secret.secretCircle, i[0], i[1])
	Hex.transformInsert(cut3mm, "early", Secret.qCircle, i[0], i[1] + 15)
	Hex.transformInsert(cut3mm, "early", Secret.questionMark, i[0] + 0.5 * (Secret.qA + Secret.qB), i[1] + 5)

indexPositions = [
	[257, 109], [257, 162], [257, 212],
	[300, 30], [300, 83], [300, 136], [300, 189],
	[343, 56], [343, 109], [343, 162], [343, 212],
	[386, 30], [386, 83]]
indexTypes = [2, 6, 6, 6, 6, 6, 6, "xx---x", 1, 2, 2, 6, 6]

for i in range(len(indexPositions)):
	j = indexPositions[i]
	Hex.transformInsert(cut3mm, "late", Hex.indexedPlate(indexTypes[i]), j[0], j[1])

for i in [9, 11]:
	j1 = indexPositions[i]
	Hex.transformInsert(cut3mm, "mid", TileForTwo.text["Open"], j1[0], j1[1] + 3)
	Hex.transformInsert(cut3mm, "mid", TileForTwo.text["Me"], j1[0], j1[1] + 12)
	Hex.transformInsert(cut3mm, "mid", TileForTwo.star[1], j1[0], j1[1] - 8)
	Hex.transformInsert(cut3mm, "early", TileForTwo.star[2], j1[0], j1[1] - 8)

	j2 = indexPositions[i + 1]
	Hex.transformInsert(cut3mm, "mid", TileForTwo.text["Öffne"], j2[0], j2[1] + 3)
	Hex.transformInsert(cut3mm, "mid", TileForTwo.text["Mich"], j2[0], j2[1] + 12)
	Hex.transformInsert(cut3mm, "mid", TileForTwo.star[1], j2[0], j2[1] - 8)
	Hex.transformInsert(cut3mm, "early", TileForTwo.star[2], j2[0], j2[1] - 8)

Hex.transformInsert(cut3mm, "mid", Specials.bombShield, 386, 136)
Hex.transformInsert(cut3mm, "early", Specials.bombTop, 386, 155)

Hex.transformInsert(cut3mm, "early", Specials.arcs[0], 32, 241, 180)
Hex.transformInsert(cut3mm, "early", Specials.arcs[1], 122, 242, 180)
Hex.transformInsert(cut3mm, "early", Specials.arcs[2], 212, 244, 180)

for x in [65, 78, 91, 155, 168, 181]:
	Hex.transformInsert(cut3mm, "mid", Specials.star, x, 17)

for x in [258, 342]:
	Hex.transformInsert(cut3mm, "early", TileForTwo.star[2], x, 17)
	Hex.transformInsert(cut3mm, "mid", TileForTwo.star[1], x, 17)

#Hex.transformInsert(cut3mm, "late", genCircle(4.5), [32, 122, 212], [227, 238])
#Hex.transformInsert(cut3mm, "late", genCircle(3.0), [286, 296, 306, 316], [222, 231])

length3mm = Hex.getLength()

Hex.saveXML(cut3mm, "Cut/Cut3mm.svg")
Hex.saveXML(cut6mm, "Cut/Cut6mm.svg")
Hex.saveXML(cut10mm, "Cut/Test10mm.svg")

print("10mm Length: " + str(length10mm))
print("6mm Length: " + str(length6mm))
print("3mm Length: " + str(length3mm))
