# Hex Tile Patterns

This is a collection of cutting patterns for laser cutting parts for wooden Hextraction tiles.
[Hextraction](https://www.playhextraction.com/) is an Open Source Board game by Zack Freedman usually intended to be 3D printed.

This project consist of python scripts which generate .svg files with the patterns needed for various tiles.
I mainly made these patterns for making some laser cut wooden Hextraction tiles, as opposed to 3D printing them.
As a result of that this, some of these scripts can be a bit chaotic.
So if you want to laser cut some of tiles too or otherwise mess around with this, here you go.

![The small board with some tiles](./Images/Tiles.png)

## What do I need to cut out

Files in Tiles/ are not intended to be cut directly those mainly serve as a preview and indicate what parts are needed and which thickness they need, while also serving as a hint for how those are put together.
For actually cutting them, those parts should be assembled into their seperate files.
The cutting patterns I had used were generated with TestBoard.py and TestCut.py.
However, what parts you need will depend on what tiles you want to get cut, so you will likely have to assembe your own and convert it to whatever format you need afterwards.

## Assembly

Since tiles can't be made in one piece, their seperate parts still need to be glued together with wood glue.
Tiles consist of one 50mm high and 3mm thick hexagonal plate ontop of which the 10mm thick parts for the tiles are glued.
From my experience it's easier to glue those one before glueing on the 3mm thick slightly smaller bottom plate with one to six indexing notches.
The Flipper tiles will need a screw and washers.
And for the Pachinko you can glue in some (1mm diameter) metal pins.

## Tiles

Current list of tiles that are included in this repository.

| Tile | Implemented In | Notes |
|:-----|:---------------|:------|
| Asterisk | Asterisk.py | |
| X | Asterisk.py | |
| Peace | Asterisk.py | |
| S | Asterisk.py | |
| Z | Asterisk.py | |
| 3Trap | Asterisk.py | More consistent at lower board angles |
| DIC | DIC.py | |
| DC | DIC.py | |
| XC | DIC.py | |
| Pisces | DIC.py | |
| 2Trap | TwoTrap.py | Very inconsistent, needs some rework |
| Flipper3 | Flipper.py | |
| Flipper6 | Flipper.py | |
| Pachinko | Flipper.py | |
| Newton | Newton.py | |
| QuadTrap | QuadTrap.py | Alternate Name: DC Trap |
| Xefros | Misc.py | Weird Tracks, kinda chaotic and unreliable |
| RHSBT | Specials.py | |
| Bomb | Specials.py | |
| Recursion | Specials.py | Trigger: Teleport balls in and out of the small board |
| Secret X | Secret.py | Secret tiles are a huge pain to assemble |
| Secret DIC | Secret.py | |
| Secret XC | Secret.py | |
| Secret Trigger | Secret.py | Keep track of when an opponent sets this off, tell them they have activated your secret trigger tile + reveal the tile, then swap whatever tiles tiles with tiles on their hand as you'd like. This system probably needs a lot more pedantic rules and would likely qualify as a forbidden effect within the Hextraction rules. I still wanted to have something like this in my tiles though. |
| TileForTwo | TileForTwo.py | File in some gaps to fit a string through. |
| DCXL | TileForTwo.py | Alternate Name: 640 |
| Clone | Specials.py | Trigger: Roll another ball down the ramp |
| King | Specials.py | Trigger: Move the tile (with the ball) to a neighbouring tile (if possible), while rotating it by 180 degree |
| Teleport | Teleport.py | On Play: Split the tile apart and place both. Limit: The Out Tile must be placed higher than the In Tile. Trigger: Move the ball from the In Tile to the matching Out Tile |
| Open Flipper | Flipper.py | |
| Down Right Flipper | Flipper.py | |
| Metastable | Flipper.py | Gets stuck for the top left to bottom right orientation, needs some rework |
| Linear Trap | LinearTrap.py | |
