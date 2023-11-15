
import os
os.makedirs("logs", exist_ok=True)

from logic import check_winner

def get_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
    for row in board:
        print (row)

def get_player_input(current_player):
    prompt = f"Player {current_player} >" 
    player_input = input(prompt)
    row_col_list= player_input.split(',') 
    row, col = [int(x) for x in row_col_list]
    return row, col

def switch_player(current_player):
    if current_player == "X":
        return "O"
    return "X"

if __name__ == '__main__':
    
    current_player = 'X'
    board = get_empty_board()
    max_moves = len(board) * len(board)


    while True:
            print_board(board)

            try:
                row, col = get_player_input(current_player)
            except ValueError:
                print("Invalid input, try again")
                continue

            if board[row][col] is None:
                board[row][col] = current_player
            else:
                print("Cell is already occupied, try again")
                continue

            max_moves -= 1

            # check for a winner
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Winner is {winner}")
                break
            elif max_moves == 0:
                print_board(board)
                print("It's a draw!")
                break

            current_player = switch_player(current_player)
            