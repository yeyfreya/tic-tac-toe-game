def check_winner(board):
    
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    for i in range(len(board)):
        column = [board[j][i] for j in range(len(board))]
        if len(set(column)) == 1:
            return board[0][i]

    top_left_to_bottom_right = [board[i][i] for i in range(len(board))]

    if len(set(top_left_to_bottom_right)) == 1:
        return board[0][0]

    top_right_to_bottom_left = [board[i][len(board)-i-1] for i in range(len(board))]
    if len(set(top_right_to_bottom_left)) == 1:
        return board[0][len(board)-1]

    flat_board = []
    for row in board:
        flat_board.extend(row)

    if not None in flat_board:
        return "Draw"

    return None  # No winner or draw yet

# if __name__ == "__main__":
#     board = [
#         ["O", "X", "O"],
#         ["X", "X", "O"],
#         ["O", "O", "X"],
#     ]
#     print(check_winner(board))
