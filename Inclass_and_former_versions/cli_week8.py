
import random

class Player:
    def __init__(self, symbol, human=True):
        self.symbol = symbol
        self.human = human

    def get_symbol(self):
        return self.symbol

    def is_human(self):
        return self.human
    

class TicTacToe:
    def __init__(self, player1, player2=None):
        self.board = self.get_empty_board()
        self.current_player = player1
        self.opponent = player2
        self.winner = None

    def get_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def print_board(self):
        # Print dashes above the board
        print("-------------")

        for row in self.board:
            print("|", end=" ")
            for cell in row:
                print(cell if cell is not None else " ", end=" | ")
            print()

        # Print dashes below the board
        print("-------------")

    def switch_player(self):
        print("Switching players")
        self.current_player, self.opponent = self.opponent, self.current_player
        print(f"Current player: {self.current_player.get_symbol()}, Opponent: {self.opponent.get_symbol()}")

    def get_player_input(self):
        if self.current_player.is_human():
            prompt = f"Player {self.current_player.get_symbol()}, enter cell number (1-9):"
            try:
                player_input = int(input(prompt))
                cell_number = int(player_input)

                # Convert cell number to row and column indices
                row = (cell_number - 1) // 3
                col = (cell_number - 1) % 3

                if 1 <= cell_number <= 9 and self.board[row][col] is None:
                    return row, col
                else:
                    print("Invalid input or spot is already occupied, try again")
                    return self.get_player_input()
            except ValueError:
                print("Invalid input, please enter a number.")
                return self.get_player_input()
        else:  # Bot player
            row, col = random.randint(0, 2), random.randint(0, 2)
            cell_number = row * 3 + col + 1
            print(f"Player {self.current_player.get_symbol()}'s move: {cell_number}")

            return row, col

    def mark_board(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player.get_symbol()
            self.winner = self.check_winner()  # Check for a winner after marking the board

            if not self.winner:
                self.switch_player()  # Switch to the next player if there is no winner
        else:
            print("Spot is already occupied, try again")

    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] is not None:
                return self.current_player

        for i in range(len(self.board)):
            column = [self.board[j][i] for j in range(len(self.board))]
            if len(set(column)) == 1 and column[0] is not None:
                return self.current_player

        top_left_to_bottom_right = [self.board[i][i] for i in range(len(self.board))]
        if len(set(top_left_to_bottom_right)) == 1 and top_left_to_bottom_right[0] is not None:
            return self.current_player

        top_right_to_bottom_left = [self.board[i][len(self.board) - i - 1] for i in range(len(self.board))]
        if len(set(top_right_to_bottom_left)) == 1 and top_right_to_bottom_left[0] is not None:
            return self.current_player

        flat_board = [cell for row in self.board for cell in row]

        if not None in flat_board:
            return "Draw"  # No winner or draw yet
        



    def is_board_full(self):
        return all(cell is not None for row in self.board for cell in row)
    

    def play_game(self):
        max_moves = 9

        while self.winner is None and max_moves != 0:
            self.print_board()
            row, col = self.get_player_input()
            self.mark_board(row, col)

            self.winner = self.check_winner()
            max_moves -= 1

            if self.winner:
                self.print_board()
                print(f"Player {self.current_player.get_symbol()} wins!")
            elif max_moves == 0:
                self.print_board()
                print("It's a draw!")
                break

            # if self.winner is None:  # Switch players only if there is no winner
            #     self.switch_player()


if __name__ == '__main__':

    # Check how many players
    num_players = input("Enter the number of players (1 or 2): ")

    # Choose player
    symbol1 = input("Enter symbol for Player 1 (X or O): ")

    # Player 1 is a human player
    player1 = Player(symbol1)
    
    if num_players == '2':
         # Player 2 is a human player
        if player1.get_symbol() == "X":
            symbol2 = "O"
            print(f"Player 2 is assigned {symbol2}.")
        else:
            symbol2 = "X"
            print(f"Player 2 is assigned {symbol2}.")
        
        player2 = Player(symbol2)

    else:
        # Player 2 is a bot player
        player2 = Player("O", human=False)

    game = TicTacToe(player1, player2)
    game.play_game()
