def GameBoard(Xpos, Opos):
    print("  ___ ___ ___ ")
    print(f"0| {symbol(0, Xpos, Opos)} | {symbol(1, Xpos, Opos)} | {symbol(2,Xpos, Opos)} |2")
    print(" |___|___|___|")
    print(f"3| {symbol(3,Xpos, Opos)} | {symbol(4, Xpos, Opos)} | {symbol(5,Xpos, Opos)} |5")
    print(" |___|___|___|")
    print(f"6| {symbol(6, Xpos, Opos)} | {symbol(7, Xpos, Opos)} | {symbol(8, Xpos, Opos)} |8")
    print(" |___|___|___|")

def symbol(i, Xpos, Opos):
    return "X" if Xpos[i] else ("O" if Opos[i] else " ")

def checkWin(Xpos, Opos):
    winseries=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for w in winseries:
        if all(Xpos[i] == 1 for i in w):   # check if X occupies all positions in w
            print("'X' Won the match")
            return 1
        if all(Opos[i] == 1 for i in w):   # check if O occupies all positions in w
            print("'O' Won the match")
            return 0
    if (sum(Xpos)+sum(Opos)==9):
        print("It's a Draw!")
        return -2
    return -1   # no winner yet

def playGame():
    Xpos=[0,0,0,0,0,0,0,0,0]
    Opos=[0,0,0,0,0,0,0,0,0]
    print("Welcome to \"Tic Tac Toe\" ")
    turn=1   #turn = 1 then 'X' chance, turn = 0 then 'O' chance
    while(True):
        GameBoard(Xpos,Opos)
        if (turn==1):
            print("X's turn")
            value=int(input("enter position(0 - 8) : "))
            if (Xpos[value] or Opos[value]):
                print("Position already taken! Try again.")
                continue
            Xpos[value]=1
        else :
            print("O's turn")
            value=int(input("enter position(0 - 8) : "))
            if (Xpos[value] or Opos[value]):
                print("Position already taken! Try again.")
                continue
            Opos[value]=1
        win=checkWin(Xpos, Opos)
        if (win==1 or win==0):
            break
        if (win==-2):
            choice = input("Do you want to play again? (y/n): ").lower()    # Ask if players want to try again
            if (choice == "y"):
                playGame()   # restart game
            else:
                print("Thanks for playing!")
            break
        turn = 1-turn

playGame()  # Start the game
