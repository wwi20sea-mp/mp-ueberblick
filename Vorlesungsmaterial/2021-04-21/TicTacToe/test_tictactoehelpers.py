from tictactoehelpers import player_X_wins #, player_O_wins
# "Include What You Use" (IWYU)

def test_player_X_wins():
  a1 = [['X','X','X'],['O','O','O'],['X','O',' ']]
  # [TODO] Mehr Tests für Diagonalen und Spalten hinzufügen.
  assert(player_X_wins(a1))

  a2 = [['X',' ',' '],['X','O','O'],['X','O',' ']]
  assert(player_X_wins(a2))

  a3 = [['X',' ',' '],['X','X','O'],[' ','O','X']]
  assert(player_X_wins(a3))

  a4 = [[' ',' ','X'],['X','X','O'],['X','O',' ']]
  assert(player_X_wins(a4))

def test_player_O_wins():
  #[TODO]
  pass # Platzhalter: Statement, das nichts macht

def run_tictactoehelpers_tests():
  test_player_X_wins()
  test_player_O_wins()