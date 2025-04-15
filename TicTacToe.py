board = ['#','X','O','X','O','X','O','X','O','X']

def display_board(board):
    print(board[1] + "|" +board[2] + "|"+ board[3])
    print(board[4] + "|" +board[5] + "|"+ board[6])
    print(board[7] + "|" +board[8] + "|"+ board[9])
# display_board(board)

def player_input():
    marker = " "
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1(choose O or X): ").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
# print(player_input())

def place_marker(board,marker,position):
    board[position] = marker
    print(display_board(board))
# place_marker(board,"&",5)

def check_win(board,mark):
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or 
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))
# print(check_win(board,'X'))

import random
def choose_first():
    '''function for choosing randomly within two user from Player_1 and Player_2'''
    choose = random.randint(0,1)
    if choose == 0:
        return "Player 2"
    else:
        return "Player 1"

def space_check(board,index):
    '''function for checking the board index is empty or not'''
    return board[index] == ' '

def full_board_check(board):
    '''Function for checking any space on the board is empty or not'''
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    '''takes postion input from user and if it is in range will return this'''
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Enter the postion(1-9): "))
    return position


def replay():
    '''function for replaying '''
    choice = input("DO you want to continue? Yes or No: ").lower().startswith('y')
    


print("Welcome to Tic tac Toe: ")

while True:
    #play the game

    ##set everything up(boards,whois first,choose marker X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')
   
    play_game = input("Ready to play?Enter Y or N : ")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False


    ##game_play
    while game_on:
        if turn  == 'Player 1':
            #player1 turn

            #show the board
            display_board(the_board)

            #choose a position
            position = player_choice(the_board)

            #place the marker on positoin
            place_marker(the_board,player1_marker,position)
            
            #check if they won
            if check_win(the_board,player1_marker):
                display_board(the_board)
                print('Congrats, PlAYER 1 HAS WON!! ')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is draw!!")
                    break
                else:
                    turn = 'Player 2'

            #or check if there is a tie
            #No tie and no win? Then next player's turn

    #player one turn

        else:
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on positoin
            place_marker(the_board,player2_marker,position)
            #check if they won
            if check_win(the_board,player2_marker):
                display_board(the_board)
                print('PlAYER 2 HAS WON!! ')
                game_on = False
                
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a drwa!!")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break

    #player two turn

