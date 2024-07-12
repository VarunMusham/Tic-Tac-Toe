import random
from itertools import cycle
from textwrap import dedent

def choose_first():
    return random.choice([0, 1])

def display_board(board):
    print('\n'.join([' | '.join(board[i:i+3]) + '\n--|---|--' if i < 6 else ' | '.join(board[i:i+3]) for i in range(0, 9, 3)]))

def player_input(player):
    while (marker := input(f"{player}, Please choose your Marker (O/X): ").upper()) not in 'OX':
        print('Enter a Valid Symbol O/X')
    return marker

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return any(all(board[i] == mark for i in combo) for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)])

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board

def player_choice(board):
    while not (player_input := input('Enter a Position (1-9): ')).isdigit() or not space_check(board, int(player_input) - 1):
        print('Enter a Number b/w 1-9' if not player_input.isdigit() else 'Position is occupied')
    return int(player_input) - 1

def replay():
    return input('Do you want to Play Again (Y/N): ').upper() == 'Y'

def clear_board(board):
    print('\n' * 5)
    board[:] = [' '] * 9

def main():
    player1 = input('Enter Player1 Name: ').title()
    player2 = input('Enter Player2 Name: ').title()
    scores = {player1: 0, player2: 0}
    
    while True:
        board = [' '] * 9
        display_board([str(x) for x in range(1, 10)])
        
        player1_marker = player_input(player1)
        player2_marker = 'O' if player1_marker == 'X' else 'X'
        
        print(f"\n{player1}'s Marker ----> {player1_marker}\n{player2}'s Marker ----> {player2_marker}")
        print('Game Begins')
        
        players = [(player1, player1_marker), (player2, player2_marker)]
        if choose_first():
            players.reverse()
        
        for player, marker in cycle(players):
            print(f"{player}'s turn:")
            place_marker(board, marker, player_choice(board))
            display_board(board)
            
            if win_check(board, marker):
                print(f"{player} Wins")
                scores[player] += 1
                break
            elif full_board_check(board):
                print("It's a Draw")
                break
        
        with open('score.txt', 'w') as f:
            f.write(dedent(f"""\
                {player1}: {scores[player1]}
                {player2}: {scores[player2]}
            """))
        
        with open('score.txt') as f:
            print(f.read())
        
        if not replay():
            print('The Game has Ended\nThank You for trying out this game')
            break
        clear_board(board)

if __name__ == '__main__':
    main()
