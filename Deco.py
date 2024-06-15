import Hex
import math

rippleLength = 3
rippleIndent = 1.5

def makeStar(size = 5):
	return [Hex.polarPos(size * (1 if ((i % 2) == 0) else 0.5), i * 36 + 90) for i in range(10)]

def makeRipple(a, b, outwards = False):
	d = Hex.dist(a, b)
	n = int(d / rippleLength + 0.5)
	if n == 0:
		return [a, b]
	return [Hex.relativeToCenter(a, b, d * 0.5 * (i / n - 1), (1 if outwards else -1) * rippleIndent * (i % 2)) for i in range(n * 2)] + [b]

def makeArcRipple(a, b, center, flip=False, outwards=False):
	phiA = -math.atan2(a[1] - center[1], a[0] - center[0])
	phiB = -math.atan2(b[1] - center[1], b[0] - center[0])
	phiD = phiB - phiA
	#print(phiA)
	#print(phiB)
	if flip:
		if(phiD > 0):
			phiD -= 2 * math.pi
	else:	
		if(phiD < 0):
			phiD += 2 * math.pi
	r = Hex.dist(a, center)
	d = r * abs(phiD)
	n = int(d / rippleLength)
	if n == 0:
		return [a, b]
	phiA *= 180 / math.pi
	phiB *= 180 / math.pi
	phiD *= 180 / math.pi
	
	rippleDir = -1 if outwards else 1

	return [Hex.add(center, Hex.polarPos(r - (rippleDir * rippleIndent * (i % 2)), phiA + 0.5 * phiD * i / n)) for i in range(n * 2)] + [b]
