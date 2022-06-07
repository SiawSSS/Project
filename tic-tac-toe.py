#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    if board[position] == ' ':
        board[position] = mark


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1

def printBoard():
    drawBoard = {
        1: ' ',
        2: ' ',
        3: ' ',
        4: ' ',
        5: ' ',
        6: ' ',
        7: ' ',
        8: ' ',
        9: ' '
    }

    for x in drawBoard.keys():
        if board[x] == ' ':
           drawBoard[x] = x 
        else:
            drawBoard[x] = board[x]

    print(
        '\n' +
        str(drawBoard[1]) + ' | '  +  str(drawBoard[2]) + ' | '  +  str(drawBoard[3]) + ' \n '  + 

        '-------- \n' +

        str(drawBoard[4]) + ' | '  +  str(drawBoard[5]) + ' | '  +  str(drawBoard[6]) + ' \n '  + 

        '-------- \n' +

        str(drawBoard[7]) + ' | '  +  str(drawBoard[8]) + ' | '  +  str(drawBoard[9]) + ' \n ' 

    )



# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):

    position = int(position)
    if position >= 1 and position <= 9:
        if board[position] == ' ':
            return True

    return False

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [3, 5, 7],
    [1, 5, 9]

]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for combination in winCombinations:
        if board[combination[0]] == player and board[combination[1]] == player and board[combination[2]] == player: 
            return True

    return False

# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for x in board:
        if board[x] == ' ':
            return False

    return True



#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################
def playGame():
    gameEnded = False
    currentTurnPlayer = 'X'

# entry point of the whole program
    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
        while not validateMove(move):
            print('Input is invalid, please enter value between 1-9')
            move = input(currentTurnPlayer + "'s turn, input: ")
        markBoard(int(move), currentTurnPlayer)
        printBoard()

        if checkWin(currentTurnPlayer):
            print('Congratulations, winner is {}. Game over!'.format(currentTurnPlayer))
            gameEnded = True

        elif checkFull():
            print('Game is tied.')
            gameEnded = True

        else:
            if currentTurnPlayer == 'X':
                currentTurnPlayer = 'O'
            else:
                currentTurnPlayer = 'X'
    return gameEnded

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over

playGame()

quitGame = False
while not quitGame:
    restartGame = input('Fancy another round of Tic-Tac-Toe? Yes or No?')
    if restartGame == 'Yes':
        board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
    }
    playGame()
else:
    print('Game ends.')
    quitGame = True



