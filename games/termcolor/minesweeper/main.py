import random, time
from termcolor import colored, cprint

#Introduction
print()
cprint('Welcome to MineSweeper v.3.0!', 'red')
cprint('=============================', 'red')
print()
print('Excited to declare version 3.0 of MineSweeper as almost fully functional!')




#Sets up the game.
def reset():
    print('''
MAIN MENU
=========

-> For instructions on how to play, type 'I'
-> To play immediately, type 'P'
''')

    choice = input('Type here: ').upper()

    if choice == 'I':
        #Prints instructions.
        print(open('instructions.txt', 'r').read())

        input('Press [enter] when ready to play. ')

    elif choice != 'P':
        reset()

    #Generates bomb locations and updates the numbers around them.
    b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for n in range (0, 10):
        generateLocation(b)

    for r in range (0, 9):
        for c in range (0, 9):
            value = l(r, c, b)
            if value == '*':
                updateValues(r, c, b)

    #Sets the variable k to a grid of questionmarks, because nothing is yet known about the grid.
    k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    printBoard(k)

    #Start timer
    startTime = time.time()

    #The game begins!
    play(b, k, startTime)

#Gets the value of a coordinate on the grid.
def l(r, c, b):
    r = b[r]
    c = r[c]
    return c

#Checks if there's a bomb in the randomly generated location. If not, it puts one there. If there is, it requests a new location to try.
def checkBomb(r, c, b):
    currentRow = b[r]
    if not currentRow[c] == '*':
        currentRow[c] = '*'
    else:
        generateLocation(b)

#Generates a random location to place a bomb.
def generateLocation(b):
    r = random.randint(0, 8)
    c = random.randint(0, 8)
    checkBomb(r, c, b)

#Adds 1 to all of the squares around a bomb.
def updateValues(rn, c, b):

    #Row above.
    if 9 > (rn-1) > -1:
        r = b[rn-1]

        if 9 > (c-1) > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > (c+1) > -1:
            if not r[c+1] == '*':
                r[c+1] += 1

    #Same row.
    r = b[rn]

    if 9 > (c-1) > -1:
        if not r[c-1] == '*':
            r[c-1] += 1

    if 9 > (c+1) > -1:
        if not r[c+1] == '*':
            r[c+1] += 1

    #Row below.
    if 9 > (rn+1) > -1:
        r = b[rn+1]

        if 9 > (c-1) > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > (c+1) > -1:
            if not r[c+1] == '*':
                r[c+1] += 1

#When a zero is found, all the squares around it are opened.
def zeroProcedure(r, c, k, b):

    kBefore = k

    #Row above
    if 9 > (r-1) > -1:
        row = k[r-1]

        if 9 > (c-1) > -1:
            v = l(r-1, c-1, b)
            row[c-1] = v

        v = l(r-1, c, b)
        row[c] = v

        if 9 > (c+1) > -1 :
            v = l(r-1, c+1, b)
            row[c+1] = v

    #Same row
    row = k[r]

    if 9 > (c-1) > -1:
        v = l(r, c-1, b)
        row[c-1] = v

    if 9 > (c+1) > -1:
        v = l(r, c+1, b)
        row[c+1] = v

    #Row below
    if 9 > (r+1) > -1:
        row = k[r+1]

        if 9 > (c-1) > -1:
            v = l(r+1, c-1, b)
            row[c-1] = v

        v = l(r+1, c, b)
        row[c] = v

        if 9 > (c+1) > -1:
            v = l(r+1, c+1, b)
            row[c+1] = v

    if k == kBefore:
        return True

#Checks known grid for 0s.
def checkZeros(k, b):
    for n in range (80):
        for r in range (0, 8):
            for c in range (0, 8):
                if l(r, c, k) == 0:
                    zeroProcedure(r, c, k, b)



#Places a marker in the given location.
def marker(r, c, k):
    row = k[r]
    row[c] = '⚐'
    printBoard(k)

#Prints the board. Depending on input, prints either the known board or the full board.
def printBoard(b):
    for n in range (0, 40):
        print()
    print('    A   B   C   D   E   F   G   H   I')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
    for r in range (0, 9):
        print(r,'║',l(r,0,b),'║',l(r,1,b),'║',l(r,2,b),'║',l(r,3,b),'║',l(r,4,b),'║',l(r,5,b),'║',l(r,6,b),'║',l(r,7,b),'║',l(r,8,b),'║')
        if not r == 8:
            print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')

#The player chooses a location.
def choose(b, k):
    #Variables 'n stuff.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    #Loop in case of invalid entry.
    while True:
        chosen = input('Choose a square (eg. E4) or place a marker (eg. mE4): ')
        chosen = chosen.lower()
        #Checks for valid square.
        if not len(chosen) == 2:
            if len(chosen) == 3 and chosen[0] == 'm':
                chosenValues = []
                chosenValues.append((ord(chosen[1]))-97)
                chosenValues.append(int(chosen[2]))
                c = chosenValues[0]
                r = chosenValues[1]
                marker(r, c, k)
                play(b, k, startTime)
                break
        if len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers:
            break
    #Sets the list chosen to the numerical coordinates, and returns it.
    chosenValues = []
    chosenValues.append((ord(chosen[0]))-97)
    chosenValues.append(int(chosen[1]))
    return chosenValues


#The majority of the gameplay happens here.
def play(b, k, startTime):
    #Player chooses square.
    chosen = choose(b, k)
    #Splits the chosen square into c and r variables
    c = chosen[0]
    r = chosen[1]
    #Gets the value at that location.
    v = l(r, c, b)
    #If you hit a bomb, it ends the game.
    if v == '*':
        printBoard(b)
        print('You Lose!')
        #Stop timer.
        stopTime = time.time()
        print('Time: ' + str(round(stopTime - startTime)) + 's')
        #Offer to play again.
        playAgain = input('Play again? (Y/N): ')
        playAgain = playAgain.lower()
        if playAgain == 'y':
            reset()
        else:
            quit()
    #Puts that value into the known grid (k).
    row = k[r]
    row[c] = v
    checkZeros(k, b)
    printBoard(k)
    #Checks to see if you have won.
    squaresLeft = 0
    for x in range (0, 9):
        row = k[x]
        squaresLeft += row.count(' ')
        squaresLeft += row.count('⚐')
    if squaresLeft == 10:
        printBoard(b)
        print('You win!')
        playAgain = input('Play again? (Y/N): ')
        playAgain = playAgain.lower()
        if playAgain == 'y':
            reset()
        else:
            quit()
    #Repeats!
    play(b, k, startTime)

reset()