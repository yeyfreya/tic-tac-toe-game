import pytest
from cli import TicTacToe, Player

def test_game_initialized_with_empty_board():
    game = TicTacToe(Player("X"), Player("O"))
    assert game.board == [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def test_game_initialized_with_two_players():
    game = TicTacToe(Player("X"), Player("O"))
    assert game.current_player.get_symbol() == "X"
    assert game.opponent.get_symbol() == "O"

def test_game_initialized_with_one_player():
    game = TicTacToe(Player("X"))
    assert game.current_player.get_symbol() == "X"
    assert game.opponent is None

def test_players_assigned_unique_pieces():
    player1 = Player("X")
    player2 = Player("O")
    assert player1.get_symbol() == "X"
    assert player2.get_symbol() == "O"

def test_players_take_turns():
    game = TicTacToe(Player("X"), Player("O"))
    game.mark_board(0, 0)  # Player X's turn
    assert game.current_player.get_symbol() == "O"
    game.mark_board(1, 1)  # Player O's turn
    assert game.current_player.get_symbol() == "X"


def test_winning_end_of_games_detected():
    game = TicTacToe(Player("X"), Player("O"))
    game.board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", None, None],
    ]
    assert game.check_winner().get_symbol() == "X"

def test_draw_games_identified():
    game = TicTacToe(Player("X"), Player("O"))
    game.board = [
        ["X", "O", "X"],
        ["O", "X", "X"],
        ["O", "X", "O"],
    ]
    assert game.check_winner() == "Draw"

def test_players_can_play_only_in_viable_spots():
    game = TicTacToe(Player("X"), Player("O"))
    game.mark_board(0, 0)
    game.mark_board(1, 1)
    assert game.board == [
        ["X", None, None],
        [None, "O", None],
        [None, None, None],
    ]

def test_correct_game_winner_detected():
    game = TicTacToe(Player("X"), Player("O"))
    game.board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", None, None],
    ]
    assert game.check_winner().get_symbol() == "X"

if __name__ == "__main__":
    pytest.main()
