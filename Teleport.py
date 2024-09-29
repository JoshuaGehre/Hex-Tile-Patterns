import Hex
import Deco
import Text
import math

plate = Hex.basePlate()
iPlate = Hex.indexedPlate(1)

star1 = Deco.makeStar()
star2 = ["group", Deco.makeStar(8), Deco.makeStar(4)]

text = {}

for t in ["Combo"]:
	text[t] = Hex.scale(Text.getText(t), 6)

ar = Hex.relativeToCenter(plate[4], plate[5], +0.5 * Hex.TrackWidth, 0)
br = Hex.relativeToCenter(plate[4], plate[5], +0.7 * Hex.TrackWidth, 0)
cr = Hex.relativeToCenter(plate[5], plate[0], -0.7 * Hex.TrackWidth, 0)

dr = Hex.relativeToCenter(plate[0], plate[1], -0.8 * Hex.TrackWidth, 0)
dl = Hex.relativeToCenter(plate[2], plate[3], +0.8 * Hex.TrackWidth, 0)

er = Hex.relativeToCenter(plate[0], plate[1], -0.7 * Hex.TrackWidth, 0)
el = Hex.relativeToCenter(plate[2], plate[3], +0.7 * Hex.TrackWidth, 0)

catchCenter = [0, -20]
catchRad = Hex.dist(catchCenter, plate[0])

teleCatch = [plate[3],
	["arc"] + Hex.add(catchCenter, [0, catchRad]),
	plate[0]] + Deco.makeArcRipple(dr, dl, catchCenter, flip=True)

teleSmallCorner = [cr, ["arc"] + Hex.add(plate[5], Hex.polarPos(Hex.dist(plate[5], cr), 120)), br, plate[5]]
teleLargeCorner = [ar, br, teleSmallCorner[1], cr, plate[0], ["arc"] + Hex.add(catchCenter, Hex.polarPos(catchRad, -70)), Hex.circleLineIntersect(ar, -90, catchCenter, catchRad)]

center = [4, -8]
radius1 = 2
radius2 = radius1 + Hex.TrackWidth

rampStart = Hex.add(center, [-15, -radius1])

rDist = er[1] - center[1]

teleTop = [el,
	Hex.add(center, [0, radius1]),
	["arc"] + Hex.add(center, Hex.polarPos(radius1, -45)),
	Hex.add(center, [radius1, 0]),
	["arc"] + Hex.add(center, Hex.polarPos(radius1, 45)),
	Hex.add(center, [0, -radius1]),
	rampStart,
	Hex.add(rampStart, [0, -2.5]),
	["arc"] + Hex.add(rampStart, [-0.15 * Hex.TrackWidth, -0.5 * Hex.TrackWidth]),
	Hex.add(rampStart, [0, -Hex.TrackWidth + 2.5]),
	Hex.add(rampStart, [0, -Hex.TrackWidth]),
	Hex.add(center, [0, -radius2]),
	["arc"] + Hex.add(center, Hex.polarPos(radius2, 45)),
	Hex.add(center, [radius2, 0]),
	["arc"] + Hex.add(Hex.add(center, [radius2 + rDist, 0]), Hex.polarPos(rDist, -135)),
	[center[0] + radius2 + rDist, er[1]],
	er, plate[1], plate[2]]

teleWedge = [[0, 0], [0, -7], [15, 0]]

arrow = [[-5, -2], [5, -2], [5, -4], [10, 0], [5, 4], [5, 2], [-5, 2]]

ph = 4
pr1 = 4
pAng = 70
pAngL = 50
portals = [[
	Hex.add([0, -ph], Hex.polarPos(pr1, pAngL + 90)),
	["arc", 0, -ph - pr1],
	Hex.add([0, -ph], Hex.polarPos(pr1, 90 - pAng)),
	["arc", pr1 + ph / math.cos(pAng / 180 * math.pi) - ph * math.tan(pAng / 180 * math.pi), 0],
	Hex.add([0, +ph], Hex.polarPos(pr1, -90 + pAng)),
	["arc", 0, ph + pr1],
	Hex.add([0, +ph], Hex.polarPos(pr1, -pAngL - 90)),
	],[
	Hex.add([0, -ph], Hex.polarPos(pr1, pAngL + 90)),
	Hex.add([0, -ph], Hex.polarPos(pr1, 90)),
	[pr1 + ph / math.cos(pAng / 180 * math.pi) - ph * math.tan(pAng / 180 * math.pi), 0],
	Hex.add([0, +ph], Hex.polarPos(pr1, -90)),
	Hex.add([0, +ph], Hex.polarPos(pr1, -pAngL - 90)),
	],False]
portals[2] = [
	portals[1][0],
	[portals[1][0][0], portals[1][1][1]],
	[portals[1][2][0], portals[1][1][1]],
	[portals[1][2][0], portals[1][3][1]],
	[portals[1][4][0], portals[1][3][1]],
	portals[1][4],
	]

teleInDeco = [["group",
	Hex.transform(arrow, -6, -1, 0),
	Hex.transform(portal, 6, -1, 0),
	] for portal in portals]

teleOutDeco = [["group",
	Hex.transform(arrow, 1, 3.5, 0),
	Hex.transform(portal, -5, 3.5, 180),
	] for portal in portals]

moonCenter = Hex.polarPos(0.2, 135)
moonRadius = 0.45

portalIcons = [
	# X
	[],
	# Point
	[[0.3, 0], ["arc", 0, 0.3], [-0.3, 0], ["arc", 0, -0.3], [0.3, 0]],
	# Moon
	[
		Hex.circleIntersect([0, 0], 0.5, moonCenter, moonRadius),
		["arc"] + Hex.add(moonCenter, Hex.polarPos(moonRadius, 0)),
		Hex.add(moonCenter, Hex.polarPos(moonRadius, -45)),
		["arc"] + Hex.add(moonCenter, Hex.polarPos(moonRadius, -90)),
		Hex.circleIntersect(moonCenter, moonRadius, [0, 0], 0.5),
		["arc"] + Hex.polarPos(0.5, -135),
		Hex.polarPos(0.5, -45),
		["arc"] + Hex.polarPos(0.5, 45),
		Hex.circleIntersect([0, 0], 0.5, moonCenter, moonRadius),
	],
	# Diagonal
	[[-0.5, -0.5], [-0.2, -0.5], [0.5, 0.5], [0.2, 0.5]],
	# Triangle
	[[-0.5, -0.5], [0.5, -0.5], [0, 0.5]],
	# Tilde
	[[0.5, -0.15], ["arc", 0.25, -0.05], [0, -0.15], ["arc", -0.25, -0.25], [-0.5, -0.15], [-0.5, 0.15], ["arc", -0.25, 0.05], [0, 0.15], ["arc", 0.25, 0.25], [0.5, 0.15]],
]

xPart = [[0.15, 0],[0.5, 0.35],[0.35, 0.5]]
for i in range(4):
	portalIcons[0] += Hex.transform(xPart, 0, 0, -90* i)

if __name__ == "__main__":
	print("Writing Teleport Tile")
	tile = Hex.loadTemplate()
	Hex.transformInsert(tile, "3mm", plate, [50, 250], [50, 110])
	Hex.transformInsert(tile, "3mm", iPlate, 50, [170, 230])
	Hex.transformInsert(tile, "3mm", iPlate, 250, [50, 110])
	
	Hex.transformInsert(tile, "3mm", star2, 50, [160, 220])
	Hex.transformInsert(tile, "3mm", text["Combo"], 50, [175, 235])

	Hex.transformInsert(tile, "10mm", teleCatch, [250, 150], 50)
	Hex.transformInsert(tile, "10mm", teleSmallCorner, [250, 150], 50)
	Hex.transformInsert(tile, "10mm", Hex.flipY(teleSmallCorner), [250, 150], 50, 180)
	
	Hex.transformInsert(tile, "10mm", teleLargeCorner, [250, 150], 110)
	Hex.transformInsert(tile, "10mm", Hex.flipY(teleLargeCorner), [250, 150], 110, 180)
	
	Hex.transformInsert(tile, "10mm", teleTop, [250, 150], 110)
	
	decoVariant = 0
	Hex.transformInsert(tile, "3mm", teleInDeco[decoVariant], [50, 250], 49, z = False)
	Hex.transformInsert(tile, "3mm", teleOutDeco[decoVariant], [50, 250], 110, z = False)

	Hex.transformInsert(tile, "3mm", teleWedge, 55, 270)
	Hex.transformInsert(tile, "3mm", Hex.flipY(teleWedge), 55, 273)
	
	Hex.transformInsert(tile, "3mm", star1, 257, 35)
	Hex.transformInsert(tile, "3mm", star1, 40, 270)

	#for i in range(len(portalIcons)):
	#	Hex.transformInsert(tile, "3mm", Hex.scale(portalIcons[i], 10), 100, 50 + 25 * i)
	
	#icon = Hex.scale(portalIcons[0], 10)
	#Hex.transformInsert(tile, "3mm", icon, [35, 235], 45)
	#Hex.transformInsert(tile, "3mm", icon, [65, 265], 112)

	Hex.saveXML(tile, "Tiles/Teleport.svg")
