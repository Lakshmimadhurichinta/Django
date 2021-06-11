def toss():
    import random

    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def player_marker():
    marker=''
    
    while not (marker == 'X' or marker == 'O'):
        marker=input("Choose X or O.")

    if marker == 'X':
        return ('X','O')
    elif marker == 'O':
        return ('O','X')

def display_board(board):
    print(' '+board[6]+'|'+board[7]+'|'+board[8])
    print(' '+board[3]+'|'+board[4]+'|'+board[5])
    print(' '+board[0]+'|'+board[1]+'|'+board[2])

def win_check(board,val):
    return ((board[0]==board[1]==board[2]==val) or
           (board[3]==board[4]==board[5]==val) or 
           (board[6]==board[7]==board[8]==val) or
           (board[0]==board[3]==board[6]==val) or
           (board[1]==board[4]==board[7]==val) or
           (board[2]==board[5]==board[8]==val) or
           (board[0]==board[4]==board[8]==val) or
           (board[2]==board[4]==board[6]==val))

def replay():
    rep=input("Do you wish to play again. Y or N? ")
    
    if rep[0].upper() == 'Y':
        play()
    elif rep[0].upper == 'N':
        print("Thanks for playing")

def play():
    print("Welcome to the Game!")

    turn=toss()
    board=[' ']*9
    dict1={}
    player_1_marker,player_2_marker=player_marker()
    dict1["Player 1"]=player_1_marker
    dict1["Player 2"]=player_2_marker
    display_board(board)

    input1=input("Are you ready to play the game? Y or N ")

    if input1[0].upper() == 'Y':
        game_on = True
    elif input[0].upper() == 'N':
        game_on = False

    while game_on:
        if turn == "Player 1":
            position=int(input("Choose a position between (1-9) "))
            board[position-1]=dict1[turn]
            display_board(board)
            if win_check(board,dict1[turn]):
                print(f"Congratulation. {turn} have won the game!")
                game_on = False
            elif ' ' not in board:
                print("The game is a draw!")
                game_on= False
            else:
                turn = "Player 2"
        if turn == "Player 2":
            position=int(input("Choose a position between (1-9) "))
            board[position-1]=dict1[turn]
            display_board(board)
            if win_check(board,dict1[turn]):
                print(f"Congratulation. {turn} have won the game!")
                game_on = False
                break
            elif ' ' not in board:
                print("The game is a draw!")
                game_on= False
                break
            else:
                turn = "Player 1"
    replay()

play()