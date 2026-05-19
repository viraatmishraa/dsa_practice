mainGrid=[0,0,0,0,0,0,0,0,0]
import os
import random
def inputNumber(str):
    x=input(str)
    try:
        x=int(x)

        return x
    except:
        print("invalid input")
        return inputNumber(str)

def isWinning(grid):
    if(grid[0]==grid[1]==grid[2]==1 or grid[0]==grid[1]==grid[2]==2):# for row1
        return 1
    elif(grid[3]==grid[4]==grid[5]==1 or grid[3]==grid[4]==grid[5]==2 ):# for row2
        return 1
    elif(grid[6]==grid[7]==grid[8]==1 or grid[6]==grid[7]==grid[8]==2 ):# for row1
        return 1
    elif(grid[0]==grid[3]==grid[6]==1 or grid[0]==grid[3]==grid[6]==2 ):# for col1
        return 1
    elif(grid[1]==grid[4]==grid[7]==1 or grid[1]==grid[4]==grid[7]==2 ):# for col2
        return 1
    elif(grid[2]==grid[5]==grid[8]==1 or grid[2]==grid[5]==grid[8]==2 ):# for col3
        return 1
    elif(grid[0]==grid[4]==grid[8]==1 or grid[0]==grid[4]==grid[8]==2 ):# for obtuse diagnol
        return 1 
    elif(grid[2]==grid[4]==grid[6]==1 or grid[2]==grid[4]==grid[6]==2 ):# for acute diagnol
        return 1 
    else:
        return 0

def printGrid(player,place,secGrid):
    if(player==1):
        subRow1="\\   / "
        subRow2="  X   "
        subRow3="/   \\ "
    elif(player==2 ):
       subRow1="┌----┐"
       subRow2="|    |"
       subRow3="└----┘"
    if(place==1):
        secGrid[0][0:6]=subRow1
        secGrid[1][0:6]=subRow2
        secGrid[2][0:6]=subRow3
    elif(place==2):
        secGrid[0][8:14]=subRow1
        secGrid[1][8:14]=subRow2
        secGrid[2][8:14]=subRow3
    elif(place==3):
        secGrid[0][17:22]=subRow1
        secGrid[1][17:22]=subRow2
        secGrid[2][17:22]=subRow3
    elif(place==4):
        secGrid[4][0:6]=subRow1
        secGrid[5][0:6]=subRow2
        secGrid[6][0:6]=subRow3
    elif(place==5):
        secGrid[4][8:14]=subRow1
        secGrid[5][8:14]=subRow2
        secGrid[6][8:14]=subRow3
    elif(place==6):
        secGrid[4][17:22]=subRow1
        secGrid[5][17:22]=subRow2
        secGrid[6][17:22]=subRow3
    elif(place==7):
        secGrid[8][0:6]=subRow1
        secGrid[9][0:6]=subRow2
        secGrid[10][0:6]=subRow3
    elif(place==8):
        secGrid[8][8:14]=subRow1
        secGrid[9][8:14]=subRow2
        secGrid[10][8:14]=subRow3
    elif(place==9):
        secGrid[8][17:22]=subRow1
        secGrid[9][17:22]=subRow2
        secGrid[10][17:22]=subRow3
    os.system('clear')
    for row in secGrid:
        print(''.join(row))
    return secGrid









def plays(player):
    if(not player==3):    
        played=inputNumber(f"player {player}! your next choice is:")
        if(played>=10 or played<=0):
            print("out of netwrok, is your input!")
            return plays(player)
        if(mainGrid[played-1]==0):
            mainGrid[played-1]=player
        else:
            print("already played there buddy!")
            return plays(player)
        return played
    else:
        played=random.randint(1,9)
        if(mainGrid[played-1]==0):
            mainGrid[played-1]=player-1
        else:
            return plays(player)
        return played


def main():
    turn=0
    modeInput=inputNumber("for playing with other player press 1\nfor playing with computer press 2")

    player=1
    secGrid = [
        list("       |       |       "),
        list("    1  |   2   |   3   "),
        list("       |       |       "),
        list(" - - - + - - - + - - - "),
        list("       |       |       "),
        list("    4  |   5   |   6   "),
        list("       |       |       "),
        list(" - - - + - - - + - - - "),
        list("       |       |       "),
        list("    7  |   8   |   9   "),
        list("       |       |       ")]
    printGrid(0,0,secGrid)
    if(modeInput==1):    
        playername1=input("enter player 1 name:")
        playername2=input("enter player 2 name:")
        while(isWinning(mainGrid)==0 and turn <9):
            if(player==1):
                secGrid=printGrid(player,plays(1),secGrid)
                player=2
                turn=turn+1
            elif(player==2):
                secGrid=printGrid(player,plays(2),secGrid)
                player=1
                turn=turn+1
        if(turn==9 and not isWinning(mainGrid)):
            print("draw dosh!")
        else:
            if(not player==1):
                print(f"{playername1} wins!")
            else:
                print(f"{playername2} wins!")
    elif(modeInput==2):
        while(isWinning(mainGrid)==0 and turn <9):
            if(player==1):
                secGrid=printGrid(player,plays(1),secGrid)
                player=3
                turn=turn+1
            elif(player==3):
                secGrid=printGrid(player-1,plays(3),secGrid)
                player=1
                turn=turn+1
        if(turn==9 and not isWinning(mainGrid)):
            print("draw dosh!")
        else:
            if(not player==1):
                print("player wins!")
            else:
                print("computer wins!")


main()


    
     
    
    
