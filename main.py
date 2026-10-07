import os
import time

RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
BLUE = '\u001b[44m'
RESET = '\u001b[0m'


# Task 1: Netherlands flag
def drawFlag():
    stripeHeight = 3
    flagWidth = 30
    for row in range(stripeHeight * 3):
        if row < stripeHeight:
            print(f"{RED}{' ' * flagWidth}{RESET}")
        elif row < stripeHeight * 2:
            print(f"{WHITE}{' ' * flagWidth}{RESET}")
        elif row < stripeHeight * 3:
            print(f"{BLUE}{' ' * flagWidth}{RESET}")


# Task 2: Pattern C
def drawPattern():
    tileSize = 5
    tilesAcross = 8
    tilesDown = 8

    for r in range(tilesDown * tileSize):
        line = ""
        for c in range(tilesAcross * tileSize):
            rowInTile = r % tileSize
            colInTile = c % tileSize
            isBlack = False
            if colInTile == rowInTile or colInTile == tileSize - 1 - rowInTile:
                isBlack = True
            if isBlack:
                line += f"{BLACK}  {RESET}"
            else:
                line += "  "
        print(line)


# Task 3: Animation
def drawAnimation():
    if os.name == 'nt':
        clearCmd = 'cls'
    else:
        clearCmd = 'clear'

    frames = 4
    totalRows = 40

    print("Starting Animation...")
    time.sleep(1)
    os.system(clearCmd)

    try:
        while True:
            for frame in range(frames):
                tileSize = 5
                tilesAcross = 8
                tilesDown = 8
                offset = frame

                for r in range(tilesDown * tileSize):
                    line = ""
                    for c in range(tilesAcross * tileSize):
                        shiftedC = c + offset
                        rowInTile = r % tileSize
                        colInTile = shiftedC % tileSize

                        isBlack = False
                        if colInTile == rowInTile or colInTile == tileSize - 1 - rowInTile:
                            isBlack = True

                        if isBlack:
                            line += f"{BLACK}  {RESET}"
                        else:
                            line += "  "
                    print(line)

                print(f'\x1b[{totalRows}A', end='')
                time.sleep(0.3)
    except KeyboardInterrupt:
        pass


# Task 4: Diagram
def drawDiagram():
    print("\nTask 4: Diagram")
    print("(odd positions = blue, even positions = red)\n")

    sequenceFile = open('sequence.txt', 'r')

    oddSum = 0.0
    evenSum = 0.0
    position = 0

    for line in sequenceFile:
        line = line.strip()
        number = float(line)

        position += 1
        if position % 2 == 0:
            evenSum += abs(number)
        else:
            oddSum += abs(number)

    sequenceFile.close()

    total = oddSum + evenSum
    oddPercent = (oddSum / total) * 100
    evenPercent = (evenSum / total) * 100

    print(f"Sum of absolute values on ODD positions: {oddSum:.2f}  ({oddPercent:.1f}%)")
    print(f"Sum of absolute values on EVEN positions:   {evenSum:.2f}  ({evenPercent:.1f}%)\n")

    barWidthBlocks = 25

    oddBlocks = round((oddPercent / 100) * barWidthBlocks)
    evenBlocks = barWidthBlocks - oddBlocks

    bar = f"{BLUE}{'  ' * oddBlocks}{RESET}{RED}{'  ' * evenBlocks}{RESET}"
    print(bar)

    oddLabel = f"{oddPercent:.1f}%"
    evenLabel = f"{evenPercent:.1f}%"

    oddPad = " " * max(0, (oddBlocks * 2 - len(oddLabel)) // 2)
    evenPad = " " * max(0, (evenBlocks * 2 - len(evenLabel)) // 2)

    print(f"{oddPad}{oddLabel}{evenPad}{evenLabel}")


# Task 5: Graph (y=2x)
def drawGraph():
    rows = 9
    cols = 9
    output = ""

    for r in range(rows):
        line = ""
        for c in range(cols):
            x = c
            y = rows - 1 - r

            isAxis = (c == 0 or r == rows - 1)
            isLine = (y == 2 * x) and (y < rows) and (x < cols)

            if isLine:
                line += f"{RED}  {RESET}"
            elif isAxis:
                line += f"{WHITE}  {RESET}"
            else:
                line += f"{BLUE}  {RESET}"
        output += line + "\n"

    print(output, end="")


print("Task 1: Netherlands Flag")
drawFlag()

input("\nPress Enter to launch Task 2 (Pattern C)...")
print("\nTask 2: Pattern C")
drawPattern()

input("\nPress Enter to launch Task 4 (Diagram)...")
drawDiagram()

input("\nPress Enter to launch Task 5 (Graph)")
drawGraph()

input("\nPress Enter to launch Task 3 (Animation)...")
drawAnimation() 