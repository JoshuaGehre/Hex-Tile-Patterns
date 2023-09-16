from xml.dom import minidom
import math
import numpy as np

TileHeight = 50
EdgeIndent = 2
TileEdge = TileHeight / math.sqrt(3)
TrackWidth = 11

PathCounter = 0
PathStr = ""
if True:
	s = "abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	for i in range(8):
		PathStr += s[int(len(s) * np.random.random())]

def style(col="000000"):
	return "fill:none;stroke:#" + col + ";stroke-width:0.264583px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"

def loadTemplate(clear=False):
	template = minidom.parse("TemplateClear.svg" if clear else "Template.svg")
	res = {
		"xml" : template,
	}
	for n in ["3mm", "10mm"]:
		res[n] = findLayer(template, n)
	return res

def loadCutTemplate(large=False):
	template = minidom.parse("CutTemplateLarge.svg" if large else "CutTemplate.svg")
	res = {
		"xml" : template,
	}
	for n in ["early", "mid", "late"]:
		res[n] = findLayer(template, n)
	return res

def findLayer(xml, layerName):
	for l in xml.getElementsByTagName("g"):
		if l.attributes.get("inkscape:label").value == layerName:
			return l
	print("Layer " + layerName + " not found!")
	return None

def saveXML(obj, fileName):
	with open(fileName, "w") as f:
		obj["xml"].writexml(f)

def polarPos(radius, angle):
	angle *= math.pi / 180
	return [radius * math.cos(angle), -radius * math.sin(angle)]

def basePlate():
	return [polarPos(TileEdge, i * 60) for i in range(7)]

def dist(a, b):
	return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def add(a, b):
	return [a[0] + b[0], a[1] + b[1]]

def relativeToCenter(a, b, x, y):
	n = [b[0] - a[0], b[1] - a[1]]
	nrm = 1.0 / math.sqrt(n[0] ** 2 + n[1] ** 2)
	n[0] *= nrm
	n[1] *= nrm
	t = [-n[1], n[0]]
	return [(b[0] + a[0]) * 0.5 + x * n[0] + y * t[0], (b[1] + a[1]) * 0.5 + x * n[1] + y * t[1]]

def indexedPlate(indents = 1):
	if indents == 1:
		indents = "x-----"
	elif indents == 2:
		indents = "x--x--"
	elif indents == 3:
		indents = "x-x-x-"
	elif indents == 6:
		indents = "xxxxxx"

	r = (TileHeight - EdgeIndent * 2) / math.sqrt(3)
	p = [polarPos(r, -120)]

	for i in range(6):
		a = p[len(p) - 1]
		b = polarPos(r, (i - 1) * 60)
		if indents[i] == "x":
			p.append(relativeToCenter(a, b, -6.35, 0))
			p.append(relativeToCenter(a, b, -6.35, -5))
			p.append(relativeToCenter(a, b, +6.35, -5))
			p.append(relativeToCenter(a, b, +6.35, 0))
		p.append(b)
	return p

def transform(path, dx, dy, angle):
	res = []
	for i in range(len(path)):
		x = 0
		y = 0
		if(len(path[i]) == 2):
			x = path[i][0]
			y = path[i][1]
		else:
			x = path[i][1]
			y = path[i][2]
		sa = math.sin(angle * math.pi / 180)
		ca = math.cos(angle * math.pi / 180)
		xt = ca * x + sa * y + dx
		yt = -sa * x + ca * y + dy
		if(len(path[i]) == 2):
			res.append([xt, yt])
		else:
			res.append([path[i][0], xt, yt])
	return res

def piRange(a):
	if a > math.pi:
		return a - 2 * math.pi
	if a < -math.pi:
		return a + 2 * math.pi
	return a

accumulatedLength = 0
def resetLength():
	global accumulatedLength
	accumulatedLength = 0

def getLength():
	global accumulatedLength
	return accumulatedLength

def arcPath(x1, y1, x2, y2, x3, y3):
	global accumulatedLength
	d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
	#print(d)
	#print((x1, y1, x2, y2, x3, y3))
	xc = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / d
	yc = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / d
	r = math.sqrt((x3 - xc) ** 2 + (y3 - yc) ** 2)
	a1 = math.atan2(y1 - yc, x1 - xc)
	a2 = math.atan2(y2 - yc, x2 - xc)
	a3 = math.atan2(y3 - yc, x3 - xc)
	#print([a1, a2, a3])
	a2 = piRange(a2 - a1)
	a3 = piRange(a3 - a1)
	#print([a2, a3])
	if a3 * a2 < 0:
		if a3 < 0:
			a3 += 2 * math.pi
		else:
			a3 -= 2 * math.pi
	arcFlag = 1 if abs(a2) > abs(a3) else 0
	arcLength = r * (2 * math.pi - abs(a3) if abs(a2) > abs(a3) else abs(a3))
	#print("Arc: " + str(arcLength))
	accumulatedLength += arcLength
	sweepFlag = 1 if a2 > 0 else 0
	#print("R: " + str(r) + " " + str(arcFlag) + " " + str(sweepFlag))
	return "A " + str(r) + "," + str(r) + " 0 " + str(arcFlag) + " " + str(sweepFlag) + " " + str(x3) + "," + str(y3)

def addAsPathToLayer(path, xml, layer, z = True):
	global PathCounter, accumulatedLength
	name = "genPath_" + str(PathCounter) + "_" + PathStr
	PathCounter += 1
	newPath = xml["xml"].createElement("path")
	newPath.setAttribute("style", style())
	newPath.setAttribute("id", name)
	d = "M " + str(path[0][0]) + "," + str(path[0][1]) + " "
	skip = 0
	for i in range(1, len(path)):
		l = path[i]
		if len(l) == 2 and skip <= 0:
			d += "L " + str(l[0]) + "," + str(l[1]) + " "
			accumulatedLength += dist(path[i - 1], l)	
		elif len(l) == 2:
			skip -= 1
		elif len(l) == 3:
			if l[0] == "arc":
				d += arcPath(path[i - 1][0], path[i - 1][1], l[1], l[2], path[i + 1][0], path[i + 1][1]) + " "
				skip = 1
	if z:
		accumulatedLength += dist(path[0], path[len(path) - 1])
		d += "z"
	newPath.setAttribute("d", d)
	newPath.setAttribute("sodipodi:nodetypes", "ccccc")
	xml[layer].appendChild(newPath)
	return

def transformInsert(xml, layer, path, dx, dy, angle=0):
	if type(dx) == list:
		for _dx in dx:
			transformInsert(xml, layer, path, _dx, dy, angle)
		return
	if type(dy) == list:
		for _dy in dy:
			transformInsert(xml, layer, path, dx, _dy, angle)
		return
	if type(angle) == list:
		for _angle in angle:
			transformInsert(xml, layer, path, dx, dy, _angle)
		return
	addAsPathToLayer(transform(path, dx, dy, angle), xml, layer)

def circleIntersect(a, r1, b, r2):
	d = dist(a, b)
	#print(str(r1) + " " + str(r2) + " " + str(d))
	phi = math.acos((r1**2 + d**2 - r2**2) / (2 * d * r1))
	phi2 = math.atan2(b[1] - a[1], b[0] - a[0])
	phi = phi2 + phi
	return [a[0] + math.cos(phi) * r1, a[1] + math.sin(phi) * r1]

def flipY(path):
	res = []
	for i in path:
		if len(i) == 2:
			res.append([i[0], -i[1]])
		elif len(i) == 3:
			res.append([i[0], i[1], -i[2]])
	return res

def makeCircle(r, x = 0, y = 0):
	return [[x + r, y], ["arc", x, y + r], [x - r, y], ["arc", x, y - r], [x + r, y]]

def intersect(p1, a1, p2, a2):
	d1 = polarPos(1, a1)
	d2 = polarPos(1, a2)
	# p1 + l * d1 = p2 + m * d2
	# l * d1 + m * d2 = p2 - p1
	det = d1[0] * d2[1] - d1[1] * d2[0]
	l = ((p2[0] - p1[0]) * d2[1] - (p2[1] - p1[1]) * d2[0]) / det
	return [p1[0] + l * d1[0], p1[1] + l * d1[1]]

def circleLineIntersect(p1, a1, p2, r, low=False):
	b = polarPos(1, a1)
	d = [p1[0] - p2[0], p1[1] - p2[1]]
	p = -(b[0] * d[0] + b[1] * d[1])
	q = d[0]**2 + d[1]**2 - r**2
	l = p + math.sqrt(p**2 - q) * (-1 if low else 1)
	return add(p1, polarPos(l, a1))

def makeRoundCorner(p, a1, a2, r):
	phi = abs(a1 - a2) * 0.5
	d = r / math.sin(phi / 180 * math.pi)
	s = d * math.cos(phi / 180 * math.pi)
	return [add(p, polarPos(s, a1)), ["arc"] + add(p, polarPos(d - r, (a1 + a2) * 0.5)), add(p, polarPos(s, a2))]
