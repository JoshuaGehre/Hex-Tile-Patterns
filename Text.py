import Hex
import math

# ?OPENMÖFICH

# COÖ?

CAng = 45
CR1 = 0.3
CR2 = 0.6
c1 = Hex.polarPos(CR2 - CR1, CAng)
c2 = [c1[0], 0]
c1 = [0, c1[1]]
c3 = [0, -c1[1]]
cOffset = CR2 - c2[0]
c1[0] += cOffset
c2[0] += cOffset
c3[0] += cOffset

OPath = [
	Hex.add(c1, [0, -CR1]),
	["arc"] + Hex.add(c1, Hex.polarPos(CR1, 90 + CAng * 0.5)),
	Hex.add(c1, Hex.polarPos(CR1, 180 - CAng)),
	["arc"] + Hex.add(c2, [-CR2, 0]),
	Hex.add(c3, Hex.polarPos(CR1, -90 - CAng * 0.5)),
	["arc"] + Hex.add(c3, Hex.polarPos(CR1, 180 + CAng)),
	Hex.add(c3, [0, CR1]),
]

qRad2 = 0.55

letters = {
	" " : {
		"width": 0.2,
		"paths": ["group"]
	},
	"C" : {
		"width": 0.6,
		"paths": [
			Hex.add(c1, Hex.polarPos(CR1, CAng)),
			["arc"] + Hex.add(c1, [0, -CR1]),
			Hex.add(c1, Hex.polarPos(CR1, 180 - CAng)),
			["arc"] + Hex.add(c2, [-CR2, 0]),
			Hex.add(c3, Hex.polarPos(CR1, 180 + CAng)),
			["arc"] + Hex.add(c3, [0, CR1]),
			Hex.add(c3, Hex.polarPos(CR1, -CAng)),
			]
	},
	"E" : {
		"width": 0.6,
		"paths": ["group", [[0, 0], [0.4, 0]], [[0.6, -0.5], [0, -0.5], [0, 0.5], [0.6, 0.5]]]
	},
	"F" : {
		"width": 0.6,
		"paths": ["group", [[0, 0], [0.4, 0]], [[0.6, -0.5], [0, -0.5], [0, 0.5]]]
	},
	"H" : {
		"width": 0.6,
		"paths": ["group", [[0, -0.5], [0, 0], [0.6, 0], [0.6, -0.5]], [[0, 0.5], [0, 0]], [[0.6, 0.5], [0.6, 0]]]
	},
	"I" : {
		"width": 0.1,
		"paths": [[0.05, -0.5], [0.05, 0.5]]
	},
	"M" : {
		"width": 0.8,
		"paths": [[0, 0.5], [0, -0.5], [0.4, 0], [0.8, -0.5], [0.8, 0.5]]
	},
	"N" : {
		"width": 0.6,
		"paths": [[0, 0.5], [0, -0.5], [0.6, 0.5], [0.6, -0.5]]
	},
	"O" : {
		"width": 1,
		"paths": ["group", OPath, Hex.transform(OPath, 1, 0, 180)]
	},
	"Ö" : {
		"width": 1,
		"paths": ["group", OPath, Hex.transform(OPath, 1, 0, 180), [[0.2, -0.65], [0.25, -0.8]], [[0.8, -0.65], [0.85, -0.8]]]
	},
	"P" : {
		"width": 0.4,
		"paths": [[0, 0.5], [0, 0], [0.15, 0], ["arc", 0.4, -0.25], [0.15, -0.5], [0, -0.5], [0, -0.35]]
	},
	"?" : {
		"width": 0.5,
		"paths": ["group", [
			[0, -0.25], ["arc", 0.25, -0.5], [0.5, -0.25],
			["arc"] + Hex.add([0.25, -0.25], Hex.polarPos(0.25, -20)),
			Hex.add([0.25, -0.25], Hex.polarPos(0.25, -45)),
			["arc"] + Hex.add(Hex.add([0.25, -0.25], Hex.polarPos(0.25 + qRad2, -45)), Hex.polarPos(qRad2, 170)),
			Hex.add([0.25 - qRad2, -0.25], Hex.polarPos(0.25 + qRad2, -45)),
			], [[0.25, 0.53], [0.3, 0.48]]]
	},
}

#print(letters["O"]["paths"])

def getText(txt):
	width = 0
	paths = ["group-z"]
	for c in txt:
		cu = c.upper()
		scale = 1 if c == cu else 0.9
		if cu in letters:
			p = Hex.transform(letters[cu]["paths"], width, 0 if c == cu else 0.1, 0)
			if scale != 1:
				p = Hex.scale(p, scale)
			width += letters[cu]["width"] * scale + 0.4
			paths.append(p)
			print(width)
	width -= 0.4
	#print(width)
	paths = Hex.transform(paths, -0.5*width, 0, 0)
	return paths
