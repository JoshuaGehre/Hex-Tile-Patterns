import Hex
import Asterisk
import DIC
import Deco
import Text

plate = Hex.basePlate()
iPlate = Hex.indexedPlate(6)

secretR = Hex.TileHeight * 0.5 * 0.85

qR = 4.5

qA = 4
qB = 12
qC = 15
qEx1 = 2
qEx2 = 2
qEx3 = 1
qAng1 = 55
qAng2 = 55
qC2 = Hex.polarPos(qC, 180 - qAng1)

secretCircle = [[0, secretR], ["arc", secretR, 0], [0, -secretR], ["arc", -secretR, 0], [0, secretR]]
qCircle = [[0, qR], ["arc", qR, 0], [0, -qR], ["arc", -qR, 0], [0, qR]]

qTop1 = Hex.add(qC2, Hex.polarPos(qC - qA, 90 + qAng2))
qTop2 = Hex.add(qC2, Hex.polarPos(qC - qB, 90 + qAng2))

questionMark = [
	[-qB, qEx1],
	[-qA, qEx1],
	[-qA, 0],
	["arc"] + Hex.polarPos(qA, 180 - 0.5 * qAng1),
	Hex.polarPos(qA, 180 - qAng1),
	["arc"] + Hex.add(qC2, [qC - qA, 0]),
	Hex.add(qC2, Hex.polarPos(qC - qA, 45)),
	["arc"] + Hex.add(qC2, [0, -qC + qA]),
	qTop1,
	Hex.add(qTop1, Hex.polarPos(qEx2, 180 + qAng2)),
	Hex.add(qTop2, Hex.polarPos(qEx3, 180 + qAng2)),
	qTop2,
	["arc"] + Hex.add(qC2, [0, -qC + qB]),
	Hex.add(qC2, Hex.polarPos(qC - qB, 45)),
	["arc"] + Hex.add(qC2, [qC - qB, 0]),
	Hex.polarPos(qB, 180 - qAng1),
	["arc"] + Hex.polarPos(qB, 180 - 0.5 * qAng1),
	[-qB, 0],
	
]

sPlate = ["group", plate, secretCircle]

secretPinR = 2.5
secretPin = [
		[(Hex.TileEdge + Hex.TrackWidth) * 0.5, 0],
		["arc", (Hex.TileEdge + Hex.TrackWidth) * 0.5 + secretPinR, secretPinR],
		[(Hex.TileEdge + Hex.TrackWidth) * 0.5 + 2 * secretPinR, 0],
		["arc", (Hex.TileEdge + Hex.TrackWidth) * 0.5 + secretPinR, -secretPinR],
		[(Hex.TileEdge + Hex.TrackWidth) * 0.5, 0],
	]

rHolder = 0.5 * (Hex.TileEdge - Hex.TrackWidth)

secretHolder = [
		Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0),
		["arc"] + Hex.add(plate[0], Hex.polarPos(rHolder, 125)),
		Hex.add(plate[0], Hex.polarPos(rHolder, 140)),
		[(Hex.TileEdge + Hex.TrackWidth) * 0.5 + secretPinR, -secretPinR],
		["arc", (Hex.TileEdge + Hex.TrackWidth) * 0.5 + 2 * secretPinR, 0],
		[(Hex.TileEdge + Hex.TrackWidth) * 0.5 + secretPinR, secretPinR],
		Hex.add(plate[0], Hex.polarPos(rHolder, -140)),
		["arc"] + Hex.add(plate[0], Hex.polarPos(rHolder, -125)),
		Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0),
		plate[0]
	]

alignerPart = [
		[(Hex.TileEdge + Hex.TrackWidth) * 0.5 + secretPinR, secretPinR],
		["arc", (Hex.TileEdge + Hex.TrackWidth) * 0.5 + 2 * secretPinR, 0],
		[(Hex.TileEdge + Hex.TrackWidth) * 0.5 + secretPinR, -secretPinR],
	]

aligner = []
for i in range(6):
	aligner += Hex.transform(alignerPart, 0, 0, i * 60)

aligner = ["group", aligner, plate]

def secretBase():
	tile = Hex.loadTemplate()
	Hex.changeWidth(tile, "6mm")
	Hex.transformInsert(tile, "3mm", plate, [50, 250], 50)
	Hex.transformInsert(tile, "3mm", sPlate, 50, 170)
	Hex.transformInsert(tile, "3mm", qCircle, 50, 185)
	Hex.transformInsert(tile, "3mm", questionMark, 50 + 0.5 * (qA + qB), 175)
	Hex.transformInsert(tile, "3mm", plate, 50, 230)
	Hex.transformInsert(tile, "3mm", iPlate, 50, 110)
	Hex.transformInsert(tile, "3mm", iPlate, 250, 50)
	dirs = [-120, -60, 0, 60, 120, 180]
	Hex.transformInsert(tile, "6mm", secretPin, 150, 110, dirs)
	Hex.transformInsert(tile, "6mm", secretPin, 250, 50, dirs)
	Hex.transformInsert(tile, "6mm", secretHolder, 150, 170, dirs)
	Hex.transformInsert(tile, "6mm", secretHolder, 250, 50, dirs)
	return tile

a1 = Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, 0)
b1 = Hex.relativeToCenter(plate[0], plate[1], 0.5 * Hex.TrackWidth, 0)
c1 = Hex.relativeToCenter(plate[1], plate[2], -0.5 * Hex.TrackWidth, 0)
a2 = Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, 0)
b2 = Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, 0)
c2 = Hex.relativeToCenter(plate[4], plate[5], 0.5 * Hex.TrackWidth, 0)

secretBigCorner = Asterisk.bigCorner + [
		b2,
		Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, -0.6 * Hex.TrackWidth),
		["arc"] + Hex.relativeToCenter(plate[5], plate[0], 0, -1.1 * Hex.TrackWidth),
		Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -0.6 * Hex.TrackWidth),
		a2,
	]

triggerR = 10

triggerRipple = Deco.makeArcRipple(
	Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, -0.5 * Hex.TrackWidth),
	Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -0.5 * Hex.TrackWidth),
	Hex.relativeToCenter(plate[5], plate[0], 0, -0.5 * Hex.TrackWidth),
	outwards = False,
	flip = True)

"""
secretTriggerPart = [c2, plate[5], b2] + Deco.makeArcRipple(
			Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, -0.4 * Hex.TrackWidth),
			Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -0.4 * Hex.TrackWidth),
			Hex.relativeToCenter(plate[5], plate[0], 0, -0.4 * Hex.TrackWidth),
			outwards = True,
			flip = True
		) + [a2, plate[0], a1] + Deco.makeArcRipple(
			Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, -0.4 * Hex.TrackWidth),
			Hex.relativeToCenter(plate[0], plate[1], 0.5 * Hex.TrackWidth, -0.4 * Hex.TrackWidth),
			Hex.relativeToCenter(plate[0], plate[1], 0, -0.4 * Hex.TrackWidth),
			outwards = True,
			flip = True
		) + [b1, plate[1], c1,
		Hex.circleLineIntersect(c1, 90, [0, 0], triggerR),
		["arc", triggerR, 0],
		Hex.circleLineIntersect(c1, -90, [0, 0], triggerR),
	]
"""
secretTriggerPart = [c2, plate[5], b2,
		Hex.relativeToCenter(plate[5], plate[0], -0.5 * Hex.TrackWidth, -0.5 * Hex.TrackWidth),
		["arc"] + Hex.relativeToCenter(plate[5], plate[0], 0, -1.0 * Hex.TrackWidth),
		Hex.relativeToCenter(plate[5], plate[0], 0.5 * Hex.TrackWidth, -0.5 * Hex.TrackWidth),
		a2, plate[0], a1,
		Hex.relativeToCenter(plate[0], plate[1], -0.5 * Hex.TrackWidth, -0.5 * Hex.TrackWidth),
		["arc"] + Hex.relativeToCenter(plate[0], plate[1], 0, -1.0 * Hex.TrackWidth),
		Hex.relativeToCenter(plate[0], plate[1], 0.5 * Hex.TrackWidth, -0.5 * Hex.TrackWidth),
		b1, plate[1], c1,
		Hex.circleLineIntersect(c1, 90, [0, 0], triggerR),
		["arc", triggerR, 0],
		Hex.circleLineIntersect(c1, -90, [0, 0], triggerR),
	]

star = Deco.makeStar(9)
qMark = Hex.scale(Text.getText("?"), 6)

if __name__ == "__main__":
	tileX = secretBase()
	tileTrigger = secretBase()
	tileDIC = secretBase()
	tileXC = secretBase()
	
	Hex.transformInsert(tileX, "6mm", Asterisk.corner, [150, 250], 50, [60, 240])
	Hex.transformInsert(tileX, "6mm", secretBigCorner, [150, 250], 50, [0, 180])

	#Hex.transformInsert(tileX, "3mm", aligner, 150, 230, 0)

	Hex.transformInsert(tileTrigger, "6mm", secretTriggerPart, [150, 250], 50, [0, 180])
	Hex.transformInsert(tileTrigger, "3mm", star, [50, 250], 50)
	Hex.transformInsert(tileTrigger, "3mm", qMark, [50, 250], 50)
	Hex.transformInsert(tileTrigger, "3mm", triggerRipple, [50, 250], 50, [0, 60, 180, 240], z=False)
	
	Hex.transformInsert(tileDIC, "6mm", DIC.roundCorner, [150, 250], 50, [0, 180])
	Hex.transformInsert(tileDIC, "6mm", DIC.partIC, [150, 250], 50, [0, 180])
	
	Hex.transformInsert(tileXC, "6mm", DIC.roundCorner, [150, 250], 50, 0)
	Hex.transformInsert(tileXC, "6mm", DIC.xcCenter, [150, 250], 50, 0)
	Hex.transformInsert(tileXC, "6mm", DIC.xcSmallCorner, [150, 250], 50, 0)
	Hex.transformInsert(tileXC, "6mm", DIC.xcLargeCorner, [150, 250], 50, -120)
	Hex.transformInsert(tileXC, "6mm", DIC.xcLargeCorner2, [150, 250], 50, 120)

	Hex.saveXML(tileX, "Tiles/SecretX.svg")
	Hex.saveXML(tileTrigger, "Tiles/SecretTrigger.svg")
	Hex.saveXML(tileDIC, "Tiles/SecretDIC.svg")
	Hex.saveXML(tileXC, "Tiles/SecretXC.svg")
