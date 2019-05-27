# Tic Tac Toe

import random

print('Welcome to the tic tac toe')

def drawBoard(board):
    # This function prints out the board that it was pased.

    # "broad" is a list of 10 strings representing the board (ignore index 0)
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')

def inputPlayerLetter():
    # Lets the player type which letter they want to be

    # returns a list with  the players letter want to be
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O ?')
        letter = input().upper()
    
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    # Randomly choose player who goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else :
        return 'player'

def playAgain():
    # This function to ask player if they want to play again
    print(' Do you want to play again? (y/n)')
    return input().lower().startswith('y')

def makeMove(board,letter,move):
    board[move] = letter

def isWinner(bo,le):
    # Given a board and a player's letter , this function check if one of those player has win
    # just give a damn board in bo and letter in le

    return (
        (bo[1] == le and bo[2] == le and bo[3] == le) or # bottom row
        (bo[1] == le and bo[4] == le and bo[7] == le) or # left column
        (bo[1] == le and bo[5] == le and bo[9] == le) or # diagonal right
        (bo[7] == le and bo[8] == le and bo[9] == le) or # top row
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal left
        (bo[4] == le and bo[5] == le and bo[6] == le) or # middle row
        (bo[8] == le and bo[5] == le and bo[2] == le) or # middle column
        (bo[9] == le and bo[6] == le and bo[3] == le)    # right column
    )

def getBoardCopy(board):
    # make a duplicate of the board list and return it duplicate
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)
    
    return dupeBoard

def isSpaceFree(board,move):
    # Return true if the passed move is free on the pased board
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('Whats is your next move (1-9):')
        move = input()
    
    return int(move)

def chooseRandomMoveFromListBoard(board,movelist):
    # Returns the valid move from the passed list on the passed board
    # returns none if there is no valid move
    possibleMove = []
    for i in movelist:
        if isSpaceFree(board, i):
            possibleMove.append(i)
    if len(possibleMove) != 0:
        return random.choice(possibleMove)
    else:
        return None

# From here we are creating an Artifical Intellegence

def computerGetMove(board,computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here the algorithm
    # First, let see, if any move that can make computer won, then do it.
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computerLetter,i)
            if isWinner(copy,computerLetter):
                return i

    # Second , check if player have a chance to win, and block them
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,playerLetter,i)
            if isWinner(copy,playerLetter):
                return i
    
    # Third, Try to take a corner if they are free
    move = chooseRandomMoveFromListBoard(board, [1,3,9,7])
    if move != None:
        return move

    # Fourth, try to take center 
    if isSpaceFree(board,5):
        return 5
    
    # Last, is the 4 Decision is failed then just put on the sides
    return chooseRandomMoveFromListBoard(board, [4,2,8,6])

def isBoardFull(board):
    # Return true if there is full board on the table
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

while True:
    
    # Reset the board
    board = [' '] * 10

    playerLetter , computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The '+ turn +' will go first')
    gameIsPlaying = True

    while gameIsPlaying:
        
        if turn == 'player':
            # Players Turn
            drawBoard(board)
            move = getPlayerMove(board)
            makeMove(board,playerLetter,move)

            if isWinner(board, playerLetter):
                drawBoard(board)
                print('You Win')
                gameIsPlaying = False
            
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'computer'
        else:
            # Computer Turn
            move = computerGetMove(board, computerLetter)
            makeMove(board,computerLetter,move)

            if isWinner(board,computerLetter):
                drawBoard(board)
                print(' The Computer Win')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
        
    if not playAgain() :
           break
    


