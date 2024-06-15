import Hex
import Deco
import Text
import math
import Asterisk

plate = Hex.basePlate()

star = ["group", Deco.makeStar(8), Deco.makeStar(4)]

text = {}

for t in ["Open", "Me", "Öffne", "Mich"]:
	text[t] = Hex.scale(Text.getText(t), 6)

al = Hex.relativeToCenter(plate[1], plate[2], +0.5 * Hex.TrackWidth, 0)
ar = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, 0)
bl = Hex.relativeToCenter(plate[4], plate[5], -0.5 * Hex.TrackWidth, 0)

lDown = Hex.relativeToCenter(plate[3], plate[4], 0.5 * Hex.TrackWidth, 0)
lUp = Hex.relativeToCenter(plate[3], plate[4], -0.5 * Hex.TrackWidth, 0)

rDown = Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, 0)
rUp = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)

innerPad = 2
anchorHeight = 7
anchorWidth = 4

halfPart = [
	Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth, -anchorHeight),
	Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth + innerPad, -anchorHeight),
	Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth + innerPad, 0),
	Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth + innerPad + anchorWidth, 0),
	Hex.relativeToCenter(plate[1], plate[2], 0.5 * Hex.TrackWidth + innerPad + anchorWidth, -anchorHeight),
	Hex.intersect([0, plate[1][1] + anchorHeight], 0, plate[2], -120),
	plate[3], plate[4], bl]

thirdPart = [
	Hex.polarPos(Hex.TrackWidth / math.sqrt(3), 30),
	rUp, plate[0],
	Hex.intersect([0, plate[1][1] + anchorHeight], 0, plate[1], -60),
	Hex.relativeToCenter(plate[1], plate[2], -(0.5 * Hex.TrackWidth + innerPad + anchorWidth), -anchorHeight),
	Hex.relativeToCenter(plate[1], plate[2], -(0.5 * Hex.TrackWidth + innerPad + anchorWidth), 0),
	Hex.relativeToCenter(plate[1], plate[2], -(0.5 * Hex.TrackWidth + innerPad), 0),
	Hex.relativeToCenter(plate[1], plate[2], -(0.5 * Hex.TrackWidth + innerPad), -anchorHeight),
	Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, -anchorHeight),
	]

centerPad = 2.5
dcxlRad = 25

innerPad = 1.6
anchorWidth = 3

dcxlRCenter = Hex.add(Hex.intersect([0.5 * (centerPad + Hex.TrackWidth),0], 90, Hex.relativeToCenter(plate[5], plate[0], 0, 0), 150), Hex.polarPos(dcxlRad / math.cos(30.0 / 180.0 * math.pi), 30))
dcxlLCenter = [-dcxlRCenter[0], dcxlRCenter[1]]

centerPart = [
	plate[5], rDown,
	Hex.add(dcxlRCenter, Hex.polarPos(dcxlRad + 0.5 * Hex.TrackWidth, -120)),
	["arc"] + Hex.add(dcxlRCenter, Hex.polarPos(dcxlRad + 0.5 * Hex.TrackWidth, -150)),
	Hex.add(dcxlRCenter, [-dcxlRad - 0.5 * Hex.TrackWidth, 0]),
	Hex.relativeToCenter(plate[1], plate[2], -0.5 * centerPad, 0),
	Hex.relativeToCenter(plate[1], plate[2], 0.5 * centerPad, 0),
	Hex.add(dcxlLCenter, [dcxlRad + 0.5 * Hex.TrackWidth, 0]),
	["arc"] + Hex.add(dcxlLCenter, Hex.polarPos(dcxlRad + 0.5 * Hex.TrackWidth, -30)),
	Hex.add(dcxlLCenter, Hex.polarPos(dcxlRad + 0.5 * Hex.TrackWidth, -60)),
	lDown, plate[4]]

rightPart = [	
	Hex.intersect([0, plate[1][1] + anchorHeight], 0, plate[1], 120),
	Hex.relativeToCenter(plate[1], plate[2], -0.5 * centerPad - Hex.TrackWidth - innerPad - anchorWidth, -anchorHeight),
	Hex.intersect([0.5 * centerPad + Hex.TrackWidth + innerPad + anchorWidth, 0], 90, plate[1], 120),
	plate[1],
	Hex.relativeToCenter(plate[1], plate[2], -0.5 * centerPad - Hex.TrackWidth - innerPad, 0),
	Hex.relativeToCenter(plate[1], plate[2], -0.5 * centerPad - Hex.TrackWidth - innerPad, -anchorHeight),
	Hex.relativeToCenter(plate[1], plate[2], -0.5 * centerPad - Hex.TrackWidth, -anchorHeight),
	Hex.add(dcxlRCenter, [-dcxlRad + 0.5 * Hex.TrackWidth, 0]),
	["arc"] + Hex.add(dcxlRCenter, Hex.polarPos(dcxlRad - 0.5 * Hex.TrackWidth, -150)),
	Hex.add(dcxlRCenter, Hex.polarPos(dcxlRad - 0.5 * Hex.TrackWidth, -120)),
	rUp,
	plate[0]]

def doubleBase(i):
	tile = Hex.loadTemplate()
	Hex.changeWidth(tile, "6mm")
	Hex.transformInsert(tile, "3mm", plate, [50, 250], [50, 110])
	iPlate = Hex.indexedPlate(i)
	Hex.transformInsert(tile, "3mm", iPlate, 50, [170, 230])
	Hex.transformInsert(tile, "3mm", iPlate, 250, [50, 110])
	Hex.transformInsert(tile, "3mm", star, 50, [162, 222])

	Hex.transformInsert(tile, "3mm", text["Open"], 50, 173)
	Hex.transformInsert(tile, "3mm", text["Me"], 50, 182)

	Hex.transformInsert(tile, "3mm", text["Öffne"], 50, 233)
	Hex.transformInsert(tile, "3mm", text["Mich"], 50, 242)
	return tile

def doubleInsert(tile, shape, angle=0):
	if angle != 0:
		shape = Hex.transform(shape, 0, 0, angle)
	Hex.transformInsert(tile, "6mm", shape, [150, 250], 110, 0)
	Hex.transformInsert(tile, "6mm", Hex.flipY(shape), [150, 250], 50, 0)

def makeAlignerCircle(tile, pos, radius):
	circle = [[-radius, 0], ["arc", 0, radius], [radius, 0], ["arc", 0, -radius], [-radius, 0]]
	aligner = [Hex.polarPos(radius, -20), ["arc", radius, 0], Hex.polarPos(radius, 20)]
	Hex.transformInsert(tile, "6mm", circle, [150 + pos[0], 250 + pos[0]], 50 + pos[1], 0)
	Hex.transformInsert(tile, "6mm", aligner, [150 + pos[0], 250 + pos[0]], 110 - pos[1], [30, 150, -90], z = False)


if __name__ == "__main__":
	tileTFT = doubleBase(6)
	tileDCXL = doubleBase(2)

	doubleInsert(tileTFT, Asterisk.corner, angle=-60)
	doubleInsert(tileTFT, halfPart)
	doubleInsert(tileTFT, thirdPart)

	makeAlignerCircle(tileTFT, [-15, 0], 4.5)
	makeAlignerCircle(tileTFT, Hex.polarPos(15, -30), 3)
	
	doubleInsert(tileDCXL, centerPart)
	doubleInsert(tileDCXL, rightPart)
	doubleInsert(tileDCXL, Hex.flipY(rightPart), angle=180)
	
	makeAlignerCircle(tileDCXL, [0, -15], 4.5)
	makeAlignerCircle(tileDCXL, Hex.polarPos(20, -15), 3)
	makeAlignerCircle(tileDCXL, Hex.polarPos(20, -165), 3)

	
	Hex.saveXML(tileTFT, "Tiles/TileForTwo.svg")
	Hex.saveXML(tileDCXL, "Tiles/DCXL.svg")
