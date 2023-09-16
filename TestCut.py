import math
import Hex
import DIC
import Flipper
import TwoTrap

cut3mm = Hex.loadCutTemplate()
cut10mm = Hex.loadCutTemplate()

Hex.resetLength()
Hex.transformInsert(cut10mm, "mid", DIC.roundCorner, 15, 30, 0)
Hex.transformInsert(cut10mm, "mid", DIC.roundCorner, 38, 30, 180)
Hex.transformInsert(cut10mm, "mid", DIC.partIC, 22, 30, 0)
Hex.transformInsert(cut10mm, "mid", DIC.partIC, 30, 30, 180)

Hex.transformInsert(cut10mm, "mid", TwoTrap.smallCorner, 100, 30, 150)
Hex.transformInsert(cut10mm, "mid", TwoTrap.largeCorner, 48, 30, 150)

Hex.transformInsert(cut10mm, "mid", Flipper.largeCorner, 90, 28, 60)
Hex.transformInsert(cut10mm, "mid", Flipper.largeCorner, 90, 32, -120)
Hex.transformInsert(cut10mm, "mid", Flipper.largeCornerIndent, 105, 30, -30)

Hex.transformInsert(cut10mm, "mid", Flipper.flipper, 100, 30, 30)
Hex.transformInsert(cut10mm, "early", Flipper.flipperCircle, 100, 30, 0)

length10mm = Hex.getLength()
Hex.resetLength()

Hex.transformInsert(cut3mm, "mid", DIC.plate, [i * 53 + 30 for i in range(3)], 32, 30)
Hex.transformInsert(cut3mm, "early", Flipper.flipperCircleBase, 30, 32, 0)

offset = Hex.polarPos(Hex.TileHeight + 3, -60)
Hex.transformInsert(cut3mm, "mid", Flipper.iPlate, 30 + offset[0], 30 + offset[1], -30)
Hex.transformInsert(cut3mm, "mid", TwoTrap.iPlate, 53 + 30 + offset[0], 30 + offset[1], -30)
Hex.transformInsert(cut3mm, "mid", DIC.i2Plate, 53 * 2 + 30 + offset[0], 30 + offset[1], -30)

length3mm = Hex.getLength()

Hex.saveXML(cut3mm, "Cut/Test3mm.svg")
Hex.saveXML(cut10mm, "Cut/Test10mm.svg")

print("10mm Length: " + str(length10mm))
print("3mm Length: " + str(length3mm))
