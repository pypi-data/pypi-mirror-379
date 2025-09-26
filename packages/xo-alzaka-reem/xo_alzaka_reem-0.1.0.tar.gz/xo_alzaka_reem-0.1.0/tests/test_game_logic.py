from xo_alzaka_reem.gui import new_board, check_winner, best_move, is_full

def test_new_board():
    b = new_board()
    assert isinstance(b, list)
    assert len(b) == 9
    assert all(cell == " " for cell in b)

def test_win_detection():
    b = ["X","X","X"," "," "," "," "," "," "]
    assert check_winner(b, "X") == [0,1,2]

def test_best_move_returns_int_or_none():
    b = ["X","O","X","O"," ","O","X"," "," "]
    m = best_move(b)
    assert (m is None) or (isinstance(m, int) and 0 <= m <= 8)
