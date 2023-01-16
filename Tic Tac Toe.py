from random import randint

def choose_first():
    return randint(0,1)

def display_board(board):
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('--|---|---')
    print(board[3]+' | '+board[4]+' | '+board[5])
    print('--|---|---')
    print(board[6]+' | '+board[7]+' | '+board[8])

def player_input():
    valid_input='OX'
    player1_marker='A'
    while player1_marker not in valid_input:
        player1_marker=input(f"{player1}, Please choose your Marker:  ").capitalize()
        if player1_marker not in valid_input:
            print('Enter a Valid Symbol O/X')
    return player1_marker

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    if board[0]+board[1]+board[2]==mark*3 or board[3]+board[4]+board[5]==mark*3 or board[6]+board[7]+board[8]==mark*3:
        return True
    if board[0]+board[3]+board[6]==mark*3 or board[1]+board[4]+board[7]==mark*3 or board[2]+board[5]+board[8]==mark*3:
        return True
    if board[0]+board[4]+board[8]==mark*3 or board[2]+board[4]+board[6]==mark*3:
        return True
    else:
        return False

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    return ' ' not in board

def player_choice(board):
    player_input='N'
    free_space=False
    while player_input.isdigit()==False or free_space == False or player_input not in range(0,8):
        player_input=input('Enter a Position:  ')
        if player_input.isdigit()==False or int(player_input)-1 not in range(0,9):
            print('Enter a Number b/w 1-9')
        else:
            free_space=space_check(board, int(player_input)-1)
            if free_space == False:
                print('The input position is occupied')
            else:
                break
    return int(player_input)-1

def replay():
    play_again='A'
    valid_input='YN'
    while play_again not in valid_input:
        play_again=input('Do you want to Play Again Y/N').capitalize()
        if play_again not in valid_input:
            print('Enter a Valid input. Y/N')
    return play_again=='Y'
def clear_board(board):
    for x in range(0,5):
        print('--------')
    board=[' ']*9
    display_board(board)
player1=input('Enter Player1 Name:  ').title()
player2=input('Enter Player2 Name:  ').title()
winner=''
player1_wins=0
player2_wins=0
board=[str(x) for x in range(1,10)]
display_board(board)

play_again=True
while play_again==True:
    player1_marker=player_input()
    player2_marker=''
    if player1_marker=='X':
        player2_marker='O'
    else:
        player2_marker='X'
    board=[' ']*9
    display_board(board)
    print(f"{player1}'s Marker ----> {player1_marker}")
    print(f"{player2}'s Marker ----> {player2_marker}")
    print('Game Begins')
    first_player=choose_first()
    i=0
    now_playing=first_player
    win_verify=False
    print(f'Player{now_playing+1} plays first')
    while i<9 and win_verify==False:

        if now_playing==0:
            print(f"{player1}'s turn:")
            player_position=player_choice(board)
            place_marker(board,player1_marker,player_position)
        if now_playing==1:
            print(f"{player2}'s turn:")
            player_position=player_choice(board)
            place_marker(board,player2_marker,player_position)
        display_board(board)
        win_verify=win_check(board,player1_marker)
        if win_verify==False:
            win_verify=win_check(board,player2_marker)
        i+=1
        now_playing=(now_playing+1)%2
        if i==9 and win_verify==False:
            print("It's a Draw")
            win_verify==True
            play_again=replay()

    if win_verify==True:
        
        if win_check(board,player1_marker)==True:
            player1_wins+=1
            print(f'{player1} Wins')
        if win_check(board,player2_marker)==True:
            player2_wins+=1
            print(f'{player2} Wins')
        with open('score.txt','w') as myfile:
            myfile.write(f'''{player1} : {player1_wins}\n{player2} : {player2_wins}''')
            myfile.close()
        with open('score.txt','r') as myfile:
            wins=myfile.read()
            myfile.close()
        print(wins)
        play_again=replay()
        if play_again==True:
            clear_board(board)
    if play_again==False:
        print(wins)
        print('The Game has Ended')
        print('Thank You for trying out this game')