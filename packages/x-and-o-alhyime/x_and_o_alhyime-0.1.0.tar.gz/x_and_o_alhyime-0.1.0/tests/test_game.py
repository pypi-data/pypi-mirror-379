from x_and_o_alhyime.cli import check_win, best_move, is_board_full

def test_win_row():
    b = ['X','X','X',' ',' ',' ',' ',' ',' ']
    assert check_win(b, 'X') is True

def test_full_board():
    b = ['X','O','X','O','X','O','X','O','X']
    assert is_board_full(b) is True

def test_best_move_not_null():
    b = ['X','O','X','O',' ','O','X',' ',' ']
    m = best_move(b)
    assert isinstance(m, int)
    assert 0 <= m <= 8
